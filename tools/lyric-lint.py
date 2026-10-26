#!/usr/bin/env python3
"""
lyric-lint.py - deterministic lyric craft readout for song files.

Per section it reports:
  - syllables per line (7-12 target; 13-15 = review; 16+ = Compression Test) and stress pattern
  - end-rhyme TYPE between lines on Pattison's ladder:
        perfect > family > additive/subtractive > assonance > consonance
  - the section's rhyme scheme (letters, X = unrhymed line), e.g. XAXA, AABB, ABAB
  - section stability: line count (even/odd), line-length match, rhyme closure
  - line endings on unstressed function words, end-of-line punctuation, cliches and cliche rhyme pairs
  - Verse 1 vs Verse 2 syllable mismatches (Suno often reuses the verse melody)

It is a READOUT, not a judge: Tenet 1 (emotion over mechanics) still applies.
Definitions: references/RHYME_AND_LYRIC_CRAFT.md.

Accuracy: install the CMU Pronouncing Dictionary wrapper for dictionary syllables, stresses and
rhymes:   pip install pronouncing
Without it a spelling heuristic runs (syllables approximate, rhyme types approximate).

Usage:
    python3 tools/lyric-lint.py songs/my_song.md
    python3 tools/lyric-lint.py --json songs/my_song.md
    python3 tools/lyric-lint.py --hook {{filePath}}     # Kiro hook mode (compact, always exit 0)
Exit code: 0 (advisory tool) unless a file cannot be read (1), or --strict and any WARN (1).
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import songfile  # noqa: E402

try:  # optional dependency
    import pronouncing  # type: ignore
    _CMU = True
except Exception:  # pragma: no cover - depends on environment
    pronouncing = None
    _CMU = False

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

FUNCTION_WORDS = {
    "a", "an", "the", "of", "to", "in", "on", "at", "by", "for", "from", "with", "as", "and", "but", "or",
    "nor", "if", "it", "its", "is", "was", "are", "were", "be", "been", "am", "my", "your", "his", "her",
    "our", "their", "that", "than", "into", "onto", "upon", "so",
}
ALWAYS_UNSTRESSED = {"a", "an", "the", "of", "to", "and", "or", "nor"}

VOWELS = {"AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"}
FAMILY = {}
for _ph in ("B", "D", "G", "P", "T", "K"):
    FAMILY[_ph] = "plosive"
for _ph in ("V", "DH", "Z", "ZH", "JH", "F", "TH", "S", "SH", "CH"):
    FAMILY[_ph] = "fricative"
for _ph in ("M", "N", "NG"):
    FAMILY[_ph] = "nasal"

RHYME_RANK = {"identity": 6, "perfect": 5, "family": 4, "additive": 3, "subtractive": 3, "assonance": 2,
              "consonance": 1, None: 0}
SCHEME_MIN_RANK = 2  # assonance or stronger counts as a rhyme for the scheme letters

DIALECT = {"'cause": "because", "cause": "because", "'til": "till", "til": "till", "'em": "them", "ya": "you",
           "y'all": "you all", "gonna": "gonna", "wanna": "wanna", "lil": "little", "o'": "of", "ol'": "old",
           "nothin'": "nothing", "somethin'": "something", "cain't": "can't", "yer": "your", "ye": "you"}


# --------------------------------------------------------------------------- word level

def words_of(line):
    line = line.replace("\u2019", "'").replace("\u2018", "'")
    line = re.sub(r"\[[^\]]*\]", " ", line)       # inline tags
    line = re.sub(r"\([^)]*\)", " ", line)         # inline parentheticals (backing / cues)
    line = re.sub(r"[\u2014\u2013]", " ", line)     # em/en dashes = breath, not words
    return [w for w in re.findall(r"[A-Za-z][A-Za-z']*", line)]


def _norm_word(w):
    lw = w.lower().strip("'")
    if w.lower() in DIALECT:
        return DIALECT[w.lower()]
    if lw in DIALECT:
        return DIALECT[lw]
    if lw.endswith("in") and w.endswith("'"):
        return lw + "g"  # runnin' -> running
    return lw


def heuristic_syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if word.lower().endswith("le") and len(word) > 2 and word.lower()[-3] not in "aeiouy":
        n += 1
    return max(1, n)


def phones(word):
    """Return a CMU phone string (first pronunciation) or None."""
    if not _CMU:
        return None
    cands = pronouncing.phones_for_word(_norm_word(word))
    if not cands and "'" in word:
        cands = pronouncing.phones_for_word(_norm_word(word).replace("'", ""))
    return cands[0] if cands else None


def word_syllables(word):
    norm = _norm_word(word)
    if " " in norm:
        return sum(word_syllables(p) for p in norm.split())
    ph = phones(word)
    if ph:
        return sum(1 for p in ph.split() if p[-1].isdigit())
    return heuristic_syllables(norm)


def word_stress(word):
    """Stress string per syllable: '1' stressed, '0' unstressed (function words forced to 0)."""
    n = word_syllables(word)
    if _norm_word(word) in ALWAYS_UNSTRESSED:
        return "0" * n
    ph = phones(word)
    if ph:
        s = "".join("1" if p[-1] in "12" else "0" for p in ph.split() if p[-1].isdigit())
        if _norm_word(word) in FUNCTION_WORDS:
            return "0" * len(s)
        return s
    if n == 1:
        return "0" if _norm_word(word) in FUNCTION_WORDS else "1"
    return "1" + "0" * (n - 1)


def rhyme_tail(word):
    """(onset_consonant, [phones from the last stressed vowel]) or None."""
    ph = phones(word)
    if not ph:
        return None
    parts = ph.split()
    idx = None
    for i in range(len(parts) - 1, -1, -1):
        if parts[i][-1] in "12":
            idx = i
            break
    if idx is None:
        for i in range(len(parts) - 1, -1, -1):
            if parts[i][-1].isdigit():
                idx = i
                break
    if idx is None:
        return None
    onset = parts[idx - 1] if idx > 0 and not parts[idx - 1][-1].isdigit() else ""
    tail = [re.sub(r"\d", "", p) for p in parts[idx:]]
    return onset, tail


def _ortho_tail(word):
    w = re.sub(r"[^a-z]", "", _norm_word(word))
    m = re.search(r"[aeiouy]+[^aeiouy]*e?$", w)
    return m.group(0) if m else w


def classify_rhyme(w1, w2):
    """Return one of identity/perfect/family/additive/subtractive/assonance/consonance or None."""
    if not w1 or not w2:
        return None
    n1, n2 = _norm_word(w1), _norm_word(w2)
    if n1 == n2:
        return "identity"
    t1, t2 = rhyme_tail(w1), rhyme_tail(w2)
    if t1 is None or t2 is None:
        a, b = _ortho_tail(w1), _ortho_tail(w2)  # approximate fallback
        if a and a == b:
            return "perfect"
        va = re.match(r"[aeiouy]+", a)
        vb = re.match(r"[aeiouy]+", b)
        if va and vb and va.group(0) == vb.group(0):
            return "assonance"
        ca, cb = re.sub(r"^[aeiouy]+", "", a), re.sub(r"^[aeiouy]+", "", b)
        if ca and ca == cb:
            return "consonance"
        return None
    (on1, tl1), (on2, tl2) = t1, t2
    v1, v2 = tl1[0], tl2[0]
    rest1, rest2 = tl1[1:], tl2[1:]
    if v1 == v2:
        if rest1 == rest2:
            return "identity" if on1 == on2 and on1 else "perfect"
        if len(rest1) == len(rest2):
            same = True
            for a, b in zip(rest1, rest2):
                if a == b:
                    continue
                if a in VOWELS or b in VOWELS or FAMILY.get(a) is None or FAMILY.get(a) != FAMILY.get(b):
                    same = False
                    break
            if same:
                return "family"
        if len(rest1) != len(rest2):
            short, long_ = (rest1, rest2) if len(rest1) < len(rest2) else (rest2, rest1)
            if long_[:len(short)] == short and not any(p in VOWELS for p in long_[len(short):]):
                return "additive" if len(rest1) < len(rest2) else "subtractive"
        return "assonance"
    cons1 = [p for p in rest1 if p not in VOWELS]
    cons2 = [p for p in rest2 if p not in VOWELS]
    if cons1 and cons1 == cons2:
        return "consonance"
    return None


# --------------------------------------------------------------------------- data

def load_cliches():
    phrases, pairs = [], []
    path = os.path.join(DATA_DIR, "cliches.txt")
    try:
        with open(path, encoding="utf-8") as fh:
            for raw in fh:
                line = raw.split("#", 1)[0].strip().lower()
                if not line:
                    continue
                if line.startswith("pair:"):
                    a, _, b = line[5:].partition("/")
                    if a.strip() and b.strip():
                        pairs.append((a.strip(), b.strip()))
                else:
                    phrases.append(line)
    except OSError:
        pass
    return phrases, pairs


# --------------------------------------------------------------------------- song level

class Line:
    def __init__(self, no, text, spoken=False):
        self.no = no
        self.text = text.strip()
        self.spoken = spoken
        self.words = words_of(text)
        self.syllables = sum(word_syllables(w) for w in self.words)
        self.stress = " ".join(word_stress(w) for w in self.words)
        self.end_word = self.words[-1] if self.words else ""
        self.flags = []   # REVIEW / COMPRESS / cliche
        self.minor = []   # line-ending notes (shown in full mode only)


def split_sections(lyrics):
    sections = []
    current = {"name": "(before first section tag)", "lines": []}
    spoken_mode = False
    for no, kind, text in songfile.iter_lyric_lines(lyrics):
        if kind == "tag":
            groups = songfile.BRACKET_GROUP_RE.findall(text.strip())
            if groups and songfile.SECTION_TAG_RE.match(groups[0]):
                if current["lines"] or current["name"] != "(before first section tag)":
                    sections.append(current)
                label = groups[0].strip("[] ").split("|")[0].strip()
                current = {"name": label, "lines": []}
                spoken_mode = bool(re.search(r"(?<!un)spoken|talk-?sing|narrat", groups[0], re.I))
            for g in groups:
                if re.match(r"\[\s*(vocal\b|male|female|lead|spoken|whisper|sung)", g, re.I):
                    spoken_mode = bool(re.search(r"(?<!un)spoken|talk-?sing|narrat", g, re.I))
            continue
        if kind != "lyric":
            continue
        s = text.strip()
        spoken = bool(re.match(r"^\(\s*(spoken|whisper(ed)?|talk(ing|-sung)?|said|narrat)", s, re.I)) or \
            bool(re.match(r"^\[\s*(spoken|vocal\s*:\s*spoken)", s, re.I))
        s_clean = re.sub(r"^(\[[^\]]*\]\s*)+", "", s)
        s_clean = re.sub(r"^\([^)]*\)\s*", "", s_clean) if spoken else s_clean
        line = Line(no, s_clean, spoken=spoken or spoken_mode)
        if line.words:
            current["lines"].append(line)
    if current["lines"]:
        sections.append(current)
    return [s for s in sections if s["lines"]]


def scheme_for(lines):
    letters = []
    reps = []  # (letter, end_word)
    next_letter = 0
    pair_types = []
    for i, ln in enumerate(lines):
        best, best_rank, best_type = None, 0, None
        for j in range(i - 1, -1, -1):
            t = classify_rhyme(lines[j].end_word, ln.end_word)
            r = RHYME_RANK.get(t, 0)
            if r > best_rank:
                best, best_rank, best_type = j, r, t
        if best is not None and best_rank >= SCHEME_MIN_RANK:
            letters.append(letters[best])
            pair_types.append((lines[best].no, ln.no, lines[best].end_word, ln.end_word, best_type))
        else:
            letters.append(chr(ord("A") + next_letter % 26))
            next_letter += 1
    counts = {l: letters.count(l) for l in letters}
    raw = [l if counts[l] > 1 else "X" for l in letters]
    # re-letter in order of first appearance, keeping X
    remap, nxt, out = {}, 0, []
    for l in raw:
        if l == "X":
            out.append("X")
            continue
        if l not in remap:
            remap[l] = chr(ord("A") + nxt % 26)
            nxt += 1
        out.append(remap[l])
    return "".join(out), pair_types


def stability(lines, scheme):
    n = len(lines)
    lengths = [l.syllables for l in lines]
    matched = (max(lengths) - min(lengths)) <= 2 if lengths else True
    closed = bool(scheme) and scheme[-1] != "X"
    marks = {"line count": "even" if n % 2 == 0 else "odd",
             "line lengths": "matched" if matched else "unmatched",
             "rhyme closure": "closed" if closed else "open"}
    unstable = sum(1 for v in marks.values() if v in ("odd", "unmatched", "open"))
    overall = "stable" if unstable == 0 else "unstable" if unstable >= 2 else "mixed"
    return overall, marks


def base_name(name):
    return re.sub(r"\s*[-\u2013\u2014:].*$", "", name).strip().lower()


def lint_song(path):
    song = songfile.SongFile(path)
    result = {"file": path, "error": None, "dictionary": "CMUdict (pronouncing)" if _CMU else "heuristic fallback",
              "sections": [], "findings": [], "summary": {}}
    if song.error:
        result["error"] = song.error
        return result
    if not song.lyrics:
        result["error"] = "no Lyrics section found"
        return result

    phrases, pairs = load_cliches()
    sections = split_sections(song.lyrics)
    findings = result["findings"]
    review = compress = 0
    for sec in sections:
        lines = sec["lines"]
        scheme, pair_types = scheme_for(lines)
        overall, marks = stability(lines, scheme)
        for ln in lines:
            if not ln.spoken:
                if ln.syllables >= 16:
                    ln.flags.append("COMPRESS: 16+ syllables, run the Compression Test")
                    compress += 1
                elif ln.syllables >= 13:
                    ln.flags.append("REVIEW: 13-15 syllables, check stress density at tempo")
                    review += 1
            last = _norm_word(ln.end_word)
            if last in FUNCTION_WORDS and len(ln.words) > 1:
                ln.minor.append(f"ends on function word '{ln.end_word}' (fine if sung stressed)")
            if re.search(r"[.,;:!?]$", ln.text):
                ln.minor.append("end-of-line punctuation (Suno rule: none)")
            low = " " + " ".join(w.lower() for w in ln.words) + " "
            for ph in phrases:
                if " " + ph + " " in low:
                    ln.flags.append(f"cliche: '{ph}' (flip it or anchor it in a concrete image)")
                    findings.append({"level": "WARN", "section": sec["name"], "line": ln.no, "message": f"cliche '{ph}'"})
        for a_no, b_no, aw, bw, typ in pair_types:
            pa, pb = _norm_word(aw), _norm_word(bw)
            for x, y in pairs:
                if {pa, pb} == {x, y}:
                    findings.append({"level": "INFO", "section": sec["name"], "line": b_no,
                                     "message": f"cliche rhyme pair {aw}/{bw} (try a family or additive rhyme)"})
        sec_out = {
            "name": sec["name"], "lines": len(lines), "scheme": scheme, "stability": overall, "marks": marks,
            "rhymes": [{"lines": [a, b], "words": [aw, bw], "type": t} for a, b, aw, bw, t in pair_types],
            "detail": [{"line": l.no, "syllables": l.syllables, "stress": l.stress, "text": l.text,
                        "spoken": l.spoken, "flags": l.flags, "notes": l.minor} for l in lines],
        }
        bn = base_name(sec["name"])
        if bn in ("chorus", "final chorus", "hook", "refrain") and overall == "unstable":
            findings.append({"level": "INFO", "section": sec["name"], "line": None,
                             "message": "chorus reads open/unstable - intended? (choruses usually resolve)"})
        if bn in ("pre-chorus", "prechorus", "pre chorus", "bridge") and overall == "stable":
            findings.append({"level": "INFO", "section": sec["name"], "line": None,
                             "message": "section reads closed/stable - pre-choruses and bridges usually push forward"})
        result["sections"].append(sec_out)

    # Verse-to-verse syllable matching (Suno tends to reuse the verse melody)
    verses = [s for s in sections if base_name(s["name"]).startswith("verse")]
    if len(verses) >= 2:
        ref = verses[0]
        for other in verses[1:]:
            for i, (a, b) in enumerate(zip(ref["lines"], other["lines"]), 1):
                if abs(a.syllables - b.syllables) > 2:
                    findings.append({"level": "INFO", "section": other["name"], "line": None,
                                     "message": f"line {i}: {b.syllables} syllables vs {a.syllables} in {ref['name']} line {i} (Suno may reuse the verse melody)"})
            if len(ref["lines"]) != len(other["lines"]):
                findings.append({"level": "INFO", "section": other["name"], "line": None,
                                 "message": f"{len(other['lines'])} lines vs {len(ref['lines'])} in {ref['name']}"})
    result["summary"] = {
        "sections": len(sections),
        "lines": sum(len(s["lines"]) for s in sections),
        "review_lines": review,
        "compress_lines": compress,
        "cliches": sum(1 for f in findings if f["message"].startswith("cliche '")),
    }
    return result


def format_text(results, compact=False):
    out = []
    for r in results:
        out.append(f"=== LYRIC LINT: {r['file']} ({r['dictionary']}) ===")
        if r.get("error"):
            out.append(f"  [ERROR] {r['error']}")
            continue
        if r.get("skipped"):
            out.append(f"  SKIP ({r['skipped']})")
            continue
        for sec in r["sections"]:
            m = sec["marks"]
            out.append(f"  [{sec['name']}] {sec['lines']} lines ({m['line count']}) | scheme {sec['scheme']} "
                       f"(rhyme {m['rhyme closure']}) | lengths {m['line lengths']} | => {sec['stability']}")
            if not compact and sec["rhymes"]:
                kinds = ", ".join(f"{w[0]}/{w[1]}={t}" for w, t in ((x["words"], x["type"]) for x in sec["rhymes"]))
                out.append(f"      rhymes: {kinds}")
            for d in sec["detail"]:
                if compact and not d["flags"]:
                    continue
                notes = d["flags"] + ([] if compact else d["notes"])
                flag = ("  <- " + "; ".join(notes)) if notes else ""
                spoken = " (spoken)" if d["spoken"] else ""
                out.append(f"      {d['syllables']:>2} syl{spoken} | {d['text'][:70]}{flag}")
        if r["findings"]:
            out.append("  Findings:")
            for f in r["findings"]:
                where = f" line {f['line']}" if f.get("line") else ""
                out.append(f"    [{f['level']}] {f['section']}{where}: {f['message']}")
        s = r["summary"]
        out.append(f"  SUMMARY: {s['sections']} sections, {s['lines']} lines, {s['review_lines']} to review (13-15), "
                   f"{s['compress_lines']} to compress (16+), {s['cliches']} cliche(s)")
        if r["dictionary"] != "CMUdict (pronouncing)":
            out.append("  NOTE: heuristic syllables/rhymes. For dictionary accuracy: pip install pronouncing")
        out.append("")
    return "\n".join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Deterministic lyric craft lint (syllables, rhyme, stability).")
    parser.add_argument("paths", nargs="*", help="song files or directories")
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument("--strict", action="store_true", help="exit 1 if any WARN finding (e.g. cliche)")
    parser.add_argument("--hook", action="store_true", help="Kiro hook mode: compact output, exit 0")
    args = parser.parse_args(argv)

    paths = args.paths
    if args.hook:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "validate_song", os.path.join(os.path.dirname(os.path.abspath(__file__)), "validate-song.py"))
        vs = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(vs)
        paths = vs.hook_paths(args.paths)
        if not paths:
            return 0
    elif not paths:
        parser.error("no paths given")

    results = []
    for path, _explicit in songfile.iter_song_paths(paths):
        if songfile.is_skippable_song_path(path):
            continue
        res = lint_song(path)
        if res.get("error") and not _explicit and res["error"] == "no Lyrics section found":
            continue
        results.append(res)

    if args.json_output:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_text(results, compact=args.hook))
    if args.hook:
        return 0
    if any(r.get("error") and r["error"] != "no Lyrics section found" for r in results):
        return 1
    if args.strict and any(f["level"] == "WARN" for r in results for f in r["findings"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
