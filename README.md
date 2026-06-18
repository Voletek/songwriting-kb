# Songwriting Knowledge Base

A professional song production system combining Nashville/LA co-writing craft, academic music theory (12 disciplines), Suno AI v5.5 formatting expertise, and concept album continuity management — with a complete Kiro IDE automation layer and platform-neutral methodology usable by any AI assistant.

---

## Architecture

The system's methodology lives in `core/methodology/` as the **single source of truth**. Everything else consumes it:

```
core/methodology/  ← THE METHOD (complete, self-contained, canonical)
       ↓ loaded by
.kiro/agents/      ← Kiro automation (thin wiring — persona + #[[file:]] load)
       ↓ also readable by
Any AI assistant   ← Just paste core/methodology/X.md into your assistant's context
       ↓ validated by
tools/             ← Deterministic checks (Python, no AI needed)
```

When the method changes, you update ONE place (`core/methodology/`). Kiro agents inherit automatically. Non-Kiro users read the same source.

---

## Quick Start

Clone this repo. Kiro users get automatic agent/skill/hook wiring. Non-Kiro users read `core/methodology/` directly.

```bash
git clone https://github.com/Voletek/songwriting-kb.git
```

**Kiro users** — just talk:
```
"Write a song about..."       → Songwriter agent activates
"Critique this song"          → Critic agent scores (12 categories + Suno optimization)
"Make this Suno-ready"        → Suno-optimizer adds meta-tags
"Check album continuity"      → Album-continuity verifies rules
```

