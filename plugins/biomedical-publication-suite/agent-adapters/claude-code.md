# Claude Code Adapter

Claude Code supports skills as directories containing SKILL.md. Current Claude Code documentation describes skills as slash-invoked Agent Skills with personal, project, and plugin locations. Personal skills live at:

    ~/.claude/skills/<skill-name>/SKILL.md

Project skills live at:

    .claude/skills/<skill-name>/SKILL.md

The Biomedical Publication Suite skill can therefore be shared with Claude Code by linking or copying this directory:

    <path-to-this-repo>/plugins/biomedical-publication-suite/skills/biomedical-publication-suite

## Recommended User-Level Install

Use the included installer:

    <path-to-this-repo>/plugins/biomedical-publication-suite/agent-adapters/scripts/install-agent-skill.sh --claude-user

Manual equivalent:

    mkdir -p ~/.claude/skills
    ln -s <path-to-this-repo>/plugins/biomedical-publication-suite/skills/biomedical-publication-suite ~/.claude/skills/biomedical-publication-suite

After installing, start or refresh Claude Code. The skill should be invokable as:

    /biomedical-publication-suite

Example prompts:

    /biomedical-publication-suite Rewrite this abstract for a high-impact oncology journal while preserving all numbers exactly.

    /biomedical-publication-suite Run a narrative audit on this manuscript package and separate publication-facing text from internal editorial rationale.

## Project-Level Sharing

For a single repository, place the skill at:

    <project>/.claude/skills/biomedical-publication-suite/SKILL.md

Use a copy when the project needs a frozen version. Use a symlink when the project should track the canonical plugin.

Claude Code also supports skills supplied by plugins. If you package this for a Claude Code plugin later, use Claude's plugin conventions and keep the Biomedical Publication Suite as the skill payload.

## CLAUDE.md Is Optional

Use CLAUDE.md for always-loaded project facts and preferences. Do not paste the full publication suite into CLAUDE.md; it is procedural and large, so it belongs in a skill. A short CLAUDE.md pointer is enough:

    # Biomedical Publication Work

    When drafting or revising biomedical manuscripts, abstracts, legends, captions, cover letters, reviewer responses, or submission artifacts, use the /biomedical-publication-suite skill if available.

## Caveats

- Claude Code does not use this repository's marketplace entry.
- Claude Code skill plugins have their own plugin conventions. This adapter intentionally exposes the Agent Skill itself, not a platform-specific plugin manifest.
- Claude Code documents live skill change detection for user skills, project skills, and .claude/skills directories inside added directories. If Claude cannot see the skill, confirm the symlink target exists and restart or refresh Claude Code.

## Documentation Checked

- Claude Code skills: https://code.claude.com/docs/en/skills
