---
name: songwriting
description: Professional songwriting power — activates the full song production system including craft methodology, Suno AI formatting, music theory, character voice design, and concept album continuity. Packages 6 agents, 5 skills, 9 SOPs, steering, hooks, and the complete knowledge base into one activatable bundle. Suno V6 is the default format.
keywords: ["song", "songwriting", "write a song", "Suno", "lyrics", "music", "album", "track", "chorus", "verse", "hook", "melody", "chord", "production", "arrangement", "critique", "score", "write", "compose", "create", "make", "draft", "brainstorm", "song about", "track about", "bridge", "idea for a song", "let's make", "give me", "need a track", "help me write", "something about", "banger", "ballad", "anthem", "duet", "concept", "rate", "review", "evaluate", "assess", "analyze", "feedback", "thoughts on", "is this good", "what's wrong", "how to improve", "strengths", "weaknesses", "grade", "judge", "opinion", "does this work", "any issues", "what do you think", "fix this", "render", "format", "optimize", "tags", "char count", "character count", "ready to render", "will this work", "style prompt", "fix formatting", "prepare", "Suno-ready", "field check", "limits", "too long", "missing tags", "continuity", "consistent", "fits the album", "album rules", "blueprint", "check against", "matches", "sonic palette", "motifs", "callbacks", "track position", "differentiation", "does this break", "violations", "set up", "configure", "create blueprint", "new album", "new project", "add character", "build", "template", "initialize", "start fresh", "preferences", "log experiment", "add track", "get started", "onboarding", "help me set up", "first time", "new here"]
---

# 🎵 Songwriting Power

A professional song production system combining Nashville/LA co-writing craft with academic music theory, Suno AI formatting expertise, and concept album continuity management.

## What This Power Provides

### Agents (6 thin wrappers — load core/methodology/)
| Agent | Role | Loads | Invoke When |
|---|---|---|---|
| **song-planner** | Builds an approvable Song Brief before lyrics (guided) | `core/methodology/song-planning.md` | "Plan a song about..." / "Song brief" |
| **songwriter** | Creates songs from concepts | `core/methodology/songwriting.md` | "Write a song about..." |
| **critic** | Multi-layer evaluation (12-cat craft + 5 advanced + Suno optimization + album-context) | `core/methodology/critique.md` | "Critique this song" / "Score this" |
| **suno-optimizer** | Post-processes for Suno rendering (V6 default; v5.5-era procedure kept as legacy) | `core/methodology/suno-optimization.md` | "Make this Suno-ready" / "Optimize for Suno" |
| **album-continuity** | Verifies concept album rules | `core/methodology/album-continuity.md` | "Check continuity" / "Does this fit the album?" |
| **builder** | Interactive setup: albums, blueprints, character voices, preferences, experiment logs | `core/methodology/builder.md` | "Set up a new album" / "Help me get started" |

### Skills (5 on-demand knowledge sets)
| Skill | Contains | Activate When |
|---|---|---|
| **song-critique** | References `core/methodology/critique.md` + scoring rubric + report template + style/genre data | Evaluating any song |
| **suno-meta-tags** | V6 tag paradigm (Style=WHAT / Lyrics=HOW, `[Instrument: X In/Out]`) + layers, templates; v5.5-era tags/features (Personas/Stems, era tags) as legacy | Formatting for Suno |
| **music-theory** | 13 disciplines, 23-point framework, 18 advanced concepts | Deep production analysis |
| **character-voice** | References `core/methodology/character-voice.md` + accent/dialect data | Writing for characters |
| **concept-album-blueprint** | Track registry, motifs, continuity rules — configure with YOUR album | Album work |

### SOPs (9 step-by-step procedures, `.kiro/sops/`)
01 Writing · 02 Critiquing · 03 Optimizing for Suno · 04 Album setup · 05 Extending an album · 06 Character voice · 07 Full pipeline · 08 Contributing · 09 Planning a song

### Steering
- Core songwriting principles + 9-step workflow (always)
- Suno formatting quick-reference — V6 first, legacy v5.5-era mechanics labelled (always)
- Output format preferences (Production Notes, layers, hit formulas) — customizable (always)
- Concept album framework (how to set up continuity, universal album rules) (auto — loads on album requests)
- Manual commands: `/quick-score` and `/full-pipeline` (or `#quick-score`, `#full-pipeline`)

### Hooks (Kiro v1 JSON, `.kiro/hooks/*.json`)
- `song-validate.json` — on create/save of song files under `songs/`: runs `python3 tools/validate-song.py --hook {{filePath}}` (char counts, required elements, V6 tag checks, exclusions format)
- `prosody-lint.json` — on save of song files under `songs/`: runs `python3 tools/lyric-lint.py --hook {{filePath}}` (syllables, stress, rhyme, section stability, clichés)
- Both skip `README.md` and `*.brief.md`; file-event hooks fire only for agent-made file changes. Hooks run in Kiro IDE 1.0+ and Kiro CLI V3; Kiro Web sessions don't run hooks — run the tools manually there.
- Album continuity: example hooks live in `examples/albums/*/continuity-hook.json` — copy one into `.kiro/hooks/` (e.g. `.kiro/hooks/<album>-continuity.json`) to enable it

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

For quick feedback, ask: "Quick score this" or run `/quick-score` → Core 12 only.

### Optimize for Suno
```
"Make this Suno-ready" / "Optimize [song] for Suno"
```
→ Suno-optimizer agent activates. Splits Style / Exclude / Lyrics, applies V6 tags (`[Instrument: X In/Out]`, `[Dynamic:]`, `[Vocal:]`, `[End]`), checks char counts. Does NOT change creative content.

