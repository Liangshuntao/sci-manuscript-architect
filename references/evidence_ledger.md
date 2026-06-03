# Evidence Ledger

The Evidence Ledger prevents unsupported claims. Use it before writing Results,
Discussion, abstract conclusions, or figure captions.

## Required Table

| Claim ID | Claim Sentence | Claim Type | Evidence Anchor | Figure/Table | Statistic | Citation | Support Strength | Status | Action |
|---|---|---|---|---|---|---|---|---|---|

## Claim Types

- `background`: literature or field context.
- `method`: protocol, device, model, algorithm, cohort, or assay.
- `result`: direct finding from user data.
- `mechanism`: causal or explanatory biological mechanism.
- `comparison`: superiority, equivalence, benchmark, or difference.
- `clinical`: patient, diagnostic, prognostic, therapeutic, or translational
  implication.
- `limitation`: uncertainty, boundary, or unresolved issue.

## Support Strength

- `strong`: directly supported by user evidence and appropriate statistics.
- `moderate`: supported, but needs cautious wording.
- `weak`: indirect, preliminary, underpowered, or missing a comparator.
- `missing`: no evidence supplied.
- `citation-only`: literature supports context, not the user's result.

## Status

- `OK`: can be used.
- `CAUTION`: use conservative wording.
- `MISSING`: do not use as a manuscript claim yet.
- `VERIFY`: citation or statistic must be verified.
- `OVERCLAIM`: revise downward before use.

## Rules

- Result claims require user evidence. Citations cannot substitute for missing
  user data.
- Mechanistic claims require mechanistic evidence. Association is not mechanism.
- Clinical implication claims require matching clinical evidence or conservative
  language.
- Abstract and conclusion claims must be traceable to ledger rows.
