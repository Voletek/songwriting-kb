---
inclusion: always
description: "Suno V6 formatting rules (default) — Style field = WHAT, Lyrics field = HOW, [Instrument: X In/Out] choreography, dynamics/vocal/transition tags, [End] terminator, field limits, Exclude-field format, style prompt formula, genre-first, artist/gear conversion, section rules, duet modes, parenthetical layers, probabilistic rendering — plus clearly labelled legacy v5.5 mechanics."
---

# Suno AI Formatting Rules

> Always loaded (`inclusion: always`). Quick reference for Suno formatting — **V6 first**; legacy v5.5-era mechanics are collected at the end.
> V6 tag dictionary: `references/V6_TAG_REFERENCE.md` · How/why + results log: `references/V6_TAG_DISCOVERY.md`
> Full procedure: `core/methodology/suno-optimization.md` → V6 Procedure (default)
> Genre theory, key/mode-emotion mapping, BPM ranges: `references/SUNO_STYLE_GENRE_REFERENCE.md`
> Deterministic check: `python3 tools/validate-song.py <file>`

---

## ⚡ V6 Paradigm (default)

Suno V6 (v6 / v6-wild / v6-mini) is the current default. Status: working model (user-reported Sept 2026; per-tag evidence in the `references/V6_TAG_DISCOVERY.md` results log).

- **Style field = the WHAT:** genre, key, tempo, vocal identity, production aesthetic (sets the world)
- **Lyrics field = the HOW:** section tags + `[Instrument: X In]` / `[Instrument: X Out]` + dynamics + delivery + transitions (choreographs the performance)
- **Exclude field = negatives only** (see Exclusions below)

**V6 lyric-field format:**
- Section tags on their own line: `[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Final Chorus]`, `[Outro]`
- Instrument choreography: `[Instrument: Cello In]` … `[Instrument: Cello Out]`
- Dynamics: `[Dynamic: Crescendo]`, `[Dynamic: Full]`, `[Dynamic: Diminuendo]`, `[Dynamic: Fade Out]`
- Delivery: `[Vocal: Whisper]` / `[Vocal: Belt]` / `[Vocal: Spoken Word]`, or the role form `[Male lead, tender then stronger]`
- Transitions: `[Transition: Drum Fill]`, compound `[Transition: Crescendo, Snare In, Synth Riser]`; key changes: `[Key Change: Up a whole step]` or `[Transition: Key Lift]`
- **2-4 tags per section** (not per line)
- End with `[End]`
- **Do NOT use:** a `[Tag Vocabulary]` block (planning aid only — not sung), v5.5 global tags (`[track:]` / `[control:]` / `[sequence:]`), or compact pipe notation `[Section | params]`

## Field Limits

| Field | Limit | Overflow To |
|---|---|---|
| Style of Music | 1000 chars | Exclude field (negatives only) |
| Lyrics | 5000 chars | Trim (no overflow — must fit) |
| Exclude | Dedicated field | Negative prompts / exclusions ONLY |

Limits carried over from v5.x. The Suno MCP enforces the same limits for V6 (`style` and `negative_style` ≤1000, `lyrics` ≤5000); whether the web UI changed them is still an open question in `references/V6_TAG_DISCOVERY.md`. Rendering through the MCP (field mapping, sliders, length caps): `references/SUNO_MCP_REFERENCE.md`.

## Style Prompt Formula (the WHAT)

```
Genre, Key, BPM, Mood, Instruments, Vocal Style, Era/Production, Space/Direction
```

**7-Dimension Rule:** Specify genre, tempo, mood, instruments, vocal, era/production, and space (plus key) for maximum control. Missing dimensions = Suno guesses (fills with statistical averages). [Tier 3]

**Genre-First Principle:** Genre MUST be the first element — it anchors everything else. [Tier 3]

**70/30 Genre Combination:** One dominant genre (70%) + one flavor (30%). 50/50 splits confuse Suno. Use `+` to combine. [Tier 3]

**Groove/Time-Feel (Optional 8th Dimension):** Add a groove descriptor (medium swing, four-on-the-floor, syncopated, etc.) for rhythmic specificity beyond BPM. [Tier 3]

**Artist Reference Conversion:** Never include artist names in the Style Prompt. Convert "in the style of X" to descriptive production language (genre + era + instruments + production characteristics + vocal style + structural habits). No artist names in final output.

