<div align="center">

# SCI Manuscript Architect

**Turn biomedical study materials into a field-positioned, evidence-bounded, submission-aware SCI manuscript.**

中文 | English

</div>

## Why This Exists

Many biomedical manuscripts do not fail because the data are useless. They fail
because the project is not positioned clearly enough:

- the motivation sounds important but is not anchored in the current field;
- the novelty is asserted before recent papers, guidelines, or target maturity
  are checked;
- the central claim is stronger than the evidence;
- figures show analyses but do not carry the manuscript's argument;
- the paper is written before anyone decides what journal level it can
  realistically target.

**SCI Manuscript Architect** is a Codex Skill for this last-mile problem in
biomedical SCI writing. It helps researchers move from experiment notes,
figures, result summaries, references, protocols, omics outputs, and partial
drafts to a manuscript strategy that is field-aware, evidence-bounded, and
journal-facing.

**SCI Manuscript Architect** 面向生物医学 SCI 论文的“最后一公里”：不是先急着写正文，而是先判断项目在领域中的位置、真实动机、创新类型、证据强度、贡献等级和可尝试的投稿层级。它帮助研究者把实验材料、图表、结果摘要、参考文献、实验方案、组学分析和半成稿，转化为一套可写、可审、可投稿的论文架构。

## Design Philosophy

This skill has three layers:

| Layer | What it answers | Main outputs |
|---|---|---|
| **Field Strategy** | Is the project worth writing, and what level can it target? | Field Scan Report, Motivation and Gap Lock, Innovation and Contribution Matrix, Submission-Level Estimate |
| **Evidence Architecture** | What can the paper safely claim? | PaperSpine Map, Evidence Ledger, Citation Support Bank, claim-boundary labels |
| **Manuscript Execution** | How should the paper be written, visualized, and audited? | IMRAD Blueprint, Introduction Flowchart, Figure Architecture Plan, Language Guard, Reviewer Audit |

The goal is not to make AI write a paper for the researcher. The goal is to make
the researcher's judgment explicit, checkable, and manuscript-ready.

## What It Can Do

### 1. Field Positioning

Map the project against the current biomedical field:

- recent PubMed/PMC literature;
- high-impact or highly cited papers;
- iCite metrics such as RCR, APT, and citation count;
- MeSH/BioPortal concept normalization;
- clinical guidelines and unmet clinical needs;
- target maturity, druggability, and translational relevance through resources
  such as Pharos and TargetMine.

If no database or web scan is performed, novelty and submission-level judgments
must be marked as `FIELD_SCAN_REQUIRED`.

### 2. Motivation and Gap Lock

Separate real motivation from decorative framing:

- clinical unmet need;
- biological mechanism gap;
- methodological bottleneck;
- translational opportunity;
- resource or atlas gap;
- over-packaged gap that the data cannot actually answer.

### 3. Innovation Taxonomy

Classify what kind of innovation the study can credibly claim:

- conceptual innovation;
- mechanistic innovation;
- methodological innovation;
- translational innovation;
- resource innovation;
- integrative multi-modal innovation.

### 4. Contribution-Level Matrix

Estimate whether the project is:

- confirmatory;
- incremental;
- a solid biomedical advance;
- field-shaping;
- translationally important.

The matrix also states why the work is not one level higher and what evidence
would be needed to upgrade it.

### 5. Submission-Level Estimator

Provide a strategic journal-tier estimate:

- `Top/high-impact`;
- `solid specialty`;
- `method/resource`;
- `descriptive/lower-level`.

Every estimate must include evidence basis, rejection risks, upgrade path, and
risk labels such as `FIELD_SCAN_REQUIRED`, `EVIDENCE_INCOMPLETE`,
`VALIDATION_REQUIRED`, and `CLAIM_OVERREACH_RISK`.

### 6. Evidence-Bounded Manuscript Building

Before drafting prose, the skill builds:

- PaperSpine Map;
- Evidence Ledger;
- Citation Support Bank;
- biomedical Introduction Flowchart;
- IMRAD Blueprint;
- Figure Architecture Plan;
- Writing Rationale Matrix;
- Language Guard;
- Reviewer and Journal-Ready Audit.

## Borrowed Strengths

### From Supervisor-Skills

This project borrows **structure**, not disciplinary assumptions, from
[HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills):

- Introduction flowchart -> biomedical six-part Introduction;
- technical-paper skeleton -> biomedical background-gap-objective-design-evidence-contribution chain;
- figure designer -> study design, workflow, mechanism, main result, and validation figure architecture;
- pre-submission reviewer -> `CRITICAL / MAJOR / MINOR` audit taxonomy;
- benchmark-paper template -> used only for dataset, resource, tool, benchmark,
  or model-comparison manuscripts.

### From ToolUniverse

