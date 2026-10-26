#!/usr/bin/env python3
"""
check-repo.py - repository integrity checks (standard library only).

Checks:
  1. `#[[file:PATH]]` includes in Markdown resolve (code spans and fenced blocks are ignored,
     so placeholders written as `#[[file:core/methodology/X.md]]` are fine).
  2. Relative Markdown links `[text](path)` resolve.
  3. Agent front matter (.kiro/agents/*.md): `resources:` file:// / skill:// entries resolve.
  4. Hooks (.kiro/hooks/*.json and examples/albums/*/continuity-hook.json) follow the Kiro v1 schema.
  5. Steering front matter (.kiro/steering, power steering, example album steering) starts at byte 0
     and uses a valid `inclusion` mode with its required keys.
  6. Skills: SKILL.md front matter `name` matches the folder, `description` present (<=1024 chars).
  7. Every *.json file parses; plugin JSON ids match their folders.

Usage:  python3 tools/check-repo.py [--root PATH]
Exit code 1 if any ERROR, else 0 (WARN lines are advisory).
"""

import argparse
import glob
import json
import os
import re
import sys

SKIP_DIRS = {".git", ".agents", "node_modules", "__pycache__", ".venv", "venv"}
VALID_TRIGGERS = {"SessionStart", "SessionEnd", "Stop", "UserPromptSubmit", "PreTaskExec", "PostTaskExec",
                  "PreToolUse", "PostToolUse", "PostFileCreate", "PostFileSave", "PostFileDelete"}
VALID_INCLUSION = {"always", "fileMatch", "manual", "auto"}


class Results:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")


def iter_files(root, suffix):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            if name.endswith(suffix):
                yield os.path.join(dirpath, name)


def strip_code(text):
    """Blank out fenced code blocks and inline code spans, preserving line count."""
    out_lines = []
    in_fence = False
    for line in text.split("\n"):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            out_lines.append("")
            continue
        if in_fence:
            out_lines.append("")
            continue
        out_lines.append(re.sub(r"`[^`]*`", "", line))
    return "\n".join(out_lines)


