#!/usr/bin/env python3
"""suno-fields.py - print a song file's Suno fields, ready to send or paste.

Outputs exactly what tools/validate-song.py counts:
  title           from the [Title: ...] tag (else the first Markdown heading)
  style           the Style Prompt section (count notes and exclusion lines removed)
  negative_style  the Exclusions, comma-separated (Suno's Exclude field)
  lyrics          the Lyrics section from the top through [End]

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
    out["_counts"] = {"style": f"{len(song.style)}/1000", "lyrics": f"{len(song.lyrics)}/5000",
                      "negative_style": f"{len(out.get('negative_style', ''))}/1000"}
    return out, None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("path")
    ap.add_argument("--field", choices=["title", "style", "negative_style", "lyrics"])
    ap.add_argument("--no-counts", action="store_true", help="omit the _counts key")
    args = ap.parse_args(argv)
    out, err = fields(args.path)
    if err:
        print(f"ERROR {args.path}: {err}", file=sys.stderr)
        return 1
    if args.field:
        print(out.get(args.field, ""))
        return 0
    if args.no_counts:
        out.pop("_counts", None)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