**Non-Kiro users** — see [Using Without Kiro](#using-without-kiro) below.

**CLI validation** (any platform):
```bash
python3 tools/validate-song.py songs/my_song.md
```

---

## Repository Structure

```
songwriting-kb/
├── core/
│   └── methodology/           5 canonical method files (SINGLE SOURCE OF TRUTH)
├── .kiro/
│   ├── steering/              4 files — auto-loaded every session
│   ├── agents/                4 thin agents — load core/methodology/ via #[[file:]]
│   ├── skills/                5 skills — reference core/methodology/
│   ├── hooks/                 5 hooks — format, char-count, prosody, score, pipeline
│   ├── powers/songwriting/    1 power — activatable master bundle
│   └── sops/                  8 SOPs — step-by-step procedures (point to core/)
├── tools/
│   └── validate-song.py       Deterministic song validator (char counts, tags, format)
├── experiments/
│   └── suno/                  Suno experiment logs (version-dated prompt tests)
├── docs/                      Architecture plans, implementation docs
├── references/                7 companion docs (critique, template, style/genre, tags, voice, 2 bibles)
├── examples/                  Reference implementations (albums, preferences)
├── songs/                     Album tracks + experimental + standalone
├── analysis/                  Critique reports + stress test outputs
├── SONGWRITING_KNOWLEDGE_BASE.md    Master craft reference (13 sections)
└── MUSIC_PRODUCTION_THEORY.md       Academic framework (12 disciplines)
```

---

## SOPs (Standard Operating Procedures)

The procedural layer — step-by-step HOW for every workflow:

| # | SOP | What It Covers | Time |
|---|---|---|---|
| **01** | [Writing a Song](/.kiro/sops/01-writing-a-song.md) | 27 steps: concept → analysis → writing → QA → formatting | 50-75 min |
| **02** | [Critiquing a Song](/.kiro/sops/02-critiquing-a-song.md) | 10 steps: read → 9-step analysis → score → Suno optimization → flag → recommend | 35-55 min |
| **03** | [Optimizing for Suno](/.kiro/sops/03-optimizing-for-suno.md) | 12 steps: char audit → tags → validate → dynamics → sliders | 15-20 min |
| **04** | [Setting Up a Concept Album](/.kiro/sops/04-setting-up-concept-album.md) | 12 steps: concept → registry → rules → motifs → documentation | 2.5-3.5 hrs |
| **05** | [Extending an Album](/.kiro/sops/05-extending-an-album.md) | 12 steps: evaluate → scope → update bible → verify → write | 1-2 hrs |
| **06** | [Character Voice Design](/.kiro/sops/06-character-voice-design.md) | 11 steps: identify → accent → template → instruments → mode | 15-25 min |
| **07** | [Full Pipeline](/.kiro/sops/07-full-pipeline.md) | 6 stages: Write → Critique → Revise → Optimize → Verify → Render | 2-3 hrs |
| **08** | [Contributing](/.kiro/sops/08-contributing.md) | Community guide: setup → customize → add albums → submit | Variable |

### The Full Pipeline (SOP 07):

```
WRITE → CRITIQUE → REVISE → OPTIMIZE → VERIFY → RENDER
  ↑         (score ≥8.5? skip revise)         |
  └──────── (if fails verification) ──────────┘
```

---

## Agents

| Agent | What It Does | Invoke With |
|---|---|---|
| **songwriter** | Creates complete songs from concepts using Nashville method, outputs Suno-ready format with Production Notes. Loads `core/methodology/songwriting.md` | "Write a song about X" |
| **critic** | Scores songs on 12 craft categories (1-10) + 5 advanced assessments + Suno optimization (genre/key/BPM/instrument evaluation with alternative Style Prompts). Loads `core/methodology/critique.md` | "Critique this" / "Score this song" |
| **suno-optimizer** | Adds meta-tags, checks char counts, validates formatting, verifies parenthetical layers. Loads `core/methodology/suno-optimization.md` | "Make this Suno-ready" |
| **album-continuity** | Runs hard rules, verifies sonic palette, motifs, character voices, key relationships. Loads `core/methodology/album-continuity.md` | "Check continuity" |

---

## Skills (On-Demand Knowledge)

| Skill | Contains | Activate When |
|---|---|---|
| **song-critique** | 12-category rubric, 5 advanced assessments, Suno optimization (7-point dimensional check + style alternatives), flag patterns | Evaluating any song |
| **suno-meta-tags** | 35+ confirmed tags, v5.5 features, layers, sliders, era tags | Formatting for Suno |
| **music-theory** | 12 disciplines, 23-point framework, 18 advanced concepts | Deep production analysis |
| **character-voice** | Accent/dialect system, voice design template (vocal + non-vocal), instrumentation maps | Writing for characters |
| **concept-album-bible** | Track registry, motifs, continuity rules (template + 2 examples) | Album work |

---

## Hooks (Automated Quality Checks)

| Hook | Fires On | Checks |
|---|---|---|
| **song-format-check** | File create in `songs/` | Required sections present |
| **suno-char-count** | File save in `songs/` | Style ≤1000, Lyrics ≤5000 |
| **prosody-lint** | File save in `songs/` | Lines >12 syllables, stuffed phrases, weak endings |
| **quick-score** | On request | Fast 12-category scoring pass |
| **full-pipeline** | On request | Complete write→critique→revise→optimize→verify flow |

**CLI alternative:** Run `python3 tools/validate-song.py songs/your_song.md` for deterministic format/char validation without hooks.

---

## Steering (Always-On Context)

| File | Purpose |
|---|---|
| `songwriting.md` | Core principles + 9-step workflow + quality gates |
| `suno-formatting.md` | Suno rules, limits, tags, sliders, v5.5 features, era tags, layers |
| `output-preferences.md` | Output format, layers, hit formulas (customize for your own) |
| `concept-album.md` | Album continuity framework + setup guide (universal) |

---

## Suno AI Integration

### Field Limits
| Field | Limit | Notes |
|---|---|---|
| Style of Music | 1000 chars | Genre, BPM, mood, instruments, vocal |
| Lyrics | 5000 chars | Confirmed June 2026 — must fit, no overflow |
| Exclude | Dedicated field | Negative prompts ONLY (plain text, no dash prefix) |

### Creative Sliders
| Slider | Default | Our Songs | Effect |
|---|---|---|---|
| Weirdness | 50% | 50-55% | Safe (0%) ↔ Chaos (100%) — creative latitude |
| Style Influence | 50% | 50-60% | How much Style Prompt steers output |
| Audio Influence | ~45% | 45% | Reference track weight (Inspo only) |

### v5.5 Features (UI — not text tags)
| Feature | What It Does | Album Use |
|---|---|---|
| **Personas/Voices** | Lock vocal identity from your own sample | Same voice across all character tracks |
| **Stems (12-track)** | Extract vocals, drums, bass, guitar, keys, strings, synth, brass, perc, backing, FX, other | DAW mixing for album consistency |
| **Custom Models** | Train Suno on your completed tracks | Learn your sound for future songs |
| **My Taste** | AI learns your preferences over time | Better defaults on quick sessions |

### Parenthetical Layers — `()` in Lyrics
| Pattern | Effect | Style Prompt Needed? |
|---|---|---|
| `(whispered) text` | Delivery cue — whispers next text | Usually works alone |
| `(spoken) text` | Spoken not sung | Usually works alone |
| `(robotic layer: text)` | Named secondary voice (AI/machine) | **YES — must declare** |
| `(echo layer: text)` | Delayed/echo treatment | **YES — must declare** |
| `(whisper layer: text)` | Background whisper texture | **YES — must declare** |
| `(response text)` | Backup vocal / duet response | Best with declaration |

### Era Tags (Production Modifiers)
Decade tags in Style Prompt aggressively bias production style:
- `"1980s"` → gated reverb drums, synth textures, bright digital
- `"1970s"` → analog warmth, tape compression, live-room bleed
- **Separation Principle:** Want vintage instruments + modern production? Be explicit: `"modern production, vintage 1970s guitar tone"`

### The Specificity Principle
The more dimensions you specify (genre, tempo, mood, vocal, instruments, space, key), the less Suno fills gaps with statistical averages. Our SOP system produces 7-dimension "precise" prompts by design.

### Genre-Emotion Alignment (Critic Evaluates This)
The critic's **Suno Optimization Assessment** evaluates whether the Style Prompt's genre, key, BPM, and instrument choices are the BEST match for the song's emotional content — and provides complete alternative Style Prompts when they aren't. Key principles:

- **Key is the #1 emotional cue** (Juslin) — wrong key = wrong emotion at the deepest level
- **Genre must SIGNIFY what the lyrics express** (Fabbri) — dark lyrics in an upbeat genre = semiotic violation
- **BPM serves two masters** — must satisfy genre convention AND emotional pacing
- **Instruments carry cultural meaning** (Tagg) — piano ≠ guitar ≠ synth even playing the same notes
- **Era anchoring > genre labeling** — time references give Suno specific sonic periods
- **70/30 Rule** — genre combinations: one dominant (70%) + one flavor (30%)
- **5-8 tags maximum** — past 10, signals conflict and Suno defaults to generic

Full reference: `references/SUNO_STYLE_GENRE_REFERENCE.md` (600+ lines covering key-emotion mapping, BPM ranges, 30+ instrument significations, genre conventions, and Suno prompt science)

### 5 Formatting Modes
| Mode | Use Case |
|---|---|
| **A** — Per-Line Vocal Tags | Intimate cinematic dialogue |
| **B** — Parenthetical () | Space-efficient call-and-response |
| **C** — Theatrical/Concept | Multi-layer concept albums (named layers) |
| **D** — Character Performance | Fantasy characters, accents |
| **E** — Solo Anthem/Intimate | Accessible solo tracks |

---

## The 9-Step Professional Workflow

Applied to every song:

1. **SEMANTIC** — What is it literally about?
2. **EMOTIONAL** — Central affect? BRECVEMA mechanisms?
3. **PROSODIC** — Stresses, breaths, syllable counts (7-12 per line)
4. **NARRATIVE** — Arc type? Where is the turn?
5. **VOICE** — Who speaks? Accent? Register?
6. **GENRE** — Fabbri's 5 rules? Fusion ratio?
7. **ARRANGEMENT** — Growth pattern? Contrast? Negative space?
8. **PRODUCTION** — Timbre? Harmonic choices? Space?
9. **COMMERCIAL** — Audience? Platform? Length? Sync?

---

## Quality Standards

- Hook arrives within 15 seconds of first sung vocal
- No line exceeds 12 syllables at the song's tempo
- V2 adds NEW information (not restatement)
- Bridge contains a genuine TURN (meaning shifts)
- Hook passes "would someone text this line?" test
- Every word earns its place — no filler
- ABCB default rhyme scheme
- Near/slant rhymes preferred over forced perfect
- Production choices must SIGNIFY correctly (Tagg semiotics)
- Named parenthetical layers must be declared in Style Prompt
- Era tags separated from production intent when mixing vintage + modern

---

## Knowledge Base

### SONGWRITING_KNOWLEDGE_BASE.md (13 Sections)
1. Song Structure & Form
2. The Hook (4 types, 6 principles)
3. Lyric Writing Mastery
4. Rhyme Types & Prosody (Pattison method)
5. Chord Progressions & Music Theory
6. Emotional Arc & Storytelling
7. Genre Conventions
8. Co-Writing & Nashville Method
9. Pitching & Industry Standards
10. Songwriter's Workflow & Exercises
11. Quick Reference Cheat Sheets
12. Suno AI Complete System (formatting, duet modes, layers, hit formulas, v5.5, era tags, specificity)
13. **Suno Advanced Meta-Tags & v5.0/5.5** (35+ tags, pipe notation, controls, sliders, stems, personas)

### MUSIC_PRODUCTION_THEORY.md
- 12 Academic Disciplines
- 23-Point Song Development Framework
- 18 Advanced Concepts
- Vocal Accent & Dialect Phonetics (real-world + fantasy)

---

## Example Albums (Reference Implementations)

### Fractured Shadows — Digital→Fantasy Concept (17 tracks)

> "The fracture made the shadows — but the shadows made the dawn."

**Act 1 — Digital Dissolution → Transfer (Tracks 1-7)**

| # | Title | Key | Emotion |
|---|---|---|---|
| 01 | Ghost In The System | F#m | Burnout |
| 02 | Signal Loss | Dm | Isolation |
| 03 | Residual Self | Em | Identity searching |
| 04 | Human Exception | Dm | AI fascination |
| 05 | Prime Directive | Dm | AI possession |
| 06 | Fracture Protocol | Fm | Consciousness torn |
| 07 | Rikan | Fm→Ab | Terrified awakening |

**Act 2 — Survival → Integration (Tracks 8-17)**

| # | Title | Key | Emotion |
|---|---|---|---|
| 08 | First Blood | Bm | Violence as discovery |
| 09 | The Shard | Em | Prophecy |
| 10 | Fractured Plains | Dm | Epic journey |
| 11 | The Custodian | Am | Mentor |
| 12 | Fall of Dawnwatch | Fm | War, loss |
| 13 | Shadow Weaver | Ebm | Villain revealed |
| 14 | Ghost of Draeven | Cm | Self-confrontation |
| 15 | The Sword Remembers | Gm | Grief |
| 16 | Campfire | **D major** | Found family |
| 17 | Both Names | Am→**C major** | Integration |

**Sonic Evolution:** Industrial/Glitch → Tribal/Primal → Cinematic Orchestral → Folk Rock → Full Orchestra + Key Change

---

### Keeper of the Light — Folk-Horror/Sea-Shanty Concept (8 tracks)

> "The light was never a beacon — it was a lullaby, and she's been singing something terrible to sleep her entire life."

| # | Title | Key | Emotion |
|---|---|---|---|
| 01 | The Keeper's Morning | D Mixolydian | Devotion, solitude |
| 02 | Sixty Years of Light | G Dorian | Ritual, quiet loneliness |
| 03 | What the Logbook Says | Em | Unease, first dread |
| 04 | The Depth Hymn | Bm | Revelation, awe-horror |
| 05 | The Night the Light Died | F#m | Panic, guilt, chaos |
| 06 | Something Stirs Below | Cm | Cosmic dread, paralysis |
| 07 | It Remembers the Sun | Fm | Ancient sorrow, terrible beauty |
| 08 | Lullaby for Leviathan | D Mixolydian (underwater) | Acceptance, transformation |

**Sonic Evolution:** Warm acoustic folk → Darkened folk → Dark ambient → Storm chaos → Near-silence → Massive choir → Transformed return

**Unique features:** Non-vocal entity character design, harmonic circle (starts/ends in D Mixolydian), the sea as ever-present instrument evolving across 8 tracks.

---

## Community Use

This system is designed for sharing. The architecture separates **universal** from **personal**:

### Universal (works for anyone — ~70% of system):
- All knowledge base files
- All SOPs
- Songwriter, Critic, Suno-Optimizer agents
- All skills (except album-bible content)
- Format-check, char-count, prosody-lint hooks
- All reference docs (except album bibles)

### Personal (customize for your projects — ~30% of system):
- `output-preferences.md` → edit with YOUR format preferences
- Album bibles in `references/` → replace YOUR_ALBUM_BIBLE.md with your own
- Album-continuity agent → configure YOUR rules
- Add conditional steering + continuity hooks for YOUR albums (see `examples/`)

### Getting Started (Community):
```bash
git clone https://github.com/Voletek/songwriting-kb.git
cd songwriting-kb
# See SOP 08 for full setup guide
# See SOP 04 to create your own concept album
# See examples/ for complete reference implementations
```

---

## Using Without Kiro

The methodology in this repository works with **any AI assistant** - not just Kiro. The `core/methodology/` files are the complete, self-contained methods.

### Quick Start (Any AI)

Load the relevant methodology file(s) into your AI's context, then ask it to follow the procedure:

| Workflow | Load These Files |
|---|---|
| **Critique a song** | `core/methodology/critique.md` + `references/CRITIQUE_REFERENCE.md` + `references/SUNO_STYLE_GENRE_REFERENCE.md` |
| **Write a song** | `core/methodology/songwriting.md` + `SONGWRITING_KNOWLEDGE_BASE.md` |
| **Optimize for Suno** | `core/methodology/suno-optimization.md` + `references/SUNO_TAGS_REFERENCE.md` |
| **Album continuity** | `core/methodology/album-continuity.md` + your album bible |
| **Character voice** | `core/methodology/character-voice.md` + `references/CHARACTER_VOICE_REFERENCE.md` |

### Example Prompts

**For ChatGPT/Claude/etc:**
```
I've loaded the critique methodology. Please critique the following song 
using the full 3-layer model (Core 12 + Advanced 5 + Suno Optimization).
Score each category 1-10 with one-sentence justification.

[paste your song here]
```

```
I've loaded the songwriting methodology. Write a song about [topic]. 
Follow the Nashville Method (chorus first) and output in full Suno-ready format.
```

### Deterministic Validation

For format checks that don't need AI judgment, use the validation script:

```bash
python3 tools/validate-song.py songs/my_song.md
python3 tools/validate-song.py --json songs/*.md
```

This checks character counts, required elements, tag compliance, and formatting rules.

### How This Differs from Kiro

| Aspect | With Kiro | Without Kiro |
|---|---|---|
| Methodology loading | Automatic via agents | Manual file loading |
| Format validation | Hooks fire on save | Run `tools/validate-song.py` manually |
| Album continuity | Agent checks on edit | Load methodology + bible, ask AI to check |
| Steering rules | Always-on context | Include in your system prompt |
| Skills | Activated on demand | Load the relevant methodology file |

---

## Sources

- Berklee Online, Pat Pattison (Berklee Professor)
- Franco Fabbri (genre theory — 5 rules of genre membership)
- Philip Tagg (music semiotics — musemes, cultural connotation of timbres)
- Patrik Juslin (BRECVEMA emotion psychology, emotional cue hierarchy)
- Allan F. Moore (functional texture layers, soundbox theory, style vs genre)
- Serge Lacasse (vocal staging, proxemic distance)
- Christian Schubart (key characteristics and emotional associations)
- Dodge et al. 2025 (6 universal evaluation criteria for popular music)
- stayen/suno-reference (November 2025 — v5.0 meta-tags)
- Suno AI official documentation + community testing (2025-2026)
- Suno community research: prompt formula (genre-first, 5-8 tags), era anchoring, genre combinations (70/30 rule), slider behavior, v5.5 features
- Battle-tested prompt engineering (real Suno playlist prompts)
- iZotope, The Song Foundry, American Songwriter, Nashville Guitar Studios

---

## License

This knowledge base is free to use, customize, and share. Attribution appreciated but not required.
