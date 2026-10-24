# Verification and model evaluation plan — DIP-8

Status: proposed draft for team and supervisor review. No tests have been executed and no dataset or measured results are claimed. Planned task owner: Askhat Nurlanuly Amirkhanov; implementation and approval remain pending.

## 1. Dataset and annotation

The pilot target is 600 anonymised messages:

| Language | Fraud | Legitimate | Total |
| --- | ---: | ---: | ---: |
| Russian (RU) | 150 | 150 | 300 |
| Kazakh (KZ; API code `kk`) | 150 | 150 | 300 |
| Total | 300 | 300 | 600 |

These are collection targets. Record actual counts and shortfalls before evaluation. Mixed-language messages receive a separate language flag and are reported separately; they do not silently count toward both language targets. Advertising spam is not automatically fraud. Synthetic examples are labelled and used for functional tests, not as evidence of real-world detection quality.

For each item record its identifier, sanitised text, language, source, source date, permission or licence, campaign group, reference label and annotation version. Remove personal identifiers, credentials and verification codes. Do not visit suspicious URLs during collection or testing.

Two team members independently annotate an initial 100-message sample, covering both languages and both proposed classes. Record agreement and disagreements before discussion. Resolve differences using the written labelling rules; retain unresolved items as uncertain and exclude them from supervised training and scored binary evaluation, while reporting their number. Refine the guidelines before labelling the remainder. Record annotator and adjudication provenance for each label. User feedback and model predictions must not automatically become reference labels.

## 2. Splitting and leakage prevention

Target proportions are 60% train, 20% validation and 20% test: approximately 360/120/120 messages if the full pilot is collected. Aim for approximately 90/30/30 items for each language/class combination, but preserve groups even when exact balance is impossible.

1. Remove exact duplicates and inspect near-duplicates before splitting.
2. Group messages from the same campaign, near-identical template or suspicious destination domain. Combine overlapping groups. Generic legitimate service domains alone should not merge unrelated campaigns; document grouping exceptions.
3. Assign whole groups to one split, aiming for language and class balance. If a large group prevents a useful split, collect additional independent groups and disclose the limitation.
4. Record the random seed, item IDs, group IDs, counts and a hash of the split manifest. Check that item and group intersections between splits are empty.
5. Fit TF-IDF vocabulary and other learned preprocessing on training data only. Use validation data for model selection, calibration if attempted, and thresholds.
6. Freeze the test set before selecting the final configuration. Do not tune after seeing test results. Any later exploratory rerun must be identified as such.

If dates and sample coverage permit, add a later-time holdout to assess temporal generalisation. Report it separately from the primary test.

## 3. Baseline comparison

| ID | Approach | Purpose |
| --- | --- | --- |
| B0 | Deterministic text and URL-structure rules | Simple reproducible baseline |
| B1 | Word/character TF-IDF and logistic regression | Classical text classification baseline |
| B2 | Multilingual encoder combined with URL features | Candidate extension, evaluated after B0/B1 |

Run all available approaches on the same frozen test items. Record preprocessing, model/checkpoint version, dependency versions, configuration, seed and training resource use. Compare text-only, URL-only and combined variants if B2 is implemented. Mark unavailable approaches as not evaluated; do not invent results to fill the comparison.

## 4. Metrics and decision rules

Fraud is the positive class. Report TP, FP, TN and FN, sample counts, fraud precision, recall and F1, macro-F1, and FPR = FP / (FP + TN), separately for RU and KZ. Include a confusion matrix for each language. Report undefined metrics as undefined with their denominators, rather than silently substituting zero.

Provisional targets from the report are recall >= 0.85 and FPR <= 0.10 per language. These require supervisor agreement and are not achieved results. Balanced pilot precision does not estimate precision at real-world fraud prevalence.

Select a binary decision threshold on validation data and freeze it for testing. Keep the UI's `high`, `suspicious` and `low_signal` labels separate from reference classes. Document how UI bands map to the binary decision. Count all scored test items in binary metrics; report the share of `suspicious` responses separately. Do not discard difficult cases to improve scores. Report service failures and evaluation coverage separately; any failure makes the run incomplete and must be resolved before claiming the targets were met.

Report 95% confidence intervals using a documented bootstrap procedure. Resample independent campaign groups, retaining their messages; use the same resampled groups for paired model comparisons and record the seed and number of replicates (proposed: 2,000). Report replicates with undefined denominators and avoid a reliable-comparison claim when too few independent groups remain. Report paired F1 differences, not just each model's best score.

At the nominal split, each language has only about 30 legitimate and 30 fraud test examples. One additional false positive changes FPR by about 3.3 percentage points. Treat results as pilot evidence and report uncertainty; expand the independent test corpus before making broad claims.

## 5. Functional and non-functional checks

All checks below are planned, not executed.

| ID | Procedure and cases | Expected evidence / acceptance |
| --- | --- | --- |
| T1 — input and language | Empty input; 1, 5,000 and 5,001 characters; Cyrillic RU/KZ; mixed-language text; interface language switching | Reject invalid lengths; accept supported Unicode; preserve original text and display the selected interface language. Document what the API counts as a character. FR1, FR5. |
| T2 — URL handling | No URL; several URLs; scheme-less address; IDN; IP address; userinfo; malformed address | Match manually specified extraction expectations; malformed input causes no crash; verify no outbound request is made when parsing links. FR2. |
| T3 — response and errors | Successful analysis; analyser unavailable; timeout; response containing HTML-like text | Validate status, category, reasons and model version; render input safely as text; errors never appear as `low_signal` or a green safety result. FR3, FR4, FR9, NFR2. |
| T4 — privacy and history | Anonymous check; no consent; explicit consent; another user's history; deletion; inspect logs with a unique synthetic marker | No text persistence without consent; owner-only access; deleted record returns 404; raw text absent from logs. FR6, FR7, NFR3, NFR4. |
| T5 — latency | 1,000 measured requests after a documented warm-up; 10 concurrent clients; 100–2,000 characters; fixed hardware and model | Record CPU/RAM, versions, request mix, p50/p95/p99 and failures; p95 <= 2 s for local analysis; unavailable state by the 5 s timeout. Report successful-request latency alongside failure rate. NFR1, NFR2. |
| T6 — model evaluation | Frozen grouped split, B0/B1 and B2 if available, per-language metrics and uncertainty | Reproducible split/configuration and results; no leakage; assess provisional targets without claiming unmeasured success. NFR5, NFR6. |
| T7 — usability | Five consenting volunteers complete a message check without assistance and explain the warning | Record completion count, time and misunderstandings; target 4/5 successful completions; explicitly disclose small sample size. NFR7. |

## 6. Execution records and review

For each executed check record: case ID, date, tester, code commit, environment, input or anonymised fixture ID, expected outcome, actual outcome, pass/fail/blocked status, evidence and linked defect. A proposed plan must not contain pre-filled passing results.

For evaluation additionally retain the dataset/annotation version, split manifest, configurations, per-item predictions without private text, metrics script version, aggregate metrics and limitations. Keep restricted data outside the public repository and describe the access route.

Before running the plan, the team must approve the class definitions, collection feasibility, grouping policy, thresholds and acceptance targets with the supervisor. A second team member reviews this plan and its consistency with report sections 6, 8 and 10. The protocol was introduced in merged PR #2 (https://github.com/Kendebaev/FraudShield/pull/2). Link actual review findings in DIP-8 when available; merging the PR does not establish review or approval. Preparing this document does not establish that data collection, experiments or supervisor approval have occurred.
