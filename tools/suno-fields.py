#!/usr/bin/env python3
"""suno-fields.py - print a song file's Suno fields, ready to send or paste.

Outputs exactly what tools/validate-song.py counts:
  title           from the [Title: ...] tag (else the first Markdown heading)
  style           the Style Prompt section (count notes and exclusion lines removed)
  negative_style  the Exclusions, comma-separated (Suno's Exclude field)
  lyrics          the Lyrics section from the top through [End]

With a `## RENDER SETTINGS` section in the song file (SOP 10), it also outputs `voice_id`, `model`,
`controls`, `duration` (+ `duration_strict: false`) and `vocal_gender`, so settings aren't retyped or
forgotten. It warns on stderr when no voice has been chosen ("voice: none" records "no saved voice").

The JSON keys match the Suno MCP `audio-create` fields (references/SUNO_MCP_REFERENCE.md), so the
output can be passed straight to that tool. Run validate-song.py first: this tool only extracts.

Usage:
  python3 tools/suno-fields.py songs/<category>/<song>.md            # JSON
  python3 tools/suno-fields.py <file> --field lyrics                   # one field as plain text
Exit code: 1 if the file can't be read or has no Style or Lyrics section.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import songfile  # noqa: E402

TITLE_TAG_RE = re.compile(r"\[\s*Title\s*:\s*([^\]]+?)\s*\]", re.I)
HEADING_TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)


def fields(path):
    song = songfile.SongFile(path)
    if song.error:
        return None, song.error
    if not song.style or not song.lyrics:
        return None, "needs both a Style Prompt and a Lyrics section"
    m = TITLE_TAG_RE.search(song.lyrics)
    if m:
        title = m.group(1)
    else:
        h = HEADING_TITLE_RE.search(song.text or "")
        title = re.sub(r"\s*[\u2014\u2013-]\s*.*$", "", h.group(1)).strip() if h else ""
    out = {"title": title, "style": song.style, "lyrics": song.lyrics}
    if song.exclusions:
        out["negative_style"] = ", ".join(i.lstrip("-\u2011\u2010\u2013 ") for i in song.exclusions)
    rs = song.render or {}
    voice_id = rs.get("voice_id", "").strip()
    voice = rs.get("voice", "").strip()
    if voice_id and voice_id.lower() not in ("none", "-"):
        out["voice_id"] = voice_id
    elif voice.lower() not in ("none", "no", "no saved voice"):
        out["_warnings"] = ["no voice chosen: ask which saved voice to use before rendering (SOP 10 Step 1), "
                            "then add 'voice_id:' under ## RENDER SETTINGS, or 'voice: none' for a generated singer"]
    if rs.get("model"):
        out["model"] = rs["model"]
    ctrl = songfile.parse_controls(rs.get("controls", ""))
    if ctrl:
        out["controls"] = ctrl
    if rs.get("vocal_gender") and "voice_id" not in out:
        out["vocal_gender"] = rs["vocal_gender"].lower()
    if rs.get("duration"):
        d = rs["duration"].strip()
        secs = int(d.split(":")[0]) * 60 + int(d.split(":")[1]) if ":" in d else int(float(d))
        out["duration"] = secs
        out["duration_strict"] = rs.get("duration_strict", "false").strip().lower() in ("true", "yes", "1")
    if rs.get("cover_of"):
        out["_cover_of"] = rs["cover_of"]
    out["_counts"] = {"style": f"{len(song.style)}/1000", "lyrics": f"{len(song.lyrics)}/5000",
                      "negative_style": f"{len(out.get('negative_style', ''))}/1000"}
    return out, None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("path")
    ap.add_argument("--field", choices=["title", "style", "negative_style", "lyrics", "voice_id", "model"])
    ap.add_argument("--no-counts", action="store_true", help="omit the _counts key")
    args = ap.parse_args(argv)
    out, err = fields(args.path)
    if err:
        print(f"ERROR {args.path}: {err}", file=sys.stderr)
        return 1
    if args.field:
        print(out.get(args.field, ""))
        return 0
    for w in out.get("_warnings", []):
        print(f"WARN {args.path}: {w}", file=sys.stderr)
    if args.no_counts:
        out.pop("_counts", None)
        out.pop("_warnings", None)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
