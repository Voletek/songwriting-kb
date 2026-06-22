---
name: songwriting
description: Professional songwriting power — activates the full song production system including craft methodology, Suno AI formatting, music theory, character voice design, and concept album continuity. Packages 4 agents, 5 skills, and complete knowledge base into one activatable bundle.
keywords: ["song", "songwriting", "write a song", "Suno", "lyrics", "music", "album", "track", "chorus", "verse", "hook", "melody", "chord", "production", "arrangement", "critique", "score", "write", "compose", "create", "make", "draft", "brainstorm", "song about", "track about", "bridge", "idea for a song", "let's make", "give me", "need a track", "help me write", "something about", "banger", "ballad", "anthem", "duet", "concept", "rate", "review", "evaluate", "assess", "analyze", "feedback", "thoughts on", "is this good", "what's wrong", "how to improve", "strengths", "weaknesses", "grade", "judge", "opinion", "does this work", "any issues", "what do you think", "fix this", "render", "format", "optimize", "tags", "char count", "character count", "ready to render", "will this work", "style prompt", "fix formatting", "prepare", "Suno-ready", "field check", "limits", "too long", "missing tags", "continuity", "consistent", "fits the album", "album rules", "blueprint", "check against", "matches", "sonic palette", "motifs", "callbacks", "track position", "differentiation", "does this break", "violations", "set up", "configure", "create blueprint", "new album", "new project", "add character", "build", "template", "initialize", "start fresh", "preferences", "log experiment", "add track", "get started", "onboarding", "help me set up", "first time", "new here"]
---

# 🎵 Songwriting Power

A professional song production system combining Nashville/LA co-writing craft with academic music theory, Suno AI formatting expertise, and concept album continuity management.

## What This Power Provides

### Agents (4 thin wrappers — load core/methodology/)
| Agent | Role | Loads | Invoke When |
|---|---|---|---|
| **songwriter** | Creates songs from concepts | `core/methodology/songwriting.md` | "Write a song about..." |
| **critic** | Multi-layer evaluation (12-cat craft + 5 advanced + Suno optimization + album-context) | `core/methodology/critique.md` | "Critique this song" / "Score this" |
| **suno-optimizer** | Post-processes for Suno v5.5 rendering | `core/methodology/suno-optimization.md` | "Make this Suno-ready" / "Optimize for Suno" |
| **album-continuity** | Verifies concept album rules | `core/methodology/album-continuity.md` | "Check continuity" / "Does this fit the album?" |

### Skills (5 on-demand knowledge sets)
| Skill | Contains | Activate When |
|---|---|---|
| **song-critique** | References `core/methodology/critique.md` + scoring rubric + report template + style/genre data | Evaluating any song |
| **suno-meta-tags** | Comprehensive tag reference, v5.5 features (Personas/Stems), layers, era tags, templates | Formatting for Suno |
| **music-theory** | 12 disciplines, 23-point framework, 18 advanced concepts | Deep production analysis |
| **character-voice** | References `core/methodology/character-voice.md` + accent/dialect data | Writing for characters |
| **concept-album-blueprint** | Track registry, motifs, continuity rules — configure with YOUR album | Album work |

### Steering (Always-on context)
- Core songwriting principles + 9-step workflow
- Suno formatting quick-reference (v5.5, Personas, Stems, Layers, Era Tags)
- Output format preferences (Production Notes, layers, hit formulas) — customizable
- Concept album framework (how to set up continuity, universal album rules)

### Hooks (Automated checks)
- Song format validation on file create
- Character count checking on file save
- Album continuity checking on album file save
- Prosody linting on file save

---

## Quick Start

### Output Locations
| Type | Directory |
|---|---|
| Songs | `songs/[album_or_category]/` |
| Critique reports | `analysis/[title]_critique.md` |
| Continuity reports | `analysis/[title]_continuity.md` |
| Optimization reports | `analysis/[title]_suno_optimization.md` |

### Write a New Song
```
"Write a song about [concept]"
```
→ Songwriter agent activates. Applies 9-step analysis. Outputs full Suno-ready format with Production Notes.

