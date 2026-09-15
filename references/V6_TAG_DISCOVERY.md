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

## V6 Technique Inventory

> **Purpose: lose nothing.** This is a capture-everything-first catalog of every distinct
> tagging technique observed across the shipped Suno V6 tagged-lyric examples. It is deliberately
> additive: it records WHICH techniques exist BEFORE the `Canonical V6 Tag Grammar` section below
> normalizes HOW they are written. Normalizing standardizes the notation; it never removes a
> technique. Every technique here remains expressible in the canonical grammar (the canonical
> section demonstrates that).
>
> Each entry gives: a name, a one-line description, a minimal concrete bracket example, and a
> **mode label**, either **Default/Roots** (folk, blues, mountain-gothic) or
> **MODE C (Cinematic/Theatrical/Concept)** for concept-album/cinematic material. Techniques are
> split into **COMMON** (the load-bearing spine, present across all/most examples) and **RARE**
> (present in only one or a few examples, most at risk of being lost in cleanup).

### COMMON techniques (the load-bearing spine, shared by both modes)

These six appear across all or most examples and form the spine that Default/Roots and MODE C both build on.

1. **Full 13-part structural arc**: the same long-form section order recurs identically across
   every example. Mode: **shared spine.**
   Order: Intro -> Verse -> Pre-Chorus -> Chorus -> Post-Chorus -> (Verse) -> Bridge -> Breakdown
   -> Build -> Drop -> Instrumental Solo -> Interlude -> Key Change -> Final Chorus -> Outro.
   ```
   [Intro] ... [Verse 1] ... [Pre-Chorus] ... [Chorus] ... [Post-Chorus] ...
   [Bridge] ... [Breakdown] ... [Build] ... [Drop] ... [Instrumental Solo] ...
   [Interlude] ... [Key Change] ... [Final Chorus] ... [Outro]
   ```

2. **Instrument entrance/exit choreography**: bring instruments In and Out on cue (the confirmed
   marquee V6 capability). Mode: **shared spine.**
   ```
   [Instrument: Banjo In]
   [Instrument: Drums Out]
   ```

3. **Dynamics as an explicit arc**: plot loudness across the song, using both classical markings
   (pp -> ff) and named moves (Crescendo/Swell/Drop): pp/hush -> crescendo -> full/ff -> drop ->
   fade. Mode: **shared spine.**
   ```
   [Dynamic: pp] ... [Dynamic: Crescendo] ... [Dynamic: Full] ... [Dynamic: Drop] ... [Dynamic: Fade Out]
   ```

4. **Call-and-response with the response on its own line**: the answering line lives on a separate
   tagged line (or Male/Female alternation). Mode: **shared spine.**
   ```
   [Call] Higher!
   [Response] Higher!
   ```

5. **Verse-1 -> Outro lyrical bookend**: reprise the opening image at the end to close the loop.
   Mode: **shared spine.**
   ```
   [Verse 1] The porch light still burns
   [Outro] The porch light, burning still
   ```

6. **Stop-time / one-beat silence before the drop or final chorus**: a single beat of held silence
   as a lift into the payoff. Mode: **shared spine.**
   ```
   [Transition: Stop-Time]
   [Chorus]
   ```

### RARE techniques (at-risk, most must be actively preserved)

These are the fragile ones. They show up in only one or a few examples and are the easiest to lose
in a cleanup pass, so they are enumerated explicitly and kept expressible in the canonical grammar.

7. **Compound/bundled transition**: multiple simultaneous events packed into one transition tag.
   Mode: **shared spine (used by both, common in Default/Roots).**
   ```
   [Transition: Crescendo, Snare In, Synth Riser]
   ```

8. **Voice-as-instrument muting**: drop the lead vocal out on cue, treating the voice as an
   instrument you can exit. Mode: **shared spine.**
   ```
   [Instrument: Male Lead Out]
   [Vocal: Vocal Out]
   ```

9. **Call-and-response used as narrative reveal**: the response does not just echo; it accuses or
   answers the narrator, telling story THROUGH the tag structure (Haunted Chamber-Folk). Mode:
   **Default/Roots (mountain-gothic).**
   ```
   [Call] Who closed the window?
   [Response] You did
   ```

10. **AI-voice-as-second-character**: a distinct AI/machine voice acts as a second character in the
    narrative, not a harmony (Fractured Shadows). Must NOT be flattened into generic harmony.
    Mode: **MODE C.**
    ```
    [Response: low-register AI voice]
    [Low AI Voice: Compliance is a form of memory.]
    ```

