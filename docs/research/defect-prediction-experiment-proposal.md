# Defect prediction: bounded JIT prioritisation experiment

**Status:** Proposed research experiment; not an implemented model, production control or authorization gate.  
**Prepared:** 2026-11-19  
**Owner:** Codex-Guidas maintainers; participating project owners retain data and change authority.

## 1. Question

Can a small, transparent, within-project change-risk signal help a maintainer decide where to spend review and test effort earlier than the existing manual process?

The experiment does **not** ask whether a model can predict with certainty that a commit will introduce a defect. It does not authorize automatic severity changes, issue creation, merge blocking, deployment decisions or closure.

## 2. Starting position

Software defect prediction research includes module-level static metrics, just-in-time (JIT) change models, cross-project transfer, deep/graph models and online learning. Public benchmark results can be distorted by class imbalance, label noise, temporal leakage, dataset age, repeated tuning and domain shift. A complex model can look strong offline yet provide little actionable value to a small team.

For this portfolio, a transparent baseline is preferable to a black-box model. Start with a descriptive checklist or simple rule-based signal; do not begin with deep learning or cross-project transfer.

## 3. Candidate first experiment

**Unit of analysis:** one change/commit in one owning repository.

**Initial features (only if reliably available):**
- lines added and deleted;
- number of files changed;
- number of directories/components touched;
- whether high-risk boundaries changed (persistence, authentication/authorization, privacy, safeguarding, scoring, migrations or CI);
- prior confirmed defect history for the touched component, measured strictly before the candidate change.

Do not use author identity, personal attributes or speculative "developer quality" proxies in the first experiment. Do not infer a defect label from a source-only observation, a proposed lesson or a failing test with no causal link.

**Label definition:** a positive label requires a later, independently reviewed defect record linked to the change by explicit evidence. A negative label requires a defined observation window and adequate follow-up; absence of a DEF record is not automatically a clean label. Mark ambiguous and censored cases Unknown and exclude them from binary training/evaluation.

## 4. Evaluation contract

Before examining model results, record:
- participating repository and exact source window;
- inclusion/exclusion rules and label provenance;
- feature definitions and collection time;
- observation/follow-up window for labels;
- temporal train/validation/test split (never random-only split across time);
- baseline heuristic and any model candidates;
- evaluation metrics and decision threshold;
- sample size, class prevalence and uncertainty;
- data minimisation, privacy and project-owner approval.

Report at minimum precision, recall, PR-AUC, MCC and confusion matrix at the chosen threshold. Include calibration only if probabilities are actually calibrated. Report false positives and false negatives in concrete review-work terms. Accuracy alone is not an acceptable headline metric for an imbalanced dataset.

Compare against a simple baseline and the existing manual process. Use confidence intervals or otherwise make small-sample uncertainty visible. Do not claim generalisation from one project or a historical public dataset.

## 5. Leakage and drift controls

- Features must be available at the time the prediction would have been made.
- Defect history must exclude information learned after the candidate commit.
- Group related commits/PRs to avoid the same change appearing in both training and test sets.
- Keep a strict chronological holdout.
- Re-evaluate after material changes in architecture, team workflow, language, platform or defect-labeling practice.
- Cross-project training/transfer remains out of scope until within-project data quality and utility are demonstrated separately for each project.

## 6. How a signal may be used

A high-risk result may suggest:
- an additional reviewer;
- targeted tests around the changed boundary;
- retrieval of relevant CG lessons and prior DEF records;
- a manual question for the HYPOTHESIZE or TRIAGE stage.

It must be displayed as **risk-prioritisation signal — unverified**, with the features and limitations visible. It must not be described as "this commit will introduce a defect." It must not change the owning project's severity, state, required approvals or merge policy.

## 7. Stop / continue criteria

**Stop** if labels cannot be traced, the sample is too small to support a meaningful comparison, feature collection creates privacy risk, leakage cannot be controlled, or the signal adds review noise without actionable benefit.

**Continue to a bounded pilot** only if the baseline is reproducible, recent held-out performance is reported, false-positive/false-negative costs are understood, and project owners agree the signal can be used as optional prioritisation.

Do not set arbitrary accuracy targets before establishing a baseline and decision costs. Pre-register the acceptance criteria for any pilot.

## 8. Relationship to Defect Intelligence

Prediction can suggest where to look; it cannot establish that a defect exists. The normal loop remains:

`DETECT → CONTAIN → RECORD → TRIAGE → SEARCH → HYPOTHESIZE → FIX → VERIFY → LEARN → CLOSE`

A prediction is not a DETECT event by itself. If it prompts an inspection, record the resulting observation and evidence in the normal way. No automatic DEF creation, severity change, lesson promotion or closure.

## 9. Decision

**Current decision:** Research only. No model, training pipeline, repository-wide scoring, CI gate or cross-project dataset is authorized by this proposal.

**Next useful proof:** Inventory whether any one project has enough time-ordered, traceable, reviewed defect/change pairs to evaluate a simple baseline without label leakage. If not, improve label quality before attempting prediction.
