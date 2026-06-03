# SCI Manuscript Architect

**SCI Manuscript Architect** is a Codex Skill for building biomedical SCI manuscripts from study materials. It combines motivation-driven paper architecture, evidence-aware claim control, corpus-based terminology/style profiling, reviewer-risk auditing, and journal-readiness checks.

**SCI Manuscript Architect** 是一个用于生物医学 SCI 论文写作的 Codex Skill。它面向“从实验材料到可投稿论文”的完整流程，结合中心论证构建、证据台账、领域语料库风格画像、审稿风险审计和投稿前检查。

## What It Does

- Builds manuscripts from experiment notes, figures, results, protocols, references, PDFs, and partial drafts.
- Locks the central motivation before drafting.
- Creates a PaperSpine Map for research gap, central claim, novelty, main finding, and take-home message.
- Maps every key claim to data, figures, statistics, citations, or missing evidence through an Evidence Ledger.
- Builds a Citation Support Bank for claim-specific literature support.
- Generates IMRAD blueprints and Writing Rationale Matrices before prose drafting.
- Uses a Corpus Intelligence Layer to align terminology, phrase patterns, hedging, and journal style with papers in the same biomedical field.
- Runs Reviewer Audit and Journal-Ready Audit before finalization.

## 核心功能

- 根据实验记录、图表、结果摘要、实验方案、参考文献、PDF 和局部初稿构建 SCI 论文。
- 在写正文前先锁定论文的 central motivation。
- 生成 PaperSpine Map，明确 research gap、central claim、novelty、main finding 和 take-home message。
- 通过 Evidence Ledger 将每个关键论断绑定到数据、图表、统计、文献或缺失证据。
- 建立 Citation Support Bank，让引用服务于具体 claim，而不是简单堆文献。
- 在正式写作前生成 IMRAD Blueprint 和 Writing Rationale Matrix。
- 通过 Corpus Intelligence Layer 积累领域术语、常见搭配、谨慎表达和期刊风格画像。
- 在定稿前执行 Reviewer Audit 和 Journal-Ready Audit。

## Installation

Use Codex's skill installer:

```powershell
python C:\Users\lstsw\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo Liangshuntao/sci-manuscript-architect --path . --name sci-manuscript-architect
```

Then restart Codex so the new Skill is picked up by the skill index.

## 安装方式

使用 Codex 的 Skill 安装脚本：

```powershell
python C:\Users\lstsw\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo Liangshuntao/sci-manuscript-architect --path . --name sci-manuscript-architect
```

安装后请重启 Codex，让新的 Skill 进入技能索引。

## Quick Start

Invoke the Skill explicitly:

```text
Use $sci-manuscript-architect to build a biomedical SCI manuscript from my study data, corpus profile, and target journal.
```

For a staged workflow:

```text
Use $sci-manuscript-architect to first create a Project Intake, Motivation Lock, PaperSpine Map, and Evidence Ledger. Do not draft the full manuscript yet.
```

For corpus-driven style alignment:

```text
Use $sci-manuscript-architect to build a corpus profile for macrophage myocardial injury, generate a term bank, phrase pattern bank, journal style profile, and language guard, then draft the Introduction.
```

## 快速开始

显式调用该 Skill：

```text
用 $sci-manuscript-architect 根据我的研究数据、语料库画像和目标期刊，构建一篇生物医学 SCI 论文。
```

建议分阶段启动：

```text
用 $sci-manuscript-architect 先生成 Project Intake、Motivation Lock、PaperSpine Map 和 Evidence Ledger。暂时不要直接写全文。
```

如果需要领域语料库风格对齐：

```text
用 $sci-manuscript-architect 为 macrophage myocardial injury 方向建立语料库画像，生成 term bank、phrase pattern bank、journal style profile 和 language guard，然后再写 Introduction。
```

## Standard Workflow

1. Project Intake
2. Materials and Source Inventory
3. Corpus Intelligence Setup
4. Exemplar and Target Journal Scan
5. Motivation Lock
6. PaperSpine Map
7. Evidence Ledger
8. Citation Support Bank
9. IMRAD Blueprint
10. Writing Rationale Matrix
11. Language Guard
12. English Section Drafting
13. Reviewer Audit
14. Journal-Ready and LaTeX-Safe Audit

## 标准工作流

1. 项目启动信息收集
2. 材料与来源清单
3. 领域语料库设置
4. 高水平论文与目标期刊扫描
5. 中心动机锁定
6. PaperSpine 主线图
7. 证据台账
8. 引用支持库
9. IMRAD 蓝图
10. 写作理由矩阵
11. 语言守门检查
12. 英文段落写作
13. 审稿人风险审计
14. 投稿前与 LaTeX 安全检查

## Corpus Intelligence

The corpus layer can collect public metadata and abstracts from PubMed/OpenAlex, extract field terminology and phrase patterns, and build a journal style profile. It is designed to help the manuscript sound like work from the same biomedical field without copying protected text.

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

## 语料库智能层

语料库层可以从 PubMed/OpenAlex 收集公开元数据和摘要，抽取领域术语与表达模式，并生成期刊风格画像。它的目标是帮助论文语言更接近同领域 SCI 论文，而不是复制受版权保护的原文。

辅助脚本：

```powershell
python scripts\collect_corpus.py --query "macrophage myocardial injury" --source both --max-results 50 --since-year 2023 --output-dir corpus_workspace
python scripts\extract_terms.py --input corpus_workspace\corpus_metadata.jsonl --output-dir corpus_workspace
python scripts\build_style_profile.py --corpus-dir corpus_workspace
```

生成文件：

- `corpus_metadata.jsonl`
- `corpus_index.md`
- `term_bank.md`
- `phrase_pattern_bank.md`
- `journal_style_profile.md`
- `language_guard.md`

## Safety Boundaries

- The Skill does not fabricate experiments, sample sizes, p-values, citations, datasets, figures, ethics approvals, or clinical claims.
- User materials are authoritative for study results.
- Corpus papers provide terminology and style evidence, not evidence for the user's findings.
- Missing evidence is marked as `MISSING`.
- Unverified citations are marked as `VERIFY`.
- Overbroad claims are marked as `OVERCLAIM`.
- Final manuscript prose should be original, evidence-bounded, and not copied from corpus papers.

## 安全边界

- 不虚构实验、样本量、p 值、引用、数据集、图表、伦理审批或临床结论。
- 用户提供的材料是研究结果的权威来源。
- 语料库论文只用于术语和风格参考，不能替代用户自己的证据。
- 缺失证据标记为 `MISSING`。
- 未验证引用标记为 `VERIFY`。
- 过度延展的论断标记为 `OVERCLAIM`。
- 最终英文正文应为原创、证据边界清楚，不能复制语料库论文句子。

## Repository Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
├── templates/
├── scripts/
└── LICENSE
```

## 目录结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
├── templates/
├── scripts/
└── LICENSE
```

## License

MIT License.

## 许可证

MIT License。
