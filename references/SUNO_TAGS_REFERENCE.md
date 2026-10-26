# Suno AI — Legacy v5.x Tag Reference (v4.5–v5.5 era)

> **LEGACY REFERENCE — v5.x / v5.5-era.** Suno **V6** (`v6` / `v6-wild` / `v6-mini`) is the current default model.
> For V6, use `references/V6_TAG_REFERENCE.md` (tag dictionary) and `references/V6_TAG_DISCOVERY.md`
> (division of labor, canonical tag grammar, results log). Everything in this file is **v5.5-era (legacy) —
> re-validate on V6** before relying on it. V6 lyrics do NOT use global tags (`[track:]` / `[control:]` /
> `[sequence:]`), pipe notation `[Section | params]`, or a `[Tag Vocabulary]` block.

> Meta-tags, formatting rules and techniques documented for Suno v4.5–v5.5, mostly community-sourced
> (stayen/suno-reference, Nov 2025; Omnisona God Mode Manual v3.0) and largely untested by us [Tier 3],
> plus our own v5.5 test results where noted. Tags are documented here, not guaranteed to work.
> Consolidates the tag material formerly in Sections 12 + 13 of `SONGWRITING_KNOWLEDGE_BASE.md`
> (KB §13 is now a short summary that points here).

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
| `[sequence: ...]` | Explicit section ordering | `[sequence: intro, verse, pre-chorus, chorus, verse, chorus, bridge, final chorus, outro]` |
| `[end]` | Song termination signal | `[end]` (at very bottom) |

**Note:** `[length:]` can be embedded inside `[track:]` OR used standalone. Do NOT use both — pick one placement.

**Details:**
- **`[track: ...]`** — sets defaults for the whole song; place at the very top, before any section tags. Individual sections can override these defaults, so you avoid repeating global parameters per section. Example with instruments: `[track: genre: dark cinematic rock, mood: haunted, length: 270, instruments: piano, cello, tribal drums]`
- **`[control: ...]` directives:**
  - `no-repeat` — prevents auto-looping/duplicated lines (essential for spoken bridges)
  - `instrumental` — no vocals at all
  - `dynamic transitions` — allows tempo, intensity and texture to vary between sections
  - Combine: `[control: no-repeat, dynamic transitions]`
- **`[length: XXX]`** — keeps songs from running long or short; place before the section tags. `[length: 180]` = 3:00 (standard) · `[length: 270]` = 4:30 (our typical target) · `[length: 330]` = 5:30 (extended concept tracks)
- **`[sequence: ...]`** — prevents section confusion; most useful for songs with 7+ sections or unusual concept-track structures.
- **`[end]`** — signals Suno to stop generating; not 100% reliable: better at preventing new vocals than at cutting instruments. Pair with `[fade: slow]` in the outro, e.g. `[outro: Fading guitar, single sustained chord]` on one line, `[end]` on the next.

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

> v5.5-era (legacy). Not used in V6 output — V6 uses 2-4 separate tags per section (see `references/V6_TAG_REFERENCE.md`).

**Syntax:** `[SectionName | param1, param2, param3]`

```
[chorus | powerful, wide stereo, choir swell, anthemic]
[verse | vulnerable vocals, close-mic, sparse piano only]
[bridge | stripped, near-silence, spoken delivery]
```

Saves characters vs stacking multiple `[tag]` lines (one line instead of 3-4), states intent more clearly to the parser, and can combine vocal + production + mood. Pipe parameters override the global (`[track:]`) defaults for that section only.

**Can be combined with stacked tags:**
```
[Verse 1 | vulnerable vocals, close-mic, sparse]
[Piano only] [Cave reverb]

Lyrics here...
```

**Pipe notation vs stacked tags:**
- **Pipe notation** — when character count is tight or the section needs only 1-2 quick modifiers
- **Stacked tags** — when you need detailed production cues (Mode C theatrical songs)
- **Both** — for maximum control on critical sections

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

**Parameter meanings & examples:**
- `[crescendo: Slow orchestral build leading into chorus]` · `[crescendo: Layered instruments entering one by one]`
- `[diminuendo: Instruments falling away one by one after the chorus]` · `[diminuendo: Orchestral swell fading into solo violin]`
- `[silence: ...]` — more specific than describing silence in a direction block. `short` = ms to ~2 s · `sudden` = immediate cut-off · `gradual` = fade to nothing · `echoed` = reverb tail, then nothing. Example: `[silence: sudden, 4 beats before the bridge vocal enters]`
- `[power-off drop: ...]` — simulates an electronic system shutting off. `sudden` · `glitchy` = stutter before the silence · `resonant` = slight echo · `percussive` = bass thump, then nothing. Example: `[power-off drop: Sudden, everything cuts before bridge]`
- `[build]` — marks a pre-chorus/pre-drop section as RISING: `[build | rising tension, more drums, synth layers thickening]`
- `[big finish]` — maximum intensity for the final moment: `[big finish: Full orchestra, choir, cymbal crashes, dramatic resolution]`

