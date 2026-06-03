#!/usr/bin/env python3
"""Collect biomedical corpus metadata and abstracts from public APIs.

This script stores metadata/abstracts, not copyrighted full text. Outputs:
corpus_metadata.jsonl and corpus_index.md.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


def fetch_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_text(url: str) -> str:
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def pubmed_search(query: str, max_results: int, since_year: int | None, email: str | None) -> list[dict]:
    term = query
    if since_year:
        term = f"({query}) AND ({since_year}:3000[pdat])"
    params = {
        "db": "pubmed",
        "term": term,
        "retmode": "json",
        "retmax": str(max_results),
        "sort": "relevance",
    }
    if email:
        params["email"] = email
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    ids = fetch_json(search_url).get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    time.sleep(0.35)
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml",
    }
    if email:
        fetch_params["email"] = email
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + urllib.parse.urlencode(fetch_params)
    root = ET.fromstring(fetch_text(fetch_url))
    records = []
    for article in root.findall(".//PubmedArticle"):
        medline = article.find("MedlineCitation")
        if medline is None:
            continue
        pmid = text_at(medline, "PMID")
        title = "".join(article.findtext(".//ArticleTitle", default="").split())
        title = article.findtext(".//ArticleTitle", default="").strip()
        journal = article.findtext(".//Journal/Title", default="").strip()
        year = first_year(article)
        doi = ""
        for aid in article.findall(".//ArticleId"):
            if aid.attrib.get("IdType") == "doi":
                doi = (aid.text or "").strip()
                break
        abstract_parts = [(" ".join(x.itertext())).strip() for x in article.findall(".//Abstract/AbstractText")]
        records.append(
            {
                "source": "PubMed",
                "id": pmid,
                "title": title,
                "year": year,
                "journal": journal,
                "doi": doi,
                "abstract": "\n".join(part for part in abstract_parts if part),
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
            }
        )
    return records


def text_at(node: ET.Element, path: str) -> str:
    child = node.find(path)
    return (child.text or "").strip() if child is not None else ""


def first_year(article: ET.Element) -> str:
    for path in (".//ArticleDate/Year", ".//PubDate/Year", ".//PubMedPubDate/Year"):
        year = article.findtext(path, default="").strip()
        if year:
            return year
    return ""


def openalex_search(query: str, max_results: int, since_year: int | None) -> list[dict]:
    filters = []
    if since_year:
        filters.append(f"from_publication_date:{since_year}-01-01")
    params = {
        "search": query,
        "per-page": str(min(max_results, 200)),
        "sort": "relevance_score:desc",
    }
    if filters:
        params["filter"] = ",".join(filters)
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = fetch_json(url)
    records = []
    for item in data.get("results", []):
        abstract = reconstruct_openalex_abstract(item.get("abstract_inverted_index") or {})
        doi = item.get("doi") or ""
        records.append(
            {
                "source": "OpenAlex",
                "id": item.get("id", ""),
                "title": item.get("title", "") or "",
                "year": str(item.get("publication_year", "") or ""),
                "journal": (item.get("primary_location") or {}).get("source", {}).get("display_name", "") or "",
                "doi": doi.replace("https://doi.org/", ""),
                "abstract": abstract,
                "url": item.get("id", ""),
                "cited_by_count": item.get("cited_by_count", 0),
            }
        )
    return records


def reconstruct_openalex_abstract(index: dict[str, list[int]]) -> str:
    if not index:
        return ""
    positioned = []
    for word, positions in index.items():
        for pos in positions:
            positioned.append((pos, word))
    return " ".join(word for _, word in sorted(positioned))


def dedupe(records: list[dict]) -> list[dict]:
    seen = set()
    result = []
    for record in records:
        key = (record.get("doi") or record.get("title") or record.get("id") or "").lower()
        if not key or key in seen:
            continue
        seen.add(key)
        result.append(record)
    return result


def write_outputs(records: list[dict], output_dir: Path, query: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    jsonl = output_dir / "corpus_metadata.jsonl"
    with jsonl.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    index = output_dir / "corpus_index.md"
    lines = [
        "# Corpus Index",
        "",
        f"Query: `{query}`",
        f"Records: {len(records)}",
        "",
        "| ID | Year | Journal | Title | Source | DOI/URL |",
        "|---|---|---|---|---|---|",
    ]
    for idx, record in enumerate(records, 1):
        title = clean_cell(record.get("title", ""))
        journal = clean_cell(record.get("journal", ""))
        doi_or_url = clean_cell(record.get("doi") or record.get("url", ""))
        lines.append(f"| C{idx:03d} | {record.get('year','')} | {journal} | {title} | {record.get('source','')} | {doi_or_url} |")
    index.write_text("\n".join(lines) + "\n", encoding="utf-8")


def clean_cell(value: str) -> str:
    return " ".join(str(value).replace("|", "/").split())


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect field corpus metadata and abstracts.")
    parser.add_argument("--query", required=True, help="Search query.")
    parser.add_argument("--output-dir", default="corpus_workspace", help="Corpus workspace.")
    parser.add_argument("--source", choices=["pubmed", "openalex", "both"], default="both")
    parser.add_argument("--max-results", type=int, default=50)
    parser.add_argument("--since-year", type=int)
    parser.add_argument("--email", help="Optional email for NCBI requests.")
    args = parser.parse_args()

    records: list[dict] = []
    if args.source in {"pubmed", "both"}:
        records.extend(pubmed_search(args.query, args.max_results, args.since_year, args.email))
    if args.source in {"openalex", "both"}:
        records.extend(openalex_search(args.query, args.max_results, args.since_year))
    records = dedupe(records)[: args.max_results]
    write_outputs(records, Path(args.output_dir), args.query)
    print(f"Wrote {len(records)} records to {Path(args.output_dir).resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
