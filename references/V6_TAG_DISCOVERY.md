# Suno V6 Tag Discovery

> **Status: PARTIALLY CONFIRMED (Sept 2026).** This documents the V6-era lyric-tag format
> discovered through hands-on testing. It is SEPARATE from the v5.5-confirmed methodology in
> `core/methodology/suno-optimization.md`. Some findings are now confirmed from real renders
> (see Confirmed Findings below); the rest await testing.

---

## CONFIRMED FINDINGS (from real V6 renders)

1. **The `[Tag Vocabulary]` declaration block is NOT needed in the final song.** It did not get
   sung (good), but it also did not prove necessary — it was useful scaffolding for organizing
   the arrangement while writing, but the production lyrics do NOT need it. **Drop it from final
   output.** Keep it only as an optional planning aid.

2. **`[Instrument: X In]` / `[Instrument: X Out]` directional tags WORK.** V6 honors instrument
   entrances and exits on cue. This is the marquee confirmed V6 capability — you can choreograph
   the arrangement (when the banjo enters, when the drums drop out) via inline tags.

3. **THE DIVISION OF LABOR — Style Prompt = WHAT, Inline Tags = HOW (confirmed).**
   These two locations are COMPLEMENTARY, not redundant:
   - **Style Prompt = the KEY DETAILS / the WHAT:** genre, key, tempo, vocal identity, overall
     sonic character, production aesthetic. It sets the WORLD the song lives in.
   - **Inline tags = the ARRANGEMENT / the HOW:** when instruments enter and exit, dynamics,
     section-by-section vocal delivery, transitions. They choreograph the PERFORMANCE within
     the world the style prompt established.
   - **Practical rule:** Put identity/character in the Style Prompt. Put execution/arrangement
     in the inline tags. A detail can live in either location, but the style carries the
     essential "what this is" and the inline tags describe "how it unfolds."

---

## Context: What V6 Is

Suno v6 launched ~Sept 8, 2026 — a licensed music model family (Warner/BMG/Believe catalogs):

| Model | Access | Character |
|---|---|---|
| **v6** | Pro/Premier | Flagship — reliable, precise, polished |
| **v6-wild** | Pro/Premier | Exploratory — less predictable, textured, ambitious |
| **v6-mini** | Everyone (free) | Fast, efficient |

All prior models (v5.5 and earlier) are being retired. Official product direction emphasizes
**plain-language instruction** ("change the chorus so it's sung by a gospel choir") and
understanding "more of the language and building blocks musicians use." This means our
v5.5-tested findings (Italian tempo, `[modulation: ascending]`, the `[silence: sudden]`
failure, slider behavior, tag-count limits) are all UNCONFIRMED under v6.

---

## The Converged V6 Tag Format

Across multiple experiments, the format that emerged as most complete is a **text-based
arrangement score**. It has five parts:

### 1. A Tag Vocabulary declaration block (at the top)
Declares the full palette before the song, teaching the model the vocabulary. Observed in
several successful renders. Two working syntaxes:

```
[Tag Vocabulary]
[Structure: Intro] [Structure: Verse] ...
[Instrument: Banjo In] [Instrument: Banjo Out] ...
[Dynamic: Crescendo] [Dynamic: Diminuendo] ...
[Feel: Half-Time] [Feel: Double-Time] ...
[Vocal: Male Lead] [Vocal: Female Counter] ...
[Transition: Riser] [Transition: Stop-Time] ...
```

or the compact pipe form:

```
[VOCABULARY:STRUCTURE=intro|verse|pre-chorus|chorus|...]
[VOCABULARY:INSTRUMENTS=piano|cello|banjo|...]
[VOCABULARY:DYNAMICS=pp|p|mp|mf|f|ff|crescendo|...]
[VOCABULARY:VOCALS=male-whisper|male-belt|female-answer|...]
```

### 2. Directional instrument tags (the biggest V6 evolution)
Control instrument entrance AND exit — real arrangement, not just "add cello":
`[Instrument: Banjo In]` / `[Instrument: Banjo Out]`, `[Piano In]` / `[Piano Out]`.

### 3. Compound transition tags
Bundle simultaneous events: `[Transition: Crescendo, Snare In, Synth Riser]`.

### 4. Vocal-character tags with inline delivery
`[Vocal: Belt]`, `[Vocal: Female Counter]`, `[Male Lead: Whisper, dry close vocal]`,
`[Female Lead: Call, lifted alto]`.

### 5. Explicit call-and-response
`[Call] Higher!` / `[Response] Higher!` on their own lines.

---

## The Full V6 Tag Taxonomy (mapped from testing)

**Structure:** Intro, Verse, Pre-Chorus, Chorus, Post-Chorus, Bridge, Breakdown, Build,
Drop, Instrumental Solo, Interlude, Key Change, Outro, Transition, End

**Instrumentation (with In/Out directionality):** Piano, Cello/Bowed Cello, Banjo, Fiddle,
Slide Guitar, Acoustic Guitar, Electric Guitar, Upright Bass, Distorted Bass, Sub-Bass,
Drums, Kick, Snare, Toms, Cymbals, Boot Stomp, Hand Claps, Tambourine, Hammond Organ,
Rhodes, Strings/Chamber Strings, Synth Pad, Synth Lead, Analog Synth, Harmonica, Room Tone,
Drone, Vocal Chop, FX/Texture

**Dynamics:** pp, p, mp, mf, f, ff (and named: Whisper/Hush, Soft, Full, Fortissimo),
Crescendo, Diminuendo, Swell, Drop, Fade In, Fade Out, Silence, Full Impact

