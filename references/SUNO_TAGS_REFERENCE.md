# Suno AI — Complete Tag Reference

> All confirmed meta-tags, formatting rules, and v5.0 techniques for Suno AI song generation.
> Consolidation of Sections 12 + 13 from the Songwriting Knowledge Base.

---

## FIELD LIMITS

| Field | Limit | Overflow |
|---|---|---|
| Style of Music | 1000 chars | Use Exclude field for negatives |
| Lyrics | 5000 chars | Trim direction blocks if needed |
| Exclude | Dedicated field | Negative prompts / exclusions ONLY |

---

## STYLE PROMPT FORMULA

```
Genre, BPM, Mood, Instruments, Vocal Style, Era/Production, Direction
```

Priority order when hitting 1000 char limit:
1. Genre + BPM + Key
2. Vocal type + delivery
3. Instruments (top 3-5)
4. Mood/direction
5. Negatives (→ Exclude field)

---

## GLOBAL CONTROL TAGS (Top of Lyrics field)

| Tag | Purpose | Example |
|---|---|---|
| `[track: ...]` | Global defaults (genre, mood, length, instruments) | `[track: genre: dark cinematic rock, mood: haunted, length: 270]` |
| `[control: ...]` | Behavioral directives | `[control: no-repeat, dynamic transitions]` |
| `[length: XXX]` | Target duration in seconds | `[length: 270]` |

**Note:** `[length:]` can be embedded inside `[track:]` OR used standalone. Do NOT use both — pick one placement.
| `[sequence: ...]` | Explicit section ordering | `[sequence: intro, verse, pre-chorus, chorus, verse, chorus, bridge, final chorus, outro]` |
| `[end]` | Song termination signal | `[end]` (at very bottom) |

---

## SECTION TAGS

### Core Structure
`[Intro]` `[Verse]` `[Verse 1]` `[Verse 2]` `[Pre-Chorus]` `[Chorus]` `[Post-Chorus]` `[Bridge]` `[Outro]` `[Instrumental]` `[Hook]` `[Break]` `[Build]` `[Drop]` `[Breakdown]` `[Interlude]` `[End]`

### Vocal Assignment
`[Male Vocal]` `[Female Vocal]` `[Duet]` `[Both]` `[Choir]` `[Ad-lib]` `[Spoken Male]` `[Spoken Female]`

### Performance/Delivery
`[Soft]` `[Powerful]` `[Whispered]` `[Belting]` `[Crescendo]` `[Intimate]` `[Energetic]` `[Falsetto]` `[A Cappella]`

### Advanced Structure
`[Ascending progression]` `[Atmospheric shift]` `[Bridge modulation]` `[Key change]` `[Half-time feel]` `[Double-time feel]`

---

## PIPE NOTATION (Inline Parameters)

**Syntax:** `[SectionName | param1, param2, param3]`

```
[chorus | powerful, wide stereo, choir swell, anthemic]
[verse | vulnerable vocals, close-mic, sparse piano only]
[bridge | stripped, near-silence, spoken delivery]
```

Saves characters vs stacking multiple `[tag]` lines. Can combine vocal + production + mood.

### Valid Pipe Parameters (USE THESE):
- **Mood/energy:** powerful, soft, intimate, energetic, stripped, atmospheric, dark, bright, warm, cold
- **Vocal delivery:** vulnerable vocals, close-mic, whispered, belting, spoken, breathy, gritty
- **Dynamics:** building, rising tension, fading, crescendo, near-silence
- **Stereo/space:** wide stereo, narrow, immersive, mono
- **Style:** anthemic, minimal, cinematic, dramatic, playful

### Invalid Pipe Parameters (DON'T DO THIS):
| ❌ Wrong | Why | ✅ Correct Alternative |
|---|---|---|
| `[verse | cello enters low]` | Instrument instruction, not a parameter | Put in Production Direction block |
| `[build | drums enter soft]` | Literal instrument cue | `[build | rising tension, soft percussion]` |
| `[chorus | maximum width]` | Not a recognized term | `[chorus | wide stereo, powerful]` |
| `[control | build across sections]` | Not a valid control value | `[control: dynamic transitions]` |

**Rule:** Pipe params should be **adjectives/descriptors**, not **instructions about what instruments do.** Instrument-specific direction belongs in `[Production Direction]` blocks or standalone production tags.

---

