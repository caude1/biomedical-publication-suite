# Sharing Biomedical Publication Suite With Other Agents

Biomedical Publication Suite is easiest to share as an Agent Skill. The portable skill directory is:

    skills/biomedical-publication-suite/SKILL.md

Claude Code, Gemini CLI, and other Agent Skills-compatible tools can use that directory through their own skill discovery systems. Platform-specific plugin metadata is included for tools that understand it, but the skill instructions, references, and Python helpers are the reusable core.

## Best Sharing Pattern

Prefer linking the canonical skill directory instead of copying it.

Why:

- All agents read the same current instructions.
- Updates made to the source package automatically become available to linked agents.
- There is one source of truth for the publication workflow, voice rules, and helper scripts.

Use the installer:

    <path-to-this-repo>/plugins/biomedical-publication-suite/agent-adapters/scripts/install-agent-skill.sh --all-user

Or link manually using the notes in:

- claude-code.md
- gemini-cli.md
- other-agents.md

## Current Sharing Options

For Agent Skills-compatible tools, share the skill directory directly. Good destinations include ~/.agents/skills/biomedical-publication-suite, .agents/skills/biomedical-publication-suite, or the tool-specific skills directory.

For Claude Code, install the skill as a personal skill under ~/.claude/skills/biomedical-publication-suite or as a project skill under .claude/skills/biomedical-publication-suite.

For Gemini CLI, install the skill under ~/.gemini/skills, ~/.agents/skills, .gemini/skills, or .agents/skills. Gemini also supports gemini skills link <path> for local development and gemini skills install <url> for Git-hosted skills.

For tools that support plugin marketplace folders, use this repository's .agents/plugins/marketplace.json file and plugins/biomedical-publication-suite package.

## What Works Cross-Agent

The portable pieces are:

- SKILL.md frontmatter and procedural instructions.
- references/ progressive-disclosure reference files.
- scripts/init_publication_package.py.
- scripts/publication_qc.py.
- scripts/verify_identifiers.py.
- scripts/extraction_audit.py.
- scripts/citation_audit.py.

The Python scripts use only the standard library. They should work from any local agent that can run Python and read the skill directory.

## Documentation Checked

- Claude Code skills and skill locations: https://code.claude.com/docs/en/skills
- Gemini CLI GEMINI.md context files: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
- Gemini CLI Agent Skills: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
- Gemini CLI skill creation and sharing: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/creating-skills.md
- Gemini CLI skill management: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md
- Gemini CLI custom commands: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/custom-commands.md
