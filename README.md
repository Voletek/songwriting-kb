# Songwriting Knowledge Base

A professional song production system combining Nashville/LA co-writing craft, academic music theory (12 disciplines), Suno AI v5.0 formatting expertise, and concept album continuity management — packaged as a complete Kiro IDE ecosystem with step-by-step SOPs for every workflow.

---

## Quick Start

Clone this repo. The `.kiro/` directory auto-configures Kiro with agents, skills, hooks, power, steering, and SOPs.

```bash
git clone https://github.com/Voletek/songwriting-kb.git
```

Then just talk:
```
"Write a song about..."       → Songwriter agent activates
"Critique this song"          → Critic agent scores (12 categories)
"Make this Suno-ready"        → Suno-optimizer adds meta-tags
"Check album continuity"      → Album-continuity verifies rules
```

For step-by-step guidance, see the **SOPs** (`.kiro/sops/`).

---

## Repository Structure

```
songwriting-kb/
├── .kiro/
│   ├── steering/              4 files — auto-loaded every session
│   ├── skills/                5 skills — loaded on demand
│   ├── hooks/                 4 hooks — automated on file events
│   ├── agents/                4 agents — invocable specialized roles
│   ├── powers/songwriting/    1 power — activatable master bundle
│   └── sops/                  8 SOPs — step-by-step procedures
├── references/                4 companion docs for skills
├── songs/                     Album tracks + experimental + standalone
├── SONGWRITING_KNOWLEDGE_BASE.md    Master craft reference (13 sections)
└── MUSIC_PRODUCTION_THEORY.md       Academic framework (12 disciplines)
```

---

## SOPs (Standard Operating Procedures)

The procedural layer — step-by-step HOW for every workflow:

| # | SOP | What It Covers | Time |
|---|---|---|---|
| **01** | [Writing a Song](/.kiro/sops/01-writing-a-song.md) | 27 steps: concept → analysis → writing → QA → formatting | 50-75 min |
| **02** | [Critiquing a Song](/.kiro/sops/02-critiquing-a-song.md) | 8 steps: read → 9-step analysis → score → flag → recommend | 30-35 min |
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
| **songwriter** | Creates complete songs from concepts using Nashville method, outputs Suno-ready format with Production Notes | "Write a song about X" |
| **critic** | Scores songs on 12 categories (1-10), identifies strongest line, flags issues with alternatives | "Critique this" / "Score this song" |
| **suno-optimizer** | Adds meta-tags, checks char counts, validates pipe params, converts to v5.0 format. Does NOT change creative content | "Make this Suno-ready" |
| **album-continuity** | Runs hard rules, verifies sonic palette, motifs, character voices, key relationships | "Check continuity" |

---

## Skills (On-Demand Knowledge)

| Skill | Contains | Activate When |
|---|---|---|
| **song-critique** | 12-category rubric, scoring examples, flag patterns | Evaluating any song |
| **suno-meta-tags** | 35 confirmed tags, v5.0 techniques, slider guide, templates | Formatting for Suno |
| **music-theory** | 12 disciplines, 23-point framework, 18 advanced concepts | Deep production analysis |
| **character-voice** | Accent/dialect system, voice design template, instrumentation maps | Writing for characters |
| **concept-album-bible** | Track registry, motifs, continuity rules (template + example) | Album work |

---

## Hooks (Automated Quality Checks)

| Hook | Fires On | Checks |
|---|---|---|
| **song-format-check** | File create in `songs/` | Required sections present |
| **suno-char-count** | File save in `songs/` | Style ≤1000, Lyrics ≤5000 |
| **prosody-lint** | File save in `songs/` | Lines >12 syllables, stuffed phrases |
| **continuity-check** | File save in album dirs | Sonic palette, key rules, phrase protection |

---

## Steering (Always-On Context)

| File | Purpose |
|---|---|
| `songwriting.md` | Core principles + 9-step workflow + quality gates |
| `suno-formatting.md` | Suno rules, limits, essential tags, creative sliders |
| `voletek-preferences.md` | Output format (customize for your own preferences) |
| `concept-album.md` | Album continuity rules (replace with your own album) |

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
12. Suno AI Complete System (formatting, duet modes, hit formulas)
13. **Suno Advanced Meta-Tags & v5.0** (35 tags, pipe notation, controls, sliders)

### MUSIC_PRODUCTION_THEORY.md
- 12 Academic Disciplines
- 23-Point Song Development Framework
- 18 Advanced Concepts
- Vocal Accent & Dialect Phonetics (real-world + fantasy)

---

## Suno AI Integration

### Field Limits
| Field | Limit | Notes |
|---|---|---|
| Style of Music | 1000 chars | Genre, BPM, mood, instruments, vocal |
| Lyrics | 5000 chars | Must fit — no overflow option |
| Exclude | Dedicated field | Negative prompts ONLY |

### Creative Sliders
| Slider | Default | Effect |
|---|---|---|
| Weirdness | 50% | Safe (0%) ↔ Chaos (100%) — creative latitude |
| Style Influence | 50% | How much Style Prompt steers output |
| Audio Influence | ~45% | How much reference track affects output (Inspo only) |

### 5 Formatting Modes
| Mode | Use Case |
|---|---|
| **A** — Per-Line Vocal Tags | Intimate cinematic dialogue |
| **B** — Parenthetical () | Space-efficient call-and-response |
| **C** — Theatrical/Concept | Multi-layer concept albums |
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

---

## Community Use

This system is designed for sharing. The architecture separates **universal** from **personal**:

### Universal (works for anyone — 72% of system):
- All knowledge base files
- All SOPs
- Songwriter, Critic, Suno-Optimizer agents
- All skills (except album-bible content)
- Format-check, char-count, prosody-lint hooks
- All reference docs (except album bible)

### Personal (customize for your projects — 28% of system):
- `concept-album.md` — replace with YOUR album rules
- `voletek-preferences.md` — rename and set YOUR preferences
- `FRACTURED_SHADOWS_BIBLE.md` — replace with YOUR album bible
- Album-continuity agent — configure YOUR rules
- Continuity-check hook — set YOUR violations

### Getting Started (Community):
```bash
git clone https://github.com/Voletek/songwriting-kb.git
cd songwriting-kb
# See SOP 08 for full setup guide
# See SOP 04 to create your own concept album
```

---

## The Concept Album: Fractured Shadows (Example)

Included as a **reference implementation** showing how a completed album system looks.

### Album Thesis
> "The fracture made the shadows — but the shadows made the dawn."

### Track Listing (17 tracks, 2 acts)

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

**Sonic Evolution:**
```
Industrial/Glitch → Tribal/Primal → Cinematic Orchestral → Folk Rock → Full Orchestra + Key Change
```

---

## Sources

- Berklee Online, Pat Pattison (Berklee Professor)
- Franco Fabbri (genre theory), Philip Tagg (music semiotics)
- Patrik Juslin (BRECVEMA emotion psychology)
- stayen/suno-reference (November 2025 — v5.0 meta-tags)
- Suno AI official documentation
- Battle-tested prompt engineering (real Suno playlist prompts)
- iZotope, The Song Foundry, American Songwriter, Nashville Guitar Studios

---

## License

This knowledge base is free to use, customize, and share. Attribution appreciated but not required.
