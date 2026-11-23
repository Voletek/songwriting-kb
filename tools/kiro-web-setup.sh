#!/usr/bin/env bash
# kiro-web-setup.sh - make this repo's Kiro config load when the repo is cloned one folder below the
# workspace root (Kiro Web clones repositories to <workspace>/<repo>/).
#
# Kiro reads steering, agents, skills, hooks and powers from <workspace>/.kiro/, and the agents and
# steering refer to repo files by repo-relative paths (core/..., references/..., tools/...). This
# script symlinks both into the workspace root. It is idempotent, never overwrites a real file or
# directory, and leaves <workspace>/.kiro/settings/ alone.
#
# Usage (from anywhere):  bash songwriting-kb/tools/kiro-web-setup.sh [WORKSPACE_ROOT]
# WORKSPACE_ROOT defaults to the repo's parent directory. Start a new Kiro session afterwards so
# agents and skills are picked up (steering loads immediately).
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WS="${1:-$(dirname "$REPO")}"
WS="$(cd "$WS" && pwd)"
NAME="$(basename "$REPO")"

if [ "$WS" = "$REPO" ]; then
  echo "The repo is the workspace root already; nothing to do."
  exit 0
fi

link() {  # link <target-relative-to-dir-of-link> <link-path>
  local target="$1" path="$2"
  if [ -L "$path" ]; then
    if [ "$(readlink "$path")" = "$target" ]; then echo "  ok      $path"; return; fi
    ln -sfn "$target" "$path"; echo "  updated $path -> $target"; return
  fi
  if [ -e "$path" ]; then echo "  SKIP    $path exists and is not a symlink (left unchanged)"; return; fi
  ln -s "$target" "$path"; echo "  linked  $path -> $target"
}

mkdir -p "$WS/.kiro"
echo "Kiro config (.kiro/):"
for d in steering agents skills hooks powers sops; do
  [ -e "$REPO/.kiro/$d" ] && link "../$NAME/.kiro/$d" "$WS/.kiro/$d"
done
echo "Repo-relative paths used by agents and steering:"
for d in core references examples tools songs analysis experiments plugins; do
  [ -e "$REPO/$d" ] && link "$NAME/$d" "$WS/$d"
done
for f in SONGWRITING_KNOWLEDGE_BASE.md MUSIC_PRODUCTION_THEORY.md; do
  [ -e "$REPO/$f" ] && link "$NAME/$f" "$WS/$f"
done
echo "Done. Edits through these links change the repo itself; commit from $REPO."
