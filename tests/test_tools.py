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
runtime = load("estimate_runtime", "estimate-runtime.py")
sunofields = load("suno_fields", "suno-fields.py")


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


class ReviewFixes(unittest.TestCase):
    """Parser, validator and lint fixes from the 2026-11-23 knowledge-base review."""

    def _write(self, text):
        handle = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        handle.write(text)
        handle.close()
        self.addCleanup(os.unlink, handle.name)
        return handle.name

    def test_section_tags_allow_leading_modifiers(self):
        for tag in ("[Final Refrain \u2014 Warm]", "[Extended Instrumental Intro \u2014 Lyre]", "[Closing Outro]"):
            self.assertTrue(songfile.SECTION_TAG_RE.match(tag), tag)
        for tag in ("[Low Baritone \u2014 Almost Whispered]", "[Deep Drum Strike]"):
            self.assertFalse(songfile.SECTION_TAG_RE.match(tag), tag)

    def test_raw_lyrics_without_headings_are_read(self):
        song = songfile.SongFile(os.path.join(FIX, "raw_lyrics.md"))
        self.assertTrue(song.lyrics_inferred)
        self.assertTrue(song.lyrics_has_end)
        self.assertIsNone(song.style)
        rep = validate.validate_file(os.path.join(FIX, "raw_lyrics.md"))
        self.assertEqual(statuses(rep)["Format"], "WARN")
        res = lint.lint_song(os.path.join(FIX, "raw_lyrics.md"))
        self.assertIsNone(res["error"])
        self.assertIn("Final Refrain \u2014 Warm", [s["name"] for s in res["sections"]])

    def test_plain_markdown_is_not_mistaken_for_lyrics(self):
        path = self._write("# Notes\n\nSome prose about [Verse 1] in passing.\n")
        self.assertFalse(songfile.SongFile(path).lyrics_inferred)

    def test_rejected_word_fails(self):
        with open(os.path.join(FIX, "v6_valid.md"), encoding="utf-8") as handle:
            text = handle.read().replace("unhurried and hopeful", "fireside-skald menace", 1)
        rep = validate.validate_file(self._write(text))
        self.assertEqual(statuses(rep)["Suno Rejected Words"], "FAIL")
        rep = validate.validate_file(os.path.join(FIX, "v6_valid.md"))
        self.assertEqual(statuses(rep)["Suno Rejected Words"], "PASS")

    def test_v6_vocabulary_info(self):
        with open(os.path.join(FIX, "v6_valid.md"), encoding="utf-8") as handle:
            text = handle.read().replace("[Bridge]", "[Refrain]", 1).replace("Cello In]", "Tagelharpa In]", 1)
        st = statuses(validate.validate_file(self._write(text)))
        self.assertEqual(st["V6: Structure Tags"], "INFO")
        self.assertEqual(st["V6: Instrument Names"], "INFO")
        st = statuses(validate.validate_file(os.path.join(FIX, "v6_valid.md")))
        self.assertNotIn("V6: Structure Tags", st)
        self.assertNotIn("V6: Instrument Names", st)

    def test_scheme_is_per_stanza(self):
        lines = [lint.Line(1, "the road was long", stanza=0), lint.Line(2, "I sang a song", stanza=0),
                 lint.Line(3, "the road was long", stanza=1), lint.Line(4, "the night was cold", stanza=1)]
        scheme, _ = lint.scheme_for(lines)
        self.assertEqual(len(scheme.split(" ")), 2)

    def test_runtime_estimate(self):
        res = runtime.estimate(os.path.join(FIX, "v6_valid.md"))
        self.assertIsNone(res["error"])
        self.assertEqual(res["bpm"], 84)
        self.assertEqual(res["meter"], "4/4")
        self.assertGreater(res["runtime_s"], 0)
        self.assertIsNotNone(res["first_chorus_s"])
        long_song = runtime.estimate(os.path.join(FIX, "v6_valid.md"), bars_per_line=40)
        self.assertIn("WARN", [f["level"] for f in long_song["findings"]])

    def test_suno_fields_match_validator_counts(self):
        out, err = sunofields.fields(os.path.join(FIX, "v6_valid.md"))
        self.assertIsNone(err)
        self.assertEqual(out["title"], "Porch Light")
        self.assertTrue(out["lyrics"].endswith("[End]"))
        self.assertEqual(out["negative_style"], "trap drums, autotune, EDM drops, gang vocals")
        song = songfile.SongFile(os.path.join(FIX, "v6_valid.md"))
        self.assertEqual(out["style"], song.style)


