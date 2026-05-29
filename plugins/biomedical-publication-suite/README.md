# Biomedical Publication Suite

Turn a biomedical study folder into the paper it is trying to become.

Biomedical Publication Suite helps a coding agent review analysis outputs, figures, tables, drafts, reviewer comments, and journal instructions, then turn them into polished manuscript materials. It is made for research projects where the hard part is not only writing clean prose, but deciding what the paper should say.

## What It Helps With

- Find the strongest manuscript story in a completed study folder.
- Decide which results belong in the main text, supplement, limitations, or author notes.
- Draft full biomedical manuscripts from project evidence.
- Find relevant papers, verify citations, and extract study details with source support.
- Rewrite abstracts, titles, captions, legends, tables, cover letters, and reviewer responses.
- Adapt a manuscript for a target journal or article type.
- Keep author checks and missing facts out of submission-facing prose.

## Prompt Library

These prompts assume the agent is already running inside the research directory that contains the study files.

For the first line, use whichever handle fits the agent:

```text
Codex: $biomedical-publication-suite
Claude Code: /biomedical-publication-suite
Plain fallback: Use Biomedical Publication Suite.
```

### 1. Propose The Manuscript Before Drafting

Use this when the project is messy, exploratory, high stakes, or still needs a narrative decision before anyone spends time on a full draft.

```text
$biomedical-publication-suite

Review this directory as a completed biomedical study and propose the manuscript before drafting it.

Run a narrative audit. Inventory the analysis, results, figures, tables, notes, and any existing draft. Return:

1. The proposed scientific story.
2. The headline finding and central manuscript thesis.
3. A one-line-per-section manuscript outline.
4. The editorial rationale for what you would feature, subordinate, move to supplement, cut, or reserve for limitations.
5. Open author-verification items for anything that cannot be confirmed from the project files.

Use your best judgment to decide what the paper is about.

Do not draft the full manuscript yet. I want to review the narrative first.
```

### 2. Build The Full Manuscript

Use this after you have approved a narrative audit, or when the project already has a clear manuscript direction.

```text
$biomedical-publication-suite

Build the full manuscript package from this directory.

If a narrative brief or narrative audit already exists, build from the approved narrative. Otherwise, treat this as a completed biomedical study: review the project evidence, decide the strongest manuscript narrative, and use your best judgment on what to feature, subordinate, move to supplement, cut, or reserve for limitations.

Infer the study design, article type, and target-journal needs from the project files when possible. If they are not clear, make conservative choices and record them as author-verification items rather than stopping.

Proceed without clarifying questions unless something is truly blocking. Do not invent missing numbers, methods, results, ethics language, citations, or journal requirements.
```

### 3. One-Shot Manuscript Draft

Use this when you want the agent to move directly from project folder to manuscript draft without a narrative checkpoint.

```text
$biomedical-publication-suite

Review this directory and produce a complete manuscript draft.

Use your best judgment to decide the manuscript narrative, including what to include, subordinate, move to supplement, cut, or reserve for limitations. Do not mechanically summarize every output. Organize the results into the strongest scientific story supported by the project files.

Create the manuscript package, draft the manuscript, run the manuscript voice audit, run QC as a final safety check, and list author-verification items separately.
```

### 4. Refine Existing Draft

Use this when a manuscript already exists but needs a stronger story, cleaner structure, or publication-facing prose.

```text
$biomedical-publication-suite

Review this directory and revise the existing manuscript draft.

Use the project outputs to judge whether the current draft has the right narrative, whether sections should be cut, reordered, or reframed, whether any included result distracts from the central thesis, and whether any omitted result should be restored.

Revise the manuscript directly. Keep author-facing notes separate from the manuscript.
```

### 5. Skeptical Pre-Draft Critique

Use this when you are not sure the project supports a manuscript yet, or when you want a hard editorial read before drafting.

```text
$biomedical-publication-suite

Review this directory as a skeptical senior reviewer.

Do not rewrite yet. Tell me:

1. What paper this project is currently trying to be.
2. Whether the central claim is earned.
3. Which results belong in the main text.
4. Which results belong in the supplement.
5. Which results should be cut or kept only as internal context.
6. What must be fixed before drafting.
7. Whether there is a publishable manuscript here, and if so, what the best version is.
```

### 6. Journal Adaptation

Use this when you have a draft and need it reshaped for a specific journal or article type.

```text
$biomedical-publication-suite

Adapt the manuscript package in this directory for the target journal and article type named in the project files.

If the target journal or article type is not specified, infer the most appropriate format conservatively and record the assumption as an author-verification item.

Match the journal's structure, abstract format, length expectations, reporting-guideline needs, references, display limits, and required statements where available. Preserve the central thesis and scientific accuracy.
```

### 7. Reviewer Response

Use this when editor or reviewer comments are available as files in the directory or pasted into the chat.

```text
$biomedical-publication-suite

Use the reviewer and editor comments in this directory, or the comments pasted below, to revise the manuscript and draft a point-by-point response.

For each comment:

1. Classify the issue.
2. Decide whether to revise, clarify, add analysis, decline, or explain.
3. Make the manuscript change when warranted.
4. Draft response text naming what changed and where.
5. If you would push back, do so respectfully and explain the reasoning.

Keep manuscript revisions separate from response-letter explanations.
```

### 8. Find And Extract The Literature

Use this when the paper needs a stronger literature base, or when you want a reliable evidence table before writing.

```text
$biomedical-publication-suite

Find the relevant biomedical literature for this question and build a verified evidence package.

Define the question and inclusion criteria first. Search broadly, including available databases, reference lists, citation trails, registries, and full text when available.

Verify each citation before using it. For every included study, extract the key details with a source locator or quote whenever possible.

Return the search strategy, candidate papers, included and excluded studies, verified citations, extracted study details, and anything that still needs full-text access or author review.
```

### Recommended Defaults

Use **Prompt 1** when the project is messy, exploratory, or high stakes. That is the best main workflow.

Use **Prompt 2** after you approve the narrative.

Use **Prompt 3** when you want the agent to produce the paper without a checkpoint.

Use **Prompt 5** when you are not sure the project actually supports a manuscript yet.

Use **Prompt 8** when you need literature discovery, citation verification, or source-backed study extraction.

## Writing Philosophy

The suite prioritizes the finished paper over the project history. It should present the final scientific logic, not the order in which analyses were tried. It should write with confidence when the evidence supports the claim, while keeping limitations and author checks in the right place.

For literature work, the suite searches broadly but verifies carefully. Search results and web pages are treated as leads until the citation is checked, and extracted study details need source support before they are used in manuscript text.