### Check Album Continuity
```
"Does this fit the album?" / "Check continuity for Track X"
```
→ Album-continuity agent activates. Checks the blueprint's hard rules (12 per bundled example blueprint), verifies sonic palette, motifs, character voices, key relationships.

### Full Pipeline (Write → Critique → Revise → Optimize → Verify)
```
"Write a song about [X], run it through the full pipeline"   (or /full-pipeline on an existing song)
```
1. Songwriter creates it (optionally from an approved Song Brief — song-planner)
2. Critic scores it (flag issues)
3. Songwriter revises (fix flagged issues)
4. Suno-optimizer formats it, then `python3 tools/validate-song.py <file>` and `python3 tools/lyric-lint.py <file>`
5. Album-continuity verifies it (if album track)

---

## The 9-Step Professional Workflow

Applied to every song concept:

1. **SEMANTIC** — What is it literally about?
2. **EMOTIONAL** — Central affect? BRECVEMA mechanisms?
3. **PROSODIC** — Stresses, breaths, syllable counts (target 7-12 per line), rhyme & stability plan
4. **NARRATIVE** — Arc type? Where is the turn?
5. **VOICE** — Who speaks? Accent? Register?
6. **GENRE** — Which of Fabbri's genre-rule types carry the weight here? Fusion ratio (70/30)?
7. **ARRANGEMENT** — Growth pattern? Contrast? Negative space?
8. **PRODUCTION** — Timbre? Harmony? Space?
9. **COMMERCIAL** — Audience? Platform? Length? Sync?

---

## Quality Standards

- Every word earns its place — no filler
- Hook passes "would someone text this line?" test
- [Tier 2] Target 7-12 syllables per line; 13-15 = review stress density and singability at tempo; 16+ = apply the Compression Test (or justify as intentional)
- [Tier 2] V2 usually adds new information or a new angle (unless reiteration is part of the form)
- [Tier 2] Bridge often works best when it creates contrast or a turn (semantic, musical, textural, or energetic); 3-6 lines (up to 8 when the turn needs it)
- [Tier 2] Hook signal within ~5-30 s of the first SUNG word (genre-dependent: pop earlier, cinematic/progressive later)
- [Tier 2] Separately, the full chorus typically arrives by ~45-60 s of track time in pitch-ready commercial songs (pop average ~39 s) — a different metric, not a conflict
- [Tier 2] No universal rhyme-scheme default: ABCB (XAXA) is a common conversational option with less closure; choose per section (stable/closed for choruses, open for pre-choruses/bridges)
- Strongest rhyme that doesn't bend meaning or syntax — perfect/family for closure, looser (assonance/consonance) for motion; never force syntax. See `references/RHYME_AND_LYRIC_CRAFT.md`
- Artist names in creative direction converted to descriptive production language (no artist names in Style Prompt or Production Direction)

---

## Architecture

```
core/methodology/  ← Single source of truth (complete methods)
       ↓
.kiro/agents/      ← Thin wrappers (persona + `resources: [file://core/methodology/X.md]` front matter)
.kiro/steering/    ← Quick-reference rules (always / auto / manual)
.kiro/skills/      ← On-demand deep knowledge (references core/ + references/)
.kiro/hooks/       ← v1 JSON hooks that run the Python tools on song saves
tools/             ← Deterministic validation (validate-song.py, lyric-lint.py, check-repo.py)
```

---

## Knowledge Base

This power draws from:
- `core/methodology/*.md` — 7 canonical methodology files (source of truth)
- `core/tenets.md` — 7 creative tenets (which rule wins when rules conflict)
- `SONGWRITING_KNOWLEDGE_BASE.md` — 13 sections of craft + Suno system
- `MUSIC_PRODUCTION_THEORY.md` — 13 disciplines + 23-point framework + 18 advanced concepts
- `references/RHYME_AND_LYRIC_CRAFT.md` — Rhyme ladder, schemes & section stability, meter, singability
- `references/CRITIQUE_REFERENCE.md` — Detailed scoring rubric tables
- `references/CRITIQUE_REPORT_TEMPLATE.md` — Standardized report output format
- `references/SUNO_STYLE_GENRE_REFERENCE.md` — Genre/key/BPM/instrument optimization data
- `references/V6_TAG_REFERENCE.md` / `references/V6_TAG_DISCOVERY.md` — V6 tag dictionary + how/why and results log
- `references/SUNO_TAGS_REFERENCE.md` — v5.x meta-tags (legacy), parenthetical layers, v5.5 features
- `references/CHARACTER_VOICE_REFERENCE.md` — Voice design system
- `tools/validate-song.py` — Deterministic format/char/V6-tag validation
- `tools/lyric-lint.py` — Deterministic syllable/stress/rhyme/section-stability/cliché lint

---

## Steering Files

Top-level (`.kiro/steering/` — 6 files):
- `songwriting.md` (`always`) — Core principles + 9-step workflow
- `suno-formatting.md` (`always`) — V6 Suno rules + legacy v5.5-era mechanics
- `output-preferences.md` (`always`) — Output format preferences (customize for your own)
- `concept-album.md` (`auto`) — Album continuity framework + setup guide; loads on album-related requests
- `quick-score.md` (`manual`) — `/quick-score`: fast 12-category score of a song
- `full-pipeline.md` (`manual`) — `/full-pipeline`: Write → Critique → Revise → Optimize → Verify

Power-specific (`.kiro/powers/songwriting/steering/` — condensed versions):
- `craft.md` — Principles quick-ref
- `preferences.md` — Format requirements quick-ref
- `suno.md` — Suno essentials quick-ref