**Instrument Naming:** Describe instruments by their SOUND, not their model name. 'Squelching acid bass' > 'Roland TB-303'. Generic category names (Rhodes, Hammond organ, Wurlitzer) are fine — Rhodes is in the V6 instrument list; brand-model gear (TB-303, TR-808, Juno-60, DX7, Telecaster, Marshall stack…) should be translated to sound descriptors. Use minimum descriptors (~20 chars each) for tight budgets or compressed (~35 chars each) as default. Full vocabulary: `references/INSTRUMENT_SOUND_REFERENCE.md`

## Section Rules

- Tags on their OWN line — never on the same line as lyrics
- Verses/choruses usually 4-8 lines (roughly 8-16 bars at ~2 bars per line); bridge 3-6 lines (up to 8 when the turn needs it)
- NO punctuation at end of lines (em-dashes for breath within a line are fine)
- Each line = one melodic phrase = one breath
- [Tier 2] Target 7-12 syllables per line; 13-15 = review stress density and singability at tempo; 16+ = apply the Compression Test

## Duet Modes

- **Mode A:** `[Male Vocal]`/`[Female Vocal]` per line (complex) — V6 role form: `[Male lead, ...]` / `[Female response, ...]`
- **Mode B:** Main + `()` response, declared in Style (efficient)
- **Mode C:** Custom layers + stacked tags (theatrical)

## Parenthetical Layers — `()` in Lyrics

Text in parentheses = secondary vocal layer. Suno treats it differently from main lyrics.

| Pattern | Effect | Style Prompt Needed? |
|---|---|---|
| `(whispered) text` | Delivery cue — whispers next text | Usually works alone |
| `(spoken) text` | Spoken not sung | Usually works alone |
| `(robotic layer: text)` | Named secondary voice (AI/machine) | **YES** — must declare |
| `(echo layer: text)` | Delayed/echo treatment | **YES** — must declare |
| `(whisper layer: text)` | Background whisper texture | **YES** — must declare |
| `(response text)` | Backup vocal / duet response | Best with declaration |

**Key rule:** Named layers (`X layer: text`) require the Style Prompt to declare them: e.g., "low-register AI voice layered during system sections." Without this, Suno may just sing parenthetical content normally. When using layers, add `vocal overlap confusion` to the Exclude field.

**Full reference:** `references/SUNO_TAGS_REFERENCE.md` → "Parenthetical Layers" section.

## Exclusions Format (Exclude field)

Exclusions go in Suno's dedicated **Exclude** field — NOT inside the Style or Lyrics text boxes. Plain comma-separated text, **no dash prefix** (neither `-` nor `‑`):

```
trap drums, beatboxing, vocal hums, bright synths
```

In song files, put them under an `## EXCLUSIONS:` section (preferred). A legacy `[Exclusions: ...]` line inside the Style section is still parsed by the validator and never counted toward Style chars. Dash-prefixed negatives were a v5.5-era technique for negation INSIDE the Style field — don't use them in the Exclude field.

## Output Template (Every Song — V6)

```
## STYLE PROMPT:
Genre (first), key, BPM, mood, instruments as sound descriptors, vocal identity, production aesthetic, space   (≤1000 chars)

## EXCLUSIONS:
trap drums, beatboxing, vocal hums, bright synths

## LYRICS:
[Title: Song Title]
[Production Direction: overall tone, dynamics arc, what to avoid]
[Vocal Direction: voice type, delivery, emotional progression]

[Intro]
[Instrument: Acoustic Guitar In]
[Dynamic: Soft]

[Verse 1]
[Vocal: Male Lead]
...lyrics...

[Chorus]
[Instrument: Drums In]
[Dynamic: Full]
...lyrics...

[Bridge]
[Instrument: Drums Out]
[Dynamic: Diminuendo]
...lyrics...

[Outro]
[Dynamic: Fade Out]
[End]
                                                       (≤5000 chars)
## PRODUCTION NOTES
Key, Tempo, Time Sig, Chords (Nashville + actual), Vocal, Instruments, Dynamics,
Hook Type, Rhyme Scheme, Emotional Arc
```

Format conventions for the Production Notes block: `output-preferences.md`.

## Genre & Style Optimization

When writing or revising songs, evaluate Style Prompt choices against the emotional content:

- **Mode is the strongest overall cue** — in Eerola, Friberg & Bresin (2013, perceived emotion with manipulated cues), mode contributed most overall; tempo mattered most for arousal. Specific key "characters" are historical tradition (Schubart), not psychology — real key effects come from vocal tessitura, instrument resonance, and mode
- **BPM serves two masters** — must satisfy genre convention AND emotional pacing
- **Instruments carry cultural meaning** (Tagg) — piano ≠ guitar ≠ synth even playing the same notes
- **Section tags = per-section musemic signification** — each tag should carry the correct connotation for THAT section's content

