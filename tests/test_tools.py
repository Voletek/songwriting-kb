"""Unit tests for tools/ (standard library unittest).

Run:  python3 -m unittest discover -s tests -v
Rhyme-type tests need the optional CMU dictionary wrapper (`pip install pronouncing`) and are
skipped without it.
"""

import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
FIX = os.path.join(ROOT, "tests", "fixtures")
sys.path.insert(0, TOOLS)


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(TOOLS, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


songfile = load("songfile", "songfile.py")
validate = load("validate_song", "validate-song.py")
lint = load("lyric_lint", "lyric-lint.py")
checkrepo = load("check_repo", "check-repo.py")


def statuses(report):
    return {c["name"]: c["status"] for c in report.checks}


def run_main(fn, argv, stdin_text=None):
    out = io.StringIO()
    old_stdin = sys.stdin
    try:
        if stdin_text is not None:
            sys.stdin = io.StringIO(stdin_text)
        with contextlib.redirect_stdout(out):
            code = fn(argv)
    finally:
        sys.stdin = old_stdin
    return code, out.getvalue()


class SongFileParsing(unittest.TestCase):
    def test_counts_only_pasteable_text(self):
        song = songfile.SongFile(os.path.join(FIX, "v6_valid.md"))
        self.assertTrue(song.style.startswith("intimate Appalachian folk"))
        self.assertNotIn("Style: 208/1000", song.style)          # count notes are not pasted
        self.assertTrue(song.lyrics.endswith("[End]"))            # stops at the terminator
        self.assertNotIn("Lyrics: 1103/5000", song.lyrics)
        self.assertTrue(song.lyrics_has_end)
        self.assertEqual(song.exclusions, ["trap drums", "autotune", "EDM drops", "gang vocals"])
        self.assertEqual(song.exclusion_sources, ["section"])

    def test_legacy_bracket_exclusions_not_counted_in_style(self):
        song = songfile.SongFile(os.path.join(FIX, "broken.md"))
        self.assertNotIn("[Exclusions", song.style)
        self.assertEqual(len(song.exclusions), 3)

    def test_bom_crlf_and_heading_variants(self):
        text = ("\ufeff# T\r\n\r\n### Style Prompt (Paste to \"Style of Music\" field)\r\n```\r\n"
                "Dark folk, 70 BPM, piano\r\n```\r\n\r\n### Lyrics Field (Suno-Ready)\r\n```\r\n"
                "[Title: T]\r\n[Verse]\r\nla la la\r\n[END]\r\n```\r\n")
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8", newline="") as fh:
            fh.write(text)
            path = fh.name
        try:
            song = songfile.SongFile(path)
            self.assertEqual(song.style, "Dark folk, 70 BPM, piano")
            self.assertTrue(song.lyrics_has_end)                  # [END] in any case
            self.assertNotIn("```", song.lyrics)
        finally:
            os.unlink(path)

    def test_bare_labels(self):
        text = "STYLE PROMPT:\nIndie pop, 100 BPM\n\nLYRICS:\n[Title: X]\n[Verse]\nhello\n[end]\n\nSTRONGEST LINE:\nnot lyrics\n"
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
            fh.write(text)
            path = fh.name
        try:
            song = songfile.SongFile(path)
            self.assertEqual(song.style, "Indie pop, 100 BPM")
            self.assertNotIn("not lyrics", song.lyrics)
        finally:
            os.unlink(path)

    def test_non_utf8_reports_error(self):
        with tempfile.NamedTemporaryFile("wb", suffix=".md", delete=False) as fh:
            fh.write(b"## STYLE PROMPT:\n\xff\xfe bad\n")
            path = fh.name
        try:
            rep = validate.validate_file(path)
            self.assertEqual(rep.result, "ERROR")
            self.assertIn("UTF-8", rep.error)
        finally:
            os.unlink(path)


class Validator(unittest.TestCase):
    def test_valid_v6_song_passes(self):
        rep = validate.validate_file(os.path.join(FIX, "v6_valid.md"))
        self.assertEqual(rep.result, "PASS", json.dumps(rep.as_dict(), indent=1))
        st = statuses(rep)
        self.assertEqual(st["Required Element: [End]"], "PASS")
        self.assertEqual(st["V6: Paradigm"], "PASS")
        self.assertEqual(st["Exclusions Format"], "PASS")

    def test_broken_song_fails_every_relevant_check(self):
        rep = validate.validate_file(os.path.join(FIX, "broken.md"))
        st = statuses(rep)
        self.assertEqual(rep.result, "FAIL")
        self.assertEqual(st["Style Prompt Characters"], "FAIL")
        self.assertEqual(st["Required Element: [Vocal Direction:]"], "FAIL")
        self.assertEqual(st["Required Element: [End]"], "PASS")          # lowercase legacy [end] accepted
        self.assertEqual(st["Genre First"], "FAIL")                       # starts with "key D minor"
        self.assertEqual(st["Exclusions Format"], "WARN")                 # dash prefixes, mixed hyphens
        self.assertEqual(st["Layer Declarations"], "FAIL")                # (ghost layer:) undeclared
        self.assertEqual(st["Tag Placement"], "FAIL")                     # [Verse 1] lyric on same line
        self.assertEqual(st["V6: Tag Vocabulary Block"], "FAIL")
        self.assertEqual(st["V6: Paradigm"], "WARN")                      # V6 tags + pipe notation
        self.assertEqual(st["V6: Instrument In/Out"], "WARN")             # [Instrument: Drums] no direction
        self.assertEqual(st["Obsolete Tags"], "WARN")                     # [bpm: 92]
        self.assertEqual(st["Artist References"], "WARN")                 # Radiohead
        self.assertEqual(st["Gear Names"], "WARN")                        # Juno-60, TB-303

    def test_legacy_marker_downgrades_missing_blocks(self):
        rep = validate.validate_file(os.path.join(FIX, "legacy.md"))
        st = statuses(rep)
        self.assertEqual(st["Required Element: [Production Direction:]"], "WARN")
        self.assertEqual(st["Required Element: [End]"], "WARN")
        self.assertNotEqual(rep.result, "FAIL")

    def test_generic_instrument_names_are_not_gear(self):
        text = ("## STYLE PROMPT:\nNeo-soul, Rhodes electric piano, Hammond organ, Wurlitzer, 90 BPM\n\n"
                "## LYRICS:\n[Title: X]\n[Production Direction: warm]\n[Vocal Direction: soft]\n[Verse]\nla\n[End]\n")
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
            fh.write(text)
            path = fh.name
        try:
            self.assertEqual(statuses(validate.validate_file(path))["Gear Names"], "PASS")
        finally:
            os.unlink(path)

    def test_genre_first_uses_word_boundaries(self):
        text = "## STYLE PROMPT:\nheartbreak feelings, slow, sad\n\n## LYRICS:\n[Title: X]\n[End]\n"
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
            fh.write(text)
            path = fh.name
        try:
            self.assertEqual(statuses(validate.validate_file(path))["Genre First"], "WARN")  # "art" in heartbreak is not a genre
        finally:
            os.unlink(path)

    def test_directory_mode_skips_readme_and_briefs(self):
        with tempfile.TemporaryDirectory() as d:
            for name in ("README.md", "song.brief.md"):
                with open(os.path.join(d, name), "w") as fh:
                    fh.write("# not a song\n")
            with open(os.path.join(FIX, "v6_valid.md")) as src, open(os.path.join(d, "song.md"), "w") as dst:
                dst.write(src.read())
            code, out = run_main(validate.main, [d])
            self.assertEqual(code, 0)
            self.assertIn("song.md", out)
            self.assertNotIn("README.md", out)
            self.assertNotIn("brief", out)

    def test_hook_mode_reads_stdin_payload_and_never_fails(self):
        payload = json.dumps({"hook_event_name": "PostFileSave", "file_path": os.path.join(FIX, "broken.md")})
        code, out = run_main(validate.main, ["--hook", "{{filePath}}"], stdin_text=payload)
        self.assertEqual(code, 0)
        self.assertIn("RESULT: FAIL", out)
        code, out = run_main(validate.main, ["--hook", os.path.join(ROOT, "songs", "README.md")])
        self.assertEqual((code, out.strip()), (0, ""))

    def test_strict_mode(self):
        code, _ = run_main(validate.main, ["--strict", os.path.join(FIX, "legacy.md")])
        self.assertEqual(code, 1)


class LyricLint(unittest.TestCase):
    def test_heuristic_syllables(self):
        for word, n in (("cat", 1), ("broken", 2), ("tomorrow", 3), ("beautiful", 3)):
            self.assertEqual(lint.heuristic_syllables(word), n, word)

    @unittest.skipUnless(lint._CMU, "pronouncing (CMUdict) not installed")
    def test_rhyme_ladder(self):
        cases = {
            ("time", "rhyme"): "perfect", ("home", "bone"): "family", ("cup", "tuck"): "family",
            ("free", "sweet"): "additive", ("sweet", "free"): "subtractive", ("fate", "game"): "assonance",
            ("rust", "lost"): "consonance", ("broken", "spoken"): "perfect", ("night", "knight"): "identity",
        }
        for (a, b), expected in cases.items():
            self.assertEqual(lint.classify_rhyme(a, b), expected, f"{a}/{b}")

    @unittest.skipUnless(lint._CMU, "pronouncing (CMUdict) not installed")
    def test_scheme_and_stability(self):
        lines = [lint.Line(i, t) for i, t in enumerate(
            ["I keep the lantern burning", "beside the open door", "the tide is slowly turning", "I wait here like before"], 1)]
        scheme, _ = lint.scheme_for(lines)
        self.assertEqual(scheme, "ABAB")
        overall, marks = lint.stability(lines, scheme)
        self.assertEqual(marks["line count"], "even")
        self.assertEqual(marks["rhyme closure"], "closed")

    def test_end_to_end_and_cliches(self):
        res = lint.lint_song(os.path.join(FIX, "broken.md"))
        self.assertIsNone(res["error"])
        messages = " ".join(f["message"] for f in res["findings"])
        self.assertIn("torn apart", messages)
        res = lint.lint_song(os.path.join(FIX, "v6_valid.md"))
        names = [s["name"] for s in res["sections"]]
        self.assertEqual(names[:2], ["Verse 1", "Chorus"])

    def test_hook_mode(self):
        code, out = run_main(lint.main, ["--hook", os.path.join(FIX, "v6_valid.md")])
        self.assertEqual(code, 0)
        self.assertIn("LYRIC LINT", out)


class RepoIntegrity(unittest.TestCase):
    def test_repository_passes_check_repo(self):
        code, out = run_main(checkrepo.main, ["--root", ROOT])
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
