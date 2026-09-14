# Suno V6 Tag Discovery

> **Status: EXPERIMENTAL / IN PROGRESS.** This documents the V6-era lyric-tag format
> discovered through hands-on testing (Sept 2026). It is SEPARATE from the v5.5-confirmed
> methodology in `core/methodology/suno-optimization.md`. Do NOT treat these as confirmed
> until the results-log table below is filled from actual renders.

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

| Tag Type | Cinematic Appalachian | Southern Gothic Stomp | Orchestral Post-Rock | Dark Folk-Electronic | Arena Folk Anthem | Haunted Chamber-Folk |
|---|---|---|---|---|---|---|
| `[Tag Vocabulary]` block (sung? ignored? helped?) | ? | ? | ? | ? | ? | ? |
| `[Instrument: X In]` (entrance on cue) | ? | ? | ? | ? | ? | ? |
| `[Instrument: X Out]` (exit on cue) | ? | ? | ? | ? | ? | ? |
| `[Male Lead]` / `[Female ...]` clean handoff | ? | ? | ? | ? | ? | ? |
| `[Whisper]` vs `[Belt]` delivery change | ? | ? | ? | ? | ? | ? |
| `[Spoken Word]` (speaks not sings) | ? | ? | ? | ? | ? | ? |
| `[Gang Vocal]` (group appears) | ? | ? | ? | ? | ? | ? |
| Call/Response formatting | ? | ? | ? | ? | ? | ? |
| `[Key Change]` / `[Key Lift]` (key actually lifts) | ? | ? | ? | ? | ? | ? |
| `[Half-Time]` / `[Double-Time]` feel shift | ? | ? | ? | ? | ? | ? |
| `[Crescendo]`/`[Diminuendo]`/`[Swell]` dynamics | ? | ? | ? | ? | ? | ? |
| Compound transitions (all events or just one?) | ? | ? | ? | ? | ? | ? |
| East Tennessee accent (from style vs from lyric) | ? | ? | ? | ? | ? | ? |
| Style Prompt vs inline tags (which wins?) | ? | ? | ? | ? | ? | ? |

**Key experiment:** Run the SAME tagged lyrics through two contrasting styles (e.g., Cinematic
Appalachian vs Dark Folk-Electronic). If the dense instrument tags hold up even when the style
says "electronic," the tags override the style. If the style washes them out, the style wins.

---

## Open Questions for V6 (to resolve through testing)

1. Does the `[Tag Vocabulary]` header improve adherence, get sung, or get silently ignored?
2. Do In/Out instrument tags actually control entrances/exits, or just suggest arrangement density?
3. Character limits under v6 — still 1000 style / 5000 lyrics, or changed?
4. Does v6 favor plain-language section descriptions over bracket tags (per official messaging)?
5. Is modulation more reliable via the new "edit one section in plain language" feature than via tags?
6. Does end punctuation (! ? .) still cause issues, or does v6 handle it? (The test renders used it freely.)
7. v6 flagship vs v6-wild: does wild honor experimental tags the flagship ignores?

---

## Relationship to the v5.5 Methodology

- `core/methodology/suno-optimization.md` remains the **v5.5-confirmed** reference.
- This doc is the **v6 frontier** — unconfirmed until the results log is filled.
- Once v6 behavior is confirmed, migrate the confirmed findings into the main methodology
  with a clear v6 version tag, and note which v5.5 findings no longer apply.

---

*Living document. Update the results log as renders are evaluated. Style prompts that pair
with these tag structures are catalogued in `references/STYLE_LIBRARY.md`.*