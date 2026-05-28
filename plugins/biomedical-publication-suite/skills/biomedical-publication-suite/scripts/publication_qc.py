#!/usr/bin/env python3
"""QC biomedical manuscript packages and publication-facing artifacts."""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
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

CORE_FILES_TIER1 = [
    "publication_context.yaml",
    "study_facts.md",
    "open_items.md",
]

CORE_FILES_TIER2 = [
    *CORE_FILES_TIER1,
    "narrative_brief.md",
    "manuscript.md",
]

PUBLICATION_FILES = [
    "manuscript.md",
    "abstract.md",
    "titles.md",
    "cover_letter.md",
    "response_to_reviewers.md",
]


@dataclass
class Finding:
    level: str
    target: str
    message: str


GLOBAL_PATTERNS: list[tuple[str, re.Pattern[str], str]] = [
    (
        "WARN",
        re.compile(
            r"\b(repo|repository|analysis workflow|project workflow|project narrative|skill|agent log|package directory|"
            r"analysis pipeline|notebook|script|codebase|control surface|claim register|results ledger|"
            r"open items|QC report|manuscript package|analysis spine|author check|quarantined)\b",
            re.I,
        ),
        "Possible internal process language in publication-facing text.",
    ),
    (
        "WARN",
        re.compile(
            r"\b(TBD|pending|placeholder|to be confirmed|authors will confirm|to be added|"
            r"will be inserted|IRB status pending|p-values will be inserted|demographics to be added)\b",
            re.I,
        ),
        "Missing-information language belongs in open_items.md or author notes, not publication text.",
    ),
    (
        "WARN",
        re.compile(
            r"\b(changed from|switched|updated analysis|revised model|demoted|elevated|"
            r"final model|final cohort|frozen cohort|locked cohort|cleanest|clearest|"
            r"we (decided|chose|opted|elected) to)\b",
            re.I,
        ),
        "Possible analysis-history leakage.",
    ),
    (
        "WARN",
        re.compile(
            r"\b(shown with reduced opacity|few patients|limited sample size|small group in this figure|"
            r"interpret cautiously|caution is warranted)\b",
            re.I,
        ),
        "Sparse-data or visual-design commentary should use counts, intervals, thresholds, captions, or footnotes.",
    ),
    (
        "WARN",
        re.compile(
            r"\b(importantly|notably|interestingly|crucially|strikingly|remarkably|"
            r"compelling|transformative|groundbreaking|promising|impactful)\b",
            re.I,
        ),
        "Inflated importance language; let the result and implication carry the claim.",
    ),
    (
        "WARN",
        re.compile(
            r"\b(delve|intricate|realm|ecosystem|tapestry|holistic|multifaceted|"
            r"rapidly evolving|leverage|unlock|seamless|shed light|deep dive|"
            r"paves the way|adds to the growing body of literature)\b",
            re.I,
        ),
        "AI-like filler or generic scientific prose.",
    ),
    (
        "WARN",
        re.compile(
            r"\b(first|next|then|subsequently),?\s+we\b|"
            r"\bwe\s+(then|proceeded to|went on to|were able to|successfully)\b|"
            r"\bthis\s+(analysis|study|figure|section)\s+(shows|demonstrates|was designed|will)\b|"
            r"\b(for completeness|as a sanity check)\b",
            re.I,
        ),
        "Memo voice found; state the current method or result without narrating the work process.",
    ),
]