## DYNAMICS & INTENSITY TAGS

| Tag | Purpose | Parameters |
|---|---|---|
| `[crescendo]` | Gradual increase | slow, fast, layered, orchestral, electronic |
| `[diminuendo]` | Gradual decrease | slow, fast, layered, orchestral |
| `[silence: sudden]` | Dead silence | short, sudden, gradual, echoed |
| `[power-off drop]` | Abrupt cut-off | sudden, glitchy, resonant, percussive |
| `[build]` | Intensity ramp section | rising tension, more drums, layers thickening |
| `[big finish]` | Grand climactic ending | orchestral, rock, electronic, percussive |
| `[swell]` | Gradual volume rise | orchestral, synth-driven, percussive, dramatic |

---

## TEMPO & RHYTHM TAGS

| Tag | Purpose | Parameters |
|---|---|---|
| `[modulation]` | Key change | sudden, ascending, descending, gradual, chromatic |
| `[beat-switch]` | Rhythm change | sudden, gradual, double-time, half-time, syncopated |
| `[accelerando]` | Tempo increase | gradual, sudden, layered |
| `[ritardando]` | Tempo decrease | gradual, sudden, expressive |
| `[fermata]` | Held note/chord | sustained, dramatic, subtle |

---

## VOCAL DELIVERY TAGS (v4.5+/v5.0)

| Tag | Purpose | When to Use |
|---|---|---|
| `[vulnerable vocals]` | Fragile, intimate, exposed delivery | Confessional verses, grief, quiet moments |
| `[whisper]` | Main vocal whispered (lead) | Intro lines, intimate moments, secrets |
| `[whispering]` | Background whisper layer (texture) | Atmosphere, psychological tension, ghost voices |
| `[spoken word]` | Poetic/rhythmic speech | Bridge monologues, narrative sections |
| `[narrator]` | Clear storyteller/presenter voice | Alaric quotes, system voices, framing |
| `[vocalist]` | Voice character description | `[vocalist \| weathered baritone, close-mic]` |
| `[chant]` | Repetitive vocal phrase | Hook repetition, name-as-mantra, ritual |
| `[chant-loop]` | Looped vocal pattern (building) | Background layers, hypnotic sections |
| `[call-and-response]` | Interaction pattern | Dialogue, duet exchanges, internal argument |
| `[distorted vocals]` | Gritty/processed voice | Industrial sections, breakdown moments |

---

## HARMONIC & TEXTURAL TAGS

| Tag | Purpose | Parameters |
|---|---|---|
| `[pedal-point]` | Sustained bass note | low, high, suspended, dissonant |
| `[texture: X]` | Sound density | thin, dense, polyphonic |
| `[aria-rise]` | Soaring vocal climax | solo, choral, orchestral |
| `[articulation: X]` | Note style | staccato, legato, marcato |
| `[tessitura: X]` | Vocal pitch area | low, mid, high |

---

## STRUCTURAL DISTINCTIONS

| This | Means | vs This | Which Means |
|---|---|---|---|
| `[breakdown]` | Strip DOWN (subtractive, extended) | `[break]` | Brief PAUSE (transitional) |
| `[whisper]` | Lead vocal whispered | `[whispering]` | Background whisper texture |
| `[build]` | Rising intensity section | `[drop]` | Sudden intensity shift (arrival) |

---

## FADE PARAMETERS

```
[fade: slow]        — Long gradual decrease
[fade: layered]     — Instruments fade at different times
[fade: reverb-tail] — Relies on reverb decay
[fade: fast]        — Quick, abrupt
```

---

## GLITCH PARAMETERS

```
[glitch: stutter]     — Repetitive audio chopping
[glitch: bit-crush]   — Lower resolution, pixelated
[glitch: tape-stop]   — Sudden halt
[glitch: granular]    — Fragmented playback
[glitch: randomized]  — Unpredictable
```

---

## EQ HINTS

```
[eq: bass-heavy]  — Emphasize low end
[eq: bright]      — Boost highs
[eq: warm]        — Midrange-heavy
[eq: lo-fi]       — Reduced highs, vintage
```

---

## SUNO v5.0 CAPABILITIES

### Genre Mashups (use + to combine)
```
[genre: dark cinematic rock + nordic folk]
[genre: industrial + neoclassical]
```

### Natural Language Tempo
```
[tempo: slow funeral march, processional weight]
[tempo: urgent combat heartbeat, elevated but controlled]
```

