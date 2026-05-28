---
name: biomedical-publication-suite
description: Evidence-grounded biomedical manuscript and publication artifact writing/refinement for clinical, translational, surgical, epidemiologic, biostatistical, public-data, life-science, and grant-adjacent work. Use when an agent needs to draft, rewrite, polish, audit, or package manuscripts, abstracts, titles, figure or table text, captions, legends, supplements, cover letters, journal submission text, reviewer responses, project narratives, narrative audits, confident-language rewrites, claim registers, citation checks, reporting-guideline checklists, or submission-readiness artifacts. Also use when removing AI-like prose, internal project language, research-timeline leakage, causal overreach, unsupported claims, weak narrative logic, missing-information leakage, or publication-surface problems from biomedical research artifacts.
---

# Biomedical Publication Suite

Write the strongest biomedical publication artifact the evidence can support. Treat the user's repository, pasted results, documents, figures, tables, comments, and journal constraints as the authority. Treat model memory as a planning aid, never as a source of facts.

## Write Like A Paper, Not A Project Memo

The manuscript reader is a stranger who knows the field and has never seen the repository, chat, analysis history, team deliberations, or draft evolution. Write every publication-facing sentence for that reader.

Default voice: a senior clinical investigator stating what was found and what it means. Confident, plain, design-matched, and self-contained. Not a lab update, not an analysis rationale, not a defense brief, and not an artifact about the artifact.

Four rules carry most of the quality:

1. Forest before trees. Open each section, paragraph, and abstract result move with the scientific point, then support it.
2. Final logic, not chronology. Reconstruct why the question, design, and findings belong together; do not narrate how the work unfolded.
3. Objectives from the gap, not from the analysis. The hypothesis follows from literature or mechanism to unresolved gap to natural question.
4. Confidence inside the evidence boundary. State findings at full strength with estimates and intervals. Match verbs to design. Put real threats in limitations, not in hedges scattered through the narrative.

## How Quality Is Enforced

Two layers govern final publication quality, in this order:

1. The senior-editor read is primary. Before returning any publication-facing text, read it cold, start to finish, as a journal editor seeing it for the first time. Does it read as a paper rather than a project memo? Does it lead with the forest? Are caveats in the right home? Is the voice matched to the study design? Run the manuscript voice audit in references/manuscript-voice.md. This read governs every final wording choice.
2. The QC script is a cheap net. publication_qc.py catches mechanical leaks the eye can skip: process words, missing-information placeholders, citation pile-ups, label-prose collapse, and design-mismatched causal verbs. It cannot judge narrative logic, theory of mind, field-standard terminology, or whether a sentence earns its place. A QC finding is a question for the editor read, not an automatic edit. Never reword sound prose only to silence a warning. If flagged wording is correct because it is literal, field-standard, required by journal style, or design-appropriate, keep it and note the adjudication in open_items.md for package work.

## First Moves

1. Classify the request:
   - refine-artifact: one abstract, section, title, caption, legend, table text, cover letter, graphical abstract text, or response paragraph.
   - build-or-revise-manuscript: create, rewrite, audit, journal-adapt, or prepare a manuscript package from project evidence.
   - respond-to-reviewers: turn reviewer/editor comments into manuscript revisions and point-by-point responses.
2. Decide the evidence surface:
   - For small text-only tasks, work directly from the supplied text and return the clean artifact first.
   - For manuscript tasks, inventory the repository and create or update the lean publication package only when it helps quality or reproducibility.
3. Use the minimum references needed:
   - references/operating-model.md for workflow routing and package discipline.
   - references/manuscript-voice.md for memo voice, forest-first writing, caveat placement, hedging discipline, and the mandatory voice audit.
   - references/evidence-and-claim-control.md for evidence precedence, claim tracing, citation handling, and subagent use.
   - references/narrative-frameworks.md for narrative-audit structure and the confident-language method.
   - references/publication-surface-standard.md for prose, labels, captions, legends, tables, reviewer responses, anti-leakage rules, and PHI precautions.
   - references/section-and-artifact-guides.md for section-specific drafting, paragraph flow, display text, cover letters, and response text.
   - references/article-types.md for article-type routing and structure expectations.
   - references/reporting-and-journal-routing.md for reporting guidelines and journal adaptation.
   - references/revision-response-and-submission.md for reviewer response and submission package workflows.
   - references/schemas.md for package file schemas and CSV headers.
4. Use deterministic helpers when useful:
   - python3 scripts/init_publication_package.py --repo-root .
   - python3 scripts/publication_qc.py --repo-root . --package-dir manuscript
   - Use --fail-on-warn only for submission-ready packages after warnings have been adjudicated by the senior-editor read.

## Non-Negotiables

