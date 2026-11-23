#!/usr/bin/env python3
"""estimate-runtime.py - estimate a song's length and when its first chorus lands.

Uses the runtime formula from core/methodology/songwriting.md (Step 8):

    runtime_s ~= (sung_lines x bars_per_line + instrumental_bars) x beats_per_bar x 60 / BPM

BPM and meter are read from the Style Prompt (or the Production Notes) unless given as options.
Sections with no sung lines count as instrumental: the intro takes its length from an
"N-bar intro" phrase in the [Production Direction] block when there is one, otherwise
--instrumental-bars (default 8); an outro with no lyrics counts half that.

Checks:
  WARN  runtime over 360 s (the Suno MCP duration cap; longer songs need an extension)
  INFO  first chorus later than 60 s of track time (pitch-ready commercial norm ~45-60 s)

The result is an estimate: Suno chooses its own phrasing. Bars per line is the biggest lever
(about 2 bars per line is typical; a slow ballad or a one-in-a-bar waltz may be 4).

Usage:
  python3 tools/estimate-runtime.py songs/<category>/<song>.md
  python3 tools/estimate-runtime.py <file> --bpm 132 --meter 3/4 --bars-per-line 2 --json
Exit code: 1 if a file can't be read or has no lyrics or BPM, else 0.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import songfile  # noqa: E402

MCP_CAP_S = 360
CHORUS_NORM_S = 60
BPM_RE = re.compile(r"(\d{2,3})\s*BPM", re.I)
METER_RE = re.compile(r"(?<![\d/])(2|3|4|5|6|7|9|12)/(4|8)(?![\d/])")
INTRO_BARS_RE = re.compile(r"(\d{1,3})[- ]bar(?:s)?\s+(?:\w+\s+){0,2}intro", re.I)


def _sections(lyrics):
    """Return [(name, sung_lines)] in order, using the shared section-tag parser."""
    out = []
    current = None
    for _no, kind, text in songfile.iter_lyric_lines(lyrics):
        if kind == "tag":
            for g in songfile.BRACKET_GROUP_RE.findall(text):
                if songfile.SECTION_TAG_RE.match(g):
                    current = [g.strip("[] "), 0]
                    out.append(current)
                    break
            continue
        if kind == "lyric" and current is not None:
            current[1] += 1
    return [(name, n) for name, n in out]


def _bare(name):
    name = re.split(r"\s*[\u2014\u2013|:]\s*|\s+-\s+", name)[0]
    return re.sub(r"\s+\d+$", "", name).strip().lower()


def estimate(path, bpm=None, meter=None, bars_per_line=2.0, instrumental_bars=8):
    song = songfile.SongFile(path)
    res = {"file": path, "error": None, "findings": []}
    if song.error:
        res["error"] = song.error
        return res
    if not song.lyrics:
        res["error"] = "no lyrics found"
        return res
    text = song.text or ""
    search = "\n".join(filter(None, [song.style, text]))
    if bpm is None:
        m = BPM_RE.search(search)
        bpm = int(m.group(1)) if m else None
    if bpm is None:
        res["error"] = "no BPM found (pass --bpm)"
        return res
    if meter is None:
        m = METER_RE.search(search)
        meter = f"{m.group(1)}/{m.group(2)}" if m else "4/4"
    beats = int(meter.split("/")[0])
    bar_s = beats * 60.0 / bpm
    m = INTRO_BARS_RE.search(text)
    intro_bars = int(m.group(1)) if m else instrumental_bars

    timeline = []
    t = 0.0
    first_sung = None
    chorus_at = None
    for name, sung in _sections(song.lyrics):
        bare = _bare(name)
        if sung:
            bars = sung * bars_per_line
            if first_sung is None:
                first_sung = t
        elif bare == "end":
            continue
        elif "intro" in bare:
            bars = intro_bars
        elif "outro" in bare:
            bars = instrumental_bars / 2
        else:
            bars = instrumental_bars
        if chorus_at is None and "chorus" in bare and "pre" not in bare and "post" not in bare and sung:
            chorus_at = t
        dur = bars * bar_s
        timeline.append({"section": name, "sung_lines": sung, "bars": bars, "start_s": round(t, 1),
                         "duration_s": round(dur, 1)})
        t += dur

    res.update({
        "bpm": bpm, "meter": meter, "bars_per_line": bars_per_line, "bar_s": round(bar_s, 2),
        "sung_lines": sum(s["sung_lines"] for s in timeline),
        "runtime_s": round(t), "runtime": f"{int(t // 60)}:{int(t % 60):02d}",
        "first_sung_s": round(first_sung, 1) if first_sung is not None else None,
        "first_chorus_s": round(chorus_at, 1) if chorus_at is not None else None,
        "hook_after_first_word_s": round(chorus_at - first_sung, 1) if chorus_at is not None and first_sung is not None else None,
        "timeline": timeline,
    })
    if t > MCP_CAP_S:
        res["findings"].append({"level": "WARN", "message": f"estimated {res['runtime']} is over the {MCP_CAP_S} s Suno MCP duration cap: "
                                "render the first part, then use audio-extensions-create + audio-full-song (references/SUNO_MCP_REFERENCE.md)"})
    if chorus_at is not None and chorus_at > CHORUS_NORM_S:
        res["findings"].append({"level": "INFO", "message": f"first chorus at ~{round(chorus_at)} s of track time "
                                f"(pitch-ready commercial norm ~45-{CHORUS_NORM_S} s; fine for cinematic or story songs)"})
    if chorus_at is None:
        res["findings"].append({"level": "INFO", "message": "no sung [Chorus] found"})
    return res


def format_text(r):
    if r.get("error"):
        return f"=== {r['file']}: ERROR {r['error']}"
    out = [f"=== RUNTIME ESTIMATE: {r['file']} ===",
           f"  {r['bpm']} BPM in {r['meter']} (one bar = {r['bar_s']} s), {r['bars_per_line']} bars per sung line, {r['sung_lines']} sung lines",
           f"  Estimated runtime: {r['runtime']} ({r['runtime_s']} s)"]
    if r["first_chorus_s"] is not None:
        out.append(f"  First chorus: ~{round(r['first_chorus_s'])} s of track time, "
                   f"~{round(r['hook_after_first_word_s'])} s after the first sung word")
    for s in r["timeline"]:
        out.append(f"    {s['start_s']:7.1f}s  {s['section'][:40]:<40} {s['bars']:>5g} bars  {s['duration_s']:6.1f}s")
    for f in r["findings"]:
        out.append(f"  [{f['level']}] {f['message']}")
    out.append("  NOTE: estimate only. Suno picks its own phrasing; bars per line is the biggest lever.")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--bpm", type=int)
    ap.add_argument("--meter", help="e.g. 3/4 or 6/8 (beats per bar = the top number)")
    ap.add_argument("--bars-per-line", type=float, default=2.0)
    ap.add_argument("--instrumental-bars", type=int, default=8)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    results = [estimate(p, args.bpm, args.meter, args.bars_per_line, args.instrumental_bars) for p in args.paths]
    if args.json:
        print(json.dumps(results if len(results) > 1 else results[0], indent=2))
    else:
        print("\n".join(format_text(r) for r in results))
    return 1 if any(r.get("error") for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