### Extended Prompt Parsing
Tags embedded in natural language sentences now parse correctly in v5.0.

### Unrecognized Tags = Section Labels
`[Verse 1 – Cold / Vast]` is parsed as a section. Our mood-labeled sections work.

---

## CREATIVE SLIDERS (UI Settings)

Suno's interface provides three sliders that affect generation behavior. These are NOT text fields — they're percentage-based controls in the UI.

### Weirdness (Safe ↔ Chaos)

Controls how much creative latitude the AI takes with your prompt.

| Value | Name | Effect | Use When |
|---|---|---|---|
| 0-20% | **Safe** | Very predictable, genre-conventional, may sound generic | You want a reliable, standard render — radio-friendly, no surprises |
| 20-40% | **Conservative** | Mostly follows prompt closely, minor creative additions | You want prompt adherence with slight organic variation |
| **50%** | **Normal (Default)** | Balanced — follows prompt but adds its own musical ideas | Standard starting point for most generations |
| 55-70% | **Experimental** | Noticeable creative departures, unexpected harmonic/timbral choices | Concept albums, atmospheric tracks, "happy accidents" |
| 70-85% | **Wild** | Significant deviation from prompt, surprising results | When you want unpredictable output and will cherry-pick |
| 85-100% | **Chaos** | May ignore prompt substantially, produces highly unusual output | Experimental/noise, vocal hallucinations, avant-garde |

**Recommended starting values by song type:**
- Radio-friendly pop/rock: 35-45%
- Concept album tracks (our songs): **50-55%**
- Atmospheric/ambient: 55-65%
- Experimental/hallucinogenic: 70%+

**Warning:** Below ~4% the AI may produce chaotic results paradoxically (undertrained behavior). Stay above 20% for usable output.

---

### Style Influence (How much the Style Prompt matters)

Controls the weight given to your Style of Music text prompt relative to the AI's own interpretation.

| Value | Effect | Use When |
|---|---|---|
| 0-25% | Style prompt mostly ignored — AI generates freely | You want maximum creative freedom, minimal steering |
| 25-40% | Light guidance — AI uses your genre/mood as suggestion only | Loose inspiration, willing to be surprised |
| **50% (Default)** | Balanced — prompt guides but doesn't dominate | Standard usage — your style sets the direction |
| 60-75% | Strong adherence — AI closely follows style descriptors | You need specific genre/instrument compliance |
| 75-100% | Maximum adherence — AI prioritizes your exact style text | Very specific production requirements, exact genre targeting |

**Recommended starting values:**
- Generic/exploratory: 40-50%
- Our concept album tracks: **50-60%** (we want genre compliance but room for production choices)
- Exact reproduction attempts: 70-80%

---

### Audio Influence (Inspo/Reference track weight)

Only active when you provide an audio reference (Inspo feature). Controls how much the reference shapes the output.

| Value | Effect | Use When |
|---|---|---|
| 0-25% | Reference barely affects output — just a light flavor | You want a vague nod to the reference, not a copy |
| 25-40% | Noticeable similarity in groove/energy but distinct song | Inspired-by without being derivative |
| **45% (Recommended start)** | Balanced blend of reference character and your prompt | Standard Inspo usage |
| 50-70% | Strong reference influence — output clearly echoes the source | You want the "feel" of a specific track replicated |
| 70-100% | Near-reproduction of reference characteristics | Remix-adjacent, very close to source material |

**Recommended starting values:**
- Inspired-by (light touch): 30-40%
- Match the vibe: **45-55%**
- Closely replicate feel: 60-70%

---

### Slider Presets by Song Type

| Song Type | Weirdness | Style | Audio (if Inspo) |
|---|---|---|---|
| **Radio pop/rock** | 35-45% | 55-65% | 40-50% |
| **Concept album (our tracks)** | 50-55% | 50-60% | 45% |
| **Dark cinematic** | 50-60% | 55-65% | 45-55% |
| **Intimate ballad** | 45-55% | 50-60% | 40-50% |
| **Epic orchestral** | 50-55% | 60-70% | 45-55% |
| **Experimental/ambient** | 60-75% | 40-50% | 30-40% |
| **Hallucinogenic/noise** | 75%+ | 30-45% | 20-35% |

---

### Slider Interaction Rules