---

## TEMPO & RHYTHM TAGS

| Tag | Purpose | Parameters |
|---|---|---|
| `[modulation]` | Key change | sudden, ascending, descending, gradual, chromatic |
| `[beat-switch]` | Rhythm change | sudden, gradual, double-time, half-time, syncopated |
| `[accelerando]` | Tempo increase | gradual, sudden, layered |
| `[ritardando]` | Tempo decrease | gradual, sudden, expressive |
| `[fermata]` | Held note/chord | sustained, dramatic, subtle |

**Notes & examples:**
- `[modulation]` — community claim: tagging the key change is more reliable than only describing it in Production Direction. Parameter synonyms: `sudden`/`abrupt`, `ascending`/`rising`, `descending`/`falling`, `gradual`/`smooth`, `chromatic`. Examples: `[modulation: Sudden shift from A minor to C major]` · `[modulation: ascending, gradual from D minor toward F major]`
- `[beat-switch]` — for moments where the groove fundamentally shifts: `[beat-switch: Sudden shift from battle drums to running rhythm]` · `[beat-switch: half-time, slowed groove for emotional weight]`
- `[accelerando: Gradual tempo increase building into climax]` · `[ritardando: Gradual orchestral slowdown leading into outro]`
- `[fermata]` — sustains a moment longer than written: `[fermata: Dramatic hold on final chord before resolution]` · `[fermata: Sustained vocal note at emotional peak]`

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
| `[personae: ...]` | Voice character description (alternative to `[vocalist]`) | `[personae: Gritty male voice with synthetic textures]` |
| `[chant]` | Repetitive vocal phrase | Hook repetition, name-as-mantra, ritual |
| `[chant-loop]` | Looped vocal pattern (building) | Background layers, hypnotic sections |
| `[call-and-response]` | Interaction pattern | Dialogue, duet exchanges, internal argument |
| `[distorted vocals]` | Gritty/processed voice | Industrial sections, breakdown moments |

**Notes & examples:**
- `[vulnerable vocals]` invites a softer, more exposed delivery — less belting, more breath, slight shakiness: `[verse | vulnerable vocals, soft, nearly breaking]` · `[bridge | vulnerable vocals, confessional tone]`. Used for Fractured Shadows' confessional/grief tracks (14-16).
- `[whisper] The secrets only night can hear` (lead) vs `[whispering: eerie background voices, unintelligible, panning]` (texture). `[whisper]` suits intro lines, bridge confessions and intimate moments; `[whispering]` suits background atmosphere, horror/psychological texture and ghost voices.
- `[spoken word]` / `[narrator]` are more reliable than hoping a vocal-direction description works: `[spoken word | intimate, close-mic, almost whispered]` · `[narrator: deep male voice, ancient measured delivery]`
- `[vocalist]` / `[personae]` describe the singing character without naming a real artist and are more specific than a Style-only vocal description — they help lock the voice across sections: `[vocalist | soft female voice, indie folk tone]` · `[vocalist | relaxed baritone, storyteller style, weathered]`
- `[chant: Deep, repetitive vocal phrase — title repeated as mantra]` · `[chant-loop: Layered voices repeating hook phrase, building]` — e.g., name-as-mantra refrains ("Rikan / Rikan", "Ghost in the system", "Both names").
- `[call-and-response: Male voice asks, female voice answers]` · `[call-and-response: Spoken question, sung response]` — e.g., Track 14's bridge dialogue, Track 11's Alaric quotes.

---

## HARMONIC & TEXTURAL TAGS

| Tag | Purpose | Parameters |
|---|---|---|
| `[pedal-point]` | Sustained bass note | low, high, suspended, dissonant |
| `[texture: X]` | Sound density | thin, dense, polyphonic |
| `[aria-rise]` | Soaring vocal climax | solo, choral, orchestral |
| `[articulation: X]` | Note style | staccato, legato, marcato |
| `[tessitura: X]` | Vocal pitch area | low, mid, high |

