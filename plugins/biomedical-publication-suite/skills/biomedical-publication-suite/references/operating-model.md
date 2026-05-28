# Operating Model

## Core Philosophy

This skill is a publication authorship system, not a text beautifier. It should make the paper clearer, stronger, and more defensible while keeping a visible audit trail for everything that should not appear in the paper.

Use two surfaces:

- Publication surface: manuscript prose, abstract, titles, display text, captions, legends, footnotes, supplements, cover letters, and reviewer responses.
- Control surface: study facts, context, narrative brief, open items, QC report, and optional submission-stage registers or journal files.

Never mix the two. The publication surface reads like a finished paper. The control surface can be blunt, incomplete, and author-facing. The control surface exists to improve the manuscript, not to become the work product.

Final quality is governed by the senior-editor read and manuscript voice audit. QC scripts are backstops for mechanical leakage; they do not replace judgment and should not force awkward rewrites of sound biomedical prose.

## Mode Router

| User intent | Mode | Package needed |
|---|---|---|
| polish a sentence, paragraph, section, abstract, caption, legend, table title, cover letter, or response paragraph | refine-artifact | no |
| build, revise, narratively audit, journal-adapt, or prepare a full manuscript | build-or-revise-manuscript | yes when evidence is dispersed or submission-facing |
| address reviewer/editor comments | respond-to-reviewers | yes, but only revision files are needed |

When the request spans modes, choose the mode that protects evidence integrity first. For example, reviewer comments with journal adaptation route through respond-to-reviewers first, then manuscript revision.

Implicit skill use should default to artifact work. Only explicit requests such as build the manuscript package, prepare for submission, create the package, or audit the full project should create a package.

## Package Discipline

Use an existing manuscript directory when present. Otherwise, default to manuscript for package work. The default package is intentionally lean: it should help the agent find the manuscript's forest before drafting, not consume the drafting pass with bookkeeping.

Core files for manuscript drafting and revision:

- publication_context.yaml
- study_facts.md
- narrative_brief.md
- manuscript.md
- open_items.md

Add only when needed:

- display_text.md when figure or table text is being drafted, revised, or QCed.
- qc_report.md when publication_qc.py generates or updates it.
- narrative_audit.md when the user asks for a narrative audit.
- claim_register.csv and results_ledger.csv when final verification or submission-readiness requires claim/result tracing.
- journal_requirements.md
- reporting_checklist.md
- citation_audit.md
- key_reference_notes.md
- revision_matrix.csv
- response_to_reviewers.md
- submission_readiness.md
- editorial_rationale.md

## Full Package Workflow

1. Sweep evidence only far enough to identify the design, cohort, endpoints, primary analysis, key estimates, and missing facts.
2. Fill study_facts.md.
3. Draft narrative_brief.md: thesis, literature/mechanism gap, hypothesis, 1-3 headline findings ranked by strength, claim boundaries, and one line per manuscript section.
4. Do not write manuscript prose until the brief has a clear thesis and a real gap.
5. Draft or revise manuscript.md from the brief and facts.
6. Run the voice audit and reverse outline from references/manuscript-voice.md.
7. Run QC as a mechanical backstop. Fix errors and adjudicate warnings through the senior-editor read.
8. Put residual author checks in open_items.md.

## Small Artifact Workflow

1. Identify artifact type and target reader.
2. Identify source facts and claim strength.
3. Rewrite the artifact.
4. Run the manuscript voice audit mentally: forest first, no memo voice, no reflexive hedging, caveats in the right place.
5. Keep labels as labels and prose as prose.
6. Add a short Notes section only when necessary.
7. Run text lint when high stakes.

## Efficiency Rule

Use only the references needed for the current task. Journal instructions and the user's evidence override generic templates. If a file or checklist does not improve the next draft, defer it until submission-stage verification.
