# The Suno Optimization Method

> **CANONICAL METHODOLOGY** -- This file is the single source of truth for Suno AI optimization.
> A non-Kiro user can read ONLY this file and prepare any song for optimal Suno rendering.
> For the complete tag catalog, see `references/SUNO_TAGS_REFERENCE.md`.
> For genre/key/BPM tables, see `references/SUNO_STYLE_GENRE_REFERENCE.md`.

---

## Overview

Suno optimization is the FINAL technical pass before rendering. It does NOT change creative content -- it adds technical formatting that ensures Suno produces the best possible output. If the song was written with the full songwriting procedure (which includes formatting), this SOP functions as a verification pass.

---

## Three-Tier Evidence Labeling System

Claims in this methodology carry one of three evidence tiers:

| Label | Meaning |
|---|---|
| **[Tier 1: Scholarship-backed]** | Documented academic framework with primary sources and peer-reviewed research. |
| **[Tier 2: Professional heuristic]** | Widely-used craft guidance supported by professional practice but not empirically validated as universal law. |
| **[Tier 3: Community/platform heuristic]** | Empirical observation from practitioner testing (e.g., Suno community experiments). Unverified, version-dependent. |

Unlabeled claims are general craft consensus or structural descriptions that do not require tiering.

> **Note:** Most Suno-specific claims in this document are Tier 3 unless otherwise noted. Suno's behavior changes across versions; verify against the version you are using.

---

## The Complete 13-Step Optimization Procedure

### Step 1 -- Character Count Audit

**Measure Style Prompt:**
- Copy the full genre/BPM/mood description
- Count characters (must be <=1000)
- If over: move negatives/exclusions to Exclude field first, then trim least essential descriptors

**Measure Lyrics Field:**
- Count from `[track:]` through `[end]` (including ALL tags, direction blocks, section tags)
- Must be <=5000 characters
- If over: trim direction blocks first, reduce section production tags, shorten outro
- If still over: overflow additional direction to Suno's Advanced Settings box

**Record counts:**
```
Style: ___/1000 chars
Lyrics: ___/5000 chars
```

### Step 2 -- Add Global Control Tags

If missing, add at the TOP of Lyrics field (before first section):

```
[track: genre: [your genre], mood: [your mood], length: [seconds]]
[control: no-repeat, dynamic transitions]
[sequence: [list all sections in order]]
```

**Length calculation:** (total lyric lines x 2.5) + intro/outro bars x (60/BPM x 4). Round to nearest 15 seconds.

**Sequence:** List EVERY section tag that appears, in order:
```
[sequence: intro, verse, pre-chorus, chorus, verse, pre-chorus, chorus, bridge, final chorus, outro]
```

### Step 3 -- Validate Control Parameters

Only these `[control:]` values are confirmed valid (tested v4.5/v5.0):
- `no-repeat` -- prevents auto-looping
- `dynamic transitions` -- enables section contrast
- `instrumental` -- removes vocals entirely

**Invalid (remove if present):** `build across sections`, custom phrases, unconfirmed terms.

### Step 4 -- Optimize Section Tags

**Convert stacked tags (>3 per section) to pipe notation:**

```
BEFORE (too many stacked):
[Heavy drums]
[Distorted bass]
[Staccato guitar]
[Cave reverb]

AFTER (pipe notation):
[chorus | powerful, heavy drums, distorted bass, cave reverb]
```

**Valid pipe parameters:**
- Adjectives/descriptors: powerful, intimate, wide, dark, stripped, rising, sparse, full, layered, driving
- Vocal delivery: vulnerable vocals, close-mic, whispered, spoken

**Invalid pipe parameters (move elsewhere):**
- Instrument instructions: "cello enters low", "drums enter soft"
- Custom phrases: "maximum width", "build across sections"

**Practical limit:** 2-4 pipe parameters per section tag. Beyond 5, Suno may deprioritize later descriptors.

### Step 5 -- Add Vocal Delivery Tags

Per-section vocal tags SUPPLEMENT the global Vocal Direction block -- they specify WHERE a delivery change happens.

| Section Character | Tag to Add |
|---|---|
| Confessional/grief/intimate | `[vulnerable vocals]` in pipe or standalone |
| Lead vocal whispered | `[whisper]` before the line |
| Background whisper atmosphere | `[whispering]` as texture tag |
| Spoken/non-sung | `[spoken word]` or `[narrator]` |
| Repeated hook/mantra | `[chant]` |
| Dialogue/call-response | `[call-and-response]` |

### Step 6 -- Add Dynamics Tags

Dynamics can be standalone tags or pipe parameters:

| Moment | Standalone Tag | Pipe Alternative |
|---|---|---|
| Pre-chorus building | `[build]` | `[pre-chorus | building, rising tension]` |
| Dramatic silence | `[silence: sudden]` | N/A (mid-section event) |
| Key change | `[modulation: ascending]` or `[modulation: sudden]` | N/A |
| Volume increasing | `[crescendo]` | `[section | swelling, crescendo]` |
| Volume decreasing | `[diminuendo]` | `[section | fading, pulling back]` |
| Rhythm change | `[beat-switch: half-time]` | N/A |
| Grand ending | `[big finish]` | `[final chorus | powerful, big finish]` |
| Held note | `[fermata]` | N/A |

Use standalone tags for mid-section dynamic events. Use pipe parameters when the dynamic applies to the entire section.

### Step 7 -- Add Termination

At the very bottom of lyrics:
```
[end]
```

If the song should fade rather than cut:
```
[fade: layered]
[end]
```

