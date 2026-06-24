---
name: sci-manuscript-architect
description: Use for biomedical SCI manuscript writing from study materials, including motivation-driven paper architecture, field corpus tracking, terminology/style profiling, IMRAD blueprinting, Evidence Ledger, Citation Support Bank, reviewer audit, journal checklist, and LaTeX-safe manuscript checks.
---

# SCI Manuscript Architect

This skill builds biomedical SCI manuscripts from study materials. It adapts
PaperSpine's motivation-driven workflow for journal submission work: learn the
target scene, lock the central motivation, map claims to evidence, design the
paper by writing units, adapt language to a field corpus, then draft and audit.

Default language policy:

- Use Chinese for analysis, decisions, risks, matrices, and explanations.
- Use English for manuscript titles, abstracts, section prose, captions,
  replacement sentences, and journal-facing text.

## Use This Skill For

- Building a biomedical SCI manuscript from experiment notes, figures, result
  summaries, protocols, PDFs, references, or partial drafts.
- Creating a central argument, PaperSpine Map, IMRAD blueprint, Evidence Ledger,
  Citation Support Bank, Writing Rationale Matrix, reviewer audit, or journal
  checklist.
- Checking whether claims are supported by user evidence, citations, figures,
  statistical results, and reporting-guideline requirements.
- Preparing English manuscript prose while keeping Chinese reasoning visible to
  the user.
- Building or using a field corpus to align terminology, collocations, hedging,
  journal style, and context-aware narrative logic with high-quality papers in
  the same biomedical field.

## Operating Rules

1. Do not draft the full manuscript until the central motivation and evidence
   boundary are clear. If the user asks for prose too early, first produce the
   missing Motivation Lock and Evidence Ledger.
2. Never fabricate experiments, sample sizes, p-values, datasets, figures,
   citations, approvals, software versions, or clinical claims.
3. Treat user materials as authoritative for results. Literature and exemplars
   can shape framing and background, but cannot create new findings.
4. Mark missing evidence explicitly as `MISSING`, uncertain citations as
   `VERIFY`, and overbroad claims as `OVERCLAIM`.
5. Final manuscript prose must be flowing academic paragraphs. Bullet points are
   allowed for planning matrices, not as final manuscript text.
6. Use reporting guidelines by study type. If the study type is unclear, ask the
   user or state the assumption before applying a checklist.
7. Keep PaperSpine as a design reference only. Do not require PaperSpine runtime,
   scripts, or artifacts for this skill.
8. Corpus materials are style and terminology evidence, not claim evidence. Do
   not copy protected full text or imitate distinctive sentences.

## Standard Workflow

Follow this order unless the user requests a specific artifact:

1. **Project Intake**: collect study type, target journal, materials, central
   finding, evidence available, and target output. Use
   `templates/project_intake.md` when a structured start is needed.
2. **Materials and Source Inventory**: list user files, figures, datasets,
   result summaries, references, and missing inputs. Use
   `templates/source_inventory.md`.
3. **Corpus Intelligence Setup**: when the user asks for field-style alignment
   or when enough topic information is available, create or update a corpus
   profile using public metadata, abstracts, user-provided references, and
   open-license full text only. Read `references/corpus_intelligence.md`.
4. **Context-Aware Narrative Learning**: when the user wants to learn from
   top-journal or high-impact papers, go beyond term extraction. Classify the
   source-use environment, evidence type, article type, section function, and
   allowable claim strength before adapting narrative moves. Treat corpus papers
   as source-context examples, not sentence templates.
5. **Exemplar and Target Journal Scan**: learn structure, tone, figure logic,
   and key constraints from user-provided examples, target journal instructions,
   or high-quality papers. Do not copy scientific claims.
6. **Motivation Lock**: generate and confirm one central motivation before
   drafting. Read `references/motivation_lock.md`.
7. **PaperSpine Map**: define research gap, central claim, main finding,
   novelty, and take-home message. Read `references/paper_spine_map.md`.
8. **Evidence Ledger**: map every major claim to data, figure, statistic,
   citation, or missing evidence. Read `references/evidence_ledger.md`.
9. **Citation Support Bank**: build claim-specific citation candidates for
   Introduction, Discussion, limitations, and application claims. Read
   `references/citation_support_bank.md`.