ToolUniverse is treated as an **external field-coordinate system**:

- PubMed/PMC: field progress and recent literature;
- iCite: citation count, RCR, APT, NIH percentile, translational signal;
- MeSH/BioPortal: biomedical concept normalization;
- guideline tools: clinical unmet need and practice context;
- Pharos/TargetMine: target maturity, disease association, and translational relevance.

ToolUniverse can support motivation, field positioning, and journal strategy. It
cannot invent findings for the user's study.

## Standard Workflow

```text
Project Intake
-> Field Scan
-> Motivation, Gap, and Innovation Lock
-> Contribution-Level Matrix
-> Submission-Level Estimate
-> Evidence and Claim Architecture
-> IMRAD and Figure Narrative Design
-> Language and Corpus Alignment
-> Drafting
-> Submission-Level Audit
```

## Quick Start

### Field scan and submission strategy

```text
Use $sci-manuscript-architect to perform a ToolUniverse-backed field scan for my biomedical project, then estimate motivation strength, innovation type, contribution level, and realistic submission tier.
```

### Offline provisional judgment

```text
Use $sci-manuscript-architect to judge this project from my materials only. Do not browse or use databases. Mark novelty and submission-level judgments with FIELD_SCAN_REQUIRED.
```

### Motivation and innovation matrix

```text
Use $sci-manuscript-architect to create a Motivation and Gap Lock plus an Innovation and Contribution Matrix for this biomedical study.
```

### Manuscript architecture before drafting

```text
Use $sci-manuscript-architect to build the Evidence Ledger, Citation Support Bank, biomedical Introduction Flowchart, IMRAD Blueprint, and Figure Architecture Plan before drafting the manuscript.
```

## 中文快速开始

### 领域扫描和投稿策略

```text
使用 $sci-manuscript-architect，结合 ToolUniverse 对我的生物医学项目做 field scan，然后评估 motivation、innovation、contribution level 和可尝试的投稿层级。
```

### 离线初判

```text
使用 $sci-manuscript-architect，只基于我提供的材料做初步判断，不联网、不查数据库。请把创新性和投稿等级判断标记为 FIELD_SCAN_REQUIRED。
```

### Motivation 和创新性矩阵

```text
使用 $sci-manuscript-architect，为这个生物医学研究生成 Motivation and Gap Lock 以及 Innovation and Contribution Matrix。
```

### 先搭论文架构，再写正文

```text
使用 $sci-manuscript-architect，先生成 Evidence Ledger、Citation Support Bank、biomedical Introduction Flowchart、IMRAD Blueprint 和 Figure Architecture Plan，再开始写正文。
```

## Installation

Use Codex's skill installer:

```powershell
python C:\Users\lstsw\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo Liangshuntao/sci-manuscript-architect --path . --name sci-manuscript-architect
```

Then restart Codex so the new skill is picked up by the skill index.

## Repository Structure

```text
.
|-- SKILL.md                  # Executable skill specification
|-- references/               # On-demand strategy and writing guides
|-- templates/                # Structured output templates
|-- scripts/                  # Optional corpus helper scripts
|-- agents/
|   `-- openai.yaml
|-- README.md
`-- LICENSE
```

## Corpus Intelligence

The corpus layer can collect public metadata and abstracts from PubMed/OpenAlex,
extract field terminology and phrase patterns, and build a journal style
profile. It helps the manuscript sound like work from the same biomedical field
without copying protected text.

```powershell
python scripts\collect_corpus.py --query "macrophage myocardial injury" --source both --max-results 50 --since-year 2023 --output-dir corpus_workspace
python scripts\extract_terms.py --input corpus_workspace\corpus_metadata.jsonl --output-dir corpus_workspace
python scripts\build_style_profile.py --corpus-dir corpus_workspace
```

Generated artifacts include:

- `corpus_metadata.jsonl`
- `corpus_index.md`
- `term_bank.md`
- `phrase_pattern_bank.md`
- `journal_style_profile.md`
- `language_guard.md`

## Safety Boundaries

- Do not fabricate experiments, sample sizes, p-values, citations, datasets,
  figures, ethics approvals, guidelines, or clinical claims.
- User materials are authoritative for study results.
- Field scans support positioning, background, gap, and journal strategy; they
  do not support invented findings.
- Corpus papers provide terminology and style evidence, not evidence for the
  user's findings.
- Missing evidence is marked as `MISSING`.
- Unverified citations are marked as `VERIFY`.
- Overbroad claims are marked as `OVERCLAIM`.
- No field scan means novelty and submission-level judgments are provisional
  and must be marked as `FIELD_SCAN_REQUIRED`.
- Submission-level estimates are strategic guidance, not acceptance
  predictions.
- Final manuscript prose should be original, evidence-bounded, and not copied
  from corpus papers.

## License

MIT License.
