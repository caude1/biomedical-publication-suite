#!/usr/bin/env python3
"""Audit literature-backed claims against the verified literature register."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Finding:
    level: str
    target: str
    message: str


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def norm(value: str | None) -> str:
    return (value or "").strip()


def audit(claim_register: Path, literature_register: Path) -> list[Finding]:
    findings: list[Finding] = []
    if not claim_register.exists():
        return [Finding("ERROR", str(claim_register), "claim_register.csv is missing.")]
    if not literature_register.exists():
        return [Finding("ERROR", str(literature_register), "literature_register.csv is missing.")]

    literature_rows = read_csv(literature_register)
    source_status: dict[str, str] = {}
    for row in literature_rows:
        source_id = norm(row.get("source_id") or row.get("study_id"))
        if not source_id:
            continue
        source_status[source_id] = norm(row.get("verify_status") or row.get("source_verify_status")).lower()

    for row_number, row in enumerate(read_csv(claim_register), start=2):
        support_type = norm(row.get("support_type")).lower()
        source_id = norm(row.get("source_id"))
        needs_literature = support_type == "external_citation" or bool(source_id)
        if not needs_literature:
            continue
        if not source_id:
            findings.append(Finding("ERROR", f"{claim_register}:{row_number}", "External citation claim lacks source_id."))
            continue
        registered_status = source_status.get(source_id)
        if registered_status is None:
            findings.append(
                Finding("ERROR", f"{claim_register}:{row_number}", f"source_id {source_id!r} is absent from literature_register.csv.")
            )
            continue
        if registered_status != "verified":
            findings.append(
                Finding("ERROR", f"{claim_register}:{row_number}", f"source_id {source_id!r} is not verified.")
            )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claim-register", default="manuscript/claim_register.csv", help="Claim register CSV.")
    parser.add_argument("--literature-register", default="manuscript/literature_register.csv", help="Literature register CSV.")
    args = parser.parse_args()

    findings = audit(Path(args.claim_register), Path(args.literature_register))
    errors = [f for f in findings if f.level == "ERROR"]
    warnings = [f for f in findings if f.level == "WARN"]
    print(f"Citation audit: {len(errors)} errors, {len(warnings)} warnings")
    for finding in findings:
        print(f"- {finding.level}: {finding.target}: {finding.message}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