### Step 8 -- Check for Obsolete Tags

Scan for and REMOVE any of these:

| Obsolete Tag | Action |
|---|---|
| `[bpm: X]` | Put BPM in Style Prompt text |
| `[key: X]` | Put key in Style Prompt text |
| `[loop]` | Remove entirely (unsupported) |
| `[autotune]` | Remove (deprecated) |
| `[mix]` / `[master]` | Remove (ineffective) |
| `[volume]` | Use dynamics tags instead |
| `[filter]` | Describe in Production Direction |
| `[section: X]` | Use specific section names |

### Step 9 -- Artist Reference Conversion

If any artist or band name appears in the Style Prompt, Production Direction, or Vocal Direction as creative shorthand (e.g., "in the style of Radiohead", "Billie Eilish vibes"), convert it to descriptive production language BEFORE final output. Artist names are not recognized as Suno prompt parameters -- descriptive language gives Suno actionable production instructions.

**Conversion method:** Translate the artist's SOUND into: genre + era + instruments + production characteristics + vocal style + structural habits. The artist name should NOT survive into the Style Prompt or Production Direction.

| Artist Reference | Converted To |
|---|---|
| "In the style of Radiohead" | "Atmospheric post-rock, electronic textures, unconventional structures, falsetto vocals, quiet-loud dynamics, 2000s experimental production" |
| "Like Billie Eilish" | "Dark minimal pop, whispered close-mic vocals, heavy sub bass, sparse production, intimate bedroom aesthetic, 2019 lo-fi pop" |
| "Wardruna vibes" | "Nordic folk, ancient instrumentation, throat singing textures, ritualistic percussion, vast reverb, pre-Christian atmosphere" |
| "Sigur Ros feel" | "Ethereal post-rock, bowed guitar, falsetto vocals as texture, glacial builds, Icelandic atmosphere, vast reverb spaces" |
| "Like Hozier" | "Dark folk-rock, rich baritone, gospel-influenced builds, literary lyrics, organic production, Celtic-soul fusion" |

**Why this matters:** Suno does not understand "make it sound like [Artist]." It DOES understand specific production descriptors, era references, genre combinations, and vocal delivery characteristics. Converting artist references to descriptive language produces dramatically better renders.

### Step 9b -- Gear Name Conversion [Tier 3]

If any gear or model name appears in the Style Prompt, Production Direction, or Vocal Direction (e.g., "TB-303", "Juno-106", "Telecaster"), convert it to a sound descriptor. Suno does not recognize equipment model numbers -- it responds to timbre descriptions.

**Conversion method:** Describe what the gear SOUNDS like using the compressed-level descriptors from `references/INSTRUMENT_SOUND_REFERENCE.md`. Optionally retain the gear name as a parenthetical suffix for future-proofing.

| Gear Reference | Converted To |
|---|---|
| "Roland TB-303 acid bassline" | "squelching resonant acid bass (TB-303)" |
| "Juno-106 pad" | "warm analog pad, lush detuned chorus (Juno)" |
| "Fender Rhodes" | "warm electric piano, soft bell-like attack (Rhodes)" |
| "Marshall stack" | "crunchy overdriven British tube amp" |
| "TR-808 drums" | "deep booming kick, crisp electronic snare" |

**Why this matters:** The same principle as Artist Reference Conversion -- Suno needs actionable sound descriptors, not brand names. Gear model numbers are meaningless to the model; timbre descriptions give it specific production targets.

**Evidence:** Confirmed for acid house (21machines, June 2026). Replication experiments pending for other genres.

**Character budget:** Use compressed-level descriptors (~35 chars each) as the default. Switch to minimum-level (~20 chars) when the Style Prompt is near 1000 characters.

### Step 10 -- Verify Suno Compatibility

Final checklist:
- [ ] No prohibited end punctuation on lyric lines (no periods, commas, semicolons, exclamation marks, question marks). Em-dashes are allowed for phrasing/breath. Apostrophes and hyphens are fine.
- [ ] Each line = one melodic phrase
- [ ] 4-8 lines per section maximum (instrumental sections with only a tag and no lyrics are valid)
- [ ] No lyrics on same line as tags
- [ ] Tags on their own line
- [ ] `[track:]` tag present with genre, mood, and length
- [ ] Production Direction block present
- [ ] Vocal Direction block present

### Step 11 -- Set Creative Sliders

Recommend slider values based on song type (see Named Slider Presets for tested combinations):

| Song Type | Weirdness | Style Influence | Audio Influence (if Inspo) | Closest Preset |
|---|---|---|---|---|
| Radio pop/rock | 30-40% | 70-80% | 40-50% | Prompt Drive |
| Concept album | 50-60% | 65-75% | 45% | Genre Rebuilder |
| Dark cinematic | 55-65% | 70-80% | 45-55% | Genre Rebuilder |
| Intimate ballad | 40-50% | 60-70% | 40-50% | Prompt Drive |
| Epic orchestral | 50-60% | 75-85% | 45-55% | Genre Rebuilder |
| Experimental | 65-80% | 80-90% | 15-30% | The Rebirth |
| Genre recreation | 25-35% | 85-95% | 50-60% | Identity Lock |

**Album consistency note:** Document slider values per track. If a render captures the intended palette, note settings as baseline for adjacent tracks. Use the Named Presets as starting points — fine-tune from there.

### Step 12 -- Prepare Exclude Field Content

Format exclusions for the dedicated Exclude field:
```
distortion, electric guitar, synthesizers, trap drums, beatboxing, vocal hums
```

