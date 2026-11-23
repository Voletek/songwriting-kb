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
  INFO  first chorus later than 60 s of track time (pitch-ready commercial norm ~45-60 s),
        when no length target is set
  INFO  outside the length target: total length, intro length, time to the first chorus

Length targets (references/SONG_LENGTH_REFERENCE.md) are presets in tools/data/length_targets.json,
merged with tools/data/length_targets.local.json if it exists. They are guidance, not rules: song
length is the artist's call (core/tenets.md, Tenet 3). Precedence: command line > the song file's
"Length Target:" line > the preset. Examples of the song-file line:
    Length Target: radio
    Length Target: cinematic, intro <= 40s
    Length Target: 5:30-6:30, intro <= 45s, hook <= 1:20
    Length Target: none

The result is an estimate: Suno chooses its own phrasing. Bars per line is the biggest lever
(about 2 bars per line is typical; a slow ballad or a one-in-a-bar waltz may be 4).

Usage:
  python3 tools/estimate-runtime.py songs/<category>/<song>.md
  python3 tools/estimate-runtime.py <file> --bpm 132 --meter 3/4 --bars-per-line 2 --json
  python3 tools/estimate-runtime.py <file> --target radio --max-intro 20
  python3 tools/estimate-runtime.py --list-targets
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
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TARGET_LINE_RE = re.compile(r"^\W*Length\s+Target\s*:\s*(.+?)\s*$", re.I | re.M)
TIME_RE = r"(\d+(?::\d{1,2})?)\s*s?"


def parse_time(text):
    """'3:30' -> 210, '45' / '45s' -> 45. Returns None on failure."""
    if text is None:
        return None
    t = str(text).strip().lower().rstrip("s").strip()
    m = re.fullmatch(r"(\d+):(\d{1,2})", t)
    if m:
        return int(m.group(1)) * 60 + int(m.group(2))
    return int(t) if t.isdigit() else None


def fmt_time(sec):
    sec = int(round(sec))
    return f"{sec // 60}:{sec % 60:02d}"


def load_targets():
    presets = {}
    for name in ("length_targets.json", "length_targets.local.json"):
        path = os.path.join(DATA_DIR, name)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as handle:
                presets.update(json.load(handle).get("presets", {}))
    return presets


def parse_target_spec(spec, presets):
    """Parse 'radio', 'cinematic, intro <= 40s', '5:30-6:30, hook <= 1:20' or 'none'.

    Returns (target dict or None, error or None). A dict may be partial."""
    spec = spec.strip().strip("*_`")
    if not spec or spec.lower() in ("none", "off", "no"):
        return None, None
    target = {}
    for part in [p.strip() for p in spec.split(",") if p.strip()]:
        low = part.lower()
        if low in presets:
            target = dict(presets[low], name=low, **{k: v for k, v in target.items() if k != "name"})
            continue
        m = re.fullmatch(TIME_RE + r"\s*[-\u2013]\s*" + TIME_RE, low)
        if m:
            target["min_s"], target["max_s"] = parse_time(m.group(1)), parse_time(m.group(2))
            target.setdefault("name", "custom")
            continue
        m = re.fullmatch(r"(intro|hook|chorus|first chorus)\s*(<=|<|\u2264|max)?\s*" + TIME_RE, low)
        if m:
            key = "max_intro_s" if m.group(1) == "intro" else "max_hook_s"
            target[key] = parse_time(m.group(3))
            target.setdefault("name", "custom")
            continue
        return None, f"unrecognised Length Target part '{part}' (presets: {', '.join(sorted(presets))})"
    return target, None


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


def estimate(path, bpm=None, meter=None, bars_per_line=2.0, instrumental_bars=8, target=None, overrides=None):
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
    bed = (song.render or {}).get("bed_duration")
    bed_s = parse_time(bed) if bed else None
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
    if bed_s:
        res["findings"].append({"level": "INFO", "message": f"sung over a fixed instrumental ({fmt_time(bed_s)}, RENDER SETTINGS bed_duration): "
                                f"length and section timing come from the bed, not from line counts; the line-based estimate was {fmt_time(t)}. "
                                "Measure intro and chorus times with audio-lyrics-alignment after rendering"})
        res["line_estimate_s"] = round(t)
        t = bed_s
        res["runtime_s"], res["runtime"] = round(t), fmt_time(t)
        res["fixed_bed"] = True
        res["first_sung_s"] = res["first_chorus_s"] = res["hook_after_first_word_s"] = None
        first_sung = chorus_at = None
    if t > MCP_CAP_S:
        res["findings"].append({"level": "WARN", "message": f"estimated {res['runtime']} is over the {MCP_CAP_S} s Suno MCP duration cap: "
                                "render the first part, then use audio-extensions-create + audio-full-song (references/SUNO_MCP_REFERENCE.md)"})
    # Length target: command line > song file > preset (all optional)
    presets = load_targets()
    chosen, source = None, None
    m = TARGET_LINE_RE.search(text)
    if m:
        chosen, err = parse_target_spec(m.group(1), presets)
        source = "song file"
        if err:
            res["findings"].append({"level": "WARN", "message": err})
        elif chosen is None:
            source = "song file (none)"
    if target:
        cli, err = parse_target_spec(target, presets)
        if err:
            res["findings"].append({"level": "WARN", "message": err})
        else:
            chosen, source = cli, "command line"
    if overrides:
        chosen = dict(chosen or {"name": "custom"}, **{k: v for k, v in overrides.items() if v is not None})
        source = (source + " + overrides") if source else "command line"
    res["length_target"] = dict(chosen, source=source) if chosen else ({"source": source} if source else None)
    if chosen:
        name = chosen.get("label") or chosen.get("name", "custom")
        lo, hi = chosen.get("min_s"), chosen.get("max_s")
        if lo is not None and t < lo:
            res["findings"].append({"level": "INFO", "message": f"{fmt_time(t)} is under the '{name}' target of {fmt_time(lo)}-{fmt_time(hi or lo)} by {fmt_time(lo - t)}"})
        elif hi is not None and t > hi:
            res["findings"].append({"level": "INFO", "message": f"{fmt_time(t)} is over the '{name}' target of {fmt_time(lo or 0)}-{fmt_time(hi)} by {fmt_time(t - hi)}: cut breaks, repeats or a stanza, or keep it and note why"})
        else:
            res["findings"].append({"level": "PASS", "message": f"{fmt_time(t)} is inside the '{name}' target"})
        mi = chosen.get("max_intro_s")
        if mi is not None and first_sung is not None and first_sung > mi:
            res["findings"].append({"level": "INFO", "message": f"intro ~{round(first_sung)} s is over the target's {mi} s (Spotify counts a stream after 30 s)"})
        mh = chosen.get("max_hook_s")
        if mh is not None and chorus_at is not None and chorus_at > mh:
            res["findings"].append({"level": "INFO", "message": f"first chorus at ~{fmt_time(chorus_at)} is later than the target's {fmt_time(mh)}"})
        res["findings"].append({"level": "INFO", "message": "length targets are guidance (Tenet 3): override with a 'Length Target:' line or --min/--max/--max-intro/--max-hook"})
    elif chorus_at is not None and chorus_at > CHORUS_NORM_S:
        res["findings"].append({"level": "INFO", "message": f"first chorus at ~{round(chorus_at)} s of track time "
                                f"(pitch-ready commercial norm ~45-{CHORUS_NORM_S} s; fine for cinematic or story songs)"})
    if chorus_at is None:
        res["findings"].append({"level": "INFO", "message": "no sung [Chorus] found"})
    return res


