# FraudShield

## Development of an Application for Detecting Phishing and Fraudulent Messages

We are developing FraudShield to help users in Kazakhstan assess suspicious messages in Russian and Kazakh. Our planned application analyses message text and URL structure, highlights risk indicators and explains the result.

## Current status

We are at the analysis and design stage. Our repository contains the project report, literature review, system and technology comparisons, requirements, architecture diagrams, interface mockups and an evaluation plan. We track 15 project tasks in [YouTrack](https://frauddetect.youtrack.cloud/issues/DIP).

The application has not been implemented yet, so there are no installation instructions, runtime environment variables or executable application tests at this stage. We have no measured detection results. Interview records and substantive supervisor feedback are not included in the current materials. Our documentation is awaiting team and supervisor review.

## Planned application

Our MVP covers manual message entry, local URL parsing without opening links, risk explanations and optional check history. It does not include automatic access to private chats or SMS, call analysis or payment blocking.

Our proposed stack is React, Express, FastAPI and PostgreSQL. We are considering a Telegram Mini App as an additional interface. These choices are provisional.

## Team

| Member | Planned responsibility | Account |
| --- | --- | --- |
| Nurassyl Auesbekuly Kendebaev, SE-2428 | Client, API, database, data collection and integration | [Kendebaev](https://github.com/Kendebaev) |
| Askhat Nurlanuly Amirkhanov, SE-2428 | Text and URL analysis, classification and evaluation | [askmirkhanov-boop](https://github.com/askmirkhanov-boop) |

Our supervisor is Azamat Galymzhanovich Serek, Associate Professor.

## Project materials

- [Project report](docs/Diploma_Report_Working.pdf) and [editable text](docs/report.md)
- [References](docs/references.json): 20 sources, including 8 scientific works
- [Architecture diagrams](diagrams/) with editable sources and PDF exports
- [Interface specification](prototype/wireframes.md)
- [Evaluation plan](tests/verification_plan.md)
- [Task list](management/tasks.csv) and [task-to-material links](management/task_links.md)
- [Actual board and task screenshots](management/YouTrack_Board_and_Tasks.pdf)
- [Interview and supervisor-feedback templates](evidence/), currently unfilled

## Project organisation

We use YouTrack for tasks and GitHub branches and pull requests for changes. Our current documentation is in [draft PR #1](https://github.com/Kendebaev/FraudShield/pull/1). Review is pending, and the final submission tag has not been created.
