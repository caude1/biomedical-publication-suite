# Evidence and Claim Control

## Evidence Precedence

Use this order when sources conflict:

1. Final structured outputs tied to the analysis.
2. Tables, figures, notebooks, or logs that directly generated those outputs.
3. Analysis scripts and configuration files.
4. Existing manuscript drafts and author notes.
5. Verified external literature when the claim is a background, context, precedent, or comparative claim.
6. Chat discussion and informal planning notes.
7. Model memory.

If a conflict cannot be resolved, use the conservative version in the publication artifact and log the conflict in the control surface.

## Evidence Sweep Checklist

For project work, inspect:

- final figures and figure source data;
- table files and table-generating scripts;
- statistical model outputs;
- notebooks and rendered reports;
- data dictionaries and cohort definitions;
- existing manuscripts, abstracts, and response documents;
- journal instructions and reviewer/editor letters;
- citation libraries, reference lists, and key PDFs;
- previous QC reports or TODO files.

Avoid broad reruns unless the user asks or the repository has a documented, minimal, safe pipeline.

## Claim Register

Every major claim should have a support trail:

- background claim maps to citation or accepted field fact needing citation;
- design claim maps to protocol, methods script, data dictionary, or author-provided text;
- numeric result maps to table, model output, figure source data, or results ledger;
- interpretation maps to supported result plus design-appropriate language;
- limitation maps to known design constraint, missing variable, bias source, or reviewer concern;
- implication maps to result plus defensible clinical, mechanistic, or policy bridge.

Use needs_verification rather than guessing.

For external literature, a claim should map to a source_id in literature_register.csv. Numeric or study-characterization claims should also map to an extraction_id in extraction_ledger.csv when available.

## Citation Discipline

Do not invent references. When web or library tools are available, verify the most important citations against full text or at least abstracts and metadata. For each key reference, note:

- what claim it supports;
- whether the cited passage is direct support, context, contrast, or method precedent;
- DOI/PMID or stable locator;
- any concern, correction, or retraction signal.

When citation verification is unavailable, write concrete search strings and exact claims needing support. Do not leave vague add citation notes.

Manual web search, review tables, citation trails, and search snippets produce leads, not verified citations. A literature source is citable only after its identifier or source record has been verified. If a PMID or DOI resolves to a different title, author, year, or journal, quarantine it and re-search by title.

For literature extraction, every non-empty extracted field needs a source locator and source quote when possible. Missing data stays not_reported, unclear, or needs_full_text. Never infer sample size, study design, outcome definitions, or effect estimates from plausibility.

## Subagent Assignments

Use agents for bounded, independent checks:

- evidence scout: find the files that support sample size, cohort, model, endpoints, tables, and figures.
- claim auditor: check whether every major claim in this draft has support in the provided files.
- literature scout: find 5 to 10 field-standard references for this exact claim family.
- identifier auditor: verify PMIDs, DOIs, registry IDs, titles, years, and source URLs before sources are cited.
- extraction auditor: check that extracted study fields have source quotes and locators.
- skeptic: find overclaims, causal leakage, missing limitations, and mismatches between abstract/results/discussion.
- surface editor: remove internal project language and rewrite for a cold reviewer.

Require short, evidence-linked outputs from agents. Treat agent findings as input, then verify high-risk facts yourself.

## Stop Rules

Stop and ask or log an author check when:

- the primary outcome, cohort, or model cannot be identified;
- numeric results disagree across authoritative outputs;
- a requested claim is stronger than the design supports;
- journal requirements are unavailable and cannot be inferred safely;
- a citation appears fabricated or does not support the claim;
- a literature source has not cleared identifier verification;
- an extracted literature field lacks a source quote or locator;
- the user asks for submission-ready output but required administrative facts are missing.
