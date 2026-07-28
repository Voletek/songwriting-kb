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

| Moment | Standalone Tag | Pipe Alternative | Status |
|---|---|---|---|
| Pre-chorus building | `[build]` | `[pre-chorus | building, rising tension]` | **Confirmed** |
| Volume decreasing | `[diminuendo]` | `[section | fading, pulling back]` | **Confirmed** |
| Key change / modulation | `[modulation: ascending]` | `[final chorus | lifted, key change up]` | **Probabilistic** (~50% success) |
| Volume increasing | `[crescendo]` | `[section | swelling, crescendo]` | Likely works |
| Rhythm change | `[beat-switch: half-time]` | N/A | Untested |
| Grand ending | `[big finish]` | `[final chorus | powerful, big finish]` | Likely works |
| Held note | `[fermata]` | N/A | Untested |
| Dramatic silence | `[silence: sudden]` | N/A | **UNRELIABLE — does not consistently produce silence** |

Use standalone tags for mid-section dynamic events. Use pipe parameters when the dynamic applies to the entire section.

**Note on `[silence: sudden]`:** Testing shows this tag does NOT reliably produce an audible pause or silence in renders. For dramatic pauses, use a blank line (which creates a natural breath/fill) or rely on the bridge strip approach (stripping instrumentation via Production Direction). Do not depend on this tag for comedic timing or dramatic beats.

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
| Concept album | 50-60% | 70-80% | 45% | Genre Rebuilder |
| Dark cinematic | 55-65% | 75-85% | 45-55% | Genre Rebuilder |
| Intimate ballad | 40-50% | 65-75% | 40-50% | Prompt Drive |
| Epic orchestral | 50-60% | 80-90% | 45-55% | Genre Rebuilder |
| Experimental | 65-80% | 85-95% | 15-30% | Shock Test |

**Album consistency note:** Document slider values per track. If a render captures the intended palette, note settings as baseline for adjacent tracks.

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
| 2 | BPM / Tempo | Tempo anchor (Italian markings preferred) | "Andante" or "92 BPM" |
| 3 | Mood | Emotional direction | "melancholic, haunting" |
| 4 | Instruments | Timbral palette | "acoustic guitar, cello, distant choir" |
| 5 | Vocal Style | Delivery character | "deep male baritone, intimate" |
| 6 | Era/Production | Sonic period | "early 2000s production warmth" |
| 7 | Space/Direction | Atmosphere | "wide reverb, cinematic" |

**Missing any dimension = Suno guesses (fills with statistical averages).**

**8th Dimension: Groove/Time-Feel (Optional):** For additional rhythmic specificity beyond BPM, add a groove descriptor (e.g., "medium swing", "four-on-the-floor", "syncopated", "laid-back shuffle"). Not required for every song, but useful when the groove character is essential to the feel. [Tier 3: Community heuristic] Credit: Omnisona (Suno AI God Mode Manual v3.0, March 2026)

---

## Italian Tempo Markings (Confirmed Working)

> [Tier 3: Confirmed — user-tested July 2026 on Suno v5.5]
> Credit: MasterofSFL (Suno community guide, 2026)

Italian tempo markings produce MORE CONSISTENT tempo results than raw BPM numbers. Use them in the Style Prompt AND as a `[Tempo: Marking]` tag in the lyrics field for reinforcement.

| Category | Marking | BPM Range | Best For |
|---|---|---|---|
| Very Slow | Grave | 20-40 | Funeral, ritual, dread |
| Very Slow | Largo | 40-60 | Sacred, processional |
| Slow | Lento | 45-60 | Atmospheric, grief |
| Slow | Adagio | 66-76 | Intimate ballad, cinematic |
| Walking | Andante | 76-108 | Standard ballad, folk, swagger |
| Moderate | Moderato | 108-120 | Pop, alt-rock |
| Moderate | Allegretto | 112-120 | Upbeat pop, light rock |
| Fast | Allegro | 120-168 | Rock, punk, driving |
| Fast | Vivace | 140-176 | High-energy, thrash |
| Very Fast | Presto | 168-200 | Speed metal, punk |
| Very Fast | Prestissimo | 200+ | Extreme metal |

