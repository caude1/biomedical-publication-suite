# Literature Intelligence

Use this reference when the task is to find papers, verify citations, extract study data, or build literature support for a manuscript, review, grant background, introduction, discussion, or reviewer response.

## Core Rule

Discovery may be broad and agentic. Inclusion, identifiers, and extraction must be deterministic and source-grounded.

Search like an expert reviewer: use multiple sources, synonyms, trial names, reference lists, citation trails, registries, full text, and supplements. Verify like an audit system: no PMID, DOI, sample size, outcome, effect estimate, study design, or citation claim is accepted unless it resolves to a source.

## Evidence Precedence For Literature

External literature is admissible evidence only after verification.

Use this order for literature facts:

1. User-provided source documents and project evidence.
2. Verified full text, supplement, trial registry, or publisher page.
3. Verified PubMed, Europe PMC, Crossref, or other authoritative metadata.
4. Systematic-review tables or reference lists, clearly labeled as secondary-source leads until the primary source is checked.
5. Search snippets, web pages, and agent findings as leads only.
6. Model memory as planning context only, never as a source.

When sources conflict, keep the conflict visible in the control surface. Do not silently pick the value that makes the manuscript easier to write.

## Build-Evidence Workflow

Use this mode when the user asks for literature search, evidence mapping, citation support, study extraction, or a field summary that needs source-level support.

1. Define the question.
   - Write the PICO or PECO elements.
   - State inclusion and exclusion criteria.
   - Name target study types, populations, interventions or exposures, comparators, outcomes, dates, and languages when known.
   - State assumptions.

2. Search broadly.
   - Run more than one route: PubMed or Entrez, Europe PMC or full-text tools when available, trial registries for clinical studies, citation and reference snowballing, review-table mining, and open-web search for non-indexed studies.
   - Save the source, query, date, result count, and notes in search_log.md.
   - Treat every hit as a candidate until verified.

3. Merge and deduplicate.
   - Deduplicate by PMID, DOI, registry ID, title fingerprint, first author, and year.
   - Preserve aliases rather than overwriting them.
   - Keep provenance: every source that found a candidate matters.

4. Verify identifiers.
   - Run scripts/verify_identifiers.py against the literature register before citing or extracting from a candidate.
   - Quarantine mismatched PMIDs, DOIs, titles, or years.
   - If a candidate has no PMID, verify it by DOI, publisher page, registry entry, or full text.
   - Never fabricate or infer a PMID or DOI.

5. Screen for relevance.
   - Record include, exclude, duplicate, protocol-only, registry-only, abstract-only, uncertain, or needs full text.
   - Give concise exclusion reasons.
   - Use independent subagents for borderline records when the task is high stakes.

6. Extract with source anchors.
   - Each extracted field needs a source_id, source locator, and source quote whenever possible.
   - Numeric fields need denominator, unit, time point, and comparison group when applicable.
   - Missing fields remain not_reported, unclear, or needs_full_text.
   - Do not extract study design, population, sample size, outcomes, or adverse events from search-result snippets unless the snippet is explicitly labeled as the source and the limitation is recorded.

7. Audit before writing.
   - Run scripts/extraction_audit.py on extraction_ledger.csv.
   - Run scripts/citation_audit.py when claims or manuscript prose cite the literature register.
   - In submission-ready mode, unverified citations and ungrounded extracted fields are blocking evidence-integrity failures.

## Lean Default Files

Keep the default package small. Create these files when building an evidence package:

- search_log.md
- literature_register.csv
- extraction_ledger.csv

Use status columns in literature_register.csv to move a record from candidate to screened to verified to included. Split into separate candidate, screening, source, identifier-audit, and conflict files only for systematic-review-scale work.

## Field Expectations

Minimum bibliographic fields:

- source_id
- title
- authors
- year
- journal
- PMID
- DOI
- registry ID when available
- publication type
- source URL
- verify_status

Minimum extraction fields:

- extraction_id
- source_id
- field group
- field name
- field value
- source locator
- source quote
- confidence or status

Clinical extraction fields should include study design, setting, population, inclusion and exclusion criteria, sample size by arm, intervention or exposure, comparator, follow-up duration, primary outcome, secondary outcomes, effect estimates, adverse events, funding, conflicts, and registry ID when supported by the source.

## Subagent Roles

Use bounded subagents when the literature task is substantial:

- search strategist: expands PICO terms, synonyms, MeSH, trial names, and query variants.
- database retriever: runs PubMed, Europe PMC, registry, and tool-based searches.
- manual snowballer: mines reviews, references, citation trails, publisher pages, and supplements.
- full-text extractor: extracts study design, population, sample size, outcomes, and adverse events from source documents.
- identifier auditor: checks PMIDs, DOIs, registry IDs, titles, and years.
- skeptical reviewer: looks for missing key studies, false inclusions, duplicated cohorts, protocol/result confusion, and unsupported fields.

Subagents return evidence-linked findings, not just conclusions.

## Stop Rules

Stop or log an author check when:

- a citation cannot be verified;
- a PMID or DOI resolves to the wrong paper;
- a study appears relevant but only a protocol, abstract, or registry entry can be found;
- full text is required for a field and cannot be accessed;
- extracted numbers disagree across sources;
- a manuscript claim depends on a source that is not in the verified literature register.

Do not call a literature package complete until broad discovery, identifier verification, screening, extraction, and evidence-integrity audits have been completed or explicitly blocked.