CAUSAL_RE = re.compile(
    r"\b(caused|drove|led to|resulted in|rescued|protected against|proved)\b",
    re.I,
)
HEDGE_RE = re.compile(
    r"\b(may|might|appears? to|seems? to|somewhat|to some extent|could suggest|"
    r"possibly|perhaps)\b",
    re.I,
)
STACKED_HEDGE_RE = re.compile(
    r"\b(may|might|could)\s+(?:\w+\s+){0,3}(potentially|possibly|conceivably|suggest|indicate)\b",
    re.I,
)
CONCESSIVE_OPENER_RE = re.compile(
    r"^\s*(although|admittedly|to be sure|it should be (noted|acknowledged)|"
    r"we acknowledge)\b",
    re.I,
)
AMBIGUOUS_CAUSAL_RE = re.compile(r"\b(due to|because of)\b|(?<!-)\bmediated\b", re.I)
BOILERPLATE_LIMITATIONS_RE = re.compile(
    r"our study has several limitations|this study is not without limitations|"
    r"future (research|studies) (is|are) (needed|warranted)|additional studies are warranted|"
    r"to the best of our knowledge",
    re.I,
)
BRACKET_CITATION_RE = re.compile(r"\[(\d+(?:\s*[-,]\s*\d+)*)\]")
DOI_OR_PMID_RE = re.compile(r"(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+|PMID\s*:?\s*\d+)", re.I)
ESTIMATE_RE = re.compile(
    r"\b(OR|HR|RR|IRR|ARR|aOR|AUC|AUROC|C-statistic|CI|p\s*[<=>]|median|mean|"
    r"n\s*=|\d+(?:\.\d+)?%|\d+/\d+)\b",
    re.I,
)
SECTION_HEADER_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9])")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def normalize_section(name: str) -> str:
    cleaned = name.replace(chr(96), "")
    cleaned = re.sub(r"[*_#]", "", cleaned).strip().lower()
    cleaned = re.sub(r"[^a-z0-9 /-]+", "", cleaned)
    if "abstract" in cleaned:
        return "abstract"
    if "introduction" in cleaned or "background" in cleaned:
        return "introduction"
    if "method" in cleaned:
        return "methods"
    if "result" in cleaned or "finding" in cleaned:
        return "results"
    if "discussion" in cleaned:
        return "discussion"
    if "limitation" in cleaned:
        return "limitations"
    if "conclusion" in cleaned:
        return "conclusion"
    return cleaned or "body"


def split_sections(text: str) -> list[tuple[str, str]]:
    matches = list(SECTION_HEADER_RE.finditer(text))
    if not matches:
        return [("body", text)]
    sections: list[tuple[str, str]] = []
    if matches[0].start() > 0:
        sections.append(("body", text[: matches[0].start()]))
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        sections.append((normalize_section(match.group(2)), text[start:end]))
    return sections


def split_sentences(text: str) -> list[str]:
    return [s.strip() for s in SENTENCE_SPLIT_RE.split(text) if s.strip()]


def context_forbids_causal(context_path: Path) -> bool:
    if not context_path.exists():
        return False
    text = read_text(context_path)
    direct = re.search(r"causal_language_allowed\s*:\s*(false|no)\b", text, re.I)
    nested = re.search(
        r"causal_language_allowed\s*:\s*\n(?:\s+[^\n]*\n){0,6}\s+value\s*:\s*(false|no)\b",
        text,
        re.I,
    )
    return bool(direct or nested)


def citation_group_count(group: str) -> int:
    total = 0
    for piece in re.split(r"\s*,\s*", group):
        if "-" in piece:
            left, right = [p.strip() for p in piece.split("-", 1)]
            if left.isdigit() and right.isdigit():
                total += max(1, int(right) - int(left) + 1)
            else:
                total += 1
        elif piece.strip().isdigit():
            total += 1
    return total


def check_citation_bloat(text: str, target: str) -> list[Finding]:
    findings: list[Finding] = []
    for match in BRACKET_CITATION_RE.finditer(text):
        if citation_group_count(match.group(1)) >= 4:
            findings.append(
                Finding(
                    "INFO",
                    target,
                    "Citation cluster with four or more references found; verify each citation earns its place.",
                )
            )
    for sentence in split_sentences(text):
        if len(BRACKET_CITATION_RE.findall(sentence)) >= 2:
            findings.append(
                Finding(
                    "INFO",
                    target,
                    "Sentence contains multiple citation groups; consider consolidating or assigning claims more precisely.",
                )
            )
            break
    return findings