### Critique an Existing Song
```
"Critique/score [song file or pasted lyrics]"
```
→ Critic agent activates. Returns:
- **Layer 1:** 12-category craft scores + composite
- **Layer 2:** 5 advanced assessments (Moore functional layers, Lacasse proxemics, Tagg musemics, Scope of Vision, Skip Test) + advanced composite
- **Layer 3 (album tracks):** 6 album-context checks (position, intention vs delivery, transitions, dramatic irony, motifs, sonic differentiation)
- **Calibration:** Self-score delta, layer audit, production-lyric alignment, discovery depth
- Strongest line, flagged issues with fixes, priority recommendations ordered by impact

For quick feedback, ask: "Quick score this" → Core 12 only.

### Optimize for Suno
```
"Make this Suno-ready" / "Optimize [song] for Suno"
```
→ Suno-optimizer agent activates. Adds meta-tags, checks char counts, converts to v5.0 format. Does NOT change creative content.

### Check Album Continuity
```
"Does this fit the album?" / "Check continuity for Track X"
```
→ Album-continuity agent activates. Runs 10-rule check, verifies sonic palette, motifs, character voices, key relationships.

### Full Pipeline (Write → Critique → Optimize → Verify)
```
"Write a song about [X], run it through the full pipeline"
```
1. Songwriter creates it
2. Critic scores it (flag issues)
3. Songwriter revises (fix flagged issues)
4. Suno-optimizer formats it
5. Album-continuity verifies it (if album track)

---

## The 9-Step Professional Workflow

Applied to every song concept:

1. **SEMANTIC** — What is it literally about?
2. **EMOTIONAL** — Central affect? BRECVEMA mechanisms?
3. **PROSODIC** — Stresses, breaths, syllables (7-12 max per line)
4. **NARRATIVE** — Arc type? Where is the turn?
5. **VOICE** — Who speaks? Accent? Register?
6. **GENRE** — Fabbri's 5 rules? Fusion ratio?
7. **ARRANGEMENT** — Growth pattern? Contrast? Negative space?
8. **PRODUCTION** — Timbre? Harmony? Space?
9. **COMMERCIAL** — Audience? Platform? Length? Sync?

---

## Quality Standards

- Every word earns its place — no filler
- Hook passes "would someone text this line?" test
- No line exceeds 12 syllables at song tempo
- V2 adds NEW information
- Bridge contains a TURN
- Hook arrives within 15 seconds of first sung vocal
- Full chorus typically arrives within 45-60 seconds of track start
- ABCB default rhyme scheme
- Near/slant rhymes preferred over forced perfect
- Artist names in creative direction converted to descriptive production language (no artist names in Style Prompt or Production Direction)

---

## Architecture

```
core/methodology/  ← Single source of truth (complete methods)
       ↓
.kiro/agents/      ← Thin wrappers (persona + #[[file:core/methodology/X.md]])
.kiro/steering/    ← Quick-reference rules (always-on)
.kiro/skills/      ← On-demand deep knowledge (references core/ + references/)
tools/             ← Deterministic validation (Python CLI)
```

---

## Knowledge Base

This power draws from:
- `core/methodology/*.md` — 5 canonical methodology files (source of truth)
- `SONGWRITING_KNOWLEDGE_BASE.md` — 13 sections of craft + Suno system
- `MUSIC_PRODUCTION_THEORY.md` — 12 disciplines + 23-point framework
- `references/CRITIQUE_REFERENCE.md` — Detailed scoring rubric tables
- `references/CRITIQUE_REPORT_TEMPLATE.md` — Standardized report output format
- `references/SUNO_STYLE_GENRE_REFERENCE.md` — Genre/key/BPM/instrument optimization data
- `references/SUNO_TAGS_REFERENCE.md` — All meta-tags, v5.5 features, parenthetical layers
- `references/CHARACTER_VOICE_REFERENCE.md` — Voice design system
- `tools/validate-song.py` — Deterministic format/char validation

---

## Steering Files

The following steering files provide always-on context:

Top-level (`.kiro/steering/` — auto-loaded in every session):
- `songwriting.md` — Core principles + 9-step workflow
- `suno-formatting.md` — Suno rules + creative sliders
- `output-preferences.md` — Output format preferences (customize for your own)
- `concept-album.md` — Album continuity framework + setup guide

Power-specific (`.kiro/powers/songwriting/steering/` — condensed versions):
- `craft.md` — Principles quick-ref
- `preferences.md` — Format requirements quick-ref
- `suno.md` — Suno essentials quick-ref
