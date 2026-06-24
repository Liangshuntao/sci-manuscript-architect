# SCI Manuscript Architect

**SCI Manuscript Architect** is a Codex Skill for biomedical SCI manuscript
strategy and writing. It helps researchers move from study materials to a
field-positioned, evidence-bounded, journal-ready manuscript by combining
biomedical literature positioning, motivation and innovation analysis,
claim-to-evidence mapping, IMRAD planning, figure architecture, corpus-based
style alignment, and pre-submission risk auditing.

**SCI Manuscript Architect** 是一个面向生物医学 SCI 论文的 Codex Skill。它不仅帮助写作，
还会先判断项目在领域中的位置：当前研究进展、真实 motivation、knowledge gap、innovation
类型、本项目贡献等级、证据强度和可冲击的投稿层级。

## Core Capabilities

- **Field Positioning**: scan field progress, recent papers, reviews,
  high-impact work, guidelines, and target maturity.
- **Motivation and Gap Lock**: distinguish real clinical unmet need,
  biological mechanism gap, methods bottleneck, translational opportunity, and
  weakly packaged gap.
- **Innovation Taxonomy**: classify conceptual, mechanistic, methodological,
  translational, resource, and integrative innovation.
- **Contribution-Level Matrix**: judge whether the project is confirmatory,
  incremental, a solid advance, field-shaping, or translationally important.
- **Submission-Level Estimator**: estimate whether the work fits a
  top/high-impact, solid specialty, method/resource, or descriptive/lower-level
  journal strategy.
- **Evidence Ledger**: map each major claim to user data, figures, statistics,
  citations, guidelines, or missing evidence.
- **Citation Support Bank**: build claim-specific literature support instead of
  stacking generic citations.
- **IMRAD Blueprint**: design Introduction, Methods, Results, and Discussion
  before prose drafting.
- **Figure Architecture**: plan study design figures, workflows, mechanistic
  models, main finding panels, validation figures, and graphical abstracts.
- **Reviewer and Journal-Ready Audit**: run severity-ranked pre-submission
  checks, reporting-guideline checks, and LaTeX-safe manuscript checks.

## 核心能力

- **领域定位**：扫描领域进展、近期论文、综述、高影响力工作、指南和靶点成熟度。
- **Motivation 与 Gap 锁定**：区分真实临床未满足需求、机制空白、方法瓶颈、转化机会和包装型 gap。
- **创新性分类**：判断 conceptual、mechanistic、methodological、translational、resource、integrative innovation。
- **贡献等级矩阵**：判断项目属于验证性、增量推进、扎实进展、领域塑形，还是有转化重要性。
- **投稿等级估计**：评估项目适合 top/high-impact、solid specialty、method/resource，还是 descriptive/lower-level 投稿策略。
- **证据台账**：把每个关键 claim 绑定到数据、图表、统计、文献、指南或缺失证据。
- **引用支持库**：让 citation 服务于具体 claim，而不是简单堆文献。
- **IMRAD 蓝图**：在写正文前设计 Introduction、Methods、Results、Discussion。
- **图表架构**：规划研究设计图、流程图、机制模型图、核心结果图、验证图和 graphical abstract。
- **投稿前审计**：进行分级风险审查、报告指南检查和 LaTeX 安全检查。

## What It Borrows

### From Supervisor-Skills

This skill borrows structure, not disciplinary assumptions:

- `intro-drafter` -> biomedical six-part Introduction flowchart.
- `tech-paper-template` -> background-gap-objective-design-evidence-contribution
  self-consistency chain.
- `figure-designer` -> figure architecture and figure-quality gates.
- `pre-submission-reviewer` -> `CRITICAL / MAJOR / MINOR` severity audit.
- `benchmark-paper-template` -> only for dataset, resource, tool, benchmark, or
  model-comparison papers.

### From ToolUniverse

ToolUniverse is used as an external field-coordinate layer:

- PubMed/PMC for field progress and recent literature.
- iCite for citation count, RCR, APT, NIH percentile, and translational
  potential.
- MeSH/BioPortal for biomedical concept normalization.
- PubMed Guidelines/TRIP Database for clinical guidelines and unmet need.
- Pharos/TargetMine for target maturity, druggability, disease associations,
  and translational relevance.

ToolUniverse findings support positioning, motivation, and journal strategy.
They do not create user findings.

## Installation

Use Codex's skill installer:

```powershell
python C:\Users\lstsw\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo Liangshuntao/sci-manuscript-architect --path . --name sci-manuscript-architect
```