def lint_publication_text(text: str, target: str, observational: bool) -> list[Finding]:
    findings: list[Finding] = []
    for level, pattern, message in GLOBAL_PATTERNS:
        if pattern.search(text):
            findings.append(Finding(level, target, message))
    if STACKED_HEDGE_RE.search(text):
        findings.append(
            Finding(
                "WARN",
                target,
                "Stacked hedging found; keep uncertainty precise and localized.",
            )
        )
    if BOILERPLATE_LIMITATIONS_RE.search(text):
        findings.append(
            Finding(
                "WARN",
                target,
                "Boilerplate limitations language found; name actual limitations and likely bias direction.",
            )
        )
    findings.extend(check_citation_bloat(text, target))

    for section_name, body in split_sections(text):
        section_target = f"{target} [{section_name}]"
        if observational and CAUSAL_RE.search(body):
            findings.append(
                Finding(
                    "ERROR",
                    section_target,
                    "Causal language found while observational/nonexperimental language discipline is active.",
                )
            )
        if section_name in {"abstract", "results"} and HEDGE_RE.search(body):
            findings.append(
                Finding(
                    "WARN",
                    section_target,
                    "Hedging found in Abstract or Results; state significant results directly and quarantine uncertainty where it belongs.",
                )
            )
        if section_name in {"abstract", "results"}:
            for sentence in split_sentences(body):
                if CONCESSIVE_OPENER_RE.search(sentence):
                    findings.append(
                        Finding(
                            "WARN",
                            section_target,
                            "Concessive sentence opener found in a high-momentum section; avoid leading with caveats.",
                        )
                    )
                    break
        if observational and section_name not in {"methods", "limitations", "references"}:
            if AMBIGUOUS_CAUSAL_RE.search(body):
                findings.append(
                    Finding(
                        "WARN",
                        section_target,
                        "Potentially causal phrasing found; keep it only when it is literal endpoint language, field-standard terminology, or otherwise design-appropriate.",
                    )
                )
        if section_name == "results":
            early = [s for s in split_sentences(body) if len(s.split()) >= 6][:2]
            if early and not any(ESTIMATE_RE.search(s) for s in early):
                findings.append(
                    Finding(
                        "INFO",
                        section_target,
                        "Opening Results sentences contain no counts, estimates, or intervals; verify the section leads with findings.",
                    )
                )
    return findings


def check_citations(text: str, target: str, require_citations: bool) -> list[Finding]:
    findings: list[Finding] = []
    has_bracket = bool(BRACKET_CITATION_RE.search(text))
    has_doi_or_pmid = bool(DOI_OR_PMID_RE.search(text))
    if require_citations and not (has_bracket or has_doi_or_pmid):
        findings.append(
            Finding(
                "ERROR",
                target,
                "No citation markers, DOI, or PMID found while citation enforcement is active.",
            )
        )
    return findings


def check_csv_header(path: Path, expected: list[str]) -> list[Finding]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        try:
            header = next(csv.reader(handle))
        except StopIteration:
            return [Finding("ERROR", str(path), "CSV is empty.")]
    if header != expected:
        return [
            Finding(
                "ERROR",
                str(path),
                f"Unexpected CSV header. Expected: {','.join(expected)}",
            )
        ]
    return []


def check_claim_register(path: Path, require_claims: bool) -> list[Finding]:
    findings: list[Finding] = []
    if not path.exists():
        if require_claims:
            return [Finding("ERROR", str(path), "claim_register.csv is required but missing.")]
        return []
    findings.extend(check_csv_header(path, CLAIM_HEADER))
    if findings:
        return findings
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if require_claims and not rows:
        findings.append(Finding("ERROR", str(path), "Claim register has no claims."))
    for idx, row in enumerate(rows, start=2):
        status = (row.get("status") or "").strip()
        support = (row.get("support_type") or "").strip()
        source = (row.get("source_file") or "").strip()
        if status in {"supported", "inferred"} and not (support and source):
            findings.append(
                Finding(
                    "WARN",
                    f"{path}:{idx}",
                    "Supported or inferred claim lacks support_type or source_file.",
                )
            )
        if status == "unsupported_remove_or_weaken":
            findings.append(
                Finding(
                    "ERROR",
                    f"{path}:{idx}",
                    "Claim is marked unsupported_remove_or_weaken. Revise the artifact or explain why it remains.",
                )
            )
    return findings


