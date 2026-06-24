---
name: sci-manuscript-architect
description: Use for biomedical SCI manuscript strategy and writing from study materials, including field positioning, motivation and gap analysis, innovation taxonomy, contribution-level estimation, submission-level strategy, evidence-aware claim control, corpus-based style profiling, IMRAD blueprinting, figure architecture, reviewer audit, journal checklist, and LaTeX-safe manuscript checks.
---

# SCI Manuscript Architect

This skill builds biomedical SCI manuscripts from study materials and first
decides where the project sits in its field. It combines ToolUniverse-backed
field positioning, Supervisor-Skills-inspired logic gates, and biomedical
evidence discipline: scan the field, lock the motivation and innovation,
estimate contribution level, map claims to evidence, design the manuscript and
figures, align language with a field corpus, then draft and audit.

Default language policy:

- Use Chinese for analysis, decisions, risks, matrices, and explanations.
- Use English for manuscript titles, abstracts, section prose, captions,
  replacement sentences, and journal-facing text.

## Use This Skill For

- Evaluating whether a biomedical project is worth writing and what submission
  level it can realistically target.
- Building a biomedical SCI manuscript from experiment notes, figures, result
  summaries, protocols, PDFs, references, datasets, or partial drafts.
- Creating Field Scan Reports, Motivation and Gap Locks, Innovation and
  Contribution Matrices, Submission-Level Estimates, PaperSpine Maps, Evidence
  Ledgers, Citation Support Banks, IMRAD Blueprints, Figure Architecture Plans,
  reviewer audits, and journal checklists.
- Checking whether claims are supported by user evidence, citations, figures,
  statistical results, reporting-guideline requirements, and external field
  context.
- Preparing English manuscript prose while keeping Chinese reasoning visible to
  the user.
- Building or using a field corpus to align terminology, collocations, hedging,
  journal style, and context-aware narrative logic with high-quality papers in
  the same biomedical field.

## Operating Rules

1. Do not draft the full manuscript until the field position, central
   motivation, contribution level, and evidence boundary are clear. If the user
   asks for prose too early, first produce the missing strategy artifacts.
2. Never fabricate experiments, sample sizes, p-values, datasets, figures,
   citations, ethics approvals, software versions, guidelines, clinical
   relevance, or therapeutic claims.
3. Treat user materials as authoritative for study results. Literature,
   ToolUniverse outputs, and exemplar papers can shape positioning,
   motivation, background, and style, but cannot create new findings.
4. If no live database or literature scan has been performed, mark novelty,
   field position, and submission-level judgments as provisional with
   `FIELD_SCAN_REQUIRED`.
5. Mark missing evidence explicitly as `MISSING`, uncertain citations as
   `VERIFY`, overbroad claims as `OVERCLAIM`, incomplete evidence as
   `EVIDENCE_INCOMPLETE`, unvalidated mechanisms as `VALIDATION_REQUIRED`, and
   submission-level overreach as `CLAIM_OVERREACH_RISK`.
6. Use reporting guidelines by study type. If the study type is unclear, ask
   the user or state the assumption before applying a checklist.
7. Corpus materials are style and terminology evidence, not claim evidence. Do
   not copy protected full text or imitate distinctive sentences.
8. Supervisor-Skills is a structure source only. Translate its logic gates into
   biomedical SCI terms; do not force CS top-conference paper patterns onto
   clinical, wet-lab, or biomedical discovery papers.
9. Submission-level estimates are strategic guidance, not acceptance
   predictions.

## Standard Workflow

Follow this order unless the user requests a specific artifact:

1. **Project Intake and Field Scan**: collect study type, disease or biological
   process, materials, core finding, target journal, evidence available, and
   target output. Use `templates/project_intake.md` and
   `templates/source_inventory.md`. When field positioning is requested, read
   `references/field_positioning.md` and use ToolUniverse-backed sources when
   available.
2. **Motivation, Gap, and Innovation Lock**: decide whether the motivation is a
   real clinical unmet need, biological mechanism gap, methods bottleneck, or
   translational opportunity. Read `references/motivation_and_gap_engine.md`,
   `references/innovation_taxonomy.md`, and
   `references/contribution_level_matrix.md`; use the matching templates.
3. **Evidence and Claim Architecture**: map every major claim to user data,
   figure, statistic, citation, guideline, or missing evidence. Read
   `references/evidence_ledger.md`, `references/citation_support_bank.md`, and
   `references/paper_spine_map.md`.
4. **IMRAD and Figure Narrative Design**: create the biomedical Introduction
   flowchart, IMRAD blueprint, writing rationale, and figure architecture plan.
   Read `references/introduction_flowchart.md`,
   `references/writing_rationale_matrix.md`, and
   `references/figure_architecture.md`.
5. **Language and Corpus Alignment**: when field-style alignment is requested
   or enough topic information is available, create or update a corpus profile
   using public metadata, abstracts, user-provided references, and open-license
   full text only. Read `references/corpus_intelligence.md` and
   `references/terminology_and_style.md`.
6. **Drafting and Submission-Level Audit**: write English manuscript sections
   from approved strategy artifacts, then run reviewer, journal-readiness, and
   severity audits. Read `references/reviewer_audit.md`,
   `references/journal_checklist.md`,
   `references/submission_level_estimator.md`,
   `references/submission_severity_audit.md`, and
   `references/ai_research_integrity.md`.