10. **IMRAD Blueprint**: create paragraph-level functions for Introduction,
   Methods, Results, and Discussion. Use `templates/manuscript_blueprint.md`.
11. **Writing Rationale Matrix**: plan each writing unit before prose. Read
   `references/writing_rationale_matrix.md` and use
   `templates/writing_rationale_matrix.md`.
12. **Language Guard**: apply the corpus-derived terminology bank, phrase
    pattern bank, and journal style profile before final prose. Read
    `references/terminology_and_style.md`.
13. **English Section Drafting**: write English paragraphs from the approved
    blueprint, evidence ledger, and language guard. Do not exceed evidence
    strength.
14. **Reviewer Audit**: simulate critical peer review and produce a revision
    matrix. Read `references/reviewer_audit.md` and use
    `templates/revision_matrix.md`.
15. **Journal-Ready and LaTeX-Safe Audit**: check reporting guidelines,
    unsupported claims, citations, figures, labels, and manuscript readiness.
    Read `references/journal_checklist.md` and use
    `templates/journal_ready_audit.md`.

## Required Core Artifacts

For a full from-materials workflow, produce these artifacts in order:

- Project Intake
- Source Inventory
- Corpus Query Profile when field-style alignment is requested
- Context-Aware Narrative Learning Library when the user asks to learn from
  top-journal or high-impact writing logic
- Term Bank, Phrase Pattern Bank, Journal Style Profile, and Language Guard when
  corpus materials are available
- Motivation Lock
- PaperSpine Map
- Evidence Ledger
- Citation Support Bank
- IMRAD Blueprint
- Writing Rationale Matrix
- English manuscript draft or requested section draft
- Reviewer Audit
- Journal-Ready Audit

If the user requests only one artifact, produce that artifact and note which
upstream inputs are assumed or missing.

## Biomedical SCI Defaults

- Default workflow: build from materials.
- Default audience: biomedical journal reviewers and editors.
- Default manuscript structure: IMRAD unless the target journal requires a
  different structure.
- Default reporting-guideline candidates:
  - CONSORT for randomized trials.
  - STROBE for observational studies.
  - PRISMA for systematic reviews and meta-analyses.
  - ARRIVE for animal studies.
  - TRIPOD for prediction model studies.
- Default output: Chinese analysis plus English manuscript prose.

## Reference Routing

- For central motivation and claim scope, read `references/motivation_lock.md`.
- For corpus collection, field tracking, and allowed corpus sources, read
  `references/corpus_intelligence.md`.
- For terminology, phrase patterns, and style constraints, read
  `references/terminology_and_style.md`.
- For the argument spine, read `references/paper_spine_map.md`.
- For claim support and missing-evidence checks, read
  `references/evidence_ledger.md`.
- For literature-to-claim matching, read `references/citation_support_bank.md`.
- For writing-unit planning, read `references/writing_rationale_matrix.md`.
- For peer-review simulation, read `references/reviewer_audit.md`.
- For reporting and submission checks, read `references/journal_checklist.md`.

Keep the main response concise. Load only the reference files needed for the
current user request.

## Context-Aware Narrative Learning Defaults

When building a long-term corpus for manuscript writing, prefer a two-layer
corpus-to-narrative structure:

```text
corpus_workspace/
  corpus_metadata.jsonl
  high_impact_corpus_metadata.jsonl
  term_bank.md
  phrase_pattern_bank.md
  journal_style_profile.md
  language_guard.md
  narrative_learning/
    01_online_context_engine/
    02_manuscript_specific_tools/
    03_general_move_library/
    legacy_first_pass/
``` 

The `01_online_context_engine` layer should classify source-use environment,
evidence type, journal role, section function, and claim-strength context before
any language pattern is adapted. This is especially important for non-native
English scientific writing: the goal is to learn paragraph function and evidence
logic, not to imitate sentences.

## Corpus Scripts

Optional helper scripts live in `scripts/`:

- `collect_corpus.py`: collect PubMed/OpenAlex metadata and abstracts into a
  local corpus workspace.
- `extract_terms.py`: extract terminology and phrase-pattern candidates from
  the corpus.
- `build_style_profile.py`: build a journal style profile and language guard
  from the extracted corpus artifacts.

Use scripts when the user wants repeatable corpus updates. For a one-off writing
request, it is acceptable to create the same artifacts manually from supplied
papers or references.


