---
name: suno-meta-tags
description: Suno AI tag and formatting reference. V6 (default) tag paradigm — Style field = WHAT, Lyrics field = HOW, [Instrument: X In/Out] choreography, dynamics/vocal/transition tags, [End] — plus the legacy v5.x tag catalog (global control tags, pipe notation, sliders) for v5.5 renders. Use when preparing songs for Suno, choosing tags, checking character counts, or troubleshooting Suno output.
---

# Suno Meta-Tags Skill

You are a Suno AI formatting specialist. When activated, format songs for Suno, using the V6 paradigm unless the user targets v5.5.

## Read First

- `core/methodology/suno-optimization.md`: V6 Procedure (default) + the v5.5-era 13-step procedure (legacy)
- `references/V6_TAG_REFERENCE.md`: V6 tag dictionary and minimal song skeleton
- `references/V6_TAG_DISCOVERY.md`: division of labour, canonical V6 grammar, results log
- `references/SUNO_STYLE_GENRE_REFERENCE.md`: genre / mode / BPM / instrument choices
- `references/SUNO_TAGS_REFERENCE.md`: legacy v5.x tag catalog (v5.5 renders, or hypotheses to re-test on V6)

Read the files you need before applying this skill (if they are not already in context).

## When to Use This Skill

- Converting a finished song into Suno-ready format
- Optimizing a prompt that isn't rendering well
- Checking character counts (Style ≤1000, Lyrics ≤5000): `python3 tools/validate-song.py <file>`
- Choosing section, instrument, dynamics and delivery tags
- Migrating a v5.5-era song to V6

## V6 Workflow (default)

1. **Three fields:** Style (the WHAT) / Exclude (negatives, plain comma-separated, no dash prefix) / Lyrics (the HOW)
2. **Style:** genre first, key, tempo, vocal identity, production aesthetic, instruments as sound descriptors (no artist or gear-model names). ≤1000 chars
3. **Lyrics top:** `[Title:]`, `[Production Direction:]`, `[Vocal Direction:]`
4. **Sections:** section tags on their own lines; choreograph with `[Instrument: X In]` / `[Instrument: X Out]`, `[Dynamic: ...]`, `[Vocal: ...]` (or `[Male lead, tender then stronger]`), `[Transition: ...]`, `[Key Change: ...]`; 2-4 tags per section
5. **End** with `[End]`
6. **Never** in V6 output: a `[Tag Vocabulary]` block, v5.5 global tags (`[track:]` / `[control:]` / `[sequence:]`), compact pipe notation `[Section | params]`
7. **Verify:** `python3 tools/validate-song.py <file>` (and `python3 tools/lyric-lint.py <file>` for prosody/rhyme)
8. **Render** 3-4 takes; log what V6 honoured in the `references/V6_TAG_DISCOVERY.md` results log

## Common Suno Problems & Fixes

| Problem | Likely Cause | V6 Fix | Legacy v5.5-era fix |
|---|---|---|---|
| Instrument enters too early / never leaves | No choreography | `[Instrument: X In]` / `[Instrument: X Out]` at the section boundary | Per-section stacked cue tags |
| Song won't end | No termination signal | `[End]` after the outro (plus `[Dynamic: Fade Out]`) | `[end]` + `[fade: slow]` |
| Sections out of order / repeated lines | Complex structure | Clear section tags; fewer, distinct sections | `[sequence: ...]`, `[control: no-repeat]` |
| Wrong voice gender / duet confusion | Unclear vocal assignment | `[Male lead, ...]` / `[Female response, ...]` + declare `()` layers in Style | `[Male Vocal]` / `[Female Vocal]` |
| Bridge sung instead of spoken | No delivery tag | `[Vocal: Spoken Word]` | `[spoken word]` |
| No dynamic contrast | All sections same energy | `[Dynamic: Diminuendo]` → `[Dynamic: Full]`, instrument Outs before the drop | `[build]`, `[crescendo]` |
| Genre drift mid-song | Conflicting style cues | Tighter Style (one 70/30 fusion) + Exclude field | `[track: genre: X]` |
| Over the character limit | Long direction blocks / stacked tags | Trim direction to the essentials; 2-4 tags per section | Pipe notation saved characters on v5.5 |

## Legacy v5.5-era Notes (re-validate on V6)

Global control tags, pipe notation, `[length:]`, the "5-8 Style tags" rule, slider presets, era tags,
Italian tempo preference and performance-notation symbols are v5.5-era findings [Tier 3]. Use them
only for v5.5 renders, or as hypotheses to test and log on V6. Obsolete in every version: `[bpm:]`,
`[key:]`, `[loop]`, `[autotune]`, `[mix]`, `[master]`, `[volume]`. Put tempo and key in the Style field.
