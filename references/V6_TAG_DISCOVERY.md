# Suno V6 Tag Discovery

> **Status: WORKING MODEL (Sept 2026).** This documents the V6-era lyric-tag format.
> The findings below are treated as the operating assumption for V6 songwriting — they were
> produced/validated via Suno's own V6 system output during testing. This remains SEPARATE from
> the v5.5-confirmed methodology in `core/methodology/suno-optimization.md`; refine as more
> renders accumulate.

---

## CONFIRMED FINDINGS (working model for V6)

1. **The `[Tag Vocabulary]` declaration block is NOT needed in the final song.** It does not get
   sung, and it is not necessary in production output. It's useful only as optional scaffolding
   for organizing an arrangement while writing. **Drop it from final output.**

2. **`[Instrument: X In]` / `[Instrument: X Out]` directional tags WORK.** V6 honors instrument
   entrances and exits on cue. This is the marquee V6 capability — you can choreograph the
   arrangement (when the banjo enters, when the drums drop out) via inline tags.

3. **THE DIVISION OF LABOR — Style Prompt = WHAT, Inline Tags = HOW.**
   These two locations are COMPLEMENTARY, not redundant:
   - **Style Prompt = the KEY DETAILS / the WHAT:** genre, key, tempo, vocal identity, overall
     sonic character, production aesthetic. It sets the WORLD the song lives in.
   - **Inline tags = the ARRANGEMENT / the HOW:** when instruments enter and exit, dynamics,
     section-by-section vocal delivery, transitions. They choreograph the PERFORMANCE within
     the world the style prompt established.
   - **Practical rule:** Put identity/character in the Style Prompt. Put execution/arrangement
     in the inline tags. A detail can live in either location, but the style carries the
     essential "what this is" and the inline tags describe "how it unfolds."

4. **The full V6 tag vocabulary is treated as functional** (per Suno system output): structure,
   directional instrumentation, dynamics (classical markings pp–ff + crescendo/diminuendo/swell),
   feel/tempo shifts (half-time, double-time, rubato), vocal-character tags (whisper, belt,
   spoken word, gang vocal, call/response, harmony, layered double, ad-lib), key changes, and
   compound transitions. See the taxonomy section below — treat all listed tags as usable.

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
understanding "more of the language and building blocks musicians use." The V6 tag findings in
this doc are the current working model; v5.5-tested findings (Italian tempo, `[modulation: ascending]`,
the `[silence: sudden]` failure, slider behavior, tag-count limits) should be re-checked under v6.

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

## The Full V6 Tag Taxonomy

> The complete, de-duplicated master tag dictionary now lives in **`references/V6_TAG_REFERENCE.md`**
> (copy-paste ready, grouped by Structure / Instrumentation / Dynamics / Feel-Tempo / Vocals /
> Transitions / Production, plus syntax forms and a minimal song skeleton). Summary below:

- **Structure (15):** Intro, Verse, Pre-Chorus, Chorus, Post-Chorus, Bridge, Breakdown, Build, Drop, Instrumental Solo, Interlude, Key Change, Outro, Transition, End
- **Instrumentation (In/Out each):** Piano, Felt Piano, Rhodes, Hammond Organ, Cello, Bowed Cello, Strings, Chamber Strings, Fiddle, Harmonica, Banjo, Acoustic/Electric/Slide/Muted Guitar, Upright/Distorted/Sub Bass, Drums, Kick, Snare, Toms, Floor Tom, Cymbals, Percussion, Brushes, Boot Stomp, Hand Claps, Tambourine, Synth Pad, Synth Lead, Analog Synth, Arp, Room Tone, Drone, Vocal Chop, FX/Texture
- **Dynamics:** pp–fff, Whisper/Hush, Soft, Full, Fortissimo, Crescendo, Diminuendo, Swell, Drop, Full Impact, Fade In/Out, Silence, Rest, Accent, Staccato, Sustain
- **Feel/Tempo:** Free Time, Rubato, Straight, Steady Stomp, Shuffle, Half-Time, Double-Time (Lift), Bar Extension, Ritardando, Accelerando, Push, Hold, + BPM/Italian markings
- **Vocals:** Male Lead, Female Lead/Counter, Baritone, Tenor Lift, Falsetto, Whisper, Breathy, Dry/Close-Mic, Spoken Word, Half-Spoken, Raspy, Growl, Belt, Full Voice, Harmony, Unison, Layered Double, Gang Vocal, Call, Response, Ad-Lib, Reverb Tail, Vocal Out, Laugh, Breath
- **Transitions:** Entrance, Exit, Pickup, Turnaround, Riser, Drum Fill, Reverse Cymbal, Cymbal Rise, Stop-Time, Breath, Hit, Cut, Hard Cut, Key Change Up/Key Lift, Filter Open/Close, Glitch Cut
- **Production/FX:** Vinyl Crackle, Tape Hiss, Room Tone, Filtered, Saturated, Detuned, Distorted, Stereo Widening, Delay, Reverb, Analog Warmth, Digital Cold

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