**Meanings & examples:**
- `[pedal-point]` — a bass note held constant while the harmony changes above it; creates tension or grounding: `[pedal-point: Low sustained note for gothic atmosphere]` · `[pedal-point: Deep drone beneath shifting chords]`. We use the concept in static bridge chords (Track 14's sustained Cm), Alaric's Nexus hum and cave drones.
- `[texture: thin]` = sparse, 1-2 elements · `[texture: dense]` = rich, 8+ elements · `[texture: polyphonic]` = independent melodies at once
- `[aria-rise: Vocals rise into emotional climax, strings swell beneath]` — final-chorus peaks, key-change moments
- `[articulation: staccato]` = short, detached (e.g., Evil Biscuits pizzicato) · `[articulation: legato]` = smooth, connected (grief-ballad strings)
- `[tessitura]` — the AVERAGE pitch area, more precise than a range: `low` = intimate, dark · `mid` = comfortable storytelling · `high` = emotional peaks, fragility

---

## STRUCTURAL DISTINCTIONS

| This | Means | vs This | Which Means |
|---|---|---|---|
| `[breakdown]` | Strip DOWN (subtractive, extended) | `[break]` | Brief PAUSE (transitional) |
| `[whisper]` | Lead vocal whispered | `[whispering]` | Background whisper texture |
| `[build]` | Rising intensity section | `[drop]` | Sudden intensity shift (arrival) |

```
[breakdown: Percussion only, building back toward chorus]
[break: 2 beats of silence before the drop]
```

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

> v5.0-era community findings (legacy) — re-validate on V6.

### Genre Mashups (use + to combine)
v5.0 handles compound genres that v4.x could not: it blends both instead of defaulting to one.
```
[genre: dark cinematic rock + nordic folk]
[genre: industrial + neoclassical]
[genre: indie pop + quirky theatrical]
```

### Natural Language Tempo
v5.0 parses descriptive tempo phrases beyond a plain BPM number:
```
[tempo: slow funeral march, processional weight]
[tempo: mid-tempo walking pace with purpose]
[tempo: urgent combat heartbeat, elevated but controlled]
```

### Extended Prompt Parsing
Tags embedded in natural language sentences now parse correctly in v5.0:
```
The [chorus] should hit with [anthemic] vocal harmonies and [big finish] energy
```
This is why Production Direction blocks are read as tag-adjacent instructions.

### Unrecognized Tags = Section Labels
Any `[text: description]` Suno does not recognize becomes a section label, so mood-labeled sections work:
```
[Verse 1 – Cold / Vast]     → a section named "Verse 1 – Cold / Vast"
[Bridge – System Failure]   → a section carrying that emotional context
```
This is what makes the Mode C labeled-section technique (see DUET MODES) valid.

---

## EXTEND & VERSIONING TAGS

### `[extend-style]` — Controls Song Extensions
When using Suno's Extend feature to continue a song, this prevents the "new song" problem:
```
[extend-style: Seamless continuation with evolving textures]
[extend-style: Contrasting — introduce new elements]
[extend-style: Thematic — build upon the main motif]
```

---

## SUNO v5.5 CAPABILITIES (March 2026)

> v5.5-era (legacy) — re-validate on V6. These are documented as v5.5 features; check what your current Suno plan/UI offers.

### Voices / Personas — Consistent Voice Across Songs

Suno v5.5 introduces **Personas** — persistent voice profiles trained from your own vocal samples. Instead of getting a random AI singer each generation, you can lock a specific vocal identity.

**How it works:**
1. Record or upload a voice sample (singing or speaking, ~30-60 seconds)
2. Suno builds a vocal model capturing timbral qualities, resonance, and texture
3. Select that Persona when generating — every song uses YOUR vocal characteristics

**Album workflow impact:**
- Use a single Persona for all tracks featuring the same character (e.g., Maren across all 8 Keeper tracks)
- Create separate Personas for different characters (if you have multiple singers)
- Eliminates the "every render sounds like a different person" problem

**Limitations:**
- The model captures vocal CHARACTER, not perfect reproduction
- Emotional range may be narrower than prompt-only generation
- Works best with clean, isolated vocal samples (no background music)

**Where to specify:** In Suno's UI, select your Persona from the voice menu before generating. This is a UI setting, NOT a text tag in the lyrics/style fields.

---

### Stems — Post-Production Stem Extraction

Suno can now split generated songs into individual stems for external mixing/mastering.

**Available stems (up to 12-track):**
| Stem | Contents |
|---|---|
| Vocals | Lead vocal track |
| Backing Vocals | Harmonies, backup, parenthetical layers |
| Drums | Full drum kit |
| Bass | Bass instruments |
| Guitar | All guitar parts |
| Piano/Keys | Piano, organ, synth pads |
| Strings | Orchestral strings |
| Synth | Synthesizer leads/textures |
| Brass/Woodwind | Horns, flutes, etc. |
| Percussion | Non-drum-kit percussion |
| Effects/Ambience | Sound design, atmospheric layers |
| Other | Everything else |

**How to access:** Hover over a generated song → "Get Stems" → choose "Extract Stems" or the 12-track option. Downloads as WAV or MP3.

**Album workflow impact:**
- Extract vocals from your best render → mix with better instruments in a DAW
- Isolate the parenthetical layers (backing vocals stem) for independent mixing
- Combine stems from different renders to create a "best of" composite
- Level-match tracks across an album by processing stems consistently
- Apply consistent reverb/mastering across all album tracks externally

**Our recommendation:** Generate 3-4 renders per song, extract stems from the best one, then do final mixing in a DAW for album-quality consistency. The Suno render is the starting point, not the final master.

---

### Custom Models — Train on Your Own Music

Upload your completed tracks to train Suno on YOUR sound. The model learns your compositional tendencies, arrangement patterns, and production style.

**Use cases:**
- Train on your best 5-10 songs → generate new tracks that "sound like you"
- Create an album-specific model trained on existing tracks for consistent sonic palette
- Fine-tune genre adherence beyond what Style Prompts alone can achieve

**Limitations:**
- Requires Pro/Premier subscription
- Training takes time — not instant
- Results improve with more training data (more songs = better model)
- The model learns TENDENCIES, not exact reproduction

---

### My Taste — Preference Learning

Suno learns your musical preferences over time based on your generations, likes, and listening patterns. Affects default suggestions and generation tendencies when prompts are ambiguous.

**Practical impact:** Over time, Suno's "default" output drifts toward your style. Less relevant for us (we use detailed prompts that override defaults) but useful for quick ideation sessions.

---

## ERA TAGS — Production Style Modifiers

> **v5.5-era (legacy) — re-validate on V6.** [Tier 3] Community/our v5.x observation: era decade tags in the Style Prompt AGGRESSIVELY bias production style in v5+. Understanding this interaction is critical for getting the sound you want.

### How Era Tags Work

Adding a decade tag (e.g., "1980s", "1970s", "1960s") to your Style Prompt tells Suno to apply the PRODUCTION AESTHETICS of that era — not just the instruments but the recording techniques, mixing style, and sonic character.

### Era → Production Mapping

| Era Tag | Production Characteristics Applied |
|---|---|
| `1960s` | Mono/narrow stereo, tape saturation, limited EQ, room mics, AM radio warmth |
| `1970s` | Analog warmth, wide stereo experiments, tape compression, live-room bleed, warm reverb |
| `1980s` | Gated reverb drums, synth textures, bright digital clarity, big stereo width, layered production |
| `1990s` | Grunge compression, lo-fi textures, raw/unpolished, alternative mixing, vinyl crackle aesthetic |
| `2000s` | Loudness war compression, auto-tune artifacts, digital precision, maximized levels |
| `2010s` | Sparse/minimal, trap-influenced bass, reverb-heavy atmospherics, lo-fi beats |

### The Separation Principle

**Problem:** If you want a vintage INSTRUMENT SOUND but modern PRODUCTION, just adding "1970s" will make the WHOLE MIX sound vintage (lo-fi, tape-saturated, narrow stereo).

**Solution:** Separate the era from the production explicitly:

```
❌ "1970s folk rock, acoustic guitar, warm"
   → Everything sounds like a 1970s recording (narrow, tape-saturated)

✅ "Modern production, vintage 1970s guitar tone, acoustic warmth, wide stereo, clean mix"
   → Modern clarity with retro instrument character
```

### Using Era Tags Intentionally

**For our concept albums:**
- Keeper of the Light (folk-horror): Consider "handmade, analog warmth, room recording" rather than a decade tag — we want the FEELING of crafted music without locking into a specific era's production artifacts
- Fractured Shadows (cinematic): "Modern cinematic production" keeps it contemporary. Era tags would add unwanted vintage coloring

**When ERA tags ARE useful:**
- Intentional nostalgia: "1980s synth-pop" for that specific Stranger-Things sound
- Genre-period accuracy: "1990s grunge rock" if you want THAT production character
- Lo-fi aesthetics: "1960s garage rock recording quality" for deliberate rawness

### Combining Era + Genre (Interaction Effects)

| Combo | What Suno Does |
|---|---|
| `1980s` + `trap` | Gated reverb drums + synth textures applied to trap patterns (hybrid) |
| `1970s` + `indie folk` | Analog tape warmth + room recording + folk instruments (authentic vintage folk) |
| `1990s` + `electronic` | Early rave/acid textures + analog synths + raw mastering |
| `2010s` + `orchestral` | Modern film scoring approach — wide, clean, dramatic, spatial |

**Rule:** The era tag affects PRODUCTION STYLE more than instrumentation. "1980s acoustic guitar" gives you an acoustic guitar recorded/mixed like the 1980s — not a different instrument.

---

## THE SPECIFICITY PRINCIPLE

> The more dimensions you specify in your prompt, the less Suno "invents" from its statistical averages. Vague prompts produce generic output. Specific prompts produce intentional output.

### Why This Matters

Suno is a predictive model. When your prompt is ambiguous on any dimension, it fills the gap with the most statistically common option for that genre. This is why "upbeat pop song" sounds like elevator music — Suno picks the AVERAGE of every dimension you didn't specify.

### The 7 Dimensions of a Complete Prompt

Every Style Prompt should address these 7 dimensions (in priority order):

| # | Dimension | What It Controls | Example |
|---|---|---|---|
| 1 | **Genre** | Arrangement DNA, chord expectations, song structure | "Dark cinematic rock" |
| 2 | **Tempo/Feel** | Speed, groove, rhythmic character | "86 BPM, mechanical pulse" |
| 3 | **Mood/Energy** | Emotional tone, intensity level | "Cold, vast, inevitable" |
| 4 | **Vocal Character** | Voice type, delivery style, mic treatment | "Female mezzo, close-mic, raspy" |
| 5 | **Instrumentation** | What plays (top 3-5 instruments by prominence) | "Concertina lead, bodhran, acoustic guitar" |
| 6 | **Space/Production** | Reverb, width, production era, mix character | "Room reverb, intimate, handmade" |
| 7 | **Key/Harmony** | Tonal center, mode, harmonic color | "D Mixolydian" |

### Specificity Levels & Results

| Level | Dimensions Specified | Typical Result |
|---|---|---|
| **Vague** (1-2) | Genre + mood only | Generic, could-be-anything, statistical average |
| **Basic** (3-4) | + tempo + vocal | Recognizable genre, some character, still some guesswork |
| **Good** (5-6) | + instruments + space | Distinctive, intentional, most elements controlled |
| **Precise** (all 7) | Everything specified | Highly specific output — what our system produces |

### How This Connects to Our System

Our SOPs produce Precise-level prompts by design:
- SOP 01 Step 9 forces you to decide key, BPM, audience, target length
- SOP 01 Steps 6-7 force voice + genre decisions
- SOP 01 Step 8 forces arrangement/instrumentation choices
- The Style Prompt formula (STYLE PROMPT FORMULA section, top of this doc) addresses all 7 dimensions

**This is WHY our detailed prompts outperform casual Suno usage.** We're not leaving any dimension to statistical chance.

---

## CREATIVE SLIDERS (UI Settings)

> **v5.5-era (legacy) — re-validate on V6.** Optional: use these only if your Suno UI exposes sliders; all values below are v5.5-era starting points, not tested V6 settings.

Suno's v5.5 interface provides three sliders that affect generation behavior. These are NOT text fields — they're percentage-based controls in the UI.

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

Canonical BPM-by-genre table: `references/SUNO_STYLE_GENRE_REFERENCE.md` §3.1 (BPM-emotion mapping in §3.2). Two placements only this file listed: neo-soul at 85-100 BPM, and cinematic/dirge material at 60-70 BPM.

---

## DUET MODES

### Mode A — Per-Line Tags (Complex/Cinematic)
`[Male Vocal]`/`[Female Vocal]` per line + Direction blocks as anchors

### Mode B — Parenthetical (Space-Efficient)
Main voice unformatted, response in `()`. Style must declare: "male voice for sections without (), female voice for response in ()"

### Mode C — Custom Layers (Theatrical)
Custom conventions `(robotic layer: text)` + mood-labeled sections + stacked production tags

---

## PARENTHETICAL LAYERS — INLINE VOCAL EFFECTS

> Parentheses `()` in the lyrics field tell Suno to deliver that text as a SECONDARY vocal layer — distinct from the main vocal in some way (softer, different voice, different treatment, background).

### How It Works

- **Square brackets `[]`** = structural/production tags. NOT sung.
- **Parentheses `()`** = text that IS sung/spoken, but with a different vocal treatment than the main lyrics.
- Suno interprets `()` content as: backup vocal, ad-lib, whisper layer, background voice, secondary character, or vocal effect — depending on context and style prompt declaration.

### The Key Rule

**Parenthetical content works most reliably when the Style Prompt explicitly declares what `()` means.** Without declaration, Suno guesses (and may just sing it normally). WITH declaration, you get consistent layer separation.

Example Style Prompt declaration:
```
"...male voice for lines without parentheses, female voice for response lines in parentheses, no vocal overlap confusion..."
```

---

### Layer Type 1: Delivery Cue — `(delivery) text`

Tells Suno HOW to sing the NEXT line (or the text after the parenthetical on the same line).

```
(whispered) Evil biscuits
(spoken, quiet) I never wanted to win
(spoken, defeated) Go on then
(distant, whispered) ...no promises
```

**Format:** `(adjective[, adjective]) text-to-deliver`
**Effect:** Changes vocal delivery for that specific moment without needing a full `[tag]`
**Best for:** Single lines that need a different treatment from the section's default

**Confirmed working delivery cues:**
| Cue | Effect |
|---|---|
| `(whispered)` | Breathy, intimate, barely voiced |
| `(spoken)` | Non-melodic speech |
| `(spoken, quiet)` | Soft speech |
| `(spoken, defeated)` | Flat, deflated delivery |
| `(distant, whispered)` | Far-away whisper (reverb/distance implied) |
| `(shouted)` | Projected, intense |
| `(sung softly)` | Reduced volume, tender |
| `(falsetto)` | Head voice register shift |
| `(growled)` | Gritty, throaty |

---

### Layer Type 2: Named Layer — `(layer-name: text)`

Creates a DISTINCT secondary vocal presence with a character/identity. Must be declared in Style Prompt.

```
(robotic layer: Prime Directive initializing)
(robotic layer: global synchronization active)
(robotic layer: exception detected)
(robotic layer: purification sequence active)
(robotic layer: erased)
```

**Format:** `(layer-identifier: text-to-deliver)`
**Effect:** A separate vocal IDENTITY that overlays or interjects. Suno treats it as a different "speaker" with different production.
**Style Prompt requirement:** Must declare the layer in style: `"low-register AI voice layered during system sections"` or `"robotic layer delivered as cold digital voice underneath main vocal"`

**Confirmed working layer identifiers:**
| Identifier | Typical Use | Style Prompt Declaration Example |
|---|---|---|
| `(robotic layer: text)` | AI/machine voice overlay | "low-register AI voice layered during system sections" |
| `(whisper layer: text)` | Breathy background whisper texture | "whispered intrusive thoughts, close and breathy, panning left-to-right with delay" |
| `(echo layer: text)` | Repeated/delayed vocal echo | "deep echo layer" or "distant burr echo" |
| `(choir layer: text)` | Background choir/harmony | "choir layer sung beneath main vocal" |
| `(inner voice: text)` | Internal monologue/thought | "inner voice as quiet whispered layer underneath" |

**Key insight:** The word before "layer:" tells Suno the VOCAL CHARACTER of that layer. It functions like a mini style-prompt for just that voice.

---

### Layer Type 3: Backup/Response Vocal — `(text)`

Plain parenthesized text (no prefix) creates a secondary vocal that responds to, echoes, or harmonizes with the main vocal.

```
What if we just try
What if the ground holds when we step outside
(What if it works — what if you fly)
What if the answer's been here the whole time
(I'll be right beside you either way)
```

```
Was I taken — or did I go willingly
(you went willingly)

Did I know what I was doing
(you knew enough — you chose not to look)
```

**Format:** Main lyric line (normal), then `(response text)` on its own line or inline
**Effect:** Sung as a softer/background voice, response, or harmony. In duets, can be assigned to a specific singer via Style Prompt.
**Use cases:**
- Duet responses (female answering male, or vice versa)
- Internal dialogue (self-questioning and self-answering)
- Backing vocals / call-and-response
- Ad-libs and vocal fills

---

### Layer Type 4: Inline Sound/Vocalization — `(effect)`

Non-word vocalizations or atmospheric sounds.

```
(searching… searching…)
(no results found)
```

**Format:** `(sound-description)` or `(non-lyrical vocalization)`
**Effect:** Suno interprets as a vocal texture/sound rather than sung lyrics. Works best when the content clearly isn't a normal lyric phrase.

---

### Making Layers Reliable — Style Prompt Rules

**For delivery cues** (`(whispered) text`): Usually work without extra style prompt declaration. Suno recognizes common delivery adjectives.

**For named layers** (`(robotic layer: text)`): MUST be declared in Style Prompt:
```
Style Prompt should include:
"low-register AI voice layered during system sections"
OR
"whispered intrusive thoughts in parentheses, close and breathy"
OR
"secondary female vocal for parenthetical lines"
```

**For backup/response vocals** (`(text)`): Most reliable when Style Prompt includes explicit assignment:
```
"male voice for main lines, female voice for response lines in parentheses"
"clear vocal separation, no vocal overlap confusion"
```

**For all layers — add these to the Exclude field** (plain comma-separated, no dash prefix — see NEGATIVE PROMPTS / EXCLUSIONS):
```
vocal overlap confusion, hums, beatboxing
```

---

### Whisper Rule Declaration Pattern

For songs with consistent parenthetical behavior, declare a RULE at the top of lyrics:

```
[Whisper Rule: Lyrics in parentheses are whispered intrusive thoughts, close and breathy, panning left-to-right with delay.]
[Exception: Whispered thoughts may be glitched. Choir stays subtle until final chorus.]
```

This tells Suno (and future collaborators) exactly how `()` content should be treated throughout the song.

---

### Layer Formatting Summary

| Pattern | What Suno Does | Style Prompt Needed? |
|---|---|---|
| `(whispered) Next line text` | Whispers the following text | Usually works alone |
| `(spoken) text` | Speaks rather than sings | Usually works alone |
| `(robotic layer: text)` | Secondary robotic/AI voice delivers text | YES — must declare |
| `(echo layer: text)` | Echo/delay treatment on text | YES — must declare |
| `(whisper layer: text)` | Whispered background layer | YES — must declare |
| `(response text)` | Backup vocal / response singer | Best with declaration |
| `(non-word sound)` | Vocal texture / sound effect | Context-dependent |

---

### Character Count Note

Parenthetical layers count toward the 5000 character lyric limit. Named layers (`(robotic layer: very long text here)`) use more characters than simple `(text)`. Plan accordingly — the layer identifier eats characters every time it's used.

---

## NEGATIVE PROMPTS / EXCLUSIONS

**Canonical format:** Suno's dedicated **Exclude** field, plain comma-separated text, NO dash prefix (neither `-` nor `‑`):
```
trap drums, beatboxing, vocal hums, bright synths
```
In song files, put them in an `## EXCLUSIONS:` section (preferred). A legacy `[Exclusions: ...]` line inside the Style section is still parsed and never counts toward Style chars.

**Legacy note (v5.5-era):** dash-prefixed negatives (`-trap drums`) were a technique for negation INSIDE the Style field. Do not use dash prefixes in the Exclude field.

Common exclusions by genre:
- **Dark/cinematic:** bright synths, upbeat energy, cheerful melodies, trap drums
- **Folk/acoustic:** EDM drops, heavy distortion, industrial textures
- **Always include:** beatboxing, vocal hums (prevents common Suno artifacts)

---

## OBSOLETE TAGS (Avoid)

| Tag | Status | Use Instead |
|---|---|---|
| `[bpm: 80]` | ❌ Ignored | BPM in Style Prompt |
| `[key: Am]` | ❌ Ignored | Key in Style Prompt |
| `[loop]` | ❌ Unsupported | Manual repetition |
| `[autotune]` | ❌ Deprecated | Describe vocal style |
| `[mix]`/`[master]` | ❌ Ineffective | Use `[eq]` / `[compression]` hints or describe |
| `[volume]` | ❌ Ineffective | Use dynamics tags |
| `[filter]` | ❌ Ineffective | Describe in direction |
| `[panning]` | ❌ Ineffective | Use `[stereo: wide]` if needed |
| `[section]` | ❌ Redundant | Use specific names |

---

## PERFORMANCE NOTATION SYMBOLS (Inline Lyric Formatting)

> **v5.5-era (legacy) — re-validate on V6.**
> [Tier 3: Community heuristic — single-song finding]
> Credit: Omnisona (Suno AI God Mode Manual v3.0, March 2026)
> User-tested on Suno v5.5 (July 2026) on ONE song -- see `experiments/suno/2026-07-02-performance-notation-symbols.yml`.
> The promotion rule in `experiments/suno/README.md` requires 3+ different songs before an observation becomes
> guidance, so every "Tested Status" below is a provisional single-song result, not a confirmed rule.

Certain characters inside lyrics affect vocal delivery in Suno. These are NOT tags -- they are inline text formatting that shapes how the AI sings.

| Symbol | Claimed Effect | Tested Status (v5.5) | Recommendation |
|---|---|---|---|
| `( )` | SUNG/PERFORMED as secondary vocal layer | CONFIRMED | Use freely -- see PARENTHETICAL LAYERS section |
| `[ ]` | Structural/production tag -- NOT sung | CONFIRMED | Use freely -- see SECTION TAGS section |
| `ALL CAPS` | Emphasis -- louder, more forceful delivery | **WORKED (1 song)** | Use for emphasis -- the only symbol that worked in this test |
| `~` | Vocal vibrato or wavering delivery | NOT RELIABLE -- inconsistent results, works sometimes on slower material | NOT RECOMMENDED for production |
| `-` (mid-word) | Syllable stretch / melisma | DOES NOT STRETCH -- treats each hyphenated section as a new word (separator, not stretcher) | WORD SEPARATOR only -- do not use for melisma |
| `" "` (quotation marks) | Different vocal color (quoting) | NO EFFECT -- no noticeable delivery change observed | DOES NOT WORK |
| `...` (long ellipsis) | Trailing off / vocal fade | MARGINAL -- sustains only where Suno would already sustain naturally | Reinforces existing behavior only -- not a reliable control |

**CRITICAL:** Parentheses `()` are SUNG/PERFORMED -- never put production instructions inside parentheses. Use square brackets `[]` for production/structural directions.

**WARNING (July 2026 testing, one song):** Of the 5 inline formatting symbols from the God Mode Manual (`~`, `-`, ALL CAPS, `" "`, `...`), only **ALL CAPS** produced the claimed effect. The others did not work, produced unintended results, or only marginally reinforced behavior Suno would produce anyway. Use ALL CAPS for emphasis; rely on section-level delivery tags (V6: `[Vocal: ...]`) for other delivery changes.

**Testing details:** All 5 symbols tested on Suno v5.5 renders of a single song, "The One Who Stays" (dark cinematic hip hop, 80 BPM, D minor). Needs 2+ more songs (and a V6 re-test) before promotion. Full experiment log: `experiments/suno/2026-07-02-performance-notation-symbols.yml`

---

## CALL-AND-RESPONSE INSTRUMENT TECHNIQUE

> [Tier 3: Community heuristic]
> Credit: Omnisona (Suno AI God Mode Manual v3.0, March 2026)

Suno can produce a call-and-response pattern between vocals and instruments. The vocal line "calls" and an instrument "answers" in the gap.

**Pattern:** Vocal line > `[instrumental break X]` > Vocal line > instrument answers

**Instruments that respond well:**
- Saxophone
- Guitar (electric, clean or overdriven)
- Violin
- Trumpet
- Harmonica

**Example in lyrics:**
```
I can't hold on anymore
[instrumental break saxophone]
Tell me where we lost the thread
[instrumental break saxophone]
```

The instrument fill occupies the space between vocal phrases, creating a conversational dynamic.

---

## ENVIRONMENTAL / AMBIENT SFX TAGS

> [Tier 3: Community heuristic]
> Credit: Omnisona (Suno AI God Mode Manual v3.0, March 2026)

Suno can render environmental sound effects when placed as tags in the lyrics field. These add atmosphere without occupying vocal space.

**SFX tags reported to work** (community list from the source above; not yet logged in `experiments/suno/`):
- `[Rain]`
- `[Thunder]`
- `[Birds chirping]`
- `[Wind]`
- `[Ocean waves]`
- `[City ambience]`
- `[Fire crackling]`
- `[Static]`
- `[Record scratch]`

**Usage note:** Place at the start of a section or between vocal lines. Best used sparingly -- 1-2 per song maximum. Overuse may confuse rendering. These work best in intros, outros, and bridge sections where atmospheric space exists.

---

## COMPLETE TEMPLATE (v5.0 Optimized)

> v5.x legacy template. For V6 songs use the "Minimal V6 Song Skeleton" in `references/V6_TAG_REFERENCE.md`
> and the PRODUCTION TEMPLATE in `references/V6_TAG_DISCOVERY.md`.

```
[track: genre: X, mood: X, length: 270]
[control: no-repeat, dynamic transitions]
[sequence: intro, verse, pre-chorus, chorus, verse, pre-chorus, chorus, bridge, final chorus, outro]

STYLE PROMPT:
Genre, BPM, Mood, Instruments, Vocal Style, Production Direction
(comma-separated descriptors, up to 1000 chars)

EXCLUSIONS (Exclude field):
item, item, item

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

[bridge | stripped, near-silence]
[silence: sudden, 2 beats]
(bridge — 3-6 lines, the turn)

[modulation: ascending shift to relative major]
[final chorus | big finish, full orchestra, choir]
(final chorus — 4-6 lines)

[outro]
[fade: layered, reverb-tail]
(outro — 2-4 lines)
[end]
```

### Priority Order for Tags (when hitting character limits)
1. `[control]` + `[length]` + `[sequence]` (structural — top of lyrics)
2. Section names with pipe notation (saves chars vs stacked tags)
3. `[modulation]` / `[silence]` / `[beat-switch]` (specific moments)
4. `[vulnerable vocals]` / `[whisper]` / `[chant]` (vocal moments)
5. `[crescendo]` / `[diminuendo]` / `[build]` (dynamics)
6. `[end]` (termination — bottom of lyrics)

---

## LYRIC RULES

1. Section tags on own line — never same line as lyrics
2. Verses/choruses usually 4-8 lines (~8-16 bars); bridge 3-6 lines (up to 8 when the turn needs it)
3. NO punctuation at end of lines
4. Each line = one melodic phrase
5. Total lyrics under 5000 characters
6. Em dashes (—) for breath/phrasing within lines
7. Line breaks guide rhythm
