# AI Research Integrity

## Purpose

Use this reference whenever AI assists literature organization, coding, figure
planning, style editing, or manuscript drafting.

## Allowed Uses

- Organizing user materials and extracting missing-input lists.
- Summarizing provided papers, abstracts, metadata, or database outputs.
- Suggesting manuscript structure, figure plans, and audit checklists.
- Improving English expression while preserving scientific meaning.
- Helping write code or analysis scripts that the user can inspect and run.

## Forbidden Uses

- Inventing experiments, sample sizes, p-values, statistics, cohorts, ethics
  approvals, guidelines, citations, datasets, or clinical conclusions.
- Treating external literature as evidence for the user's own results.
- Copying distinctive sentences from protected papers.
- Hiding missing validation behind stronger wording.
- Presenting provisional novelty or submission-level estimates as final.

## Integrity Labels

- `FIELD_SCAN_REQUIRED`: external field scan not yet performed.
- `VERIFY`: citation, guideline, database result, or factual claim needs user
  confirmation.
- `MISSING`: required evidence is absent.
- `OVERCLAIM`: wording exceeds evidence.
- `EVIDENCE_INCOMPLETE`: evidence exists but is insufficient for the claim.
- `VALIDATION_REQUIRED`: independent or orthogonal validation is needed.
- `CLAIM_OVERREACH_RISK`: submission strategy depends on a claim that may be too
  strong.

## Output Rule

When uncertainty affects manuscript strategy, state it visibly. Do not bury
integrity labels in footnotes or prose.