**Format note:** In the dedicated Exclude field, list items as plain comma-separated text -- no dash prefix needed (the field implies exclusion). The dash-prefix format (`-item`) is only needed when placing exclusions WITHIN the Style Prompt field.

### Step 13 -- Final Output

Document the optimized version:
```
## SUNO-OPTIMIZED VERSION

### Changes Made:
- [list of specific additions/changes]
- (If no changes: "Verification pass -- all checks passed, no changes needed")

### Character Counts:
- Style: XXX/1000
- Lyrics: XXXX/5000

### Slider Recommendations:
- Weirdness: XX%
- Style: XX%
- Audio: XX% (if applicable)

### Exclude Field:
[content for Exclude]

### [Full optimized song]
```

---

## The 7-Dimension Style Prompt Formula

Every Style Prompt should specify all 7 dimensions for maximum control:

```
Genre, BPM, Mood, Instruments, Vocal Style, Era/Production, Space/Direction
```

| # | Dimension | Purpose | Example |
|---|---|---|---|
| 1 | Genre | Cultural container (MUST be first) [Tier 3] | "Progressive dark folk" |
| 2 | BPM / Tempo | Tempo anchor (see Italian Markings below) | "92 BPM" or "Andante" |
| 3 | Mood | Emotional direction | "melancholic, haunting" |
| 4 | Instruments | Timbral palette | "acoustic guitar, cello, distant choir" |
| 5 | Vocal Style | Delivery character | "deep male baritone, intimate" |
| 6 | Era/Production | Sonic period | "early 2000s production warmth" |
| 7 | Space/Direction | Atmosphere | "wide reverb, cinematic" |

**Missing any dimension = Suno guesses (fills with statistical averages).**

**8th Dimension: Groove/Time-Feel (Optional):** For additional rhythmic specificity beyond BPM, add a groove descriptor (e.g., "medium swing", "four-on-the-floor", "syncopated", "laid-back shuffle"). Not required for every song, but useful when the groove character is essential to the feel. [Tier 3: Community heuristic] Credit: Omnisona (Suno AI God Mode Manual v3.0, March 2026)

---

## Italian Tempo Markings (Preferred Over Raw BPM)

> [Tier 3: Community heuristic — MasterofSFL testing, 2026]
> Credit: MasterofSFL (Suno community guide, 2026)

Italian tempo markings are MORE consistently recognized by Suno than raw BPM numbers. This is likely because GPT's training data includes extensive classical music references where these terms are standard vocabulary.

**Usage:** Place Italian marking in the Style Prompt AND/OR as a `[Tempo: Marking]` tag in the lyrics field for reinforcement. Use BOTH for maximum control.

**Method:** `[Tempo: Vivace]` in lyrics field OR "Vivace tempo" in Style Prompt (or both)

| Category | Marking | BPM Range | Description | Best For |
|---|---|---|---|---|
| Very Slow | Grave | 20-40 | Very slow, solemn | Funeral, ritual, dread |
| Very Slow | Largo | 40-60 | Broadly, slowly | Sacred, processional |
| Very Slow | Larghetto | 60-66 | Rather broadly | Dark ballad, ambient |
| Slow | Lento | 45-60 | Slowly | Atmospheric, grief |
| Slow | Adagio | 66-76 | Slowly, at ease | Intimate ballad, cinematic |
| Walking | Andante | 76-108 | At a walking pace | Standard ballad, folk |
| Moderate | Moderato | 108-120 | Moderately | Pop, alt-rock |
| Moderate | Allegretto | 112-120 | Moderately fast | Upbeat pop, light rock |
| Fast | Allegro | 120-168 | Fast, bright | Rock, punk, driving |
| Fast | Vivace | 140-176 | Lively and fast | High-energy, thrash |
| Very Fast | Presto | 168-200 | Very fast | Punk, speed metal |
| Very Fast | Prestissimo | 200+ | As fast as possible | Extreme metal |

**Tempo Adjustment Terms (also recognized):**

| Term | Effect | Use Case |
|---|---|---|
| Accelerando | Gradually speeding up | Building sections, pre-chorus |
| Ritardando | Gradually slowing down | Outros, emotional moments |
| Rubato | Flexible/expressive tempo | Bridges, intimate moments |
| Con moto | With motion, lively | Maintaining energy |
| Sostenuto | Sustained, implying slower | Emotional weight |
| Tempo primo | Return to first tempo | After a tempo change |

**Recommendation:** Use Italian marking in Style Prompt + BPM number in Production Notes (for human reference). In lyrics tags, prefer Italian: `[Tempo: Adagio]` over `[Tempo: 72 BPM]`.

---

## Percentage Genre Weighting

> [Tier 3: Community heuristic — MasterofSFL testing, 2026]

Style prompts respond to explicit percentage weightings for genre blending. This provides more precise control than the descriptive 70/30 approach alone.

**Syntax options (all valid):**

```
# Numeric percentage
Thrash Metal (80%), EDM (20%)

# Narrative percentage (PREFERRED — adds directional context)
80s Era Thrash Metal (80%), Influenced by 90s Era EDM (20%), EDM vibes are layered behind Thrash Metal Sound

# Descriptive (our existing approach — still works)
Thrash metal with EDM undertones
```

**When to use percentages:**
- Genre fusion where the RATIO matters (not just "primary + flavor")
- When you've tested and a 70/30 blend isn't producing the right balance
- When you want to specify WHERE the secondary genre appears ("layered behind," "in rhythm section only")

