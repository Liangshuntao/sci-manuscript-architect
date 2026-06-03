#!/usr/bin/env python3
"""Extract terminology and safe phrase-pattern candidates from a corpus JSONL."""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path


STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has",
    "have", "in", "into", "is", "it", "its", "of", "on", "or", "that",
    "the", "their", "these", "this", "to", "was", "were", "with", "we",
    "our", "using", "used", "use", "study", "studies", "results", "result",
}

PATTERNS = {
    "gap framing": [
        r"\bhowever[, ]+[^.]{20,160}\.",
        r"\bremains? (?:unclear|unknown|poorly understood)[^.]*\.",
        r"\blimited (?:evidence|data|knowledge)[^.]*\.",
    ],
    "objective statement": [
        r"\bwe (?:aimed|sought) to [^.]*\.",
        r"\bthis study (?:aimed|investigated|evaluated|examined) [^.]*\.",
    ],
    "result reporting": [
        r"\bwe (?:found|observed|identified|demonstrated) [^.]*\.",
        r"\bwas associated with [^.]*\.",
    ],
    "cautious implication": [
        r"\bmay (?:suggest|indicate|reflect|contribute to) [^.]*\.",
        r"\bthese findings (?:suggest|indicate|support) [^.]*\.",
    ],
    "limitation": [
        r"\b(?:limitations?|caveats?) (?:include|included) [^.]*\.",
        r"\bfurther (?:studies|validation|research) (?:are|is) needed [^.]*\.",
    ],
}


def read_records(path: Path) -> list[dict]:
    records = []
    with path.open("r", encoding="utf-8-sig") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def tokenize(text: str) -> list[str]:
    return re.findall(r"[A-Za-z][A-Za-z0-9-]+", text.lower())


def extract_ngrams(tokens: list[str], min_n: int = 2, max_n: int = 5) -> collections.Counter:
    counts: collections.Counter = collections.Counter()
    for n in range(min_n, max_n + 1):
        for i in range(0, len(tokens) - n + 1):
            chunk = tokens[i : i + n]
            if chunk[0] in STOPWORDS or chunk[-1] in STOPWORDS:
                continue
            if sum(1 for word in chunk if word not in STOPWORDS) < 2:
                continue
            counts[" ".join(chunk)] += 1
    return counts


def extract_patterns(text: str) -> dict[str, collections.Counter]:
    found = {name: collections.Counter() for name in PATTERNS}
    normalized = " ".join(text.split())
    for name, regexes in PATTERNS.items():
        for regex in regexes:
            for match in re.findall(regex, normalized, flags=re.IGNORECASE):
                found[name][generalize(match)] += 1
    return found


def generalize(sentence: str) -> str:
    sentence = re.sub(r"\b\d+(?:\.\d+)?%?\b", "[value]", sentence)
    sentence = re.sub(r"\bp\s*[<=>]\s*0?\.\d+\b", "[p value]", sentence, flags=re.IGNORECASE)
    return sentence.strip()


def write_term_bank(counts: collections.Counter, output_dir: Path, limit: int) -> None:
    lines = [
        "# Term Bank",
        "",
        "| Term | Category | Preferred Form | Avoid | Example Use | Source Count | Status |",
        "|---|---|---|---|---|---|---|",
    ]
    for term, count in counts.most_common(limit):
        lines.append(f"| {term} | verify | {term} | | | {count} | verify |")
    (output_dir / "term_bank.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_phrase_bank(patterns: dict[str, collections.Counter], output_dir: Path, limit: int) -> None:
    lines = [
        "# Phrase Pattern Bank",
        "",
        "| Pattern Type | Safe Pattern | Use For | Strength | Notes |",
        "|---|---|---|---|---|",
    ]
    for pattern_type, counter in patterns.items():
        for phrase, count in counter.most_common(limit):
            safe = phrase.replace("|", "/")
            lines.append(f"| {pattern_type} | {safe} | {pattern_type} | corpus-derived | Seen {count} time(s); rewrite before use |")
    (output_dir / "phrase_pattern_bank.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract term and phrase banks from corpus_metadata.jsonl.")
    parser.add_argument("--input", default="corpus_workspace/corpus_metadata.jsonl")
    parser.add_argument("--output-dir", default="corpus_workspace")
    parser.add_argument("--term-limit", type=int, default=120)
    parser.add_argument("--pattern-limit", type=int, default=8)
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    records = read_records(input_path)
    text = "\n".join((r.get("title", "") + "\n" + r.get("abstract", "")) for r in records)
    tokens = [tok for tok in tokenize(text) if tok not in STOPWORDS and len(tok) > 2]
    ngrams = extract_ngrams(tokens)
    pattern_counts = extract_patterns(text)
    write_term_bank(ngrams, output_dir, args.term_limit)
    write_phrase_bank(pattern_counts, output_dir, args.pattern_limit)
    print(f"Wrote term and phrase banks to {output_dir.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