def check_result_integrity(package: Path) -> list[Finding]:
    claim_path = package / "claim_register.csv"
    result_path = package / "results_ledger.csv"
    if not claim_path.exists() or not result_path.exists():
        return []
    findings: list[Finding] = []
    findings.extend(check_csv_header(result_path, RESULTS_HEADER))
    if findings:
        return findings
    with result_path.open(newline="", encoding="utf-8") as handle:
        result_ids = {row.get("result_id", "").strip() for row in csv.DictReader(handle)}
    result_ids.discard("")
    if not result_ids:
        return []
    with claim_path.open(newline="", encoding="utf-8") as handle:
        for idx, row in enumerate(csv.DictReader(handle), start=2):
            result_id = (row.get("result_id") or "").strip()
            if result_id and result_id not in result_ids:
                findings.append(
                    Finding(
                        "ERROR",
                        f"{claim_path}:{idx}",
                        f"result_id {result_id!r} does not resolve in results_ledger.csv.",
                    )
                )
    return findings


def extract_part1_narrative(text: str) -> str:
    part1 = re.search(r"part\s*1\s*[-:]\s*(scientific|manuscript|external|project)\s+narrative", text, re.I)
    part2 = re.search(r"part\s*2\s*[-:]\s*editorial rationale", text, re.I)
    if part1 and part2 and part2.start() > part1.end():
        return text[part1.end() : part2.start()]
    if part1:
        return text[part1.end() :]
    return ""


def check_narrative_audit(path: Path, observational: bool) -> list[Finding]:
    if not path.exists():
        return []
    text = read_text(path)
    findings: list[Finding] = []
    if not re.search(r"Part\s*1\s*[-:]\s*(Scientific|Manuscript|External)\s+Narrative", text, re.I):
        findings.append(
            Finding(
                "WARN",
                str(path),
                "Narrative audit should use Part 1 - Scientific Narrative, Manuscript Narrative, or External Narrative.",
            )
        )
    if not re.search(r"Part\s*2\s*[-:]\s*Editorial Rationale", text, re.I):
        findings.append(
            Finding(
                "WARN",
                str(path),
                "Narrative audit should include Part 2 - Editorial Rationale.",
            )
        )
    part1 = extract_part1_narrative(text)
    if part1:
        findings.extend(lint_publication_text(part1, f"{path} [Part 1]", observational))
    return findings


def check_display_text(path: Path) -> list[Finding]:
    if not path.exists():
        return []
    text = read_text(path)
    findings: list[Finding] = []
    label_prefixes = ("title", "subtitle", "axis", "panel", "legend", "row label", "column header")
    for idx, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or ":" not in stripped:
            continue
        key, value = [part.strip() for part in stripped.split(":", 1)]
        key_norm = key.lower().strip("-* ")
        if not any(key_norm.startswith(prefix) for prefix in label_prefixes):
            continue
        if key_norm.startswith("title") and len(value.split()) > 15:
            findings.append(
                Finding(
                    "WARN",
                    f"{path}:{idx}",
                    "Figure or table title is long; titles should identify, not explain.",
                )
            )
        if re.search(r"\b(because|due to|in order to|this shows|this demonstrates|we)\b", value, re.I):
            findings.append(
                Finding(
                    "WARN",
                    f"{path}:{idx}",
                    "Label-prose collapse found; move explanations to captions, footnotes, Results, or Notes.",
                )
            )
        if re.search(r"\b(limited|preliminary|caution|few patients|small sample|interpret cautiously)\b", value, re.I):
            findings.append(
                Finding(
                    "WARN",
                    f"{path}:{idx}",
                    "Caveat appears in a label field; use counts, intervals, thresholds, captions, or footnotes.",
                )
            )
    return findings