11. **Progressive signal/glitch degradation**: a glitch/degradation parameter escalates over the
    course of the song (time-based automation, cyber material). Mode: **MODE C.**
    ```
    [glitch-density: low -> medium -> high]
    [Transition: Glitch Cut]
    ```

12. **Spoken-word surveillance interludes**: a clinical, telephone-filtered, calm-but-invasive
    whispered second voice delivered as an interlude; a whole delivery mode (Fractured Shadows
    03/04). Mode: **MODE C.**
    ```
    [Interlude: spoken word, telephone-filtered]
    [Second Voice: calm, invasive whisper] This call is being recorded for your safety.
    ```

13. **BPM change mid-song**: an actual tempo modulation named in numbers (distinct from a
    half-time feel). Mode: **shared spine (payoff device).**
    ```
    [Tempo Change: 72 to 60 BPM]
    [accelerando: 78 to 82 BPM]
    ```

14. **Panning / spatial cues**: stereo-field direction for a part or ad-lib. Mode:
    **shared spine (common in MODE C).**
    ```
    (whispered thoughts) panning left-to-right
    [whispered ad-lib, panned right]
    ```
    Canonical spelling: `[Vocal: Whispered ad-lib, panned right]` (see the demonstration table
    in the Canonical V6 Tag Grammar section); the raw forms above are captured as observed.

15. **Key change with the specific modulation named**: the exact interval is stated because it
    carries meaning; reserved for emotional payoffs. Mode: **shared spine (payoff device).**
    ```
    [Key Change: A minor -> C major]   (relative-major comeback)
    [Key Change: D minor -> E-flat minor]   (up-a-semitone unease)
    [Key Change: Fm -> Ab]
    ```

16. **Em-dash for breath/phrasing within a line**, a micro-level delivery mark placed inside a
    lyric line to force a breath/phrasing pause; easily destroyed by punctuation cleanup, so it is
    called out explicitly. Mode: **shared spine (common in MODE C).**
    ```
    Another night — another screen glow
    ```

### Observations (recorded, NOT endorsed as practice)

The examples are inconsistent and contain artifacts. These are logged so nothing is silently lost,
but they are described, not recommended. The `Canonical V6 Tag Grammar` section resolves them.

**Six inconsistent tag grammars for the same concepts were observed:**

- (a) **Namespaced**: `[Instrument: Banjo In]`
- (b) **Bare**: `[Banjo In]`
- (c) **Verbose**: `[Instrument Entrance: Banjo, enters on final two lines]`
- (d) **Compact-pipe vocabulary**: `[VOCABULARY:INSTRUMENTS=piano|cello|banjo|...]`
- (e) **Per-line-prefixed**: `[VERSE 1][GUITAR:ENTER]` repeated on every single line
- (f) **ALL-CAPS**: `[STRUCTURE:VERSE]`

**Two artifacts flagged:**

- **Over-tagging**: several examples pile 15-25 tags onto a 4-line verse, and some lines are
  all tags with no lyric at all. This is noise, not control.
- **Full-song duplication**: examples #4, #5, and #6 contain the ENTIRE song pasted twice. This is
  a copy/paste artifact, not an intentional double-length structure.

---

## Canonical V6 Tag Grammar

> **This is the ONE recommended way to write V6 tags.** It is grounded in the CONFIRMED FINDINGS
> above and in the best shipped song, *From the Floor to the Fire*. It standardizes HOW techniques
> are written; it does not remove any technique from the inventory above. Every technique 1-16
> remains expressible here (see the demonstration below).

### The five canonical rules

1. **Light-namespaced event tags.** Write events as `[Category: Value]`:
   `[Instrument: Banjo In]`, `[Vocal: Belt]`, `[Dynamic: Crescendo]`, `[Transition: Riser]`.
   Prefer this over bare, ALL-CAPS, or pipe forms.

2. **`[Role, inline-adjective]` is a first-class delivery form.** For vocal delivery, put the role
   and the adjective in one tag: `[Female response, rising]`, `[Male lead, tender then stronger]`,
   `[Second voice, calm invasive whisper]`. This is recommended, not a fallback.

3. **NO `[Tag Vocabulary]` block in final output.** Confirmed: it is not sung and not needed.
   Use it, if at all, only as private planning scaffolding, never ship it.

4. **2-4 tags per SECTION, not per line.** Tag the entrance/dynamic/delivery at the top of a
   section; do not prefix every lyric line. This kills the over-tagging artifact.

5. **No bar-level micro-tags in the lyrics field.** Directions like "enters on final two lines" or
   "sixteen-bar solo" belong in Production Notes, not inline in the lyrics. Keep the lyrics field
   about identity-of-the-moment, not bar math.

