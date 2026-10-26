"""songfile.py - shared parser for Suno song files.

Used by tools/validate-song.py and tools/lyric-lint.py. Standard library only.

A song file is Markdown with (at minimum) a Style Prompt section and a Lyrics section,
optionally an Exclusions section. Headings may carry suffixes, e.g.
"## STYLE PROMPT:", "### Style Prompt (Paste to "Style of Music" field)", "## Lyrics",
"### Lyrics Field (Suno-Ready)", "## EXCLUSIONS:", "### Exclude Field". A bare label line
("STYLE PROMPT:", "LYRICS:") also starts a section.

What gets counted is what you would actually paste into Suno:
- Style: the Style section minus [Exclusions: ...]/[Exclude: ...] lines, character-count
  notes ("Style: 807/1000 chars"), code fences, separators and blank edges.
- Lyrics: the Lyrics section up to and including the end terminator ([End] or [end]);
  anything after the terminator (count notes, separators) is not pasted.
- Exclusions: an EXCLUSIONS / Exclude Field section, plus any legacy [Exclusions: ...] line.
"""

import os
import re
import unicodedata

LEGACY_MARKER_RE = re.compile(r"<!--\s*song-format:\s*legacy\b[^>]*-->", re.IGNORECASE)
SKIP_MARKER_RE = re.compile(r"<!--\s*validate:\s*skip\b\s*(.*?)\s*-->", re.IGNORECASE)

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
# Bare label lines such as "STYLE PROMPT:" or "**LYRICS:**" (whole line, upper-case label).
BARE_LABEL_RE = re.compile(r"^\**\s*([A-Z][A-Z0-9 &/'\-\u2014()]{2,60}?)\s*:\s*\**\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
SEPARATOR_RE = re.compile(r"^\s*([-=_*\u2500-\u257F]\s*){3,}$")
COUNT_NOTE_RE = re.compile(
    r"^\s*[*_>(]*\s*(style(\s*prompt)?|lyrics(\s*field)?|exclu\w*|char(acter)?s?(\s*count)?)"
    r"\s*[*_]*\s*[:=]?\s*[*_]*\s*~?\s*\d[\d,]*\s*/\s*\d[\d,]*\s*(chars?|characters)?\b.*$",
    re.IGNORECASE,
)

STYLE_LABELS = {"STYLE", "STYLE OF MUSIC", "STYLE FIELD", "STYLE BOX", "STYLE OF MUSIC FIELD"}
LYRICS_LABELS = {"LYRICS", "LYRICS FIELD", "LYRICS BOX", "LYRIC FIELD", "FULL LYRICS", "FINAL LYRICS"}
EXCLUSION_LABELS = {"EXCLUSIONS", "EXCLUSION", "EXCLUDE", "EXCLUDE FIELD", "EXCLUSIONS FIELD",
                    "EXCLUDE BOX", "NEGATIVE PROMPTS", "EXCLUDE STYLES"}
EXCLUSIONS_LINE_RE = re.compile(r"^\s*\[\s*(Exclusions?|Exclude)\s*:(.*?)\]\s*$", re.IGNORECASE | re.DOTALL)
END_TAG_RE = re.compile(r"^\s*\[\s*end\s*\]\s*$", re.IGNORECASE)


def _norm_label(text):
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"\(.*?\)", "", text)
    text = text.replace("\u2014", " ").replace("\u2013", " ")
    return re.sub(r"\s+", " ", text).strip().rstrip(":").strip().upper()


def classify_label(text):
    """Return 'style' | 'exclusions' | 'lyrics' | None for a heading/label text."""
    label = _norm_label(text)
    if (label.startswith("STYLE PROMPT") and "ALTERNATIVE" not in label) or label in STYLE_LABELS:
        return "style"
    if label in EXCLUSION_LABELS:
        return "exclusions"
    if label in LYRICS_LABELS:
        return "lyrics"
    return None


def read_text(path):
    """Read a file as UTF-8 (BOM tolerated). Returns (text, error)."""
    try:
        with open(path, "r", encoding="utf-8-sig", newline=None) as handle:
            return handle.read(), None
    except UnicodeDecodeError as exc:
        return None, f"not valid UTF-8 ({exc.reason} at byte {exc.start})"
    except OSError as exc:
        return None, str(exc)