def package_findings(args: argparse.Namespace) -> list[Finding]:
    root = Path(args.repo_root).resolve()
    package = root / args.package_dir
    findings: list[Finding] = []

    if not package.exists():
        return [Finding("ERROR", str(package), "Publication package directory does not exist.")]

    core_files = CORE_FILES_TIER1 if args.tier == "1" else CORE_FILES_TIER2
    for rel in core_files:
        if not (package / rel).exists():
            findings.append(Finding("ERROR", str(package / rel), "Required core file is missing."))

    observational = args.observational or context_forbids_causal(package / "publication_context.yaml")

    for rel in PUBLICATION_FILES:
        path = package / rel
        if path.exists():
            text = read_text(path)
            findings.extend(lint_publication_text(text, str(path), observational))
            findings.extend(check_citations(text, str(path), args.require_citations and rel == "manuscript.md"))

    findings.extend(check_display_text(package / "display_text.md"))
    findings.extend(check_claim_register(package / "claim_register.csv", args.require_claim_register))
    findings.extend(check_csv_header(package / "results_ledger.csv", RESULTS_HEADER))
    findings.extend(check_result_integrity(package))
    findings.extend(check_narrative_audit(package / "narrative_audit.md", observational))

    return findings


def format_report(findings: list[Finding]) -> str:
    errors = [f for f in findings if f.level == "ERROR"]
    warnings = [f for f in findings if f.level == "WARN"]
    infos = [f for f in findings if f.level == "INFO"]
    lines = [
        "# Publication QC Report",
        "",
        "This report is a mechanical tripwire, not an editor. Findings flag patterns that are often problems; they are not edits. The senior-editor read and manuscript voice audit govern final wording. Do not reword sound, field-standard, or design-appropriate prose only to clear a warning.",
        "",
        f"Errors: {len(errors)}",
        f"Warnings: {len(warnings)}",
        f"Info: {len(infos)}",
        "",
    ]
    if not findings:
        lines.append("No findings.")
    else:
        for item in findings:
            lines.append(f"- {item.level}: {item.target}: {item.message}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository or project root.")
    parser.add_argument("--package-dir", default="manuscript", help="Publication package directory.")
    parser.add_argument("--tier", choices=("1", "2"), default="2", help="Package tier to validate.")
    parser.add_argument("--file", help="Single publication-facing artifact to lint.")
    parser.add_argument("--observational", action="store_true", help="Forbid causal language.")
    parser.add_argument(
        "--strict-confidence",
        action="store_true",
        help="Deprecated compatibility flag; confidence checks are now section-aware by default.",
    )
    parser.add_argument("--require-claim-register", action="store_true", help="Require nonempty claim register.")
    parser.add_argument("--require-citations", action="store_true", help="Require citation markers in manuscript or file.")
    parser.add_argument("--fail-on-warn", action="store_true", help="Exit nonzero when warnings are present.")
    parser.add_argument("--no-write-report", action="store_true", help="Do not update qc_report.md in package mode.")
    args = parser.parse_args()

    if args.file:
        path = Path(args.file).resolve()
        if not path.exists():
            findings = [Finding("ERROR", str(path), "File does not exist.")]
        else:
            text = read_text(path)
            findings = lint_publication_text(text, str(path), args.observational)
            findings.extend(check_citations(text, str(path), args.require_citations))
    else:
        findings = package_findings(args)

    report = format_report(findings)
    print(report)
    if not args.file and not args.no_write_report:
        package = Path(args.repo_root).resolve() / args.package_dir
        if package.exists():
            (package / "qc_report.md").write_text(report, encoding="utf-8")

    has_error = any(item.level == "ERROR" for item in findings)
    has_warn = any(item.level == "WARN" for item in findings)
    if has_error or (args.fail_on_warn and has_warn):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