1. **Weirdness + Style are inversely effective** — high weirdness can override strong style influence. If you want predictable output, BOTH should be moderate (weirdness 45-55%, style 55-65%).
2. **Audio overrides Style when high** — at audio 70%+, the reference dominates regardless of style text.
3. **For maximum prompt adherence**: weirdness 40%, style 65%, audio 45% (if used).
4. **For maximum creative surprise**: weirdness 70%, style 35%, audio 25% (if used).
5. **Our concept album sweet spot**: weirdness 50-55%, style 50-60% — enough adherence to honor our detailed prompts while allowing Suno to add musicality.

---

## BPM REFERENCE

| Range | Feel | Genres |
|---|---|---|
| 60-70 | Ballad, ambient, cinematic | Grief, intimate, dirge |
| 70-85 | R&B, soul, trip-hop | Vulnerability, confession |
| 85-100 | Hip-hop, neo-soul | Indie, alternative |
| 100-115 | Pop, indie, folk | Walking pace, accessible |
| 115-125 | Pop, dance-pop, funk | Energy, dance |
| 125-135 | Rock, EDM | Driving, aggressive |
| 135+ | Punk, metal, D&B | Maximum intensity |

---

## DUET MODES

### Mode A — Per-Line Tags (Complex/Cinematic)
`[Male Vocal]`/`[Female Vocal]` per line + Direction blocks as anchors

### Mode B — Parenthetical (Space-Efficient)
Main voice unformatted, response in `()`. Style must declare: "male voice for sections without (), female voice for response in ()"

### Mode C — Custom Layers (Theatrical)
Custom conventions `(robotic layer: text)` + mood-labeled sections + stacked production tags

---

## NEGATIVE PROMPTS / EXCLUSIONS

Format: `[Exclusions: ‑item, ‑item, ‑item]`

Common exclusions by genre:
- **Dark/cinematic:** ‑bright synths, ‑upbeat energy, ‑cheerful melodies, ‑trap drums
- **Folk/acoustic:** ‑EDM drops, ‑heavy distortion, ‑industrial textures
- **Always include:** ‑beatboxing, ‑vocal hums (prevents common Suno artifacts)

---

## OBSOLETE TAGS (Avoid)

| Tag | Status | Use Instead |
|---|---|---|
| `[bpm: 80]` | ❌ Ignored | BPM in Style Prompt |
| `[key: Am]` | ❌ Ignored | Key in Style Prompt |
| `[loop]` | ❌ Unsupported | Manual repetition |
| `[autotune]` | ❌ Deprecated | Describe vocal style |
| `[mix]`/`[master]` | ❌ Ineffective | Use `[eq]` or describe |
| `[volume]` | ❌ Ineffective | Use dynamics tags |
| `[filter]` | ❌ Ineffective | Describe in direction |
| `[section]` | ❌ Redundant | Use specific names |

---

## COMPLETE TEMPLATE (v5.0 Optimized)

```
[track: genre: X, mood: X, length: 270]
[control: no-repeat, dynamic transitions]
[sequence: intro, verse, pre-chorus, chorus, verse, pre-chorus, chorus, bridge, final chorus, outro]

STYLE PROMPT:
Genre, BPM, Mood, Instruments, Vocal Style, Production Direction

[Exclusions: ‑item, ‑item, ‑item]

LYRICS:

[Title: Song Title]

[Production Direction: Overall tone, dynamics, key decisions]
[Vocal Direction: Voice type, delivery, emotional progression]

[intro | atmospheric, sparse]
(lyrics)

[verse | vulnerable vocals, close-mic]
(lyrics — 4-8 lines, no end punctuation)

[build | rising tension]
(pre-chorus — 2-4 lines)

[chorus | powerful, wide]
(chorus — 4-6 lines, hook prominent)

[bridge | stripped]
[silence: sudden]
(bridge — 3-4 lines, the turn)

[modulation: ascending to relative major]
[final chorus | big finish, choir]
(final chorus — 4-6 lines)

[outro]
[fade: layered, reverb-tail]
(outro — 2-4 lines)
[end]
```

---

## LYRIC RULES

1. Section tags on own line — never same line as lyrics
2. 4-8 lines per section maximum
3. NO punctuation at end of lines
4. Each line = one melodic phrase
5. Total lyrics under 5000 characters
6. Em dashes (—) for breath/phrasing within lines
7. Line breaks guide rhythm