def _sections(lines):
    """Split lines into (kind, level, start, end) blocks for recognised sections.

    A section runs until the next heading of the same or higher level, or the next
    bare label line. Unrecognised headings deeper than the section heading are kept
    inside it (rare for lyrics, harmless).
    """
    markers = []  # (index, kind_or_None, level)
    for idx, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if m:
            markers.append((idx, classify_label(m.group(2)), len(m.group(1))))
            continue
        b = BARE_LABEL_RE.match(line)
        if b and not line.lstrip().startswith("["):
            kind = classify_label(b.group(1))
            # Bare labels act as level-7 boundaries (weaker than any heading).
            markers.append((idx, kind, 7))
    blocks = []
    in_fence = False
    fence_lines = set()
    for idx, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            fence_lines.add(idx)
    markers = [m for m in markers if m[0] not in fence_lines]
    for pos, (idx, kind, level) in enumerate(markers):
        if kind is None:
            continue
        end = len(lines)
        for nidx, _nkind, nlevel in markers[pos + 1:]:
            if nlevel <= level or nlevel == 7 or level == 7:
                end = nidx
                break
        blocks.append((kind, level, idx + 1, end))
    return blocks


def _clean_block(lines, stop_at_end=False):
    """Drop fences, separators, count notes and blank edges. Optionally stop after [End]."""
    out = []
    ended = False
    for line in lines:
        if FENCE_RE.match(line) or SEPARATOR_RE.match(line) or COUNT_NOTE_RE.match(line):
            continue
        if re.match(r"^\s*\u2550{3,}", line):  # ═══ decoration
            continue
        out.append(line.rstrip())
        if stop_at_end and END_TAG_RE.match(line):
            ended = True
            break
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return out, ended


def split_exclusion_items(raw):
    if not raw:
        return []
    raw = raw.replace("\n", ",")
    items = [i.strip() for i in raw.split(",")]
    return [i for i in items if i]


class SongFile:
    """Parsed song file. Attributes are None when a section is absent."""

    def __init__(self, path):
        self.path = path
        self.error = None
        self.text = None
        self.legacy = False
        self.skip_reason = None
        self.style = None            # pasteable Style text
        self.lyrics = None           # pasteable Lyrics text
        self.lyrics_has_end = False
        self.exclusions_raw = None   # joined raw exclusion text (all sources)
        self.exclusions = []         # list of items
        self.exclusion_sources = []  # e.g. ["section", "style-bracket", "lyrics-bracket"]
        self._parse()

    @property
    def has_song_sections(self):
        return self.style is not None or self.lyrics is not None

    def _parse(self):
        text, err = read_text(self.path)
        if err:
            self.error = err
            return
        self.text = text
        self.legacy = bool(LEGACY_MARKER_RE.search(text))
        skip = SKIP_MARKER_RE.search(text)
        if skip:
            self.skip_reason = "validate: skip marker" + (f" ({skip.group(1).strip(' ()')})" if skip.group(1).strip() else "")
        lines = text.split("\n")
        blocks = _sections(lines)
        exclusion_parts = []

        # Use the last occurrence of each kind (final, Suno-ready output usually comes last).
        chosen = {}
        for kind, level, start, end in blocks:
            chosen[kind] = (start, end)

        if "style" in chosen:
            start, end = chosen["style"]
            cleaned, _ = _clean_block(lines[start:end])
            kept = []
            for line in cleaned:
                m = EXCLUSIONS_LINE_RE.match(line)
                if m:
                    exclusion_parts.append(m.group(2))
                    self.exclusion_sources.append("style-bracket")
                    continue
                kept.append(line)
            while kept and not kept[-1].strip():
                kept.pop()
            self.style = "\n".join(kept).strip()

        if "lyrics" in chosen:
            start, end = chosen["lyrics"]
            cleaned, ended = _clean_block(lines[start:end], stop_at_end=True)
            kept = []
            for line in cleaned:
                m = EXCLUSIONS_LINE_RE.match(line)
                if m:
                    exclusion_parts.append(m.group(2))
                    self.exclusion_sources.append("lyrics-bracket")
                    continue
                kept.append(line)
            self.lyrics = "\n".join(kept).strip()
            self.lyrics_has_end = ended

        if "exclusions" in chosen:
            start, end = chosen["exclusions"]
            cleaned, _ = _clean_block(lines[start:end])
            body = []
            for line in cleaned:
                m = EXCLUSIONS_LINE_RE.match(line)
                body.append(m.group(2) if m else line)
            joined = " ".join(l.strip() for l in body if l.strip() and not l.strip().startswith(">"))
            if joined:
                exclusion_parts.append(joined)
                self.exclusion_sources.append("section")

        if exclusion_parts:
            self.exclusions_raw = ", ".join(p.strip() for p in exclusion_parts if p.strip())
            seen = []
            for item in split_exclusion_items(self.exclusions_raw):
                key = item.lstrip("-\u2011\u2010\u2013 ").lower()
                if key not in [s.lstrip("-\u2011\u2010\u2013 ").lower() for s in seen]:
                    seen.append(item)
            self.exclusions = seen


