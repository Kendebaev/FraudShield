# FraudShield

## Development of an Application for Detecting Phishing and Fraudulent Messages

We are developing FraudShield to help users in Kazakhstan assess suspicious messages in Russian and Kazakh. Our planned application analyses message text and URL structure, highlights risk indicators and explains the result.

## Current status

We are at the analysis and design stage. Our repository contains the project report, literature review, system and technology comparisons, requirements, architecture diagrams, interface mockups and an evaluation plan. We track 15 project tasks in [YouTrack](https://frauddetect.youtrack.cloud/issues/DIP).

The application has not been implemented yet, so there are no installation instructions, runtime environment variables or executable application tests at this stage. We have no measured detection results. User discussion records are not yet available. The team has recorded the supervisor's recommendations from chat correspondence in [supervisor_review.md](evidence/supervisor_review.md); final supervisor comments and approval are pending. Teammate comments on the report have led to documentation corrections; no formal GitHub PR reviews are recorded.

## Planned application

Following the supervisor's recommendation, the intended focus is phishing email messages, with the approved project title unchanged. The report still contains SMS/smishing material; adaptation of the scope, data collection and evaluation to email is not yet complete.

The current MVP design covers manual message entry, local URL parsing without opening links, risk explanations and optional check history. It does not include automatic access to private chats or SMS, call analysis or payment blocking.

Our proposed stack is React, Express, FastAPI and PostgreSQL. The existing design also considers a Telegram Mini App; its relevance should be reassessed as part of the email-focused revision. These choices are provisional.

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
- [Interface specification and restored mockups](prototype/wireframes.md)
- [Evaluation plan](tests/verification_plan.md)
- [Task list](management/tasks.csv), [management overview](management/README.md) and [contribution records](management/contributions.md)
- [Actual board and task screenshots](management/YouTrack_Board_and_Tasks.pdf)
- [User discussion template](evidence/interview_template.md), not yet completed
- [Recorded supervisor recommendations and team responses](evidence/supervisor_review.md), pending supervisor confirmation

## Project organisation

Our current materials are in `main`. PRs [#1](https://github.com/Kendebaev/FraudShield/pull/1), [#2](https://github.com/Kendebaev/FraudShield/pull/2), [#3](https://github.com/Kendebaev/FraudShield/pull/3), [#4](https://github.com/Kendebaev/FraudShield/pull/4), [#5](https://github.com/Kendebaev/FraudShield/pull/5) and [#6](https://github.com/Kendebaev/FraudShield/pull/6) have been merged. They include the initial documentation, evaluation protocol, management evidence, restored mockups, report contents and supervisor-recommendation record. Merge status does not establish substantive review or supervisor approval.

The management snapshot records 7 tasks for Nurassyl/admin and 8 for Askhat/askmirkhanov. Assignment does not imply task acceptance or completed experiments.

## Submission version

The [pre-defense-1 tag](https://github.com/Kendebaev/FraudShield/tree/pre-defense-1) identifies the first pre-defense submission snapshot. Use the report and YouTrack PDFs from that same tag when submitting. The tag records a repository version, not supervisor approval. Once submitted to the committee, keep the tag fixed; subsequent work belongs in later commits.


See [report build instructions](docs/BUILD_REPORT.md) to regenerate the PDF from its sources.
