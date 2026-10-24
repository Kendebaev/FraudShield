# Building the project report

The PDF is generated from docs/report.md, the three PDF exports in diagrams/, and prototype/mockups.png. The restored mockup's editable vector source is prototype/mockups.svg. Keep the PNG and SVG consistent when revising the design.

## Dependencies and command

Use Python 3.9 or newer in an isolated environment. Install the dependencies listed in report-requirements.txt, then run the builder from any working directory:

    python -m pip install -r docs/report-requirements.txt
    python docs/build_report.py

The builder writes docs/Diploma_Report_Working.pdf. It uses Arial on macOS or DejaVu Sans on Linux. Set REPORT_FONT_DIR to a directory containing DejaVuSans.ttf and DejaVuSans-Bold.ttf if neither location is available. Fonts are embedded; pagination can vary between font families.

## Verification

Render and visually inspect the result before committing. Confirm all three architecture diagrams and the three UX mockups are present, tables are readable, links and lists are separated, and page numbers appear without draft-task footers. Readiness and contribution statements must match the actual repository and evidence; generating a PDF does not establish review or approval.

Commit both report.md and the regenerated PDF when changing report content. Include changed figure sources and exports when applicable.