**Feel / Tempo:** Free Time, Rubato, Straight, Half-Time, Double-Time (Lift), Shuffle,
Ritardando, Accelerando, Bar Extension; plus explicit BPM and Italian markings

**Vocals:** Male Lead, Female Lead/Counter/Counterline, Whisper, Breathy, Raspy, Belt,
Growl, Harmony, Gang Vocal, Call, Response, Spoken Word, Ad-Lib, Layered Double, Unison,
Falsetto, Dry/Close-Mic, Reverb Tail, Vocal Out

**Transitions:** Entrance, Exit, Pickup, Stop-Time, Riser, Turnaround, Drum Fill,
Reverse Cymbal, Breath, Hit, Key Change Up / Key Lift, Cut, Hard Cut

**Production (observed):** Vinyl Crackle, Tape Hiss, Filtered, Saturated, Detuned,
Distorted, Stereo Widening, Delay, Reverb, Analog Warmth, Digital Cold

---

## Format Evolution (across the test attempts)

| Attempt | Approach | Notes |
|---|---|---|
| 1 | Simple bracketed labels, one per line | Cleanest, likely parses well. Baseline. |
| 2 | Verbose pipe-delimited multi-param tags (pan, bar numbers, pp/mf/ff) | Extreme density — likely over-tagged; per-bar micro-control probably ignored/averaged |
| 3 | `[Tag Vocabulary]` block + inline categorized flow tags | The taxonomy-declaration idea emerges |
| 4-6 | Refined: vocabulary header + `[Instrument: X In/Out]` + classical dynamics + `[Feel:]` + Entrance/Exit transitions | The converged "best" format. Full arrangement-score control. |

---

## RESULTS LOG — What V6 Actually Honors (TO FILL FROM RENDERS)

For each style test, render and log whether each tag TYPE produced an audible, reliable effect.
Rate: ✅ works / ⚠️ partial / ❌ ignored / ? untested.

| Tag Type | Result | Notes |
|---|---|---|
| `[Tag Vocabulary]` block | ✅ not sung / ❌ not needed | Did not get sung. Not necessary in final output — drop it. Optional planning aid only. |
| `[Instrument: X In]` (entrance on cue) | ✅ works | Confirmed — instruments enter on cue |
| `[Instrument: X Out]` (exit on cue) | ✅ works | Confirmed — instruments exit on cue |
| Style Prompt vs inline tags | ✅ complementary | NOT a competition — style = WHAT (identity), inline = HOW (arrangement). Both used together. |
| `[Male Lead]` / `[Female ...]` clean handoff | ? | Awaiting focused eval |
| `[Whisper]` vs `[Belt]` delivery change | ? | Awaiting focused eval |
| `[Spoken Word]` (speaks not sings) | ? | Awaiting focused eval |
| `[Gang Vocal]` (group appears) | ? | Awaiting focused eval |
| Call/Response formatting | ? | Awaiting focused eval |
| `[Key Change]` / `[Key Lift]` (key actually lifts) | ? | Awaiting focused eval |
| `[Half-Time]` / `[Double-Time]` feel shift | ? | Awaiting focused eval |
| `[Crescendo]`/`[Diminuendo]`/`[Swell]` dynamics | ? | Awaiting focused eval |
| Compound transitions (all events or just one?) | ? | Awaiting focused eval |
| East Tennessee accent (from style vs from lyric) | ? | Awaiting focused eval |

---

## Open Questions for V6 (still to resolve)

1. ~~Does the `[Tag Vocabulary]` header get sung/help/ignored?~~ **RESOLVED: not sung, not needed — drop from final output.**
2. ~~Do In/Out instrument tags actually control entrances/exits?~~ **RESOLVED: yes, they work.**
3. ~~Style Prompt vs inline tags — which wins?~~ **RESOLVED: complementary. Style = WHAT/identity, inline = HOW/arrangement.**
4. Character limits under v6 — still 1000 style / 5000 lyrics, or changed?
5. Does v6 favor plain-language section descriptions over bracket tags for some events?
6. Is modulation more reliable via the "edit one section in plain language" feature than via tags?
7. Does end punctuation (! ? .) still cause issues, or does v6 handle it? (test renders used it freely)
8. v6 flagship vs v6-wild: does wild honor experimental tags the flagship ignores?
9. Which vocal-delivery tags (Whisper, Belt, Spoken Word, Gang Vocal) are honored vs decorative?
10. Do dynamics tags (Crescendo/Diminuendo/Swell) and feel shifts (Half/Double-Time) execute reliably?

---

## PRODUCTION TEMPLATE (based on confirmed findings)

For a V6 song, the working structure is:

**Style field (the WHAT — identity):**
- Genre, key, tempo, vocal identity/character, overall sonic + production aesthetic
- This sets the world.

**Lyrics field (the HOW — arrangement):**
- NO `[Tag Vocabulary]` block (confirmed unnecessary)
- Section tags (`[Verse]`, `[Chorus]`, etc.)
- `[Instrument: X In]` / `[Instrument: X Out]` to choreograph the arrangement (confirmed working)
- Vocal-delivery and dynamics tags inline (pending confirmation on which are honored)
- The lyrics themselves

Keep identity in the style; keep execution in the inline tags.

---

## Relationship to the v5.5 Methodology

- `core/methodology/suno-optimization.md` remains the **v5.5-confirmed** reference.
- This doc is the **v6 frontier** — unconfirmed until the results log is filled.
- Once v6 behavior is confirmed, migrate the confirmed findings into the main methodology
  with a clear v6 version tag, and note which v5.5 findings no longer apply.

---

*Living document. Update the results log as renders are evaluated. Style prompts that pair
with these tag structures are catalogued in `references/STYLE_LIBRARY.md`.*