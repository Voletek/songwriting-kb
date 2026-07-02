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

## SUNO v5.5 CAPABILITIES (March 2026)

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

> Era decade tags in the Style Prompt now AGGRESSIVELY bias production style in v5+. Understanding this interaction is critical for getting the sound you want.

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
- The Style Prompt formula (Section 2 of this doc) addresses all 7 dimensions

**This is WHY our detailed prompts outperform casual Suno usage.** We're not leaving any dimension to statistical chance.

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

**For all layers — include negative prompts:**
```
-vocal overlap confusion, -hums, -beatboxing
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

## PERFORMANCE NOTATION SYMBOLS (Inline Lyric Formatting)

> [Tier 3: Community heuristic]
> Credit: Omnisona (Suno AI God Mode Manual v3.0, March 2026)

Certain characters inside lyrics affect vocal delivery in Suno. These are NOT tags -- they are inline text formatting that shapes how the AI sings.

| Symbol | What Suno Does | Example |
|---|---|---|
| `( )` | SUNG/PERFORMED as secondary vocal layer (backup, response, whisper) -- see PARENTHETICAL LAYERS section above for full details | `(I was always here)` |
| `[ ]` | Structural/production tag -- NOT sung -- see SECTION TAGS section above for full details | `[Verse 1]` |
| `~` | Adds vocal vibrato or wavering delivery | `I'm still waiting~` |
| `-` (mid-word) | Syllable stretch / melisma -- extends the note | `Fa-a-all from grace` |
| `ALL CAPS` | Emphasis -- louder, more forceful delivery | `I said NEVER again` |
| `" "` (quotation marks) | Slightly different vocal color -- as if quoting someone | `She said "don't look back"` |
| `...` (long ellipsis) | Trailing off -- vocal fades or hesitates | `Maybe I should just...` |

**CRITICAL:** Parentheses `()` are SUNG/PERFORMED -- never put production instructions inside parentheses. Use square brackets `[]` for production/structural directions.

**Note:** Effects of `~`, `-`, ALL CAPS, quotation marks, and ellipsis are community-observed patterns. Results vary by Suno version and are not guaranteed. The `()` and `[]` behaviors are well-established; see the PARENTHETICAL LAYERS and SECTION TAGS sections above for comprehensive documentation.

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

**Confirmed working SFX tags:**
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