### Every Part-1 technique stays expressible (demonstration)

Normalizing the grammar does NOT drop any technique. Here is each inventory technique in canonical form:

| # | Technique | Canonical form |
|---|---|---|
| 1 | 13-part structural arc | `[Intro]` `[Verse 1]` `[Pre-Chorus]` `[Chorus]` ... `[Final Chorus]` `[Outro]` (section tags only) |
| 2 | Instrument entrance/exit | `[Instrument: Banjo In]` / `[Instrument: Drums Out]` |
| 3 | Dynamics arc | `[Dynamic: pp]` -> `[Dynamic: Crescendo]` -> `[Dynamic: Full]` -> `[Dynamic: Drop]` -> `[Dynamic: Fade Out]` |
| 4 | Call-and-response | `[Call]` line / `[Response]` line |
| 5 | Verse-1 -> Outro bookend | reprise the opening image under `[Outro]` (no special tag needed) |
| 6 | Stop-time before drop | `[Transition: Stop-Time]` above the section |
| 7 | Compound transition | `[Transition: Crescendo, Snare In, Synth Riser]` |
| 8 | Voice-as-instrument muting | `[Instrument: Male Lead Out]` / `[Vocal: Vocal Out]` |
| 9 | Call-and-response as narrative reveal | `[Call]` / `[Response]` with story content on the response line |
| 10 | AI-voice-as-second-character | `[Response, low-register AI voice]` delivery tag (MODE C) |
| 11 | Progressive glitch degradation | `[FX: Glitch, escalating]` inline; escalation curve in Production Notes (MODE C) |
| 12 | Spoken-word surveillance interlude | `[Interlude]` + `[Second voice, calm invasive whisper, telephone-filtered]` (MODE C) |
| 13 | BPM change mid-song | `[Tempo: 72 to 60 BPM]` (numeric, distinct from `[Feel: Half-Time]`) |
| 14 | Panning / spatial cue | `[Vocal: Whispered ad-lib, panned right]` |
| 15 | Named key-change modulation | `[Key Change: A minor to C major]` (name the interval; reserve for payoffs) |
| 16 | Em-dash breath within a line | keep the literal dash inside the lyric line: `Another night — another screen glow` |

Two clarifications so nothing is lost in translation: technique **13** stays numeric (`[Tempo: ... BPM]`)
and is deliberately kept distinct from the `[Feel: Half-Time]` perception shift; technique **16** keeps
its literal in-line dash. It is the one place an em-dash belongs, because the technique itself is about
the dash.

### Grammar migration table

Map each observed dialect (a-f from the observations above) to the canonical form:

| Observed dialect | Example | Canonical form |
|---|---|---|
| (a) Namespaced | `[Instrument: Banjo In]` | `[Instrument: Banjo In]` (already canonical) |
| (b) Bare | `[Banjo In]` | `[Instrument: Banjo In]` |
| (c) Verbose | `[Instrument Entrance: Banjo, enters on final two lines]` | `[Instrument: Banjo In]` + move "final two lines" to Production Notes |
| (d) Compact-pipe vocabulary | `[VOCABULARY:INSTRUMENTS=piano\|cello\|banjo\|...]` | delete from output (no `[Tag Vocabulary]` block); use per-section event tags |
| (e) Per-line-prefixed | `[VERSE 1][GUITAR:ENTER]` on every line | one `[Verse 1]` + one `[Instrument: Guitar In]` at the section top |
| (f) ALL-CAPS | `[STRUCTURE:VERSE]` | `[Verse]` |

---

## Labeled Modes (Default/Roots vs. MODE C)

> Mode-specific techniques are grouped under an explicit mode rather than merged into one default.
> **Both modes share the common spine (Technique Inventory items 1-6);** they diverge only in their
> mode-specific tools. Naming the mode keeps a MODE C device (an AI second voice) from being
> flattened into a Default/Roots reading (a harmony vocal).

### Default/Roots mode (folk, blues, mountain-gothic)