def parse_front_matter(text):
    """Minimal YAML front-matter parser: scalars, quoted strings, flow lists and block lists."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    body = text[3:end].strip("\n")
    data, key = {}, None
    for raw in body.split("\n"):
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", raw)
        if m and not raw.startswith((" ", "\t", "-")):
            key, val = m.group(1), m.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                items = [i.strip().strip("'\"") for i in val[1:-1].split(",") if i.strip()]
                data[key] = items
            elif val == "":
                data[key] = []
            else:
                data[key] = val.strip("'\"")
            continue
        lm = re.match(r"^\s*-\s+(.*)$", raw)
        if lm and key is not None:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(lm.group(1).strip().strip("'\""))
    return data


def check_includes_and_links(root, res):
    for path in iter_files(root, ".md"):
        rel = os.path.relpath(path, root)
        with open(path, encoding="utf-8-sig") as fh:
            text = fh.read()
        clean = strip_code(text)
        for no, line in enumerate(clean.split("\n"), 1):
            for m in re.finditer(r"#\[\[(file|folder):([^\]]+)\]\]", line):
                target = m.group(2).strip()
                target = re.sub(r":\d+(-\d+)?$", "", target)
                if any(ch in target for ch in "<>[]*") or target in ("...", "path"):
                    res.warn(f"{rel}:{no}", f"placeholder include #[[{m.group(1)}:{target}]] outside a code span")
                    continue
                if not os.path.exists(os.path.join(root, target)):
                    res.error(f"{rel}:{no}", f"#[[{m.group(1)}:{target}]] does not exist")
            for m in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", line):
                href = m.group(1)
                if re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I) or href.startswith("#"):
                    continue
                target = href.split("#", 1)[0]
                if not target:
                    continue
                base = root if target.startswith("/") else os.path.dirname(path)
                full = os.path.normpath(os.path.join(base, target.lstrip("/")))
                if not os.path.exists(full):
                    res.error(f"{rel}:{no}", f"broken link ({href})")


def check_agents(root, res):
    for path in sorted(glob.glob(os.path.join(root, ".kiro", "agents", "*.md"))):
        rel = os.path.relpath(path, root)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        fm = parse_front_matter(text)
        if fm is None:
            res.error(rel, "missing front matter")
            continue
        if not fm.get("description"):
            res.error(rel, "front matter has no description")
        resources = fm.get("resources", [])
        if isinstance(resources, str):
            resources = [resources]
        for r in resources:
            if r.startswith("file://"):
                target = r[len("file://"):].lstrip("./")
                matches = glob.glob(os.path.join(root, target))
                if not matches:
                    res.error(rel, f"resource {r} does not exist")
            elif r.startswith("skill://"):
                target = r[len("skill://"):]
                if not glob.glob(os.path.join(root, target)):
                    res.error(rel, f"resource {r} does not exist")
            else:
                res.warn(rel, f"resource '{r}' is not a file:// or skill:// URI")
        if "#[[file:" in strip_code(text):
            res.warn(rel, "uses #[[file:]] (documented for steering only); prefer resources: in front matter")


def check_hooks(root, res):
    paths = sorted(glob.glob(os.path.join(root, ".kiro", "hooks", "*")))
    paths += sorted(glob.glob(os.path.join(root, "examples", "albums", "*", "continuity-hook.json")))
    for path in paths:
        rel = os.path.relpath(path, root)
        if not path.endswith(".json"):
            res.error(rel, "hook files must be .json (Kiro v1 schema)")
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except ValueError as exc:
            res.error(rel, f"invalid JSON: {exc}")
            continue
        if data.get("version") != "v1" or not isinstance(data.get("hooks"), list) or not data["hooks"]:
            res.error(rel, "not a Kiro v1 hook file (needs version: \"v1\" and a non-empty hooks[] array)")
            continue
        for i, hook in enumerate(data["hooks"]):
            where = f"{rel} hooks[{i}]"
            if not isinstance(hook.get("name"), str) or not hook["name"]:
                res.error(where, "missing name")
            if hook.get("trigger") not in VALID_TRIGGERS:
                res.error(where, f"invalid trigger {hook.get('trigger')!r}")
            action = hook.get("action") or {}
            if action.get("type") == "agent":
                if not action.get("prompt"):
                    res.error(where, "agent action needs a prompt")
            elif action.get("type") == "command":
                if not action.get("command"):
                    res.error(where, "command action needs a command")
                else:
                    for script in re.findall(r"(tools/[\w./-]+\.py)", action["command"]):
                        if not os.path.exists(os.path.join(root, script)):
                            res.error(where, f"command references missing script {script}")
            else:
                res.error(where, f"action.type must be 'agent' or 'command', got {action.get('type')!r}")
            matcher = hook.get("matcher")
            if matcher is not None:
                try:
                    re.compile(matcher)
                except re.error as exc:
                    res.error(where, f"matcher is not a valid regex: {exc}")
                if re.search(r"\(\?<?[=!]", matcher):
                    res.warn(where, "matcher uses lookaround; the regex engine is not documented, avoid it")


def check_steering(root, res):
    paths = sorted(glob.glob(os.path.join(root, ".kiro", "steering", "*.md")))
    paths += sorted(glob.glob(os.path.join(root, ".kiro", "powers", "*", "steering", "*.md")))
    paths += sorted(glob.glob(os.path.join(root, "examples", "albums", "*", "steering.md")))
    for path in paths:
        rel = os.path.relpath(path, root)
        with open(path, "rb") as fh:
            raw = fh.read()
        text = raw.decode("utf-8-sig")
        if not raw.startswith(b"---"):
            if "/powers/" in rel:
                continue  # power steering files may be plain guides
            res.error(rel, "front matter must be the first bytes of the file")
            continue
        fm = parse_front_matter(text)
        if fm is None:
            res.error(rel, "unterminated front matter")
            continue
        inc = fm.get("inclusion", "always")
        if inc not in VALID_INCLUSION:
            res.error(rel, f"invalid inclusion {inc!r}")
        if inc == "auto" and not (fm.get("name") and fm.get("description")):
            res.error(rel, "inclusion: auto requires name and description")
        if inc == "fileMatch" and not fm.get("fileMatchPattern"):
            res.error(rel, "inclusion: fileMatch requires fileMatchPattern")


def check_skills(root, res):
    for path in sorted(glob.glob(os.path.join(root, ".kiro", "skills", "*", "SKILL.md"))):
        rel = os.path.relpath(path, root)
        folder = os.path.basename(os.path.dirname(path))
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        fm = parse_front_matter(text)
        if fm is None:
            res.error(rel, "missing front matter")
            continue
        if fm.get("name") != folder:
            res.error(rel, f"name {fm.get('name')!r} must match folder {folder!r}")
        desc = fm.get("description") or ""
        if not desc:
            res.error(rel, "missing description")
        elif len(desc) > 1024:
            res.error(rel, f"description is {len(desc)} chars (max 1024)")
        for m in re.finditer(r"`([\w./-]+\.(?:md|py|json|yml))`", text):
            target = m.group(1)
            if "/" in target and not os.path.exists(os.path.join(root, target)) and "YOUR" not in target:
                res.error(rel, f"references missing file {target}")


def check_json(root, res):
    for path in iter_files(root, ".json"):
        rel = os.path.relpath(path, root)
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except ValueError as exc:
            res.error(rel, f"invalid JSON: {exc}")
            continue
        if path.endswith(".plugin.json"):
            folder = os.path.basename(os.path.dirname(path))
            if data.get("id") != folder:
                res.error(rel, f"plugin id {data.get('id')!r} does not match folder {folder!r}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Repository integrity checks.")
    parser.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = parser.parse_args(argv)
    root = os.path.abspath(args.root)
    res = Results()
    check_includes_and_links(root, res)
    check_agents(root, res)
    check_hooks(root, res)
    check_steering(root, res)
    check_skills(root, res)
    check_json(root, res)
    for w in res.warnings:
        print(f"[WARN]  {w}")
    for e in res.errors:
        print(f"[ERROR] {e}")
    print(f"check-repo: {len(res.errors)} error(s), {len(res.warnings)} warning(s)")
    return 1 if res.errors else 0


if __name__ == "__main__":
    sys.exit(main())
