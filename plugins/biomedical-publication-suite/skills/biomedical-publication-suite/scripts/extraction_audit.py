#!/usr/bin/env python3
"""Audit literature extraction rows for source grounding."""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path


REQUIRED_COLUMNS = [
    "extraction_id",
    "source_id",
    "field_group",
    "field_name",
    "field_value",
    "source_locator",
    "source_quote",
    "status",
]

NUMERIC_RE = re.compile(r"\d")
NUMERIC_FIELD_RE = re.compile(
    r"\b(sample|n_|n\b|number|outcome|event|effect|estimate|rate|risk|odds|hazard|mean|median|"
    r"proportion|percent|percentage|adverse|mortality|survival|follow[- ]?up)\b",
    re.I,
)


@dataclass
class Finding:
    level: str
    row: int
    message: str


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def present(row: dict[str, str], key: str) -> bool:
    return bool((row.get(key) or "").strip())


def audit(path: Path) -> list[Finding]:
    fieldnames, rows = read_rows(path)
    findings: list[Finding] = []
    missing = [col for col in REQUIRED_COLUMNS if col not in fieldnames]
    if missing:
        return [Finding("ERROR", 1, "Missing required columns: " + ", ".join(missing))]

    for row_number, row in enumerate(rows, start=2):
        status = (row.get("status") or "").strip().lower()
        value = (row.get("field_value") or "").strip()
        if status in {"not_reported", "not found", "not_found", "unclear", "needs_full_text"} and not value:
            continue
        if value and not present(row, "source_id"):
            findings.append(Finding("ERROR", row_number, "Extracted value lacks source_id."))
        if value and not present(row, "source_locator"):
            findings.append(Finding("ERROR", row_number, "Extracted value lacks source_locator."))
        if value and not present(row, "source_quote"):
            findings.append(Finding("ERROR", row_number, "Extracted value lacks source_quote."))

        field_name = row.get("field_name") or ""
        is_numeric = bool(value and NUMERIC_RE.search(value) and NUMERIC_FIELD_RE.search(field_name))
        if is_numeric:
            for col in ["denominator", "unit", "timepoint", "comparison"]:
                if col in fieldnames and not present(row, col):
                    findings.append(Finding("WARN", row_number, f"Numeric extraction lacks {col}."))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="manuscript/extraction_ledger.csv", help="Extraction ledger CSV.")
    parser.add_argument("--fail-on-warn", action="store_true", help="Exit nonzero when warnings are present.")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.exists():
        print(f"ERROR: {path}: extraction ledger does not exist.")
        return 2
    findings = audit(path)
    errors = [f for f in findings if f.level == "ERROR"]
    warnings = [f for f in findings if f.level == "WARN"]
    print(f"Extraction audit: {len(errors)} errors, {len(warnings)} warnings")
    for finding in findings:
        print(f"- {finding.level}: row {finding.row}: {finding.message}")
    return 1 if errors or (args.fail_on_warn and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