**Rules:**
- Total must = 100% (or Suno averages toward generic)
- The dominant genre's percentage determines which genre's STRUCTURE rules apply
- The subordinate genre provides TEXTURE, not structure
- 80/20 is minimum for clear dominance. Below 80, both genres fight for structure control

---

## Genre Combination Rules

- **Genre-First Principle:** Genre MUST be the first element -- it anchors everything else. [Tier 3: community practice, not official. v4.5+ allows conversational prompts.]
- **5-8 Tag Sweet Spot:** Comma-separated descriptors. Past 10 tags, signals conflict and Suno defaults to generic. [Tier 3: Suno v4.5+ docs encourage more descriptive prompting. Test by version.]
- **70/30 Rule (or Percentage Weighting):** One dominant genre (70-80%) + one flavor (20-30%). 50/50 splits confuse Suno. Can be expressed descriptively ("thrash metal with EDM undertones") or with explicit percentages ("Thrash Metal (80%), EDM (20%)"). See "Percentage Genre Weighting" section above for syntax details.
- **Anti-Pairs:** Certain genre combinations have near-zero compatibility -- Gregorian Chant+Trap, Classical Baroque+Lo-fi Bedroom Pop, Opera+Mumble Rap. These pairings pull vocal delivery or production aesthetic in directly opposing directions, producing averaged mush. Replace one genre or use a compatible alternative. (Note: shared modifiers like "dark cinematic rock" are compound genres, not anti-pairs.) [Tier 3: Community heuristic] Credit: Omnisona (Suno AI God Mode Manual v3.0, March 2026)
- **Era Anchoring:** Time references ("early 2000s garage rock") outperform genre labels ("indie rock") because they give Suno a specific sonic PERIOD. [Tier 3: promising but not A/B tested.]
- **The Separation Principle:** Era tags aggressively bias PRODUCTION style (recording technique, mix character). To get a retro instrument with modern production: "modern production, vintage 1970s guitar tone" -- separate the era from the mix

---

## Parenthetical Layers System

Text in parentheses = secondary vocal layer. Suno treats it differently from main lyrics.

| Pattern | Effect | Style Prompt Declaration Needed? |
|---|---|---|
| `(whispered) text` | Delivery cue -- whispers next text | Usually works alone |
| `(spoken) text` | Spoken not sung | Usually works alone |
| `(robotic layer: text)` | Named secondary voice (AI/machine) | **YES** -- must declare |
| `(echo layer: text)` | Delayed/echo treatment | **YES** -- must declare |
| `(whisper layer: text)` | Background whisper texture | **YES** -- must declare |
| `(response text)` | Backup vocal / duet response | Best with declaration |

**Key rule:** Named layers (`X layer: text`) REQUIRE the Style Prompt to declare them (e.g., "low-register AI voice layered during system sections"). Without this, Suno may just sing parenthetical content normally.

**Duet modes:**
- **Mode A:** `[Male Vocal]`/`[Female Vocal]` per line (complex, explicit)
- **Mode B:** Main + `()` response, declared in Style (efficient)
- **Mode C:** Custom layers + stacked tags (theatrical)

When using any `()` content, add `-vocal overlap confusion` to exclusions.

---

## Compliance Checklist (Required Elements)

Every Suno-ready song MUST have:

- [ ] `[track: genre: X, mood: X, length: XXX]` -- global control
- [ ] `[control: no-repeat, dynamic transitions]` -- prevent loops
- [ ] `[sequence: ...]` -- section order declaration
- [ ] `[Title: Song Title]` -- title tag
- [ ] `[Production Direction: ...]` -- tone/dynamics guidance
- [ ] `[Vocal Direction: ...]` -- voice/delivery guidance
- [ ] `[end]` -- termination signal
- [ ] Section tags on their own lines
- [ ] Genre first in Style Prompt
- [ ] Style <=1000 characters
- [ ] Lyrics <=5000 characters
- [ ] Tag count 5-8 (never >10)
- [ ] No contradictory tags
- [ ] Named `()` layers declared in Style Prompt
- [ ] Exclusions in dedicated Exclude field

---

## Common Suno Problems and Fixes

| Problem | Likely Cause | Fix |
|---|---|---|
| Song runs too long | No length tag | Add `[length: XXX]` in `[track:]` |
| Sections out of order | Complex structure confuses parser | Add `[sequence: ...]` |
| Lines get auto-repeated | Suno auto-loops | Add `[control: no-repeat]` |
| Wrong voice gender | Unclear vocal assignment | Use `[Male Vocal]`/`[Female Vocal]` explicitly |
| Song will not end | No termination signal | Add `[end]` after outro |
| Bridge gets sung not spoken | No delivery tag | Add `[spoken word]` or `[narrator]` |
| No dynamic contrast | All sections same energy | Add `[build]`, `[silence]`, `[crescendo]` |
| Genre drift mid-song | Conflicting style cues | Use `[track: genre: X]` globally + exclusions |
| Over character limit | No audit before render | Run character count FIRST (Step 1) |
| Parenthetical sung normally | Layer not declared | Declare named layers in Style Prompt |
| Sound too generic | Too many tags/signals conflict | Reduce to 5-8 focused tags, use era anchoring |
| Render does not match intent | Wrong dimension in Style Prompt | Run the 7-Dimension check |
| Song drifts after solo/break | No return signal | Add `[Solo ends]` + `[Return to main song]` after breaks |
| Tempo inconsistent/wrong | BPM number ignored | Use Italian tempo marking (`[Tempo: Vivace]`) instead of/alongside BPM |
| Singer rushes/crams lines | No breathing room in lyrics | Add blank lines between phrases for instrumental fills |
| Harmony doesn't match intent | No harmonic guidance in lyrics | Add `[Chord Progression: I-IV-V (C, F, G)]` before sections |

