# Motivation and Gap Engine

## Purpose

Use this reference to decide whether a manuscript's motivation is real,
field-grounded, and strong enough to support the target submission level.

## Motivation Types

- **Clinical unmet need**: diagnosis, prognosis, treatment response, safety,
  disease stratification, or clinical decision problem remains unsolved.
- **Biological mechanism gap**: a disease or phenotype is known, but the
  cellular, molecular, spatial, immune, metabolic, or regulatory mechanism is
  unclear.
- **Methodological bottleneck**: current assays, analysis methods, models, or
  validation designs cannot answer a biomedical question reliably.
- **Translational opportunity**: a target, biomarker, pathway, or intervention
  is biologically plausible but not clinically connected.
- **Resource gap**: missing atlas, cohort, benchmark, perturbation resource,
  database, or reproducible workflow.

## Gap Quality Test

A strong gap should be:

- Specific: names what prior work could not answer.
- Field-grounded: supported by papers, guidelines, reviews, or databases.
- Consequential: explains why the missing answer matters biologically or
  clinically.
- Addressable: the user's data can actually reduce the gap.
- Claim-bounded: does not promise causal, clinical, or therapeutic conclusions
  beyond the evidence.

## Weak Gap Patterns

- "Few studies have investigated..." without explaining why it matters.
- A broad disease area is important, but the manuscript does not identify a
  precise missing answer.
- The gap is already addressed by recent studies.
- The data are descriptive but the framing claims mechanism or clinical utility.
- The motivation depends on citations or guidelines not yet verified.

## Output

Produce a Motivation and Gap Lock with:

- Motivation type.
- One-sentence central motivation.
- External evidence supporting the gap.
- What the user's study can and cannot answer.
- Missing field-scan items or `FIELD_SCAN_REQUIRED`.
- Risk labels: `VERIFY`, `OVERCLAIM`, `EVIDENCE_INCOMPLETE`.
