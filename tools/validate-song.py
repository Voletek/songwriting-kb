#!/usr/bin/env python3
"""
validate-song.py - deterministic Suno format checks for song files (V6 default, v5.5-era aware).

Checks: Style/Lyrics character limits, required lyric elements, Exclude-field format,
genre-first, style descriptor count, named-layer declarations, tag placement, V6 tag
grammar ([Tag Vocabulary] block, [Instrument: X In/Out] choreography, mixed paradigms,
obsolete tags), artist references and gear/model names.

Usage:
    python3 tools/validate-song.py songs/my_song.md
    python3 tools/validate-song.py songs/                 # directories are scanned recursively
    python3 tools/validate-song.py --json examples/songs/
    python3 tools/validate-song.py --strict songs/        # WARN also fails (exit 1)
    python3 tools/validate-song.py --hook {{filePath}}    # Kiro hook mode: always exit 0

Statuses: PASS, INFO (advisory), WARN (review), FAIL (must fix), ERROR (unreadable).
README.md and *.brief.md are skipped. A file containing <!-- song-format: legacy --> is an
archived pre-standard example: missing direction blocks are reported as WARN, not FAIL.
Exit code: 1 if any FAIL/ERROR (or WARN with --strict), else 0. --hook always exits 0.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import songfile  # noqa: E402

STYLE_LIMIT = 1000
LYRICS_LIMIT = 5000
STYLE_WARN = 900
LYRICS_WARN = 4500
DESCRIPTOR_WARN = 10  # v5.5-era Tier 3 heuristic (5-8 sweet spot, past ~10 conflicts)

GENRE_TERMS = [
    "rock", "pop", "folk", "jazz", "blues", "metal", "punk", "indie", "electronic", "electronica",
    "ambient", "cinematic", "orchestral", "classical", "country", "soul", "r&b", "rnb", "hip-hop",
    "hip hop", "rap", "trap", "dance", "house", "techno", "trance", "dubstep", "drum and bass", "dnb",
    "edm", "alternative", "post-rock", "post rock", "post-punk", "neo-soul", "neo soul", "synthwave",
    "synth-pop", "synthpop", "darkwave", "lo-fi", "lofi", "acoustic", "industrial", "tribal", "chant",
    "gothic", "goth", "doom", "grunge", "funk", "disco", "reggae", "ska", "latin", "celtic", "nordic",
    "experimental", "noise", "drone", "shoegaze", "trip-hop", "trip hop", "psychedelic", "emo",
    "hardcore", "progressive", "prog", "art rock", "art pop", "chamber", "baroque", "bluegrass",
    "americana", "gospel", "choral", "soundtrack", "score", "ballad", "singer-songwriter", "hymn",
    "shanty", "sea shanty", "waltz", "lullaby", "bossa nova", "samba", "flamenco", "afrobeat",
    "k-pop", "j-pop", "j-rock", "grime", "drill", "phonk", "hyperpop", "new wave", "britpop",
    "emo-rap", "dark ambient", "dark folk", "neofolk", "heavy", "metalcore", "deathcore", "black metal",
    "power ballad", "anthem", "march", "carnatic", "raga", "polka", "zydeco", "cajun", "motown",
    "dream pop", "bedroom pop", "chillwave", "vaporwave", "breakbeat", "garage", "big band", "swing",
    "bebop", "fusion", "world", "worldbeat", "medieval", "renaissance", "opera", "operatic", "musical",
    "broadway", "cabaret", "chanson", "fado", "tango", "mariachi", "cumbia", "reggaeton", "dancehall",
    "soca", "calypso", "highlife", "kizomba", "spoken word", "slam",
]
GENRE_RE = re.compile(r"(?<![a-z])(" + "|".join(re.escape(t) for t in sorted(GENRE_TERMS, key=len, reverse=True)) + r")(?![a-z])", re.I)
TECHNICAL_ITEM_RE = re.compile(
    r"^\s*(~?\d+\s*(-\s*\d+\s*)?bpm|bpm\b|tempo\b|key\b|in the key|[a-g][#b\u266f\u266d]?\s*(major|minor|maj|min|m)\b|"
    r"\d+/\d+|time signature|vocal range|(male|female)?\s*\w*\s*[a-g][#b]?\d\s*[-\u2013]\s*[a-g][#b]?\d)",
    re.I,
)

LAYER_ALIASES = {
    "robotic": ["robot", "robotic", "ai voice", "a.i. voice", "machine", "synthetic", "digital voice", "vocoder", "android", "computer voice"],
    "echo": ["echo", "delay"],
    "whisper": ["whisper"],
    "choir": ["choir", "choral"],
    "ghost": ["ghost", "spectral"],
    "distant": ["distant", "far"],
}

OBSOLETE_TAGS = [
    (r"\[\s*bpm\s*:", "[bpm:] (put BPM in the Style field)"),
    (r"\[\s*key\s*:", "[key:] (put key in the Style field)"),
    (r"\[\s*loop\b", "[loop] (unsupported)"),
    (r"\[\s*autotune\b", "[autotune] (deprecated)"),
    (r"\[\s*(mix|master)\b", "[mix]/[master] (ineffective)"),
    (r"\[\s*volume\b", "[volume] (use dynamics tags)"),
    (r"\[\s*filter\b(?!\s*(open|close))", "[filter] (describe in Production Direction)"),
    (r"\[\s*panning\b", "[panning] (ineffective)"),
]

ARTIST_NAMES = [
    "Radiohead", "Billie Eilish", "Wardruna", "Sigur Ros", "Hozier", "Taylor Swift", "The Beatles",
    "Beatles", "Pink Floyd", "Nirvana", "Beyonce", "Adele", "Drake", "Kendrick Lamar", "Led Zeppelin",
    "Bob Dylan", "Coldplay", "Daft Punk", "Aphex Twin", "Nine Inch Nails", "Bjork", "Massive Attack",
    "Portishead", "Mumford", "Arctic Monkeys", "Danny Elfman", "Hans Zimmer", "Ed Sheeran", "Lana Del Rey",
    "The Weeknd", "Post Malone", "Imagine Dragons", "Linkin Park", "Metallica", "Johnny Cash",
    "Dolly Parton", "Chris Stapleton", "Zach Bryan", "Bon Iver", "Phoebe Bridgers", "Florence",
    "Enya", "Vulfpeck", "Rex Orange County", "Tool", "Deftones", "Evanescence", "Gojira", "Sleep Token",
    "Ghost", "Fleetwood Mac", "Queen", "David Bowie", "Prince", "Michael Jackson", "Eminem", "Kanye",
    "Rihanna", "Lady Gaga", "Olivia Rodrigo", "Noah Kahan", "Tyler Childers", "Sturgill Simpson",
]
# Words that commonly follow "like"/precede "vibes"/"feel" in normal prose.
NON_ARTIST_WORDS = {
    "the", "a", "an", "every", "pure", "raw", "glass", "fire", "water", "thunder", "gold", "silver", "ice",
    "stone", "wind", "rain", "smoke", "velvet", "silk", "honey", "iron", "steel", "dark", "light", "soft",
    "hard", "gothic", "folk", "cinematic", "warm", "cold", "vintage", "retro", "modern", "live", "late",
    "early", "summer", "winter", "night", "morning", "church", "campfire", "western", "southern",
    "nordic", "celtic", "medieval", "tribal", "epic", "lofi", "lo-fi", "jazz", "soul", "pop", "rock",
    "a cappella", "chamber", "parlor", "room", "studio", "radio", "vinyl", "tape", "it", "this", "that",
    "someone", "something", "home", "heartbeat", "breath", "ghost", "machine", "prayer", "lullaby",
}

GEAR_PATTERNS = [
    r"\bTB-?303\b", r"\bTR-?(808|909|606|707)\b", r"\b808s?\b(?!\s*(bass|kick|drum)s?\b)", r"\bKorg\s*M1\b",
    r"\bMini-?moog\b", r"\bMoog\s+(Model\s*D|Sub\s*\d+|Voyager|Grandmother|Matriarch)\b", r"\bJuno-?\d{2,3}\b",
    r"\bJupiter-?\d\b", r"\bDX-?7\b", r"\bProphet-?(5|6|10|12|08)\b", r"\bOB-?(X|Xa|6|8)\b", r"\bFairlight\b",
    r"\bTelecaster\b", r"\bStratocaster\b", r"\bLes\s*Paul\b", r"\bSG\s+Standard\b", r"\bMarshall\s+(amp|stack|head|cab|JCM\w*|Plexi)\b",
    r"\bVox\s*AC-?\d+\b", r"\bFender\s+(Twin|Deluxe|Bassman|Jazzmaster|Jaguar|Precision|P-Bass|Jazz\s*Bass)\b",
    r"\bGibson\s+(J-?45|Hummingbird|SG|ES-?\d+|Flying\s*V|Explorer)\b", r"\bSteinway(\s+Model\s+\w+)?\b",
    r"\bMPC\s*\d{2,4}\b", r"\bSP-?(404|1200)\b", r"\bLinnDrum\b", r"\bLM-?1\b", r"\bMellotron\s+M\d+\b",
    r"\bCS-?80\b", r"\bMS-?20\b", r"\bSH-?101\b", r"\bRE-?201\b", r"\bLA-?2A\b", r"\b1176\b", r"\bNeve\s*\d+\b",
    r"\bSM-?(57|58|7B)\b", r"\bU-?(47|87)\b",
]


class Report:
    def __init__(self, path):
        self.path = path
        self.error = None
        self.skipped = None
        self.checks = []

    def add(self, name, status, detail, items=None):
        entry = {"name": name, "status": status, "detail": detail}
        if items:
            entry["items"] = items
        self.checks.append(entry)

    @property
    def failures(self):
        return sum(1 for c in self.checks if c["status"] == "FAIL")

    @property
    def warnings(self):
        return sum(1 for c in self.checks if c["status"] == "WARN")

    @property
    def result(self):
        if self.error:
            return "ERROR"
        if self.skipped:
            return "SKIP"
        if self.failures:
            return "FAIL"
        if self.warnings:
            return "WARN"
        return "PASS"

    def as_dict(self):
        return {
            "file": self.path,
            "result": self.result,
            "error": self.error,
            "skipped": self.skipped,
            "failures": self.failures,
            "warnings": self.warnings,
            "checks": self.checks,
        }


# --------------------------------------------------------------------------- checks

def check_char_counts(song, rep):
    if song.style is None:
        rep.add("Style Prompt Characters", "FAIL", "no Style Prompt section found")
    else:
        n = len(song.style)
        status = "FAIL" if n > STYLE_LIMIT else "INFO" if n > STYLE_WARN else "PASS"
        rep.add("Style Prompt Characters", status, f"{n}/{STYLE_LIMIT} chars (exclusions and count notes not counted)")
    if song.lyrics is None:
        rep.add("Lyrics Field Characters", "FAIL", "no Lyrics section found")
    else:
        n = len(song.lyrics)
        status = "FAIL" if n > LYRICS_LIMIT else "INFO" if n > LYRICS_WARN else "PASS"
        rep.add("Lyrics Field Characters", status, f"{n}/{LYRICS_LIMIT} chars (through the end terminator)")


def check_required_elements(song, rep):
    lyr = song.lyrics or ""
    present = {
        "[Title:]": bool(re.search(r"\[\s*Title\s*:", lyr, re.I)),
        "[Production Direction:]": bool(re.search(r"\[\s*(Production|Composition)\s+Direction\b", lyr, re.I)),
        "[Vocal Direction:]": bool(re.search(r"\[\s*Vocal\s+Direction\b", lyr, re.I)),
        "[End]": song.lyrics_has_end,
    }
    for name, ok in present.items():
        if ok:
            rep.add(f"Required Element: {name}", "PASS", "present")
            continue
        if song.lyrics is None:
            rep.add(f"Required Element: {name}", "FAIL", "missing (no Lyrics section)")
        elif song.legacy:
            rep.add(f"Required Element: {name}", "WARN", "missing (archived legacy example; required for new songs)")
        else:
            hint = " ([End] for V6; legacy [end] accepted)" if name == "[End]" else ""
            if name == "[Production Direction:]":
                hint = " ([Composition Direction] accepted as an alias)"
            rep.add(f"Required Element: {name}", "FAIL", "missing" + hint)


def check_exclusions(song, rep):
    if not song.exclusions:
        rep.add("Exclusions", "INFO", "no exclusions found (optional; put negatives in an ## EXCLUSIONS: section)")
        return
    prefixed = [i for i in song.exclusions if re.match(r"^\s*[-\u2011\u2010\u2012\u2013\u2212]", i)]
    hyphen_kinds = {i.strip()[0] for i in prefixed}
    problems = []
    if prefixed:
        kinds = ", ".join(sorted("U+%04X" % ord(k) for k in hyphen_kinds))
        problems.append(f"{len(prefixed)} item(s) carry a dash prefix ({kinds}); the Exclude field takes plain comma-separated text")
    if len(hyphen_kinds) > 1:
        problems.append("mixed hyphen characters (ASCII and Unicode look identical)")
    if "lyrics-bracket" in song.exclusion_sources:
        problems.append("an [Exclusions:] line sits inside the Lyrics section; move it to the Exclude field")
    if problems:
        rep.add("Exclusions Format", "WARN", "; ".join(problems))
    else:
        src = "## EXCLUSIONS section" if "section" in song.exclusion_sources else "legacy [Exclusions:] line"
        rep.add("Exclusions Format", "PASS", f"{len(song.exclusions)} plain item(s) from {src}")


def _style_items(style):
    main = []
    for line in style.split("\n"):
        s = line.strip()
        if not s:
            if main:
                break
            continue
        if re.match(r"^(structure|vocal|production|style)\s*:", s, re.I) and main:
            break
        main.append(re.sub(r"^(style)\s*:\s*", "", s, flags=re.I))
    return [i.strip() for i in " ".join(main).split(",") if i.strip()]


def check_genre_first(song, rep):
    if not song.style:
        rep.add("Genre First", "FAIL", "no Style Prompt text")
        return
    items = _style_items(song.style)
    first = items[0] if items else ""
    if TECHNICAL_ITEM_RE.match(first):
        rep.add("Genre First", "FAIL", f"first element is a technical parameter: '{first[:60]}'")
    elif GENRE_RE.search(first):
        rep.add("Genre First", "PASS", first[:60])
    else:
        rep.add("Genre First", "WARN", f"'{first[:60]}' may not be a genre")


def check_descriptor_count(song, rep):
    if not song.style:
        return
    items = [i for i in _style_items(song.style) if not TECHNICAL_ITEM_RE.match(i)]
    n = len(items)
    if n < 3:
        rep.add("Style Descriptor Count", "WARN", f"{n} descriptors: too few to steer the render")
    elif n > DESCRIPTOR_WARN:
        rep.add("Style Descriptor Count", "INFO",
                f"{n} descriptors (excluding BPM/key/range); v5.5-era Tier 3 heuristic: 5-8, conflicts past ~10. Re-validate on V6")
    else:
        rep.add("Style Descriptor Count", "PASS", f"{n} descriptors (excluding BPM/key/range)")


def check_layer_declarations(song, rep):
    if not song.lyrics:
        return
    layers = sorted({m.lower() for m in re.findall(r"\(\s*([A-Za-z]+)\s+layer\s*:", song.lyrics, re.I)})
    if not layers:
        rep.add("Layer Declarations", "PASS", "no named () layers")
        return
    declared_text = " ".join([song.style or ""] + songfile.directive_blocks(song.lyrics)).lower()
    undeclared = []
    for layer in layers:
        terms = LAYER_ALIASES.get(layer, [layer])
        if layer not in terms:
            terms = terms + [layer]
        if not any(t in declared_text for t in terms):
            undeclared.append(layer)
    if undeclared:
        rep.add("Layer Declarations", "FAIL",
                f"named layer(s) not declared in Style or a direction/rule block: {', '.join(undeclared)}")
    else:
        rep.add("Layer Declarations", "PASS", f"declared: {', '.join(layers)}")


def check_tag_placement(song, rep):
    if not song.lyrics:
        return
    violations = []
    for no, kind, text in songfile.iter_lyric_lines(song.lyrics):
        if kind != "lyric":
            continue
        s = text.strip()
        m = songfile.SECTION_TAG_RE.match(s) or songfile.V6_DIRECTIVE_RE.match(s)
        if m and s.startswith("["):
            tag_end = s.find("]") + 1
            rest = songfile.BRACKET_GROUP_RE.sub("", s[tag_end:]).strip()
            if rest:
                violations.append(f"line {no}: {s[:60]}")
    if violations:
        rep.add("Tag Placement", "FAIL", f"{len(violations)} section/directive tag(s) share a line with lyrics", violations[:10])
    else:
        rep.add("Tag Placement", "PASS", "section and directive tags on their own lines")


PAREN_INSTRUCTION_RE = re.compile(
    r"^\(\s*(instrumental|no vocals?|music only|production|sfx|sound effects?|guitar solo|drum fill|beat (drops|switch)|"
    r"fade (in|out)|tempo|key change|silence|pause)\b", re.I)


def check_parenthetical_instructions(song, rep):
    """Parentheses are SUNG. Production instructions inside () get performed as backing vocals."""
    if not song.lyrics:
        return
    hits = []
    for no, kind, text in songfile.iter_lyric_lines(song.lyrics):
        if kind in ("paren", "lyric") and PAREN_INSTRUCTION_RE.match(text.strip()):
            hits.append(f"line {no}: {text.strip()[:60]}")
    if hits:
        rep.add("Parenthetical Instructions", "WARN",
                f"{len(hits)} production instruction(s) inside () will be sung; use a [bracket] tag instead", hits[:5])


def check_v6_grammar(song, rep):
    lyr = song.lyrics or ""
    if not lyr:
        return
    if re.search(r"\[\s*Tag\s+Vocabulary", lyr, re.I):
        rep.add("V6: Tag Vocabulary Block", "FAIL", "remove the [Tag Vocabulary] block (planning scaffolding; not for final output)")
    v6_tags = re.findall(r"\[\s*(Instrument|Dynamic|Vocal|Transition|Feel|Key Change)\s*:", lyr, re.I)
    global_tags = re.findall(r"\[\s*(track|control|sequence)\s*:", lyr, re.I)
    pipe_tags = [t for t in re.findall(r"\[[^\[\]\n]*\|[^\[\]\n]*\]", lyr)]
    paradigm = "v6" if v6_tags else ("v5.5" if (global_tags or pipe_tags) else "neutral")
    if v6_tags and (global_tags or pipe_tags):
        what = []
        if global_tags:
            what.append("global [track:]/[control:]/[sequence:] tags")
        if pipe_tags:
            what.append(f"{len(pipe_tags)} pipe-notation tag(s)")
        rep.add("V6: Paradigm", "WARN", "mixes V6 tags with v5.5-era " + " and ".join(what) + "; use one paradigm")
    elif paradigm == "v5.5":
        rep.add("V6: Paradigm", "INFO", "v5.5-era format (global tags / pipe notation). Fine for v5.5 renders; migrate for V6 (see V6_TAG_REFERENCE.md)")
    else:
        rep.add("V6: Paradigm", "PASS", "V6 tag grammar" if v6_tags else "no paradigm-specific tags")

    # [Instrument: X In/Out] choreography
    state = {}
    problems = []
    redundant = []
    for m in re.finditer(r"\[\s*Instrument\s*:\s*([^\]]+?)\s*\]", lyr, re.I):
        body = m.group(1).strip()
        dm = re.match(r"^(.*?)\s+(In|Out)$", body, re.I)
        if not dm:
            problems.append(f"'[Instrument: {body}]' has no In/Out direction")
            continue
        inst, direction = dm.group(1).strip().lower(), dm.group(2).lower()
        if direction == "in" and state.get(inst) == "in":
            note = f"'{dm.group(1).strip()}' re-entered without an Out (redundant, or add an Out earlier)"
            if note not in redundant:
                redundant.append(note)
        state[inst] = direction
    if problems:
        rep.add("V6: Instrument In/Out", "WARN", "; ".join(problems[:5]))
    elif redundant:
        rep.add("V6: Instrument In/Out", "INFO", "; ".join(redundant[:5]))
    elif state:
        rep.add("V6: Instrument In/Out", "PASS", f"{len(state)} instrument(s) choreographed")

    # tag density per section (V6 guideline 2-4 tags per section)
    if paradigm == "v6":
        dense = []
        current, count = None, 0
        for _no, kind, text in songfile.iter_lyric_lines(lyr):
            if kind == "tag":
                for g in songfile.BRACKET_GROUP_RE.findall(text):
                    if songfile.SECTION_TAG_RE.match(g):
                        if current and count > 4:
                            dense.append(f"{current} ({count})")
                        current, count = g.strip("[]")[:30], 0
                    elif not re.match(r"\[\s*(Title|End)\b", g, re.I):
                        count += 1
        if current and count > 4:
            dense.append(f"{current} ({count})")
        if dense:
            rep.add("V6: Tags per Section", "INFO", "over the 2-4 guideline: " + ", ".join(dense[:6]))

    obsolete = [label for pat, label in OBSOLETE_TAGS if re.search(pat, lyr, re.I)]
    if obsolete:
        rep.add("Obsolete Tags", "WARN", "remove: " + "; ".join(obsolete))


def _scan_segments(song):
    segs = []
    if song.style:
        segs.append(song.style)
    if song.lyrics:
        segs.extend(songfile.directive_blocks(song.lyrics))
    return "\n".join(segs)


ARTIST_CONTEXT_STOP = NON_ARTIST_WORDS | {
    "production", "vocal", "vocals", "voice", "ai", "song", "track", "mix", "chorus", "verse", "bridge",
    "intro", "outro", "final", "lead", "male", "female", "choir", "bass", "drums", "piano", "guitar",
    "strings", "synth", "this", "each", "every", "his", "her", "their", "our", "my", "your", "no", "not",
    "keep", "make", "let", "start", "end", "build", "strip", "classic", "big", "small", "huge", "deep",
}


def _looks_like_name(name):
    words = name.split()
    if not words or any(not w[0].isupper() for w in words):
        return False
    return words[0].lower() not in ARTIST_CONTEXT_STOP and words[-1].lower() not in ARTIST_CONTEXT_STOP


def check_artist_references(song, rep):
    text = _scan_segments(song)
    if not text:
        return
    plain = songfile.strip_accents(text)
    found = []
    name = r"([A-Z][\w'.&-]*(?:[ \t]+[A-Z][\w'.&-]*){0,3})"
    patterns = (
        r"(?i:in the style of)\s+" + name,
        r"(?i:inspired by)\s+" + name,
        name + r"[ \t]+(?:vibes|feel|sound|style)\b",
        r"\b(?i:like)[ \t]+" + name,
        name + r"[ \t]+meets[ \t]+" + name,
        r"\bmeets[ \t]+" + name,
    )
    for pat in patterns:
        for m in re.finditer(pat, plain):
            for cand in m.groups():
                if cand and _looks_like_name(cand.strip()):
                    found.append(cand.strip())
    for artist in ARTIST_NAMES:
        flags = re.I if " " in artist else 0
        if re.search(r"(?<![\w])" + re.escape(artist) + r"(?![\w])", plain, flags):
            found.append(artist)
    unique = []
    for f in sorted(set(found), key=lambda x: (-len(x), x.lower())):
        if not any(f.lower() in u.lower() for u in unique):
            unique.append(f)
    if unique:
        rep.add("Artist References", "WARN", "convert to descriptive production language: " + ", ".join(sorted(unique, key=str.lower)[:6]))
    else:
        rep.add("Artist References", "PASS", "none detected")


def check_gear_names(song, rep):
    text = re.sub(r"\([^)]*\)", "", _scan_segments(song))  # parenthetical gear notes are allowed (Step 9b)
    if not text:
        return
    found = []
    for pat in GEAR_PATTERNS:
        for m in re.finditer(pat, text, re.I):
            if m.group(0).lower() not in [f.lower() for f in found]:
                found.append(m.group(0))
    if found:
        rep.add("Gear Names", "WARN",
                "describe the sound instead of the model: " + ", ".join(found[:6]) + " (see references/INSTRUMENT_SOUND_REFERENCE.md)")
    else:
        rep.add("Gear Names", "PASS", "no model/gear names (generic Rhodes/Hammond/Wurlitzer are fine)")


# --------------------------------------------------------------------------- driver

def validate_file(path, explicit=True):
    rep = Report(path)
    song = songfile.SongFile(path)
    if song.error:
        rep.error = song.error
        return rep
    if song.skip_reason:
        rep.skipped = song.skip_reason
        return rep
    if not song.has_song_sections:
        if explicit:
            rep.error = ("format not recognised: no Style Prompt or Lyrics section "
                         "(expected headings like '## STYLE PROMPT:' and '## LYRICS:')")
        else:
            rep.skipped = "not a Suno-ready song file (no Style/Lyrics sections)"
        return rep
    check_char_counts(song, rep)
    check_required_elements(song, rep)
    check_exclusions(song, rep)
    check_genre_first(song, rep)
    check_descriptor_count(song, rep)
    check_layer_declarations(song, rep)
    check_tag_placement(song, rep)
    check_parenthetical_instructions(song, rep)
    check_v6_grammar(song, rep)
    check_artist_references(song, rep)
    check_gear_names(song, rep)
    if song.legacy:
        rep.add("Legacy Marker", "INFO", "archived pre-standard example (<!-- song-format: legacy -->)")
    return rep


def format_text(reports, compact=False):
    out = []
    for rep in reports:
        if rep.result == "SKIP":
            if not compact:
                out.append(f"=== {rep.path}: SKIP ({rep.skipped})")
            continue
        out.append(f"=== FILE: {rep.path} ===")
        if rep.error:
            out.append(f"  [ERROR] {rep.error}")
            out.append("")
            continue
        for c in rep.checks:
            if compact and c["status"] in ("PASS",):
                continue
            out.append(f"  [{c['status']}] {c['name']}: {c['detail']}")
            for item in c.get("items", [])[:10]:
                out.append(f"         - {item}")
        out.append(f"  RESULT: {rep.result} ({rep.failures} failures, {rep.warnings} warnings)")
        out.append("")
    if len([r for r in reports if r.result != "SKIP"]) > 1:
        tally = {}
        for r in reports:
            tally[r.result] = tally.get(r.result, 0) + 1
        out.append("SUMMARY: " + ", ".join(f"{k} {v}" for k, v in sorted(tally.items())))
    return "\n".join(out)


def hook_paths(args_paths):
    """Resolve paths for Kiro hook mode: CLI args, else any *.md path in the stdin JSON payload."""
    paths = [p for p in args_paths if p and "{{" not in p]
    if paths:
        return paths
    try:
        raw = sys.stdin.read() if not sys.stdin.isatty() else ""
    except OSError:
        raw = ""
    found = []

    def walk(obj):
        if isinstance(obj, dict):
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for v in obj:
                walk(v)
        elif isinstance(obj, str) and obj.endswith(".md"):
            found.append(obj)

    try:
        walk(json.loads(raw)) if raw.strip() else None
    except ValueError:
        found.extend(re.findall(r"[\w./\\-]+\.md", raw))
    return found


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate Suno song files (V6 default, v5.5-era aware).")
    parser.add_argument("paths", nargs="*", help="song files or directories (recursive)")
    parser.add_argument("--json", action="store_true", dest="json_output", help="JSON output")
    parser.add_argument("--strict", action="store_true", help="treat WARN as failure for the exit code")
    parser.add_argument("--hook", action="store_true", help="Kiro hook mode: skip non-song files, compact output, exit 0")
    args = parser.parse_args(argv)

    paths = hook_paths(args.paths) if args.hook else args.paths
    if not paths:
        if args.hook:
            return 0
        parser.error("no paths given")

    reports = []
    for path, explicit in songfile.iter_song_paths(paths):
        if args.hook and songfile.is_skippable_song_path(path):
            continue
        reports.append(validate_file(path, explicit=explicit and not args.hook))

    if args.json_output:
        print(json.dumps([r.as_dict() for r in reports], indent=2, ensure_ascii=False))
    else:
        text = format_text(reports, compact=args.hook)
        if text:
            print(text)

    if args.hook:
        return 0
    bad = {"FAIL", "ERROR"} | ({"WARN"} if args.strict else set())
    return 1 if any(r.result in bad for r in reports) else 0


if __name__ == "__main__":
    sys.exit(main())