- **Spine:** all six COMMON techniques (items 1-6).
- **Mode-leaning techniques:** call-and-response as narrative reveal (#9, mountain-gothic accusation),
  compound acoustic transitions (#7), named relative-major key changes as emotional payoff (#15),
  bookends (#5), stop-time lifts (#6).
- **Voice:** human lead(s), harmony, gang vocal, spoken word used as a roots device.

### MODE C (Cinematic/Theatrical/Concept): concept-album / cinematic material

- **Spine:** the same six COMMON techniques (items 1-6). MODE C is the spine PLUS its own tools.
- **Mode-specific techniques (expected here, NOT in the folk default):**
  - **AI-voice-as-second-character (#10)**: a machine voice as a narrative character, never a harmony.
  - **Progressive glitch degradation (#11)**: an escalating glitch/degradation curve across the song.
  - **Spoken-word surveillance interludes (#12)**: clinical, telephone-filtered, calm-invasive whisper.
- **Commonly combined here:** panning/spatial cues (#14), em-dash breath phrasing (#16), and named
  up-a-semitone key changes (#15) for unease.

Both modes are written in the single `Canonical V6 Tag Grammar` above; the mode changes WHICH
techniques you reach for, not HOW you notate them.

---

## The Converged V6 Tag Format (early experiment / superseded)

> **Historical note, kept for provenance.** This passage records an EARLY experimental format from
> the first test attempts. Part 1 of it (the `[Tag Vocabulary]` declaration block) is **NOT
> recommended for final output**. It is not sung and not needed (see CONFIRMED FINDINGS #1 and the
> RESULTS LOG). For the current recommendation, use the **`Canonical V6 Tag Grammar`** section above.
> The rest of this passage (directional tags, compound transitions, inline delivery, call/response)
> is preserved by the canonical grammar.

Across multiple experiments, this early format read as a **text-based arrangement score**. It had
five parts:

### 1. A Tag Vocabulary declaration block (at the top), EARLY EXPERIMENT, NOT RECOMMENDED
Declared the full palette before the song, to teach the model the vocabulary. It was observed in
several early renders but is **not recommended for final output**, it does not get sung and is not
needed. **Drop it** and use per-section event tags from the canonical grammar instead. The two
syntaxes below are recorded only to document what was tried:

```
[Tag Vocabulary]
[Structure: Intro] [Structure: Verse] ...
[Instrument: Banjo In] [Instrument: Banjo Out] ...
[Dynamic: Crescendo] [Dynamic: Diminuendo] ...
[Feel: Half-Time] [Feel: Double-Time] ...
[Vocal: Male Lead] [Vocal: Female Counter] ...
[Transition: Riser] [Transition: Stop-Time] ...
```

or the compact pipe form (this is dialect (d) in the observations, do not ship it):

```
[VOCABULARY:STRUCTURE=intro|verse|pre-chorus|chorus|...]
[VOCABULARY:INSTRUMENTS=piano|cello|banjo|...]
[VOCABULARY:DYNAMICS=pp|p|mp|mf|f|ff|crescendo|...]
[VOCABULARY:VOCALS=male-whisper|male-belt|female-answer|...]
```

### 2. Directional instrument tags (the biggest V6 evolution)
Control instrument entrance AND exit, real arrangement, not just "add cello":
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
| 3 | `[Tag Vocabulary]` block + inline categorized flow tags | The taxonomy-declaration idea emerges, later dropped (block is not sung; see CONFIRMED FINDINGS #1) |
| 4-6 | Refined: vocabulary header + `[Instrument: X In/Out]` + classical dynamics + `[Feel:]` + Entrance/Exit transitions | The converged "best" format. Full arrangement-score control. |
| now | **`Canonical V6 Tag Grammar`** (light-namespaced event tags, `[Role, inline-adjective]` delivery, 2-4 tags/section, no vocabulary block) | Current recommendation; supersedes the vocabulary-header approach |

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
| Voice-as-instrument muting (`[Vocal: Vocal Out]`) | ? untested | Technique #8, drop the lead on cue |
| AI-voice-as-second-character | ? untested | Technique #10, MODE C narrative device; verify it reads as a distinct voice, not a harmony |
| Progressive glitch degradation | ? untested | Technique #11, MODE C escalating curve; may need Production Notes rather than one tag |
| Spoken-word surveillance interlude | ? untested | Technique #12, MODE C; telephone-filtered calm-invasive whisper |
| Numeric BPM change (`[Tempo: X to Y BPM]`) | ? untested | Technique #13, distinct from `[Feel: Half-Time]` |
| Panning / spatial cue | ? untested | Technique #14, stereo-field direction for a part/ad-lib |
| Named key-change modulation | ? untested | Technique #15, does the specific interval read, or only the fact of a change? |
| Em-dash breath within a line | ? untested | Technique #16, does the in-line dash produce a phrasing pause? |

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
6. Do the MODE C devices (AI second voice #10, glitch degradation #11, surveillance interlude #12) read as intended, or collapse into harmony/FX?
7. Does a named key-change interval (#15) actually modulate to that interval, or just "change key"?
8. Is progressive glitch degradation (#11) better expressed as one escalating tag or as Production-Notes automation?
9. Does the in-line em-dash (#16) survive rendering as a breath, or get normalized away?

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