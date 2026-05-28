# Other Agent Adapters

For agents that support the Agent Skills open pattern, share this directory:

    <path-to-this-repo>/plugins/biomedical-publication-suite/skills/biomedical-publication-suite

The minimum required entrypoint is:

    SKILL.md

Supporting references and scripts should stay beside it. Do not flatten the skill into one giant prompt unless the target agent cannot read folders.

## Generic Install Strategy

1. Find the target agent's user-level or project-level skills directory.
2. Link or copy the canonical skill directory into that location.
3. Restart or reload the agent's skills.
4. Ask the agent to list available skills and confirm biomedical-publication-suite appears.
5. Test with a narrow prompt, such as rewriting an abstract while preserving all numbers exactly.

## Fallback For Agents Without Skills

If the target agent cannot load Agent Skills, give it:

1. SKILL.md.
2. The relevant reference file for the task.
3. The two helper script paths if package creation or QC is needed.

Use this compact instruction:

    Use the Biomedical Publication Suite operating model. Work only from supplied evidence. Preserve all numbers exactly. Use association language for observational work. Strip internal workflow language. Return publication-facing text first, with author-facing issues in notes.

This fallback is less reliable than a proper skill install because it loses progressive disclosure and script discovery.