class LengthTargets(unittest.TestCase):
    def _song(self, extra):
        with open(os.path.join(FIX, "v6_valid.md"), encoding="utf-8") as handle:
            text = handle.read().replace("# Porch Light (test fixture, V6 format)", "# Porch Light\n\n" + extra, 1)
        handle = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        handle.write(text)
        handle.close()
        self.addCleanup(os.unlink, handle.name)
        return handle.name

    def test_presets_load_and_parse(self):
        presets = runtime.load_targets()
        for name in ("radio", "streaming", "short", "sync30", "cinematic"):
            self.assertIn(name, presets)
        t, err = runtime.parse_target_spec("cinematic, intro <= 40s", presets)
        self.assertIsNone(err)
        self.assertEqual(t["max_intro_s"], 40)
        self.assertEqual(t["max_s"], presets["cinematic"]["max_s"])
        t, err = runtime.parse_target_spec("5:30-6:30, hook <= 1:20", presets)
        self.assertEqual((t["min_s"], t["max_s"], t["max_hook_s"]), (330, 390, 80))
        self.assertEqual(runtime.parse_target_spec("none", presets), (None, None))
        self.assertIsNotNone(runtime.parse_target_spec("radioo", presets)[1])

    def test_song_file_target_and_precedence(self):
        path = self._song("Length Target: radio")
        res = runtime.estimate(path)
        self.assertEqual(res["length_target"]["source"], "song file")
        self.assertTrue(any("under the 'Radio edit' target" in f["message"] for f in res["findings"]))
        res = runtime.estimate(path, target="1:00-2:00")
        self.assertEqual(res["length_target"]["source"], "command line")
        self.assertTrue(any(f["level"] == "PASS" for f in res["findings"]))
        res = runtime.estimate(path, overrides={"min_s": 60, "max_s": 120})
        self.assertIn("overrides", res["length_target"]["source"])

    def test_target_none_and_findings_never_fail(self):
        res = runtime.estimate(self._song("Length Target: none"))
        self.assertEqual(res["length_target"], {"source": "song file (none)"})
        res = runtime.estimate(os.path.join(FIX, "v6_valid.md"), target="sync30")
        self.assertFalse(any(f["level"] in ("FAIL", "ERROR") for f in res["findings"]))


class RenderSettings(unittest.TestCase):
    SETTINGS = "\n## RENDER SETTINGS:\n\n- voice: Test Voice\n- voice_id: 1111-2222\n- model: v6\n- controls: weirdness 0.3, style_influence 0.75, variety 1\n- duration: 5:59\n"

    def _song(self, settings):
        with open(os.path.join(FIX, "v6_valid.md"), encoding="utf-8") as handle:
            text = handle.read().replace("## LYRICS:", settings + "\n---\n\n## LYRICS:", 1)
        handle = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        handle.write(text)
        handle.close()
        self.addCleanup(os.unlink, handle.name)
        return handle.name

    def test_parse_and_export(self):
        path = self._song(self.SETTINGS)
        song = songfile.SongFile(path)
        self.assertEqual(song.render["voice_id"], "1111-2222")
        self.assertTrue(song.lyrics.startswith("[Title: Porch Light]"))
        out, err = sunofields.fields(path)
        self.assertIsNone(err)
        self.assertEqual(out["voice_id"], "1111-2222")
        self.assertEqual(out["model"], "v6")
        self.assertEqual(out["controls"], {"weirdness": 0.3, "style_influence": 0.75, "variety": 1})
        self.assertEqual((out["duration"], out["duration_strict"]), (359, False))
        self.assertNotIn("_warnings", out)
        self.assertEqual(statuses(validate.validate_file(path))["Render Settings"], "PASS")

    def test_workspace_exported(self):
        out, _ = sunofields.fields(self._song("\n## RENDER SETTINGS:\n\n- voice: none\n- workspace: Test WS\n- workspace_id: ws-123 (Test WS)\n"))
        self.assertEqual(out["workspace_id"], "ws-123")

    def test_missing_voice_warns_but_none_is_a_choice(self):
        out, _ = sunofields.fields(os.path.join(FIX, "v6_valid.md"))
        self.assertIn("_warnings", out)
        self.assertEqual(statuses(validate.validate_file(os.path.join(FIX, "v6_valid.md")))["Render Settings"], "INFO")
        out, _ = sunofields.fields(self._song("\n## RENDER SETTINGS:\n\n- voice: none\n"))
        self.assertNotIn("_warnings", out)
        self.assertNotIn("voice_id", out)

    def test_fixed_bed_uses_bed_length(self):
        path = self._song("\n## RENDER SETTINGS:\n\n- voice: none\n- cover_of: abcd\n- bed_duration: 5:59\n")
        res = runtime.estimate(path, target="radio")
        self.assertTrue(res["fixed_bed"])
        self.assertEqual(res["runtime_s"], 359)
        self.assertIsNone(res["first_chorus_s"])
        self.assertTrue(any("over the 'Radio edit' target" in f["message"] for f in res["findings"]))


class RepoIntegrity(unittest.TestCase):
    def test_repository_passes_check_repo(self):
        code, out = run_main(checkrepo.main, ["--root", ROOT])
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