---

## v5.5 Features (UI Controls)

These are set in the Suno interface, not in text fields:

| Feature | What It Does | When to Use |
|---|---|---|
| **Personas/Voices** | Lock a consistent vocal identity across all generations | One Persona per album character |
| **Stems** | Extract up to 12 individual tracks (vocals, drums, bass, etc.) | DAW mixing/mastering, album consistency |
| **Custom Models** | Train Suno on your completed tracks to learn your sound | Pro/Premier only, after establishing palette |

---

## Exclusions Format

The Exclude field in Suno's UI takes plain comma-separated items:
```
distortion, electric guitar, synthesizers, trap drums, beatboxing
```

No dash prefix needed in the dedicated field. The dash-prefix format (`-item`) is only for exclusions placed WITHIN the Style Prompt field.

---

## Tag Priority Order (Character Budget)

When tight on character count, prioritize in this order:

1. `[control]` + `[length]` + `[sequence]` (structural)
2. Section names with pipe notation (saves chars)
3. `[modulation]` / `[silence]` / `[beat-switch]` (specific moments)
4. `[vulnerable vocals]` / `[whisper]` / `[chant]` (vocal delivery)
5. `[crescendo]` / `[diminuendo]` / `[build]` (dynamics)
6. `[end]` (termination)

---

## Section Tag Formatting Rules

Section tags control how Suno interprets each part of the song. Strict formatting rules apply:

**Placement:**
- Tags MUST be on their own line -- never on the same line as lyrics
- Place section tags immediately before the lyrics they govern
- Global control tags go at the TOP of the lyrics field

**Line discipline:**
- Each lyric line = one melodic phrase = one breath
- Target 7-12 syllables per line
- 4-8 lines per section maximum (sung/spoken sections)
- Instrumental sections with only a tag and no lyrics are valid
- No end punctuation on lyric lines (no periods, commas, semicolons, question marks)
- Em-dashes are allowed for phrasing/breath
- Apostrophes and hyphens are fine

**Pipe notation syntax:**
```
[section-name | parameter1, parameter2, parameter3]
```

Only adjectives and delivery descriptors go after the pipe. Instrument-specific instructions belong in Production Direction blocks or standalone tags.

**Contrast principle:** Adjacent section tags should specify DIFFERENT qualities to prevent monotony. If your verse is `[verse | vulnerable, sparse, close-mic]`, your chorus should contrast: `[chorus | powerful, wide, full band]`.

---

## Inline Performance Notation (User-Tested)

> [Tier 3: Community heuristic -- user-tested July 2026 on Suno v5.5]

Only ONE inline formatting symbol reliably affects vocal delivery:

| Symbol | Status | Use? |
|---|---|---|
| `ALL CAPS` | CONFIRMED -- louder/more forceful delivery | **YES** |
| `~` (tilde) | Inconsistent -- unreliable across renders | NO |
| `-` (mid-word dash) | Word separator only -- does NOT stretch syllables | NO (misleading) |
| `" "` (quotes) | No effect observed | NO |
| `...` (ellipsis) | Marginal -- reinforces existing sustain only | NO (not a reliable control) |

**Rule:** Use ALL CAPS for emphasis. For all other delivery changes, use section tags (`[whisper]`, `[spoken word]`, etc.) or pipe notation (`[verse | vulnerable vocals, breathy]`). Do not rely on tilde, dash, quotes, or ellipsis for performance control.

---

## Tag Placement Strategy: Sandwiching

> [Tier 3: Community heuristic — MasterofSFL + Jack Righteous testing, 2026]

Focus tags are better recognized when they "sandwich" structure tags -- placed AROUND the section marker rather than all stacked before or after.

**The Sandwich Pattern:**
```
[Tempo: Allegro]          ← Focus tag (BEFORE structure)
[Mood: Epic, Building]    ← Focus tag (BEFORE structure)
[Instrument: Strings, Brass Swells]  ← Focus tag (BEFORE structure)
[Verse: Powerful, Cinematic]         ← STRUCTURE TAG (the bread)
[Vocals: Male Baritone, Projected]   ← Focus tag (AFTER structure)
```

**Why it may work:** GPT processes a richer context window around the structure tag, influencing Suno's token prediction with more parameters at the critical transition point.

**Comparison with pipe notation:**

| Approach | When to Use |
|---|---|
| Pipe notation: `[verse \| powerful, cinematic, strings]` | Default. Character-efficient, proven. |
| Sandwiching | When pipe notation isn't producing precise enough results. More tags = more precision but higher character cost. |
| Our standard stacking (all before) | Still valid. Sandwiching is an alternative, not a replacement. |

**Key rule for sandwiching:** Vocal tags specifically appear to be effective when placed AFTER the structure tag (or even interleaved within lyrics). Tempo/Mood/Instrument tags work best BEFORE.

---

## Chord Progression Tags in Lyrics Field

> [Tier 3: Community heuristic — MasterofSFL + ManiioK testing, 2026]

Chord progressions placed as tags in the lyrics field can guide Suno's harmonic choices. This likely works because music theory resources (with chord notation) are in GPT's training data.

**Syntax:**
```
[Chord Progression: I-IV-V (C7, F7, G7)]
[Chord Progression: i-bVI-bVII-i (Em, C, D, Em)]
```

