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

## Optional Plugin Package

This repository also includes a plugin package for agents that support plugin marketplace folders:

    .agents/plugins/marketplace.json
    plugins/biomedical-publication-suite/

If your agent supports adding a plugin marketplace from GitHub, add this repository as the marketplace source, then install **Biomedical Publication Suite** from the plugin list.

The plugin package is optional. Agents that support skills directly should use the portable skill folder instead.

## Best First Prompt

Use this when you want the agent to study the project and propose the paper before writing the full draft:

    Use Biomedical Publication Suite.

    Review this directory as a completed biomedical study and propose the manuscript before drafting it.

    Inventory the analysis, results, figures, tables, notes, and any existing draft. Return:

    1. The proposed scientific story.
    2. The headline finding and central manuscript thesis.
    3. A one-line-per-section manuscript outline.
    4. What you would feature, shorten, move to the supplement, or leave out, with a brief reason for each choice.
    5. Anything the authors need to verify before submission.

    Use your best judgment to decide what the paper is about.

    Do not draft the full manuscript yet. I want to review the proposed story first.

## Full Draft Prompt

Use this when you want the agent to go straight from project folder to manuscript draft:

    Use Biomedical Publication Suite.

    Review this directory and produce a complete manuscript draft.

    Use your best judgment to decide the manuscript narrative, including what to feature, shorten, move to the supplement, or leave out. Do not summarize every output. Organize the results into the strongest accurate scientific story supported by the project files.

    Draft the manuscript, check the voice and structure, and list anything the authors need to verify separately.

## Good Follow-Up Prompts

    Build the full manuscript from the approved story.

    Revise the existing draft using the project outputs. Cut, reorder, or reframe sections as needed.

    Adapt the manuscript for JAMA Network Open as an original investigation.

    Use the reviewer and editor comments in this directory to revise the manuscript and draft a point-by-point response.

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
