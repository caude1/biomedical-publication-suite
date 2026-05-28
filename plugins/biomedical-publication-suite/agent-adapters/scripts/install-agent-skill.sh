#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Install or link Biomedical Publication Suite for other local agents.

Usage:
  install-agent-skill.sh --claude-user
  install-agent-skill.sh --gemini-user
  install-agent-skill.sh --agents-user
  install-agent-skill.sh --all-user
  install-agent-skill.sh --print

This script creates symlinks only when the destination does not already exist.
It refuses to overwrite existing files or directories.
USAGE
}

script_dir="$(cd "$(dirname "$0")" && pwd)"
plugin_root="$(cd "$script_dir/../.." && pwd)"
skill_name="biomedical-publication-suite"
skill_src="$plugin_root/skills/$skill_name"

link_skill() {
  local dest_root="$1"
  local label="$2"
  local dest="$dest_root/$skill_name"

  if [ ! -f "$skill_src/SKILL.md" ]; then
    echo "Missing source skill: $skill_src/SKILL.md" >&2
    return 1
  fi

  mkdir -p "$dest_root"

  if [ -L "$dest" ]; then
    local target
    target="$(readlink "$dest")"
    if [ "$target" = "$skill_src" ]; then
      echo "$label: already linked to $skill_src"
      return 0
    fi
    echo "$label: destination is already a symlink to $target; refusing to overwrite." >&2
    return 1
  fi

  if [ -e "$dest" ]; then
    echo "$label: destination already exists at $dest; refusing to overwrite." >&2
    return 1
  fi

  ln -s "$skill_src" "$dest"
  echo "$label: linked $dest -> $skill_src"
}

if [ "$#" -ne 1 ]; then
  usage
  exit 2
fi

case "$1" in
  --claude-user)
    link_skill "$HOME/.claude/skills" "Claude Code"
    ;;
  --gemini-user)
    link_skill "$HOME/.gemini/skills" "Gemini CLI"
    ;;
  --agents-user)
    link_skill "$HOME/.agents/skills" "Agent Skills alias"
    ;;
  --all-user)
    link_skill "$HOME/.claude/skills" "Claude Code"
    link_skill "$HOME/.gemini/skills" "Gemini CLI"
    link_skill "$HOME/.agents/skills" "Agent Skills alias"
    ;;
  --print)
    echo "Source skill: $skill_src"
    echo "Claude user destination: $HOME/.claude/skills/$skill_name"
    echo "Gemini user destination: $HOME/.gemini/skills/$skill_name"
    echo "Agent Skills alias destination: $HOME/.agents/skills/$skill_name"
    ;;
  -h|--help)
    usage
    ;;
  *)
    usage
    exit 2
    ;;
esac

