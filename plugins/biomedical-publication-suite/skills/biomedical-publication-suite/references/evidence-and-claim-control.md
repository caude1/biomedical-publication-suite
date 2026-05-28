# Evidence and Claim Control

## Evidence Precedence

Use this order when sources conflict:

1. Final structured outputs tied to the analysis.
2. Tables, figures, notebooks, or logs that directly generated those outputs.
3. Analysis scripts and configuration files.
4. Existing manuscript drafts and author notes.
5. Chat discussion and informal planning notes.
6. Model memory.

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

## Citation Discipline

Do not invent references. When web or library tools are available, verify the most important citations against full text or at least abstracts and metadata. For each key reference, note:

- what claim it supports;
- whether the cited passage is direct support, context, contrast, or method precedent;
- DOI/PMID or stable locator;
- any concern, correction, or retraction signal.

When citation verification is unavailable, write concrete search strings and exact claims needing support. Do not leave vague add citation notes.

## Subagent Assignments

Use agents for bounded, independent checks:

- evidence scout: find the files that support sample size, cohort, model, endpoints, tables, and figures.
- claim auditor: check whether every major claim in this draft has support in the provided files.
- literature scout: find 5 to 10 field-standard references for this exact claim family.
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
- the user asks for submission-ready output but required administrative facts are missing.