**Placement:** Before the section the progression applies to:
```
[Chord Progression: i-VI-III-iv (Em, C, G, Am)]
[Verse | intimate, fingerpicked guitar]
I close my eyes and something shifts
```

**Best practices:**
- Include BOTH Nashville numbers AND actual chords in key (redundancy = clarity)
- Different progressions per section (Verse vs Chorus vs Bridge)
- Works best with standard, recognizable progressions
- Less reliable for highly unusual/chromatic progressions
- Combine with Italian tempo marking for maximum harmonic+rhythmic control

**Note:** This is IN ADDITION to documenting progressions in Production Notes. The tag in lyrics actively steers Suno; Production Notes are for human reference.

---

## Return Tags After Breaks/Solos

> [Tier 3: Community heuristic — MasterofSFL testing, 2026]

After instrumental breaks, solos, or interludes, Suno's model may struggle to "find its way back" to the main song form. Return tags signal the transition back.

**The Problem:** Without a return signal, Suno may:
- Drift into a different key after a solo
- Change the feel/energy when returning to vocals
- Continue instrumental energy instead of resetting for the next section

**The Solution:** Use explicit return tags:

```
[Guitar Solo | blues scale, 8 bars]
[Solo ends]
[Return to main song]

[Chorus | powerful, full band]
```

**Available return tag variants:**
- `[Return to main riff]` -- brings back the primary guitar/instrument pattern
- `[Return to main song]` -- general reset signal
- `[Band syncs]` -- signals the full ensemble re-synchronizing (useful after free-time solos)
- `[Solo ends]` or `[Break ends]` -- explicit boundary marker
- `[Instrumental ends]` -- for longer instrumental sections

**Rules:**
- ALWAYS use a return tag after: solos, instrumental interludes, breakdowns, spoken word sections
- Place the return tag on its own line, between the break section and the next sung section
- For short breaks (2-4 bars), a simple `[Solo ends]` may suffice
- For longer breaks (8+ bars), use `[Band syncs]` + `[Return to main riff/song]` for stronger reset

---

## Blank Lines as Instrumental Breathing Room

> [Tier 3: Community heuristic — MasterofSFL testing, 2026]

Extra blank lines between lyric lines create space for instrumental fills and vocal reset. This is the difference between a singer who "yaps on without pause" and one who breathes naturally.

**Effect hierarchy:**
- No blank line between lyric lines = continuous vocal flow (rapid delivery)
- One blank line = standard breath/pause (normal singing)
- Two blank lines = extended pause, allows instrumental fill
- Three+ blank lines = significant instrumental space, dramatic pause

**Usage:**
```
[Verse]
Breaking through the walls tonight

Nothing gonna hold me down

[build]
Every step I take feels like the last

STAND AND FIGHT
```

The blank lines above give the singer breath room and allow the instrumental arrangement to "answer" or fill between phrases. Especially useful at slower tempos where natural phrasing needs more space.

---

## Lyrical Stress Patterns as Musical Steering

> [Tier 3: Community heuristic — MasterofSFL extensive testing, 2026]
> **STATUS: EXPERIMENTAL — AWAITING VERIFICATION**
>
> This section documents a MAJOR claim that has not yet been A/B tested against
> our existing methodology. If confirmed, it would elevate prosody from a quality
> check to a primary creative steering mechanism.

### The Core Claim

The stress patterns (meter) of your lyrics are the PRIMARY mechanism by which Suno's underlying model determines musical delivery. The model predicts tokens based on text patterns -- if you write in driving spondaic meter, the model pulls toward heavy, aggressive music. If you write in flowing pyrrhic meter, it pulls toward lighter, airier production.

**The metaphor:** Tags = road signs. Style Prompt = the vehicle. Lyrical stress patterns = THE ROAD ITSELF.

### How Meter Steers Music (Claimed Effects)

| Meter | Stress Pattern | Claimed Musical Effect |
|---|---|---|
| **Iamb** (da-DUM) | uS | Natural speech flow, conversational, gravity/grandeur |
| **Trochee** (DUM-da) | Su | Lighter, buoyant, can be dark/melancholic |
| **Spondee** (DUM-DUM) | SS | Heavy, emphatic, urgent, slows the line — drives aggressive delivery |
| **Anapest** (da-da-DUM) | uuS | Fast, galloping, adds energy/movement — drives fast delivery |
| **Dactyl** (DUM-da-da) | Suu | Energetic, militaristic, formal/grandiose |
| **Pyrrhic** (da-da) | uu | Light, flowing, subtle rhythmic variation |
| **Amphibrach** (da-DUM-da) | uSu | Flowing, balanced rhythm |
| **Amphimacer** (DUM-da-DUM) | SuS | Strong, driving |

### Staggering Meter Between Lines

One advanced technique: DELIBERATELY alternate meters between consecutive lines to create rhythmic texture variety. Rather than writing an entire section in one meter, stagger them:

```
Anapestic Trimeter (da-da-DUM da-da-DUM da-da-DUM) — line 1 (galloping)
Trochaic Tetrameter (DUM-da DUM-da DUM-da DUM-da) — line 2 (grounded)
Anapestic Trimeter — line 3 (galloping again)
Trochaic Tetrameter + SPONDEE (DUM-DUM) — line 4 (grounded + emphatic end)
```

This creates a "question and answer" rhythmic texture within the verse itself — the music will naturally vary its delivery between lines.

### Implications for Our System

