#!/usr/bin/env python3
"""Verify literature identifiers against public metadata sources."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path


OUTPUT_FIELDS = [
    "verify_status",
    "verified_pmid",
    "verified_doi",
    "verified_title",
    "verified_year",
    "verification_source",
    "verification_message",
]


def norm_text(value: str | None) -> str:
    value = (value or "").lower()
    value = re.sub(r"https?://doi.org/", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def norm_doi(value: str | None) -> str:
    value = (value or "").strip().lower()
    value = value.replace("https://doi.org/", "").replace("http://doi.org/", "")
    return value.rstrip(".,;")


def title_similarity(left: str | None, right: str | None) -> float:
    a = norm_text(left)
    b = norm_text(right)
    if not a or not b:
        return 0.0
    if a in b or b in a:
        return 1.0
    return SequenceMatcher(None, a, b).ratio()


def fetch_json(url: str, timeout: int = 20) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "biomedical-publication-suite/identifier-verifier"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def pubmed_esummary(pmid: str, email: str | None = None) -> dict | None:
    pmid = re.sub(r"\D+", "", pmid or "")
    if not pmid:
        return None
    params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "json",
        "tool": "biomedical_publication_suite",
    }
    if email:
        params["email"] = email
    api_key = os.environ.get("NCBI_API_KEY")
    if api_key:
        params["api_key"] = api_key
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(params)
    data = fetch_json(url)
    record = data.get("result", {}).get(pmid)
    if not isinstance(record, dict):
        return None
    doi = ""
    for article_id in record.get("articleids", []):
        if article_id.get("idtype") == "doi":
            doi = article_id.get("value", "")
            break
    return {
        "pmid": pmid,
        "doi": doi,
        "title": record.get("title", ""),
        "year": str(record.get("pubdate", ""))[:4],
        "source": "pubmed",
    }


def crossref_work(doi: str) -> dict | None:
    doi_norm = norm_doi(doi)
    if not doi_norm:
        return None
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi_norm, safe="")
    data = fetch_json(url)
    msg = data.get("message", {})
    titles = msg.get("title") or []
    year = ""
    for key in ["published-print", "published-online", "created", "issued"]:
        parts = (((msg.get(key) or {}).get("date-parts") or [[]])[0])
        if parts:
            year = str(parts[0])
            break
    return {
        "pmid": "",
        "doi": doi_norm,
        "title": titles[0] if titles else "",
        "year": year,
        "source": "crossref",
    }


def verify_row(row: dict[str, str], title_threshold: float, allow_year_miss: bool) -> dict[str, str]:
    expected_title = row.get("title") or row.get("article_title") or row.get("citation_title") or ""
    expected_year = (row.get("year") or "").strip()[:4]
    expected_doi = norm_doi(row.get("doi"))
    pmid = (row.get("pmid") or row.get("PMID") or "").strip()
    doi = expected_doi

    candidates: list[dict] = []
    messages: list[str] = []

    if pmid:
        try:
            record = pubmed_esummary(pmid, row.get("email"))
            if record:
                candidates.append(record)
            else:
                messages.append("PMID did not resolve in PubMed")
        except Exception as exc:  # pragma: no cover - network failure path
            messages.append(f"PubMed lookup failed: {exc}")

    if doi:
        try:
            record = crossref_work(doi)
            if record:
                candidates.append(record)
            else:
                messages.append("DOI did not resolve in Crossref")
        except Exception as exc:  # pragma: no cover - network failure path
            messages.append(f"Crossref lookup failed: {exc}")

    if not candidates:
        return {
            "verify_status": "quarantine",
            "verified_pmid": "",
            "verified_doi": "",
            "verified_title": "",
            "verified_year": "",
            "verification_source": "",
            "verification_message": "; ".join(messages) or "No PMID or DOI available for verification",
        }

    best = max(candidates, key=lambda item: title_similarity(expected_title, item.get("title")))
    similarity = title_similarity(expected_title, best.get("title"))
    year_ok = not expected_year or not best.get("year") or expected_year == str(best.get("year"))[:4]
    doi_ok = not expected_doi or not best.get("doi") or expected_doi == norm_doi(best.get("doi"))
    title_ok = not expected_title or similarity >= title_threshold

    status = "verified" if title_ok and (year_ok or allow_year_miss) and doi_ok else "quarantine"
    problems: list[str] = []
    if not title_ok:
        problems.append(f"title similarity {similarity:.2f} below threshold {title_threshold:.2f}")
    if not year_ok and not allow_year_miss:
        problems.append(f"year mismatch: expected {expected_year}, found {best.get('year')}")
    if not doi_ok:
        problems.append(f"DOI mismatch: expected {expected_doi}, found {best.get('doi')}")
    if not problems:
        problems.append("identifier and title/year checks passed")

    return {
        "verify_status": status,
        "verified_pmid": best.get("pmid", ""),
        "verified_doi": norm_doi(best.get("doi")),
        "verified_title": best.get("title", ""),
        "verified_year": str(best.get("year", ""))[:4],
        "verification_source": best.get("source", ""),
        "verification_message": "; ".join(problems),
    }


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="manuscript/literature_register.csv", help="Literature register CSV.")
    parser.add_argument("--verified-output", default="manuscript/verified_sources.csv", help="Verified rows output CSV.")
    parser.add_argument("--quarantine-output", default="manuscript/quarantine_sources.csv", help="Quarantined rows output CSV.")
    parser.add_argument("--title-threshold", type=float, default=0.82, help="Minimum normalized title similarity.")
    parser.add_argument("--allow-year-miss", action="store_true", help="Do not quarantine when year is missing or mismatched.")
    parser.add_argument("--fail-on-quarantine", action="store_true", help="Exit nonzero when any row is quarantined.")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Input not found: {input_path}", file=sys.stderr)
        return 2

    fieldnames, rows = read_rows(input_path)
    output_fields = fieldnames + [field for field in OUTPUT_FIELDS if field not in fieldnames]
    verified: list[dict[str, str]] = []
    quarantine: list[dict[str, str]] = []

    for row in rows:
        result = verify_row(row, args.title_threshold, args.allow_year_miss)
        merged = {**row, **result}
        if result["verify_status"] == "verified":
            verified.append(merged)
        else:
            quarantine.append(merged)

    write_rows(Path(args.verified_output), output_fields, verified)
    write_rows(Path(args.quarantine_output), output_fields, quarantine)

    print(f"Verified: {len(verified)}")
    print(f"Quarantined: {len(quarantine)}")
    if quarantine:
        print(f"Quarantine file: {args.quarantine_output}")
    return 1 if quarantine and args.fail_on_quarantine else 0


if __name__ == "__main__":
    raise SystemExit(main())