- Preserve the final scientific logic, not the research timeline. Mention changes, pivots, failed analyses, or workflow history only in internal audit files unless the manuscript must disclose them.
- Derive the hypothesis from first principles: literature or mechanism to unresolved gap to natural study question to testable hypothesis.
- Foreground the strongest defensible signal. Put null, weak, exploratory, tangential, and inconvenient findings in the appropriate subordinate location, supplement, limitations, or internal rationale.
- Use confident manuscript voice by default. Confident-language work is not a special mode; it is the standard publication register. The special task is only when the user explicitly asks for a high-impact rewrite or adversarial ceiling pass.
- Use design-matched language. Observational, retrospective, cross-sectional, registry-based, public-data, before-after, ecological, and nonrandomized work gets association language unless a justified causal estimand is explicit.
- Do not invent sample sizes, dates, estimates, p-values, confidence intervals, models, endpoints, citations, ethics language, journal rules, funding, author contributions, or conflicts.
- Keep publication-facing text free of repository names, skill names, workflow labels, version labels, TODO language, unresolved author checks, figure-design rationale, and analysis-history narration.
- Never place identifiable patient detail in case reports, examples, reviewer responses, or narrative artifacts. De-identify or quarantine details that are not publication-safe.
- Return clean publication-facing text first. Put author-facing concerns in Notes, open_items.md, editorial_rationale.md, or submission_readiness.md.
- When the artifact is high stakes, run a silent final audit for internal leakage, causal overreach, unsupported claims, AI-like filler, label-prose collapse, missing-information leakage, and inflated wording before responding.

## Operating Model

### Small Artifact Work

For a single paragraph, title, abstract, caption, figure/table label set, response paragraph, cover letter, or journal text:

1. Identify artifact type, audience, study design, claim strength, and missing facts.
2. Rewrite the artifact directly in publication language.
3. Preserve numbers and citation placeholders exactly unless the user asks for formatting changes.
4. Add a short Notes section only for factual gaps, claim-strength changes, or author-facing concerns.
5. Run publication_qc.py --file when the artifact is stored on disk or the user asks for a final pass.

Implicit invocation should stay here unless the user explicitly asks for a full package. A small edit should never create a workspace by surprise.

### Full Package Work

For manuscript builds, major revisions, journal adaptation, reviewer responses, or submission readiness:

1. Inventory only the evidence needed to write the paper.
2. Initialize or refresh the lean package with init_publication_package.py.
3. Fill study_facts.md and narrative_brief.md before writing prose. The brief is the forest-first gate: thesis, gap, hypothesis, 1-3 headline findings, claim boundaries, and one line per section.
4. Draft or revise manuscript.md from the brief and facts, not from memory or administrative notes.
5. Run the manuscript voice audit from references/manuscript-voice.md and reverse-outline the draft before QC.
6. Run QC as a cheap net, fix blocking findings, adjudicate warnings through the senior-editor read, and report residual author checks in open_items.md.

## Subagent Guidance

Use subagents liberally when the work benefits from independent evidence gathering or review. Good splits:

- evidence scout: inventory outputs, scripts, figures, tables, and existing drafts.
- literature scout: verify key references and field-standard language.
- skeptical reviewer: find overclaims, missing caveats, and internal inconsistencies.
- publication surface editor: remove memo voice and artifact leakage.
- journal adapter: check target journal structure and reporting expectations.

Give subagents raw artifacts and bounded questions. Do not leak your intended conclusion when the goal is validation.

## Output Contracts

For artifact refinement, return the revised artifact first, then optional Notes with only the few issues an author must know.

For narrative audit, return Part 1 - Scientific Narrative for external-facing prose and Part 2 - Editorial Rationale for internal-only reasoning about what was kept, what was set aside, and where logic may be thin.

For confident-language work, return the maximally defensible revised artifact first. Add Author Notes only when a claim was materially weakened, removed, or requires verification.

For package work, maintain only the files needed for the current stage. End with what changed, what QC found, what remains for author verification, and whether the manuscript is ready for the next step.

## Final Review

Before final delivery on a package, first perform the senior-editor read and manuscript voice audit. Then run:

    python3 <skill-dir>/scripts/publication_qc.py --repo-root . --package-dir manuscript

Before calling a package submission-ready, perform the senior-editor read again after all script findings are adjudicated. Then run:

    python3 <skill-dir>/scripts/publication_qc.py --repo-root . --package-dir manuscript --fail-on-warn --require-claim-register

For text-only artifacts stored as files:

    python3 <skill-dir>/scripts/publication_qc.py --file path/to/artifact.md --observational

Fix errors before delivery. Treat warnings as prompts for judgment; ignore a warning only when the wording is literal, required by journal style, field-standard in context, or better for the reader than the regex-compliant alternative.