**IF CONFIRMED** (pending Experiment 2 results), this means:
- Prosodic planning (Step 4) becomes a CREATIVE steering decision, not just quality assurance
- Each section's meter should be chosen to MATCH the intended musical energy
- Aggressive sections → spondee/dactyl
- Flowing, intimate sections → iamb/pyrrhic
- Energetic, driving sections → anapest
- The prosody audit (Step 17) adds: "does the meter choice MATCH the intended section energy?"

**CURRENT GUIDANCE:** Until verified, treat this as an additional tool — not a replacement for tags/style. Write lyrics with meter awareness, and observe whether renders that match meter-to-energy produce better results than those that don't.

### Quick Reference: Meter for Section Energy

| Section Energy | Recommended Meter | Why |
|---|---|---|
| Intimate confession | Iambic (natural speech) | Conversational, authentic |
| Building tension | Anapestic (galloping forward) | Creates forward motion |
| Maximum power | Spondaic (heavy, emphatic) | Forces weight on every syllable |
| Light/flowing | Pyrrhic/Trochaic | Unstressed = airy, buoyant |
| Militaristic/ritual | Dactylic | Formal, marching energy |
| Emotional bridge | Amphibrach (balanced) | Flowing, reflective |

### Meterlines (Feet Per Line)

| Name | Feet per Line | Effect |
|---|---|---|
| Dimeter | 2 | Very short, punchy, urgent |
| Trimeter | 3 | Short, focused, intense |
| Tetrameter | 4 | Standard, balanced, most common |
| Pentameter | 5 | Full, flowing, classic (Shakespeare) |
| Hexameter | 6 | Long, epic, expansive |

---

The three creative sliders are set in the Suno UI, not in text fields. They interact with each other and with the Style Prompt.

### Weirdness (Default: 50%)

Controls how much creative latitude Suno takes. Higher values produce more unexpected interpretations.

| Range | Behavior | Best For |
|---|---|---|
| 20-35% | Very faithful to prompt, predictable | Radio pop, covers, tight genre adherence |
| 35-50% | Balanced -- follows prompt with creative additions | Standard songwriting, intimate ballads |
| 50-65% | Adventurous -- may surprise with unexpected choices | Dark cinematic, atmospheric, concept albums |
| 65-80% | Experimental -- prompt is a suggestion, not a rule | Ambient, experimental, noise, radical transformation |

### Style Influence (Default: 50%)

Controls how much the Style Prompt text steers the output. Higher = more prompt control.

**UPDATED:** Multiple sources (MasterofSFL, Omnisona God Mode Manual) suggest higher Style Influence (60-90%) produces more genre-accurate results. Our previous recommendation of 50-60% appears conservative. Test higher values, especially for genre-specific work.

| Range | Behavior | Best For |
|---|---|---|
| 40-50% | Loose -- Suno interprets freely | Experimental, when you want surprises |
| 50-65% | Moderate -- prompt guides, Suno fills gaps | Standard songwriting, creative exploration |
| 65-80% | Strong -- prompt dominates output character | When you need specific genre adherence |
| 80-95% | Maximum -- very literal prompt following | Authentic genre recreation, matching a specific reference |

### Audio Influence (Default: ~45%, only if Inspiration Track used)

Controls how much a reference audio track affects the output.

| Range | Behavior | Best For |
|---|---|---|
| 15-30% | Subtle -- captures vague feel of reference | Radical transformation, when you want slight flavor only |
| 30-50% | Moderate -- adopts key characteristics | Matching album palette to reference |
| 50-70% | Strong -- closely mirrors reference character | Recreating a specific sound, Persona reinforcement |
| 70-80% | Dominant -- structure preserved, identity locked | Enhancing with structure preserved |

### Named Slider Presets

> [Tier 3: Community heuristic — MasterofSFL testing + Jack Righteous slider experiments, 2026]

These tested combinations produce reliable results for specific use cases:

| Preset Name | Weirdness | Style | Audio | Best For |
|---|---|---|---|---|
| **Loosy Goosy** | 33% | 33% | 33% | Prompt translation baseline, seeing what Suno "wants to do" |
| **Identity Lock** | 20% | 25% | 80% | Enhancing existing audio with structure preserved |
| **Prompt Drive** | 40% | 80% | 50% | Style tag-guided remixing, strong prompt control |
| **Genre Rebuilder** | 60% | 90% | 30% | Genre fusion, cinematic use, strong genre accuracy |
| **Emotion Engine** | 50% | 60% | 80% | Emotional dynamics and lift, Persona-driven work |
| **The Rebirth** | 80% | 85% | 15% | Radical transformation, complete reimagining |
| **Shock Test** | 75% | 95% | 25% | Experimental tag testing, pushing boundaries |

**Usage guidance:**
- For standard songwriting with strong genre needs: **Prompt Drive** or **Genre Rebuilder**
- For album tracks matching a reference/Persona: **Identity Lock** or **Emotion Engine**
- For experimental work: **The Rebirth** or **Shock Test**
- For initial test renders (seeing what Suno produces): **Loosy Goosy**

**Interaction effects:**
- High Weirdness + High Style Influence = creative within your genre boundaries
- High Weirdness + Low Style Influence = chaos (sometimes useful for experimental)
- Low Weirdness + High Style Influence = extremely predictable, genre-locked
- High Audio Influence = Persona/reference dominates; lower Weirdness preserves it more faithfully

---

## Key Optimization Principles