**Usage:** Place in Style Prompt ("Dark cinematic rock, Adagio, E minor...") AND as a tag in lyrics (`[Tempo: Adagio]`) for double reinforcement. Include BPM in Production Notes for human reference.

**Tempo modification terms (also recognized):** Accelerando (speeding up), Ritardando (slowing down), Rubato (flexible/expressive), Con moto (with motion), Sostenuto (sustained/slower).

---

## Genre Combination Rules

- **Genre-First Principle:** Genre MUST be the first element -- it anchors everything else. [Tier 3: community practice, not official. v4.5+ allows conversational prompts.]
- **5-8 Tag Sweet Spot:** Comma-separated descriptors. Past 10 tags, signals conflict and Suno defaults to generic. [Tier 3: Suno v4.5+ docs encourage more descriptive prompting. Test by version.]
- **70/30 Rule:** One dominant genre (70%) + one flavor (30%). 50/50 splits confuse Suno. Can also use explicit percentage syntax in style: "Thrash Metal (80%), EDM (20%)"
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
| No dynamic contrast | All sections same energy | Add `[build]` and `[diminuendo]` (confirmed working) |
| Genre drift mid-song | Conflicting style cues | Use `[track: genre: X]` globally + exclusions |
| Over character limit | No audit before render | Run character count FIRST (Step 1) |
| Parenthetical sung normally | Layer not declared | Declare named layers in Style Prompt |
| Sound too generic | Too many tags/signals conflict | Reduce to 5-8 focused tags, use era anchoring |
| Render does not match intent | Wrong dimension in Style Prompt | Run the 7-Dimension check |
| Song drifts after solo/break | No return signal | Add `[Solo ends]` + `[Return to main riff]` (confirmed) |
| Tempo inconsistent/wrong | BPM number ignored | Use Italian tempo marking (`[Tempo: Andante]`) — confirmed more reliable |
| Want a key change but doesn't happen | Weak modulation signal | Stack: `[modulation: ascending]` + "lifted" in pipe + Style Prompt mention |
| `[silence: sudden]` not producing pause | Tag unreliable | Use blank lines or strip instrumentation in Production Direction instead |

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
2. `[Tempo: Italian marking]` (confirmed — tempo control)
3. Section names with pipe notation (saves chars)
4. `[modulation]` / `[build]` / `[diminuendo]` (confirmed dynamics)
5. `[vulnerable vocals]` / `[whisper]` / `[chant]` (vocal delivery)
6. `[Solo ends]` / `[Return to main riff]` (confirmed — transition control)
7. `[end]` (termination)

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

## Return Tags After Breaks/Solos (Confirmed Working)

> [Tier 3: Confirmed — user-tested July 2026]
> Credit: MasterofSFL (Suno community guide, 2026)

After instrumental breaks, solos, or interludes, use return tags to signal the transition back to the main song. Without these, Suno may drift in key, feel, or energy after a break.

**Usage:**
```
[Instrumental Break | filthy blues guitar solo, organ answering]
[Solo ends]
[Return to main riff]

[Final Chorus | full band, maximum power]
```

**Available return tag variants:**
- `[Solo ends]` -- explicit boundary marker
- `[Return to main riff]` -- brings back the primary pattern
- `[Return to main song]` -- general reset signal
- `[Band syncs]` -- full ensemble re-synchronizing (after free-time solos)

**Rules:**
- Use after: solos, instrumental interludes, breakdowns, extended spoken word sections
- Place on its own line between the break and the next sung section
- For short breaks (2-4 bars), `[Solo ends]` alone may suffice
- For longer breaks (8+ bars), combine: `[Solo ends]` + `[Return to main riff]`

---

## Key Change / Modulation (Probabilistic)

> [Tier 3: Community heuristic — multiple sources, probabilistic results]
> Credit: Jack Righteous, Suno community, howtopromptsuno.com

Suno CAN produce key changes but it is **probabilistic (~40-60% success rate)**. There is no guaranteed command. Use multiple reinforcing signals to increase the odds.

**Best approach for a single key lift (e.g., Queen-style Final Chorus):**

```
[modulation: ascending]
[Final Chorus | bigger, lifted, key change up, maximum power, layered harmonies]
```

**Reinforcement methods (stack these for higher success):**