The Critic agent's Suno Optimization Assessment evaluates all of this. Full methodology: `references/SUNO_STYLE_GENRE_REFERENCE.md`

**Probabilistic Rendering:** Tags shape probability — they do not guarantee outcomes. Generate 3-4 versions of each song and select the best render. [Tier 3]

---

## V6 Controls & Features (suno.com UI and Suno MCP)

These are current V6 features, in the suno.com UI and through the Suno MCP (field names and costs:
`references/SUNO_MCP_REFERENCE.md`). Slider *values* are v5.5-era starting points [Tier 3]; re-validate on V6.

| Control | MCP field | What it does | Starting point |
|---|---|---|---|
| Weirdness | `controls.weirdness` (0–1) | Creative latitude (safe ↔ chaos) | 0.50–0.55 |
| Style Influence | `controls.style_influence` (0–1) | How strictly the Style Prompt steers | 0.50–0.60 (later v5.5 tests favoured 0.70–0.90) |
| Audio Influence | `controls.audio_influence` (0–1) | With a voice: closeness to that voice. In covers, extensions and mashups: closeness to the source audio | 0.45 |
| Variety | `controls.variety` (0–4) | How far the style tags are reinterpreted: Off / Normal / High / Extra / Max | Untested: leave at the default |
| Max Mode | `max_mode` | More compute for consistency, at a multiple of the credits | Only when the user asks for it |
| Model | `model` | `v6`, `v6-wild`, `v6-mini` | `v6`; name the model you use in the render log |

UI percentages map to MCP fractions: 60% = `0.6`. Record every non-default value in the song's `## RENDERS` log.

- **Voices** (v5.5 called them Personas): lock a vocal identity across generations (`voice_id`, from `voices-list`). One voice per album character.
- **Stems:** `two` (vocals + instrumental) or `twelve` parts, for Studio or DAW mixing and the stem-targeted plugins in `plugins/`.
- **Section edits and extensions:** redo one section of a finished song, or continue past the 6:00 cap. See SOP 10 (`.kiro/sops/10-rendering-through-the-suno-mcp.md`).
- **Custom Models / My Taste:** v5.5-era UI features, not exposed through the MCP. Check the UI before relying on them.

---

## Legacy v5.5-era mechanics (re-validate on V6)

> Everything in this section is **v5.5-era (legacy) — re-validate on V6**. Use it for v5.5 renders, or as starting points to test on V6. Do not present it as a current rule.

**Terminator:** v5.5 used lowercase `[end]`; V6 uses `[End]`. The validator accepts both.

**Global tags (v5.5 "Essential Tags")** — top of the Lyrics field, v5.5 renders only:
```
[track: genre: X, mood: X, length: 270]
[control: no-repeat, dynamic transitions]
[sequence: intro, verse, pre-chorus, chorus, ...]
```

**Compact pipe notation (saves chars on v5.5):**
```
[chorus | powerful, wide, choir swell]
[verse | vulnerable vocals, close-mic, sparse]
```
V6 canonical grammar replaces this with separate namespaced tags (see `references/V6_TAG_DISCOVERY.md` → Grammar migration table).

**5-8 tag sweet spot (Style Prompt):** v5.5-era community heuristic — past ~10 comma-separated descriptors, signals conflicted and output went generic. [Tier 3]

**Era tags (Style Prompt):** On v5.5, decade tags ("1980s", "1970s") biased PRODUCTION style (recording technique, mix character), not just instruments. To get a retro instrument with modern production: "modern production, vintage 1970s guitar tone" — separate the era from the mix. Era anchoring ("early 2000s garage rock") was observed to beat bare genre labels. [Tier 3]

**Italian tempo markings** (`Adagio`, `[Tempo: Andante]`) were preferred over raw BPM on v5.5. [Tier 3]

**`[silence: sudden]`** was unreliable on v5.5 — use a blank line or strip instrumentation instead. V6 dictionary has `[Dynamic: Silence]` / `[Transition: Hard Cut]` (log results).

**Performance notation:** On v5.5, only ALL CAPS reliably changed inline delivery (louder/more forceful); `~`, mid-word `-`, quotes, and ellipsis were unreliable. See `references/SUNO_TAGS_REFERENCE.md` → Performance Notation Symbols. On V6, use `[Vocal: ...]` / `[Dynamic: ...]` tags for delivery changes.