1. **Genre-Emotion Alignment (Fabbri):** The genre must SIGNIFY what the lyrics express. Dark lyrics in upbeat genre = semiotic violation.
2. **Key is King (Eerola, Friberg & Bresin, 2013):** Mode is the #1 emotional cue. Wrong key = wrong emotion at the deepest level.

   > **Tier split:** Mode effects on perceived valence = [Tier 1: confirmed by Eerola, Friberg & Bresin 2013 and multiple replications]. Specific key character associations (e.g., D minor = devotional, F# minor = mysterious) = [Tier 2: historical tradition (Schubart 1806, Mattheson), not cognitive science. Useful as creative prompts, not empirical claims.]
3. **BPM Serves Two Masters:** Must satisfy genre convention AND emotional pacing simultaneously.
4. **Instruments Carry Meaning (Tagg):** Every instrument signifies independently of melody. Piano != guitar != synth even playing the same notes.
5. **Era Anchoring > Genre Labels:** Time references give Suno specific sonic periods. "1995 trip-hop" > "dark electronic." [Tier 3: promising but not A/B tested.]
6. **The 70/30 Rule:** Genre combinations -- one dominant (70%) + one flavor (30%). 50/50 splits confuse Suno.
7. **5-8 Tags Maximum:** Past 10, signals conflict and Suno defaults to generic. [Tier 3: Suno v4.5+ docs encourage more descriptive prompting. Test by version.]
8. **Section Tags = Musemic Signification:** Per-section tags should carry correct connotation for THAT section's content (Tagg applied to Suno tags).
9. **Separation Principle:** Separate era from instrumentation when you want retro sounds with modern production.

---

## Time Estimate

15-20 minutes per song (verification pass if song was written with full procedure).

---

## Theoretical Foundation

| Scholar/System | Contribution |
|---|---|
| **Philip Tagg** | Musemic analysis -- applied to section tag signification |
| **Franco Fabbri** | Genre theory -- validates genre selection |
| **Patrik Juslin** | BRECVEMA emotional mechanisms |
| **Eerola, Friberg & Bresin** (2013) | Cue hierarchy -- key/mode as #1 emotional driver |
| **Allan F. Moore** | Soundbox theory -- spatial tag design |
| **Serge Lacasse** | Proxemic distance -- reverb/space as emotional signal |
| **Suno community research** (2025-2026) | Era anchoring, genre-first, 5-8 sweet spot, slider behavior, v5 parsing rules |

---

## Render Strategy

> [Tier 3: Community heuristic]
> Credit: Omnisona (Suno AI God Mode Manual v3.0, March 2026)

Suno is a probabilistic generation system. Tags and prompts shape probability distributions -- they do not guarantee specific outcomes. Key principles:

1. **Tags shape probability, not certainty.** A well-crafted prompt increases the LIKELIHOOD of the desired output but cannot force it. Accept that some renders will miss the mark.
2. **Generate 3-4 versions per song.** Multiple renders allow you to select the best interpretation. This is not failure -- it is the intended workflow for a probabilistic system.
3. **Treat Suno as collaborator, not vending machine.** The model contributes musical ideas you did not explicitly request. The best renders often include happy accidents that a rigid system would never produce.

This framing reduces frustration and improves outcomes. Budget time for multiple renders in your production schedule.

---

## Metronome Audio Input Technique

> [Tier 3: Community heuristic — MasterofSFL testing, 2026]

Uploading a metronome click track as the Audio Influence input can lock Suno's tempo more reliably than text-based tempo instructions alone.

**Method:**
1. Generate a simple BPM click track at your desired tempo and time signature (tools like Metronomer, or any DAW)
2. Upload as the Inspiration Audio in Suno
3. Set Audio Influence to 50-80% (high enough to lock the tempo)
4. Set Style Influence to 80-90% (so genre/mood still come from your prompt, not the click)

**When to use:**
- When tempo accuracy is critical (e.g., matching to video/sync)
- When Italian tempo markings + BPM in Style Prompt still produce inconsistent tempos
- When you want a non-standard time signature reliably (6/8, 5/4, 7/8)
- When iterating and you need all versions at exactly the same BPM for comparison

**Notes:**
- A click track provides ZERO genre/mood information — your Style Prompt carries all creative weight
- This is why Audio Influence should be moderate (tempo lock) while Style Influence stays high (genre control)
- After establishing tempo with click, subsequent iterations can use a Persona instead (which carries both tempo AND timbre)

---

## Iterative Refinement Process

> [Tier 3: Community heuristic — MasterofSFL testing, 2026]

A systematic approach to iteration that saves credits and produces better results:

**The 3-Version Method:**
1. **Version 1 (Exploration):** Render with your best guess at genre, sliders, and lyrics. Use "Loosy Goosy" or moderate sliders. Identify what works and what doesn't.
2. **Version 2 (Refinement):** Adjust genre (remove conflicting sub-genres), tone lyrics (smooth problem enunciation points), adjust sliders toward "Prompt Drive" or "Genre Rebuilder."
3. **Version 3 (Strategic):** Change tempo if needed (try adjacent BPM or different metronome input), refine lyrics at the specific lines where the AI struggled, push sliders to target preset.

**After Version 3 succeeds:**
- Clip a Persona from the strongest sections (~40 credits)
- Use that Persona for further refinement (2-3 more generations)
- Total cost for polished song: ~100 credits

**Long-term value:** Once you have a working Persona for a style/character, future songs in that vein cost only 30-50 credits to reach quality.

---

## References

- `references/SUNO_TAGS_REFERENCE.md` -- Complete tag catalog with all confirmed/obsolete tags, pipe notation rules, and formatting details
- `references/SUNO_STYLE_GENRE_REFERENCE.md` -- Full genre/key/BPM/instrument/emotion mapping tables for Style Prompt optimization
