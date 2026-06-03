#!/usr/bin/env python3
"""Build a journal style profile and language guard from corpus artifacts."""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path


PROMOTIONAL_WORDS = [
    "breakthrough",
    "revolutionary",
    "remarkable",
    "excellent",
    "perfect",
    "dramatically",
    "huge",
]

CAUSAL_WORDS = [
    "prove",
    "confirmed that",
    "demonstrates that",
    "caused",
    "drives",
]


def read_jsonl(path: Path) -> list[dict]:
    records = []
    if not path.exists():
        return records
    with path.open("r", encoding="utf-8-sig") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def top_journals(records: list[dict], limit: int = 8) -> list[tuple[str, int]]:
    counts = collections.Counter(r.get("journal", "") for r in records if r.get("journal"))
    return counts.most_common(limit)


def read_top_terms(path: Path, limit: int = 30) -> list[str]:
    if not path.exists():
        return []
    terms = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| ") and not line.startswith("| Term") and not line.startswith("|---"):
            parts = [part.strip() for part in line.strip("|").split("|")]
            if parts:
                terms.append(parts[0])
        if len(terms) >= limit:
            break
    return terms


def infer_style(records: list[dict]) -> dict[str, str]:
    abstracts = " ".join(r.get("abstract", "") for r in records)
    has_assoc = bool(re.search(r"\bassociated with\b", abstracts, flags=re.IGNORECASE))
    has_may = bool(re.search(r"\bmay\b", abstracts, flags=re.IGNORECASE))
    return {
        "Gap framing": "Use a problem-gap-objective progression; state the unresolved issue before the study objective.",
        "Objective wording": "Prefer precise verbs such as evaluate, investigate, examine, characterize, or determine.",
        "Result reporting": "Report direction, endpoint, model/cohort, and statistic when available.",
        "Mechanistic language": "Use cautious mechanistic wording unless perturbation or validation evidence is available.",
        "Clinical implication": "Use may/support/suggest language for translational implications unless clinical utility is directly tested.",
        "Limitation language": "State sample, model, measurement, and generalizability limits explicitly.",
        "Abstract conclusion": "Keep the conclusion evidence-bounded and avoid promotional novelty claims.",
        "Figure caption tone": "Use descriptive captions with assay/model, endpoint, n, and statistical annotation.",
        "Association preference": "Corpus frequently uses association language." if has_assoc else "No strong association-language signal detected.",
        "Hedging preference": "Corpus uses hedging; preserve may/suggest wording." if has_may else "Add hedging when evidence is preliminary.",
    }


def write_style_profile(records: list[dict], terms: list[str], output_dir: Path) -> None:
    style = infer_style(records)
    lines = [
        "# Journal Style Profile",
        "",
        "## Corpus Journals",
        "",
        "| Journal | Records |",
        "|---|---|",
    ]
    for journal, count in top_journals(records):
        lines.append(f"| {journal.replace('|', '/')} | {count} |")
    lines.extend(["", "## Style Dimensions", "", "| Style Dimension | Corpus Pattern | Target Manuscript Rule |", "|---|---|---|"])
    for key, value in style.items():
        lines.append(f"| {key} | {value} | Apply during English drafting |")
    lines.extend(["", "## Recommended Vocabulary", "", "| Use | Avoid | Reason |", "|---|---|---|"])
    for term in terms[:20]:
        lines.append(f"| {term} | vague synonym | Corpus-supported field term |")
    (output_dir / "journal_style_profile.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_language_guard(output_dir: Path) -> None:
    lines = [
        "# Language Guard",
        "",
        "| Check | Status | Fix |",
        "|---|---|---|",
        "| Preferred terminology used consistently | pending | Compare against term_bank.md |",
        "| Risky promotional words removed | pending | Replace with evidence-bounded wording |",
        "| Causal wording matches evidence strength | pending | Downgrade causal verbs when evidence is associative |",
        "| Field-standard assay/model terms used | pending | Check term bank and user methods |",
        "| Statistical wording precise | pending | Include effect size, CI, p value, or mark missing |",
        "| Limitations stated conservatively | pending | Add sample/model/generalizability limits |",
        "| No copied source sentences | pending | Rewrite corpus patterns in original wording |",
        "",
        "## Risky Words",
        "",
        ", ".join(PROMOTIONAL_WORDS),
        "",
        "## Causal Words To Check",
        "",
        ", ".join(CAUSAL_WORDS),
    ]
    (output_dir / "language_guard.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build corpus-derived style profile and language guard.")
    parser.add_argument("--corpus-dir", default="corpus_workspace")
    args = parser.parse_args()
    corpus_dir = Path(args.corpus_dir)
    records = read_jsonl(corpus_dir / "corpus_metadata.jsonl")
    terms = read_top_terms(corpus_dir / "term_bank.md")
    write_style_profile(records, terms, corpus_dir)
    write_language_guard(corpus_dir)
    print(f"Wrote style profile and language guard to {corpus_dir.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
