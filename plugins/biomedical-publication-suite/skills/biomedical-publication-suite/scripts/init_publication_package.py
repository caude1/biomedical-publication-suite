#!/usr/bin/env python3
"""Initialize a lean biomedical publication package."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


CLAIM_HEADER = [
    "claim_id",
    "artifact",
    "section",
    "claim_text",
    "claim_type",
    "support_type",
    "source_file",
    "source_locator",
    "result_id",
    "citation_locator",
    "status",
    "notes",
]

RESULTS_HEADER = [
    "result_id",
    "outcome_type",
    "outcome_name",
    "population",
    "model_label",
    "estimate_type",
    "estimate",
    "ci_lower",
    "ci_upper",
    "p_value",
    "n_total",
    "n_events",
    "time_at_risk",
    "unit",
    "source_file",
    "source_locator",
    "notes",
]


PUBLICATION_CONTEXT = """working_title:
  value: ""
  source: ""
  notes: ""
study_type:
  value: ""
  source: ""
  notes: "observational, randomized, diagnostic, prediction, systematic review, translational, or other"
reporting_guideline:
  value: ""
  source: ""
  notes: "CONSORT, STROBE, STARD, TRIPOD, PRISMA, or domain-specific"
causal_language_allowed:
  value: false
  source: "default"
  notes: "Set true only when design and estimand justify causal language."
primary_question:
  value: ""
  source: ""
  notes: ""
hypothesis:
  value: ""
  source: ""
  notes: ""
primary_outcome:
  value: ""
  source: ""
  notes: ""
primary_analysis:
  value: ""
  source: ""
  notes: ""
authoritative_files: []
known_limitations: []
open_author_checks: []
"""

STUDY_FACTS = """# Study Facts

## Study Design and Setting

## Data Source and Dates

## Population and Analytic Cohort

## Exposure, Intervention, or Comparator

## Primary Endpoint

## Secondary or Exploratory Endpoints

## Covariates and Adjustment Set

## Primary Analysis

## Key Results

## Key References

## Missing or Uncertain Facts

## Authoritative Files
"""

NARRATIVE_BRIEF = """# Narrative Brief

## Central Thesis

## Context and Gap

## Hypothesis or Objective

## Approach

## Headline Findings, Ranked

## Secondary or Subordinate Findings

## Claim Boundaries

## Section Storyline

## Open Narrative Risks
"""

MANUSCRIPT = """# Manuscript

## Abstract

## Introduction

## Methods

## Results

## Discussion

### Limitations

## Conclusion
"""

DISPLAY_TEXT = """# Display Text

## Figure or Table 1

Title:

Subtitle:

Axis labels:

Panel labels:

Legend keys:

Caption:

Footnotes:
"""

OPEN_ITEMS = """# Open Items

## Blocking

## Author Checks

## Citation Checks

## Journal Checks
"""

ARTIFACT_REGISTER = """# Artifact Register

| Artifact | Purpose | Source | Status | Notes |
|---|---|---|---|---|
"""

JOURNAL_REQUIREMENTS = """# Journal Requirements

- Target journal:
- Article type:
- Abstract structure:
- Word limit:
- Display limits:
- Reference style:
- Required statements:
- Open journal checks:
"""

REPORTING_CHECKLIST = """# Reporting Checklist

## Governing Framework

| Item | Requirement | Manuscript Location | Status | Notes |
|---|---|---|---|---|
"""

SUBMISSION_READINESS = """# Submission Readiness

## Overall Status

## Blocking Issues

## Nonblocking Issues

## Author Checks

## Journal Checks

## QC Summary
"""


def write_text(path: Path, content: str, overwrite: bool) -> bool:
    if path.exists() and not overwrite:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def write_csv(path: Path, header: list[str], overwrite: bool) -> bool:
    if path.exists() and not overwrite:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        csv.writer(handle).writerow(header)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository or project root.")
    parser.add_argument("--package-dir", default="manuscript", help="Publication package directory.")
    parser.add_argument(
        "--tier",
        choices=("1", "2"),
        default="2",
        help="Backward-compatible alias: tier 1 creates minimal control files; tier 2 creates the lean manuscript drafting package.",
    )
    parser.add_argument(
        "--profile",
        choices=("lean", "submission"),
        default="lean",
        help="lean creates drafting files; submission adds final verification and journal files.",
    )
    parser.add_argument(
        "--include-display-text",
        action="store_true",
        help="Create display_text.md when drafting or QCing figure/table text.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing package files.")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    package = root / args.package_dir
    package.mkdir(parents=True, exist_ok=True)

    templates = {
        "publication_context.yaml": PUBLICATION_CONTEXT,
        "study_facts.md": STUDY_FACTS,
        "open_items.md": OPEN_ITEMS,
    }
    if args.tier == "2":
        templates.update(
            {
                "narrative_brief.md": NARRATIVE_BRIEF,
                "manuscript.md": MANUSCRIPT,
            }
        )
    if args.include_display_text:
        templates["display_text.md"] = DISPLAY_TEXT
    if args.profile == "submission":
        templates.update(
            {
                "artifact_register.md": ARTIFACT_REGISTER,
                "journal_requirements.md": JOURNAL_REQUIREMENTS,
                "reporting_checklist.md": REPORTING_CHECKLIST,
                "submission_readiness.md": SUBMISSION_READINESS,
            }
        )

    created: list[str] = []
    skipped: list[str] = []
    for rel, text in templates.items():
        if write_text(package / rel, text, args.overwrite):
            created.append(rel)
        else:
            skipped.append(rel)

    csv_files: dict[str, list[str]] = {}
    if args.profile == "submission":
        csv_files["claim_register.csv"] = CLAIM_HEADER
        csv_files["results_ledger.csv"] = RESULTS_HEADER

    for rel, header in csv_files.items():
        if write_csv(package / rel, header, args.overwrite):
            created.append(rel)
        else:
            skipped.append(rel)

    print(f"Publication package: {package}")
    print(f"Profile: {args.profile}")
    if created:
        print("Created:")
        for item in created:
            print(f"  - {item}")
    if skipped:
        print("Skipped existing files:")
        for item in skipped:
            print(f"  - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
