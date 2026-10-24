from pathlib import Path
import re,html,fitz,tempfile,os
from urllib.parse import urljoin
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
base=Path(__file__).resolve().parents[1]
render_tmp=tempfile.TemporaryDirectory(prefix='fraudshield-report-')
tmp=Path(render_tmp.name)
font_pairs = [
 (Path(os.environ.get('REPORT_FONT_DIR', '/nonexistent')), 'DejaVuSans.ttf', 'DejaVuSans-Bold.ttf'),
 (Path('/usr/share/fonts/truetype/dejavu'), 'DejaVuSans.ttf', 'DejaVuSans-Bold.ttf'),
 (Path('/System/Library/Fonts/Supplemental'), 'Arial.ttf', 'Arial Bold.ttf'),
]
for directory, regular, bold in font_pairs:
 if (directory/regular).is_file() and (directory/bold).is_file():
  pdfmetrics.registerFont(TTFont('Arial',str(directory/regular)))
  pdfmetrics.registerFont(TTFont('Arial-Bold',str(directory/bold)))
  break
else:
 raise RuntimeError('Install DejaVu Sans or set REPORT_FONT_DIR to its font directory.')
styles=getSampleStyleSheet()
for s in styles.byName.values():s.fontName='Arial';s.fontSize=10;s.leading=14
styles['Title'].fontSize=24;styles['Title'].leading=29;styles['Title'].fontName='Arial-Bold'
styles['Heading1'].fontName='Arial-Bold';styles['Heading1'].fontSize=18;styles['Heading1'].leading=23;styles['Heading1'].spaceBefore=16
styles['Heading2'].fontName='Arial-Bold';styles['Heading2'].fontSize=12;styles['Heading2'].leading=16;styles['Heading2'].spaceBefore=12
styles.add(ParagraphStyle(name='Cell',fontName='Arial',fontSize=8,leading=11,spaceAfter=2))
styles.add(ParagraphStyle(name='CellHead',parent=styles['Cell'],fontName='Arial-Bold',textColor=colors.black))
def para(t,style='BodyText'):
 t=html.escape(html.unescape(t)).replace('—','-').replace('–','-')
 t=re.sub(r'`([^`]+)`',r'\1',t)
 t=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',t)
 def link(m):
  target=html.unescape(m.group(2))
  if '://' not in target:
   target=urljoin('https://github.com/Kendebaev/FraudShield/blob/main/docs/',target)
  return '<link href="'+html.escape(target,quote=True)+'">'+m.group(1)+'</link>'
 t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,t)
 return Paragraph(t,styles[style])
def footer(c,d):
 c.setStrokeColor(colors.HexColor('#dce2e9'));c.line(42,37,553,37)
 c.setFont('Arial',8);c.setFillColor(colors.HexColor('#526176'));c.drawRightString(553,25,str(d.page))
def build(text,path,report=False):
 story=[];lines=text.splitlines();i=0
 while i<len(lines):
  line=lines[i].strip();i+=1
  if not line:continue
  if line == 'FraudShield':
   story.extend([Spacer(1,90),para(line,'Title'),Spacer(1,15)]);continue
  match=re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)',line)
  if match:
   path_image=(base/'docs'/match.group(2)).resolve()
   image=Image(str(path_image))
   scale=min(511/image.imageWidth,385/image.imageHeight)
   image.drawWidth=image.imageWidth*scale;image.drawHeight=image.imageHeight*scale
   story.extend([image,Spacer(1,9)]);continue
  if line.startswith('|'):
   rows=[line]
   while i<len(lines) and lines[i].strip().startswith('|'):rows.append(lines[i].strip());i+=1
   rows=[r for r in rows if not re.fullmatch(r'[| :\-]+',r)]
   cells=[[x.strip() for x in r.strip('|').split('|')] for r in rows]
   n=len(cells[0]);widths=[511/n]*n
   if n==3:widths=[100,205,206]
   if n==4:widths=[80,75,170,186]
   if n==5:widths=[90,105,105,105,106]
   data=[[para(x,'CellHead' if j==0 else 'Cell') for x in row] for j,row in enumerate(cells)]
   table=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
   table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.white),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.white]),('GRID',(0,0),(-1,-1),0.5,colors.black)]))
   story.extend([table,Spacer(1,9)]);continue
  if line.startswith('# '):
   if report and story:story.append(PageBreak())
   story.append(para(line[2:],'Heading1'))
   diagram={'7 Architecture and use cases':'context','7 Use case diagram':'usecase','7 Components and data':'components'}.get(line[2:]) if report else None
   if diagram:
    doc=fitz.open(base/'diagrams'/(diagram+'.pdf'));pg=doc[0]
    # Crop exported diagram to occupied content to avoid full-page margins.
    bounds=None
    for block in pg.get_text('blocks'):
     r=fitz.Rect(block[:4]);bounds=r if bounds is None else bounds|r
    for draw in pg.get_drawings():bounds=draw['rect'] if bounds is None else bounds|draw['rect']
    pix=pg.get_pixmap(matrix=fitz.Matrix(2,2),clip=(bounds+(-10,-10,10,10))&pg.rect if bounds else None)
    png=str(tmp/(diagram+'.png'));pix.save(png)
    w,h=pix.width,pix.height;scale=min(511/w,320/h)
    story.extend([Image(png,width=w*scale,height=h*scale),Spacer(1,12)])
   continue
  if line.startswith('## '):story.append(para(line[3:],'Heading2'));continue
  story.append(para(line));story.append(Spacer(1,5))
 SimpleDocTemplate(str(path),pagesize=(595.28,841.89),rightMargin=42,leftMargin=42,topMargin=40,bottomMargin=51,title=path.stem,author='FraudShield - working draft').build(story,onFirstPage=footer,onLaterPages=footer)

if __name__ == '__main__':
 build((base/'docs/report.md').read_text(),base/'docs/Diploma_Report_Working.pdf',True)
 render_tmp.cleanup()
