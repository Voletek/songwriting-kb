---
inclusion: auto
description: Suno AI field limits, section tags, pipe notation, creative sliders, v5.5 features, era tags, parenthetical layers, formatting rules, and genre/style optimization principles.
---

# Suno AI Formatting Rules

> Auto-loaded. Quick-reference for Suno formatting. Full tag details in the suno-meta-tags skill.
> For comprehensive genre theory, key-emotion mapping, BPM ranges, and style optimization:
> see `references/SUNO_STYLE_GENRE_REFERENCE.md`

---

## Field Limits

| Field | Limit | Overflow To |
|---|---|---|
| Style of Music | 1000 chars | Exclude field (negatives only) |
| Lyrics | 5000 chars | Trim (no overflow — must fit) |
| Exclude | Dedicated field | Negative prompts / exclusions ONLY |

## Creative Sliders (UI — not text fields)

| Slider | Default | Our Songs | Effect |
|---|---|---|---|
| Weirdness | 50% | 50-55% | Creative latitude (Safe↔Chaos) |
| Style Influence | 50% | 50-60% | How much Style Prompt steers output |
| Audio Influence | ~45% | 45% (if Inspo) | How much reference track affects output |

## v5.5 Features (UI — not text tags)

- **Personas/Voices:** Lock a consistent vocal identity across all generations. Select from voice menu before generating. Use one Persona per album character.
- **Stems:** Extract up to 12 individual tracks (vocals, drums, bass, etc.) from renders. Use for DAW mixing/mastering and album-level consistency.
- **Custom Models:** Train Suno on your completed tracks to learn your sound. Pro/Premier only.

## Era Tags (in Style Prompt)

Era decade tags ("1980s", "1970s") now aggressively bias PRODUCTION style (recording technique, mix character), not just instruments. To get a retro instrument with modern production, be explicit: "modern production, vintage 1970s guitar tone" — separate the era from the mix.

## Style Prompt Formula

```
Genre, BPM, Mood, Instruments, Vocal Style, Era/Production, Direction
```

**7-Dimension Rule:** Every Style Prompt should specify all 7 dimensions for maximum control. Missing any dimension = Suno guesses (fills with statistical averages).

**Genre-First Principle:** Genre MUST be the first element — it anchors everything else.

**5-8 Tag Sweet Spot:** Comma-separated descriptors. Past 10 tags, signals conflict and Suno defaults to generic. Keep focused and non-contradictory.

**Era Anchoring:** Time references ("early 2000s garage rock") outperform genre labels ("indie rock") because they give Suno a specific sonic PERIOD, not just a category.

**70/30 Genre Combination:** One dominant genre (70%) + one flavor (30%). 50/50 splits confuse Suno. Use `+` to combine.

**Groove/Time-Feel (Optional 8th Dimension):** Add a groove descriptor (medium swing, four-on-the-floor, syncopated, etc.) for rhythmic specificity beyond BPM. [Tier 3]

**Artist Reference Conversion:** Never include artist names in the Style Prompt. Convert "in the style of X" to descriptive production language (genre + era + instruments + production characteristics + vocal style + structural habits). No artist names in final output.

**Instrument Naming:** Describe instruments by their SOUND, not their model name. 'Squelching acid bass' > 'Roland TB-303'. Use minimum descriptors (~20 chars each) for tight budgets or compressed (~35 chars each) as default. Full vocabulary: `references/INSTRUMENT_SOUND_REFERENCE.md`

**Full genre/key/BPM/instrument reference:** `references/SUNO_STYLE_GENRE_REFERENCE.md`

## Essential Tags (Use in every song)

```
[track: genre: X, mood: X, length: 270]
[control: no-repeat, dynamic transitions]
[sequence: intro, verse, pre-chorus, chorus, ...]
```

Place at top of Lyrics field. Add `[end]` at bottom.

## Section Rules

- Tags on their OWN line — never same line as lyrics
- 4-8 lines per section maximum
- NO punctuation at end of lines
- Each line = one melodic phrase = one breath
- Target 7-12 syllables per line

## Pipe Notation (saves chars)

```
[chorus | powerful, wide, choir swell]
[verse | vulnerable vocals, close-mic, sparse]
```

## Duet Modes

- **Mode A:** `[Male Vocal]`/`[Female Vocal]` per line (complex)
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

**Key rule:** Named layers (`X layer: text`) require the Style Prompt to declare: e.g., "low-register AI voice layered during system sections." Without this, Suno may just sing parenthetical content normally.

**Performance Notation:** Inline symbols (~, -, ALL CAPS, ..., quotes) affect vocal delivery inside lyrics. See `references/SUNO_TAGS_REFERENCE.md` -> Performance Notation.

**Full reference:** `references/SUNO_TAGS_REFERENCE.md` → "Parenthetical Layers" section.

## Exclusions Format

**Important:** The `[Exclusions:]` content below goes in Suno's dedicated **Exclude** field in the UI — NOT inside the Lyrics text box.

```
‑trap drums, ‑beatboxing, ‑vocal hums, ‑bright synths
```

## Output Template (Every Song)

Always include: Style Prompt + Exclusions + Title tag + Production Direction + Vocal Direction + Lyrics with section tags + Production Notes block (Key, Tempo, Time Sig, Chords Nashville+actual, Vocal, Instruments, Dynamics, Hook Type, Rhyme Scheme, Emotional Arc)

## Genre & Style Optimization

When writing or revising songs, evaluate Style Prompt choices against the emotional content:

- **Key is the #1 emotional cue** (Eerola, Friberg & Bresin, 2013) — choose key for emotional character, not just instrument convenience
- **BPM serves two masters** — must satisfy genre convention AND emotional pacing
- **Instruments carry cultural meaning** (Tagg) — piano ≠ guitar ≠ synth even playing the same notes
- **Section tags = per-section musemic signification** — each tag should carry the correct connotation for THAT section's content

The Critic agent's Suno Optimization Assessment evaluates all of this. Full methodology: `references/SUNO_STYLE_GENRE_REFERENCE.md`

**Probabilistic Rendering:** Tags shape probability -- they do not guarantee outcomes. Generate 3-4 versions of each song and select the best render. [Tier 3]