Working model (treated as functional per Suno V6 system output; refine as renders accumulate):

| Tag Type | Result | Notes |
|---|---|---|
| `[Tag Vocabulary]` block | ❌ not needed | Not sung, not necessary — drop from final output. Optional planning aid only. |
| `[Instrument: X In]` (entrance on cue) | ✅ works | Instruments enter on cue |
| `[Instrument: X Out]` (exit on cue) | ✅ works | Instruments exit on cue |
| Style Prompt vs inline tags | ✅ complementary | Style = WHAT (identity), inline = HOW (arrangement). Used together. |
| `[Male Lead]` / `[Female ...]` clean handoff | ✅ working model | Distinct-voice assignment |
| `[Whisper]` vs `[Belt]` delivery change | ✅ working model | Vocal delivery shifts |
| `[Spoken Word]` (speaks not sings) | ✅ working model | Spoken delivery |
| `[Gang Vocal]` (group appears) | ✅ working model | Group/ensemble vocal |
| Call/Response formatting | ✅ working model | Alternating lead/response |
| `[Key Change]` / `[Key Lift]` | ✅ working model | Modulation on cue |
| `[Half-Time]` / `[Double-Time]` feel shift | ✅ working model | Feel/tempo-perception shift |
| `[Crescendo]`/`[Diminuendo]`/`[Swell]` dynamics | ✅ working model | Dynamic motion |
| Compound transitions | ✅ working model | Bundled simultaneous events |
| East Tennessee accent | ✅ working model | Carried by style prompt; reinforced by lyric dialect |

---

## Resolved / Working Model

- ~~`[Tag Vocabulary]` header~~ → **not sung, not needed — drop from final output.**
- ~~In/Out instrument tags~~ → **work; control entrances/exits.**
- ~~Style Prompt vs inline tags~~ → **complementary. Style = WHAT/identity, inline = HOW/arrangement.**
- ~~Vocal-delivery tags (Whisper/Belt/Spoken/Gang)~~ → **treated as functional.**
- ~~Dynamics + feel shifts~~ → **treated as functional.**
- ~~Key changes + compound transitions~~ → **treated as functional.**

## Still Open (refine as more renders accumulate)

1. Character limits under v6 — still 1000 style / 5000 lyrics, or changed?
2. Does v6 favor plain-language section descriptions over bracket tags for some events?
3. Is modulation even more reliable via the "edit one section in plain language" feature than via tags?
4. Does end punctuation (! ? .) cause issues, or does v6 handle it cleanly? (test renders used it freely)
5. v6 flagship vs v6-wild vs v6-mini: do they differ in how strictly they honor these tags?

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

- `core/methodology/suno-optimization.md` is the **v5.5-era** reference (still valid for v5.5 renders).
- This doc + `references/V6_TAG_REFERENCE.md` are the **V6 working model**.
- For V6 songs: use the V6 tag reference and the division-of-labor rule (Style = WHAT, inline = HOW).
- v5.5-specific mechanics (Italian tempo preference, `[silence: sudden]` failure, named slider
  presets, tag-count sweet spot) are NOT assumed to carry into V6 — re-validate before relying on them.

---

*Living document. Update the results log as renders are evaluated. Style prompts that pair
with these tag structures are catalogued in `references/STYLE_LIBRARY.md`.*