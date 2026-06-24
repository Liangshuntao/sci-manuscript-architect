# Corpus Intelligence

Corpus Intelligence helps the skill track high-quality papers in the user's
field and convert them into safe writing guidance: terminology, collocations,
hedging style, section moves, and journal style profile.

## Purpose

Use corpus intelligence when the user asks for:

- Field-style alignment.
- Accurate terminology and collocations.
- Tracking recent high-impact SCI papers.
- Learning how target journals express claims, gaps, limitations, and
  implications.

## Source Policy

Allowed sources:

- Metadata, abstracts, keywords, MeSH terms, and citation metadata from public
  scholarly APIs.
- User-provided PDFs or references for local analysis.
- Open-license full text, such as open-access PMC or publisher pages when the
  license allows reuse.

Avoid:

- Bulk-saving copyrighted full text.
- Copying distinctive sentences from papers into manuscript prose.
- Treating corpus language as evidence for the user's scientific claims.

## Recommended Workspace

Use a project-local corpus workspace:

```text
corpus_workspace/
  corpus_query_profile.md
  corpus_metadata.jsonl
  corpus_index.md
  term_bank.md
  phrase_pattern_bank.md
  journal_style_profile.md
  language_guard.md
```

## Collection Workflow

1. Define a query profile using `templates/corpus_query_profile.md`.
2. Collect metadata and abstracts with `scripts/collect_corpus.py`.
3. Extract term and phrase candidates with `scripts/extract_terms.py`.
4. Build a style profile and language guard with
   `scripts/build_style_profile.py`.
5. During drafting, read `term_bank.md`, `phrase_pattern_bank.md`,
   `journal_style_profile.md`, and `language_guard.md`.

## Quality Filters

Prefer papers that match:

- User field, disease, model, assay, material, or technology.
- Target journal or comparable journal tier.
- Recent publication date, usually last 3-5 years.
- High relevance over journal prestige alone.
- Article type matching the user's manuscript when possible.


## Context-Aware Narrative Learning

When the user's goal is to learn from top-journal or high-impact papers, corpus
intelligence must go beyond terminology extraction. Build a narrative-learning
layer that records the **usage environment** of each source:

- journal or venue role;
- article type, such as review, clinical cohort, mechanistic experiment,
  metabolism/omics study, or single-cell/spatial atlas;
- evidence environment and assay context;
- abstract or section move profile when public metadata supports it;
- claim-strength context, including what the source can and cannot support;
- manuscript placement, such as Introduction, Results, Discussion, limitations,
  or future validation.

Recommended narrative-learning structure:

```text
narrative_learning/
  README.md
  01_online_context_engine/
    journal_narrative_playbook.md
    evidence_environment_map.md
    online_source_context_matrix.md
    section_move_library.md
    non_native_scientific_narrative_training.md
    from_corpus_to_narrative_architecture.md
  02_manuscript_specific_tools/
    storyline_rewrite_rules.md
    imrad_blueprint.md
    writing_rationale_matrix.md
    reviewer_audit_bank.md
    limitation_hedging_patterns.md
  03_general_move_library/
  legacy_first_pass/
```

Narrative-learning outputs should answer: "Why can this source speak this way,
where does that move belong, and is the user's evidence strong enough to borrow
that claim strength?" This prevents non-native writers from copying surface
phrasing while missing the evidentiary logic that makes high-impact prose work.

## Output Rules

Corpus-derived guidance should produce:

- Recommended terminology.
- Common noun phrases and verb-object collocations.
- Conservative claim verbs.
- Section-specific phrase patterns.
- Risky or imprecise words to avoid.
- Journal style profile.

Do not produce sentence templates that are near-copies of source papers.

