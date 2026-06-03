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

## Output Rules

Corpus-derived guidance should produce:

- Recommended terminology.
- Common noun phrases and verb-object collocations.
- Conservative claim verbs.
- Section-specific phrase patterns.
- Risky or imprecise words to avoid.
- Journal style profile.

Do not produce sentence templates that are near-copies of source papers.