## Required Core Artifacts

For a full from-materials workflow, produce these artifacts in order:

- Project Intake
- Source Inventory
- Field Scan Report or `FIELD_SCAN_REQUIRED` provisional note
- Motivation and Gap Lock
- Innovation and Contribution Matrix
- Submission-Level Estimate
- Motivation Lock
- PaperSpine Map
- Evidence Ledger
- Citation Support Bank
- Biomedical Introduction Flowchart
- IMRAD Blueprint
- Figure Architecture Plan
- Writing Rationale Matrix
- Term Bank, Phrase Pattern Bank, Journal Style Profile, and Language Guard
  when corpus materials are available
- English manuscript draft or requested section draft
- Reviewer Audit
- Journal-Ready Audit
- Submission Severity Audit

If the user requests only one artifact, produce that artifact and note which
upstream inputs are assumed, missing, or provisional.

## ToolUniverse Field-Positioning Sources

Use ToolUniverse when the user asks for current field progress, novelty,
submission level, clinical relevance, translational value, or target maturity.
Use only the tools needed for the task:

- `PubMed_search_articles` and `PMC_search_papers` for field progress, recent
  work, reviews, and open full text.
- `iCite_search_publications` and `iCite_get_publications` for citation count,
  RCR, APT, NIH percentile, and human/animal/molecular flags.
- `MeSH_search_descriptors` and `BioPortal_annotate_text` for concept
  normalization.
- `PubMed_Guidelines_Search` and `TRIP_Database_Guidelines_Search` for clinical
  guidelines and unmet clinical need.
- `Pharos_search_targets` and `TargetMine_search` for target development level,
  target-disease context, druggability, and translational relevance.

If these tools are not used, clearly mark field and journal-level judgments as
provisional.

## Supervisor-Skills Adaptation

Use these Supervisor-Skills ideas only after translating them into biomedical
SCI context:

- `intro-drafter`: biomedical six-part Introduction flowchart.
- `tech-paper-template`: background, gap, objective, study design, evidence,
  contribution self-consistency chain.
- `figure-designer`: study design figure, workflow figure, mechanistic model,
  main finding figure, validation figure, and graphical abstract logic.
- `pre-submission-reviewer`: `CRITICAL`, `MAJOR`, `MINOR` submission severity
  taxonomy.
- `benchmark-paper-template`: only for dataset, resource, tool, benchmark, or
  model-comparison papers.
- `vibe-research-workflow`: AI integrity rules; AI may accelerate organization,
  code, figures, and language polish, but cannot own scientific judgment.

## Submission-Level Estimate

Every submission-level estimate must include:

- Recommended tier: `Top/high-impact`, `solid specialty`,
  `method/resource`, or `descriptive/lower-level`.
- Evidence basis: field heat, novelty, evidence strength, translational value,
  target or mechanism maturity, guideline relevance, and journal fit.
- Risk labels: `FIELD_SCAN_REQUIRED`, `EVIDENCE_INCOMPLETE`,
  `VALIDATION_REQUIRED`, and/or `CLAIM_OVERREACH_RISK`.
- Upgrade path: concrete evidence, validation, analysis, figure, or framing
  changes needed to target a higher tier.

## Biomedical SCI Defaults

- Default workflow: strategy first, then manuscript building from materials.
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

- For field progress and ToolUniverse scan planning, read
  `references/field_positioning.md`.
- For motivation and gap quality, read
  `references/motivation_and_gap_engine.md`.
- For innovation type, read `references/innovation_taxonomy.md`.
- For contribution level, read `references/contribution_level_matrix.md`.
- For submission-level strategy, read
  `references/submission_level_estimator.md`.
- For central motivation and claim scope, read `references/motivation_lock.md`.
- For the argument spine, read `references/paper_spine_map.md`.
- For claim support and missing-evidence checks, read
  `references/evidence_ledger.md`.
- For literature-to-claim matching, read
  `references/citation_support_bank.md`.
- For Introduction structure, read `references/introduction_flowchart.md`.
- For writing-unit planning, read `references/writing_rationale_matrix.md`.
- For figure logic, read `references/figure_architecture.md`.
- For corpus collection, field tracking, and allowed corpus sources, read
  `references/corpus_intelligence.md`.
- For terminology, phrase patterns, and style constraints, read
  `references/terminology_and_style.md`.
- For peer-review simulation, read `references/reviewer_audit.md`.
- For severity-ranked final audit, read
  `references/submission_severity_audit.md`.
- For reporting and submission checks, read `references/journal_checklist.md`.
- For AI-assisted research boundaries, read
  `references/ai_research_integrity.md`.

Keep the main response concise. Load only the reference files needed for the
current user request.

## Context-Aware Narrative Learning Defaults

When building a long-term corpus for manuscript writing, prefer a two-layer
corpus-to-narrative structure:

```text
corpus_workspace/
  corpus_metadata.jsonl
  high_impact_corpus_metadata.jsonl
  field_scan_report.md
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

Use scripts when the user wants repeatable corpus updates. For a one-off
strategy or writing request, it is acceptable to create the same artifacts
manually from supplied papers, references, or ToolUniverse outputs.
