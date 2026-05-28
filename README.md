# Biomedical Publication Suite

Turn a biomedical study folder into the paper it is trying to become.

Biomedical Publication Suite is an Agent Skill for biomedical manuscript writing and publication polish. It helps a coding agent review a study folder, understand the analysis outputs, find the strongest scientific story, decide what belongs in the paper, and draft or revise publication-ready materials.

It is built for real research projects with figures, tables, model outputs, notes, partial drafts, reviewer comments, journal instructions, and messy intermediate files. The goal is not to summarize everything in the folder. The goal is to help the agent write like a careful biomedical author: clear, accurate, confident where the evidence supports confidence, and honest about what still needs author review.

## What It Helps You Do

- Find the main scientific story in a completed analysis project.
- Decide which results to feature, shorten, move to the supplement, or leave out.
- Draft full biomedical manuscripts from the evidence in a project folder.
- Improve abstracts, titles, figure legends, table text, cover letters, and reviewer responses.
- Adapt a manuscript for a target journal or article type.
- Keep author notes and unresolved checks separate from text meant for submission.

## Install As An Agent Skill

The portable skill lives here:

    plugins/biomedical-publication-suite/skills/biomedical-publication-suite

Use that folder with any coding agent that supports Agent Skills or skill-style instruction folders.

Common installation patterns:

    ~/.agents/skills/biomedical-publication-suite
    ~/.claude/skills/biomedical-publication-suite
    ~/.gemini/skills/biomedical-publication-suite
    .agents/skills/biomedical-publication-suite

For a personal install, copy or link the skill folder into one of those locations, then restart or refresh your agent's skill list.

For a project install, copy the skill folder into the project's skill directory so everyone using that project gets the same manuscript-writing behavior.

If your agent uses the common `~/.agents/skills` folder, this is the direct install:

```bash
git clone https://github.com/caude1/biomedical-publication-suite.git
mkdir -p ~/.agents/skills
cp -R biomedical-publication-suite/plugins/biomedical-publication-suite/skills/biomedical-publication-suite ~/.agents/skills/
```

## Optional Plugin Package

This repository also includes a plugin package for agents that support plugin marketplace folders:

    .agents/plugins/marketplace.json
    plugins/biomedical-publication-suite/

If your agent supports adding a plugin marketplace from GitHub, add this repository as the marketplace source, then install **Biomedical Publication Suite** from the plugin list.

The plugin package is optional. Agents that support skills directly should use the portable skill folder instead.

For Codex users, after cloning the repository:

```bash
codex plugin marketplace add /path/to/biomedical-publication-suite
codex plugin add biomedical-publication-suite@biomedical-publication-suite
```

Start a new thread after installing so the agent loads the new skill.

## Prompt Library

These prompts are written for the most common setup: the agent is already running inside the research directory that contains the analysis, results, figures, tables, notes, and drafts.

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

### Recommended Defaults

Use **Prompt 1** when the project is messy, exploratory, or high stakes. That is the best main workflow.

Use **Prompt 2** after you approve the narrative.

Use **Prompt 3** when you want the agent to produce the paper without a checkpoint.

Use **Prompt 5** when you are not sure the project actually supports a manuscript yet.

## What Makes It Different

Many manuscript-writing prompts produce a project memo: a chronological summary of files, decisions, caveats, and disconnected results. Biomedical Publication Suite pushes the agent toward the finished paper instead. It asks the agent to write for the reader of the manuscript, not for the person managing the project.

The skill emphasizes:

- the final scientific logic, not the research timeline;
- the strongest accurate finding, not every available output;
- confident language inside the evidence boundary;
- limitations in the right place, not defensive hedging throughout the manuscript;
- clean publication text first, with author checks kept separate.

## Repository Layout

    plugins/biomedical-publication-suite/

The full plugin package.

    plugins/biomedical-publication-suite/skills/biomedical-publication-suite/

The portable Agent Skill. This is the folder to copy or link for agents that support skills directly.

    .agents/plugins/marketplace.json

An optional plugin marketplace entry for agents that support marketplace-based plugin installation.