# ---------------------------------------------------------------------------
# Lyric structure helpers (used by lyric-lint and the validator's tag checks)
# ---------------------------------------------------------------------------

SECTION_KEYWORDS = (
    "intro", "verse", "pre-chorus", "pre chorus", "prechorus", "chorus", "post-chorus", "post chorus",
    "final chorus", "hook", "refrain", "bridge", "breakdown", "build", "drop", "interlude",
    "instrumental", "solo", "break", "outro", "tag", "coda", "movement", "the plea", "final movement",
)
SECTION_TAG_RE = re.compile(
    r"^\[\s*(" + "|".join(re.escape(k) for k in sorted(SECTION_KEYWORDS, key=len, reverse=True)) + r")\b[^\]]*\]",
    re.IGNORECASE,
)
V6_DIRECTIVE_RE = re.compile(r"^\[\s*(Instrument|Dynamic|Transition|Feel|Tempo|Key Change)\s*:", re.IGNORECASE)
BRACKET_GROUP_RE = re.compile(r"\[[^\[\]]*\]")


def iter_lyric_lines(lyrics):
    """Yield (line_no, kind, text) for the lyrics field.

    kind: 'blank' | 'tag' | 'block' (multi-line [Direction: ...] block) | 'paren' (whole line in
    parentheses: backing/layer/cue) | 'lyric'.
    line_no is 1-based within the lyrics field.
    """
    lines = lyrics.split("\n")
    i = 0
    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        if not s:
            yield i + 1, "blank", raw
            i += 1
            continue
        if s.startswith("[") and s.count("[") > s.count("]"):
            # multi-line bracket block
            start = i
            depth = s.count("[") - s.count("]")
            buf = [raw]
            while depth > 0 and i + 1 < len(lines):
                i += 1
                buf.append(lines[i])
                depth += lines[i].count("[") - lines[i].count("]")
            yield start + 1, "block", "\n".join(buf)
            i += 1
            continue
        if s.startswith("[") and not BRACKET_GROUP_RE.sub("", s).strip():
            yield i + 1, "tag", raw
            i += 1
            continue
        if s.startswith("(") and s.endswith(")") and s.count("(") == 1:
            yield i + 1, "paren", raw
            i += 1
            continue
        yield i + 1, "lyric", raw
        i += 1


def directive_blocks(lyrics):
    """Return the text of [Production/Composition/Vocal Direction ...] and [... Rule: ...] blocks."""
    out = []
    if not lyrics:
        return out
    for _no, kind, text in iter_lyric_lines(lyrics):
        if kind not in ("tag", "block"):
            continue
        for m in re.finditer(r"\[\s*((Production|Composition|Vocal)\s+Direction|[A-Za-z ]+Rule|Exceptions?)\s*:?(.*?)\]",
                             text, re.IGNORECASE | re.DOTALL):
            out.append(m.group(3).strip())
    return out


def strip_accents(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))


def iter_song_paths(paths, skip_names=("README.md",), skip_suffixes=(".brief.md",)):
    """Expand files/directories into .md paths (recursive), skipping READMEs and briefs.

    Yields (path, explicit) where explicit=True for paths given directly as files.
    """
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = sorted(d for d in dirs if not d.startswith("."))
                for name in sorted(files):
                    if not name.endswith(".md"):
                        continue
                    if name in skip_names or any(name.endswith(s) for s in skip_suffixes):
                        continue
                    yield os.path.join(root, name), False
        else:
            yield p, True


def is_skippable_song_path(path):
    name = os.path.basename(path)
    return name == "README.md" or name.endswith(".brief.md") or not name.endswith(".md")
