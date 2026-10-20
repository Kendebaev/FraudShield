# Development of an Application for Detecting Phishing and Fraudulent Messages

**FraudShield** supports manual checking of suspicious Russian and Kazakh messages in Kazakhstan. The aim is to provide risk indicators, explanations and advice from text and URL analysis.

## Team
- Nurassyl Auesbekuly Kendebaev, SE-2428: client, API, database, data collection and integration. GitHub: https://github.com/Kendebaev.
- Askhat Nurlanuly Amirkhanov, SE-2428: text/URL analysis, classification and evaluation. GitHub: https://github.com/askmirkhanov-boop.
- Supervisor: Azamat Galymzhanovich Serek, Associate Professor.

Names are transliterated for this English draft; confirm official Latin spellings before submission.

## Scope and status
This package contains analysis, requirements, architecture, mockups and data/evaluation protocols. Application code, local experiments, user interviews and substantive review are not yet verified. A complete application is not required for this first period.

MVP: manual text entry, local URL parsing without visiting links, explanations and opt-in history. Automatic access to chats/SMS and call analysis are outside scope.

## Provisional stack
React web, Express API, FastAPI analyser, PostgreSQL, Docker; optional Telegram Mini App. The team must review these decisions; see the report.

## Materials
- docs/Diploma_Report_Working.pdf: unified working report in English.
- docs/report.md: editable report text.
- docs/references.json: 20 sources, including 8 scientific works.
- diagrams/: editable Mermaid/PlantUML and readable PDF exports.
- prototype/wireframes.md: interaction specification.
- management/tasks.csv: 15 YouTrack tasks, planned owners and acceptance criteria. Amirkhanov's tasks do not yet have a separate YouTrack user; responsibility is recorded in descriptions.
- management/YouTrack_Board_and_Tasks.pdf: actual board and task screenshots.
- evidence/: blank templates for actual interviews and review, not completion evidence.
- tests/verification_plan.md: verification plan.

## Links and access
Repository: https://github.com/Kendebaev/FraudShield
YouTrack: https://frauddetect.youtrack.cloud/issues/DIP
Provide supervisor/commission access and verify their ability to open links before submission.

## Running and testing
This package contains no working application. Open PDFs in a standard viewer. Once code exists, add setup instructions, environment variables and executable test commands.

## Process
Each member uses their own account. Task -> branch with ID -> PR -> review -> merge. Record genuine work; do not create fictitious contributions, backdated commits or invented evidence. The final report and real board screenshots must match the prob-period-1 tag declared in the form. One representative submits for the team by 18:00 on 24 October 2026.