def format_text(r):
    if r.get("error"):
        return f"=== {r['file']}: ERROR {r['error']}"
    lt = r.get("length_target")
    out = [f"=== RUNTIME ESTIMATE: {r['file']} ===",
           f"  {r['bpm']} BPM in {r['meter']} (one bar = {r['bar_s']} s), {r['bars_per_line']} bars per sung line, {r['sung_lines']} sung lines",
           f"  Estimated runtime: {r['runtime']} ({r['runtime_s']} s)"]
    if r["first_chorus_s"] is not None:
        out.append(f"  First chorus: ~{round(r['first_chorus_s'])} s of track time, "
                   f"~{round(r['hook_after_first_word_s'])} s after the first sung word")
    if lt and lt.get("name"):
        rng = f"{fmt_time(lt['min_s'])}-{fmt_time(lt['max_s'])}" if lt.get("min_s") is not None and lt.get("max_s") is not None else "no length range"
        extra = "".join(f", {k} <= {fmt_time(lt[v]) if v == 'max_hook_s' else str(lt[v]) + ' s'}" for k, v in (("intro", "max_intro_s"), ("first chorus", "max_hook_s")) if lt.get(v) is not None)
        out.append(f"  Length target: {lt.get('label') or lt['name']} ({rng}{extra}) [from {lt['source']}]")
    elif lt:
        out.append(f"  Length target: none [from {lt['source']}]")
    for s in r["timeline"]:
        out.append(f"    {s['start_s']:7.1f}s  {s['section'][:40]:<40} {s['bars']:>5g} bars  {s['duration_s']:6.1f}s")
    for f in r["findings"]:
        out.append(f"  [{f['level']}] {f['message']}")
    out.append("  NOTE: estimate only. Suno picks its own phrasing; bars per line is the biggest lever.")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--bpm", type=int)
    ap.add_argument("--meter", help="e.g. 3/4 or 6/8 (beats per bar = the top number)")
    ap.add_argument("--bars-per-line", type=float, default=2.0)
    ap.add_argument("--instrumental-bars", type=int, default=8)
    ap.add_argument("--target", help="length preset (see --list-targets) or a spec like '3:00-3:45, intro <= 15s'")
    ap.add_argument("--min", help="override the target's minimum length (m:ss or seconds)")
    ap.add_argument("--max", help="override the target's maximum length (m:ss or seconds)")
    ap.add_argument("--max-intro", help="override the target's maximum intro (seconds)")
    ap.add_argument("--max-hook", help="override the latest first chorus (m:ss or seconds)")
    ap.add_argument("--list-targets", action="store_true", help="print the length presets and exit")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if args.list_targets:
        for name, t in sorted(load_targets().items()):
            print(f"{name:10} {t.get('label', ''):45} {fmt_time(t['min_s'])}-{fmt_time(t['max_s'])}  intro <= {t.get('max_intro_s')} s  first chorus <= {fmt_time(t.get('max_hook_s', 0))}")
        return 0
    if not args.paths:
        ap.error("give at least one song file")
    overrides = {"min_s": parse_time(args.min), "max_s": parse_time(args.max),
                 "max_intro_s": parse_time(args.max_intro), "max_hook_s": parse_time(args.max_hook)}
    overrides = {k: v for k, v in overrides.items() if v is not None} or None
    results = [estimate(p, args.bpm, args.meter, args.bars_per_line, args.instrumental_bars, args.target, overrides)
               for p in args.paths]
    if args.json:
        print(json.dumps(results if len(results) > 1 else results[0], indent=2))
    else:
        print("\n".join(format_text(r) for r in results))
    return 1 if any(r.get("error") for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
