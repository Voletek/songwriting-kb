---
name: songwriting
description: Professional songwriting power — activates the full song production system including craft methodology, Suno AI formatting, music theory, character voice design, and concept album continuity. Packages 4 agents, 5 skills, and complete knowledge base into one activatable bundle.
keywords: ["song", "songwriting", "write a song", "Suno", "lyrics", "music", "album", "track", "chorus", "verse", "hook", "melody", "chord", "production", "arrangement", "critique", "score"]
---

# 🎵 Songwriting Power

A professional song production system combining Nashville/LA co-writing craft with academic music theory, Suno AI formatting expertise, and concept album continuity management.

## What This Power Provides

### Agents (4 specialized roles)
| Agent | Role | Invoke When |
|---|---|---|
| **songwriter** | Creates songs from concepts | "Write a song about..." |
| **critic** | Scores/evaluates songs (12 categories) | "Critique this song" / "Score this" |
| **suno-optimizer** | Post-processes for Suno rendering | "Make this Suno-ready" / "Optimize for Suno" |
| **album-continuity** | Verifies concept album rules | "Check continuity" / "Does this fit the album?" |

### Skills (5 on-demand knowledge sets)
| Skill | Contains | Activate When |
|---|---|---|
| **song-critique** | 12-category rubric, scoring guide, flag patterns | Evaluating any song |
| **suno-meta-tags** | Comprehensive tag reference, v5.0 techniques, templates | Formatting for Suno |
| **music-theory** | 12 disciplines, 23-point framework, 18 advanced concepts | Deep production analysis |
| **character-voice** | Accent/dialect system, voice design template | Writing for characters |
| **concept-album-bible** | Track registry, motifs, continuity rules | Album work |

### Steering (Always-on context)
- Core songwriting principles + 9-step workflow
- Suno formatting quick-reference
- Voletek's output preferences (Production Notes, duet modes)
- Album continuity rules (10 hard rules, sonic palette)

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
→ Critic agent activates. Returns 12-category scores, strongest line, flagged issues with alternatives, priority recommendations.

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

---

## Knowledge Base

This power draws from:
- `SONGWRITING_KNOWLEDGE_BASE.md` — 13 sections of craft + Suno system
- `MUSIC_PRODUCTION_THEORY.md` — 12 disciplines + 23-point framework + accents
- `references/CRITIQUE_REFERENCE.md` — Scoring rubric
- `references/SUNO_TAGS_REFERENCE.md` — All meta-tags
- `references/CHARACTER_VOICE_REFERENCE.md` — Voice design system
- `references/FRACTURED_SHADOWS_BIBLE.md` — Album continuity bible

---

## Steering Files

The following steering files provide always-on context:

Top-level (`.kiro/steering/` — auto-loaded in every session):
- `songwriting.md` — Core principles + 9-step workflow
- `suno-formatting.md` — Suno rules + creative sliders
- `voletek-preferences.md` — Output format preferences (rename for your own)
- `concept-album.md` — Album continuity rules (replace with your own)

Power-specific (`.kiro/powers/songwriting/steering/` — condensed versions):
- `craft.md` — Principles quick-ref
- `preferences.md` — Format requirements quick-ref
- `suno.md` — Suno essentials quick-ref
