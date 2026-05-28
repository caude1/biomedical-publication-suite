# Gemini CLI Adapter

Gemini CLI supports GEMINI.md context files and Agent Skills. The publication suite should usually be shared as an Agent Skill, not as always-loaded context.

The canonical skill directory is:

    <path-to-this-repo>/plugins/biomedical-publication-suite/skills/biomedical-publication-suite

## Recommended User-Level Install

Use the included installer:

    <path-to-this-repo>/plugins/biomedical-publication-suite/agent-adapters/scripts/install-agent-skill.sh --gemini-user

Manual symlink equivalent:

    mkdir -p ~/.gemini/skills
    ln -s <path-to-this-repo>/plugins/biomedical-publication-suite/skills/biomedical-publication-suite ~/.gemini/skills/biomedical-publication-suite

Gemini CLI also documents a terminal utility:

    gemini skills link <path-to-this-repo>/plugins/biomedical-publication-suite/skills/biomedical-publication-suite

For Git-hosted sharing, Gemini CLI documents:

    gemini skills install <url>

After installing or linking, use:

    /skills list

If the skill does not appear after installation, refresh discovery:

    /skills reload

or:

    /skills refresh

Then invoke or trigger:

    /biomedical-publication-suite Refine this discussion section for a retrospective cohort study without causal overreach.

## Workspace-Level Sharing

For a single project, place the skill at either:

    <project>/.gemini/skills/biomedical-publication-suite/SKILL.md

or the interoperable alias:

    <project>/.agents/skills/biomedical-publication-suite/SKILL.md

Gemini CLI also recognizes user-level skills in:

    ~/.gemini/skills/
    ~/.agents/skills/

Within the same tier, Gemini documents .agents/skills as an interoperable alias for .gemini/skills. That makes .agents/skills a good choice when a project should be readable by multiple Agent Skills-compatible tools.

## GEMINI.md Is Optional

Use GEMINI.md for compact always-loaded context. Do not import the full skill into every prompt unless you truly want the context cost. A lightweight pointer is enough:

    # Biomedical Publication Work

    For biomedical manuscripts, abstracts, figure legends, captions, cover letters, reviewer responses, narrative audits, confident-language edits, claim checks, and submission-readiness work, use the biomedical-publication-suite Agent Skill if available.

Gemini supports @file.md imports inside GEMINI.md, but importing the full skill defeats progressive disclosure. Prefer the skill system.

## Optional Custom Command

Gemini custom commands are TOML files under ~/.gemini/commands/ or <project>/.gemini/commands/. This adapter includes an optional command template at:

    agent-adapters/gemini-cli/commands/biomed-pub.toml

Copy it only if you want a shorter manual command. The skill install is still the primary sharing mechanism.

## Documentation Checked

- Gemini CLI Agent Skills: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
- Gemini CLI skill creation and sharing: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/creating-skills.md
- Gemini CLI skill management: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md
- Gemini CLI GEMINI.md context files: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