| Method | Where | Example |
|---|---|---|
| `[modulation: ascending]` tag | Lyrics field, before Final Chorus | Standalone tag on own line |
| "lifted" in pipe notation | Section tag | `[Final Chorus | lifted, bigger]` |
| Style Prompt mention | Style field | "dramatic key change for final chorus" |
| Production Direction | Direction block | "Final chorus modulates up one half step" |
| Lyrical energy escalation | In the lyrics themselves | More emphatic words, caps, shorter punchy lines |

**What works vs what doesn't:**

| Approach | Success Rate | Notes |
|---|---|---|
| `[modulation: ascending]` + "lifted" in pipe | ~50-60% | Best in-Suno approach |
| Style Prompt "key change up" alone | ~30-40% | Weaker without lyrics-field reinforcement |
| Specifying exact keys (Am to Bbm) | ~20-30% | Suno rarely executes exact key targets |
| DAW post-production pitch shift | 100% | Guaranteed — render best version, shift final section in BandLab/DAW |

**For multiple modulations (Queen/Bohemian Rhapsody style):**
- One modulation per song is achievable with tags
- Multiple modulations require the Extend/Replace Section workflow (render sections separately) or DAW post-production
- The most reliable approach: render the full song, then pitch-shift specific sections in a DAW

**When to use modulation:**
- Final chorus emotional lift (most common — "the key change that makes you cry")
- Bridge-to-chorus transition (the turn hits harder with a key shift)
- Anthem climax (Queen, Whitney Houston, Bon Jovi territory)

---

## Creative Sliders -- Detailed Guidance

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

> **CONFIRMED:** Higher Style Influence (70-90%) produces more genre-accurate results than our previous 50-60% recommendation. Multiple sources and user testing confirm this.

| Range | Behavior | Best For |
|---|---|---|
| 40-50% | Loose -- Suno interprets freely | Experimental, when you want surprises |
| 50-65% | Moderate -- prompt guides, Suno fills gaps | Creative exploration, first drafts |
| 65-80% | Strong -- prompt dominates output character | Standard songwriting with genre needs |
| 80-95% | Maximum -- very literal prompt following | Genre recreation, specific sound targets |

### Audio Influence (Default: ~45%, only if Inspiration Track used)

Controls how much a reference audio track affects the output.

| Range | Behavior | Best For |
|---|---|---|
| 15-30% | Subtle -- captures vague feel of reference | Radical transformation, slight flavor |
| 30-50% | Moderate -- adopts key characteristics | Matching album palette to reference |
| 50-70% | Strong -- closely mirrors reference character | Recreating a specific sound, Persona reinforcement |
| 70-80% | Dominant -- structure preserved, identity locked | Enhancing with structure preserved |

### Named Slider Presets (Confirmed Working)

> [Tier 3: Confirmed — user-tested July 2026. Credit: MasterofSFL + Jack Righteous]

| Preset Name | Weirdness | Style | Audio | Best For |
|---|---|---|---|---|
| **Prompt Drive** | 40% | 80% | 50% | Standard songwriting with strong genre control |
| **Genre Rebuilder** | 60% | 90% | 30% | Genre fusion, specific sound targets, most songs |
| **Emotion Engine** | 50% | 60% | 80% | Persona-driven work, emotional dynamics |
| **The Rebirth** | 80% | 85% | 15% | Radical transformation, reimagining |
| **Shock Test** | 75% | 95% | 25% | Experimental, pushing boundaries, unusual genres |

**Recommended defaults:**
- For most songs: **Genre Rebuilder** (60/90/30) — strong genre lock with creative room
- For Persona-based work: **Emotion Engine** (50/60/80) — reference audio carries identity
- For experimental: **Shock Test** (75/95/25) — maximum creative latitude with style lock

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
| **MasterofSFL** (2026) | Italian tempo recognition, higher slider ranges, return tags, stress pattern awareness |

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

## References

- `references/SUNO_TAGS_REFERENCE.md` -- Complete tag catalog with all confirmed/obsolete tags, pipe notation rules, and formatting details
- `references/SUNO_STYLE_GENRE_REFERENCE.md` -- Full genre/key/BPM/instrument/emotion mapping tables for Style Prompt optimization