Then restart Codex so the new skill is picked up by the skill index.

## 安装方式

使用 Codex 的 skill installer：

```powershell
python C:\Users\lstsw\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo Liangshuntao/sci-manuscript-architect --path . --name sci-manuscript-architect
```

安装后重启 Codex，让 skill 进入索引。

## Quick Start

### Field scan and submission-level estimate

```text
Use $sci-manuscript-architect to perform a ToolUniverse-backed field scan for my project, then estimate motivation strength, innovation type, contribution level, and realistic submission tier.
```

### Provisional offline judgment

```text
Use $sci-manuscript-architect to judge this project from my materials only. Do not browse or use databases. Mark novelty and submission-level judgments with FIELD_SCAN_REQUIRED.
```

### Motivation, innovation, and contribution matrix

```text
Use $sci-manuscript-architect to create a Motivation and Gap Lock plus an Innovation and Contribution Matrix for this biomedical study.
```

### Manuscript drafting after evidence lock

```text
Use $sci-manuscript-architect to build the Evidence Ledger, Citation Support Bank, biomedical Introduction Flowchart, IMRAD Blueprint, and Figure Architecture Plan before drafting the manuscript.
```

## 快速开始

### 领域扫描和投稿等级预估

```text
使用 $sci-manuscript-architect，结合 ToolUniverse 对我的项目做 field scan，然后评估 motivation、innovation、contribution level 和可尝试的投稿层级。
```

### 离线初判

```text
使用 $sci-manuscript-architect，只基于我提供的材料做初步判断，不联网、不查数据库。请把创新性和投稿等级判断标记为 FIELD_SCAN_REQUIRED。
```

### Motivation、Innovation 和 Contribution 矩阵

```text
使用 $sci-manuscript-architect，为这个生物医学研究生成 Motivation and Gap Lock 以及 Innovation and Contribution Matrix。
```

### 锁定证据后再写稿

```text
使用 $sci-manuscript-architect，先生成 Evidence Ledger、Citation Support Bank、biomedical Introduction Flowchart、IMRAD Blueprint 和 Figure Architecture Plan，再开始写正文。
```

## Standard Workflow

1. Project Intake and Field Scan
2. Motivation, Gap, and Innovation Lock
3. Evidence and Claim Architecture
4. IMRAD and Figure Narrative Design
5. Language and Corpus Alignment
6. Drafting and Submission-Level Audit

## 标准工作流

1. 项目启动与领域扫描
2. Motivation、Gap 与 Innovation 锁定
3. 证据与 Claim 架构
4. IMRAD 与图表叙事设计
5. 语言与领域语料对齐
6. 正文写作与投稿等级审计

## Corpus Intelligence

The corpus layer can collect public metadata and abstracts from PubMed/OpenAlex,
extract field terminology and phrase patterns, and build a journal style
profile. It helps the manuscript sound like work from the same biomedical field
without copying protected text.

Helper scripts:

```powershell
python scripts\collect_corpus.py --query "macrophage myocardial injury" --source both --max-results 50 --since-year 2023 --output-dir corpus_workspace
python scripts\extract_terms.py --input corpus_workspace\corpus_metadata.jsonl --output-dir corpus_workspace
python scripts\build_style_profile.py --corpus-dir corpus_workspace
```

Generated artifacts:

- `corpus_metadata.jsonl`
- `corpus_index.md`
- `term_bank.md`
- `phrase_pattern_bank.md`
- `journal_style_profile.md`
- `language_guard.md`

## Safety Boundaries

- The skill does not fabricate experiments, sample sizes, p-values, citations,
  datasets, figures, ethics approvals, guidelines, or clinical claims.
- User materials are authoritative for study results.
- Field scan outputs support positioning, background, gap, and journal strategy;
  they do not support invented findings.
- Corpus papers provide terminology and style evidence, not evidence for the
  user's findings.
- Missing evidence is marked as `MISSING`.
- Unverified citations are marked as `VERIFY`.
- Overbroad claims are marked as `OVERCLAIM`.
- If no field scan has been performed, novelty and submission-level judgments
  are marked as `FIELD_SCAN_REQUIRED`.
- Submission-level estimates are strategic guidance, not acceptance
  predictions.
- Final manuscript prose should be original, evidence-bounded, and not copied
  from corpus papers.

## Repository Structure

```text
.
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|-- templates/
|-- scripts/
|-- README.md
`-- LICENSE
```

## License

MIT License.
