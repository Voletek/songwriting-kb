# .kiro/ — Kiro Automation Layer

> This directory is the **Kiro IDE automation adapter** for the songwriting methodology.
> The canonical methodology lives in `core/methodology/` — this directory wires it into Kiro's agent/skill/hook system.
> Agents here are THIN: they define persona + load the methodology via `#[[file:]]` references.

---

## Architecture

```
core/methodology/  ← Source of truth (complete methods)
       ↓
.kiro/agents/      ← Thin loaders (persona + #[[file:core/methodology/X.md]])
.kiro/steering/    ← Quick-reference rules (always-on subset)
.kiro/skills/      ← On-demand activation (loads core/ + references/)
.kiro/hooks/       ← Automated checks on file events
.kiro/sops/        ← Step-by-step procedures (point to core/ as canonical)
```

---

## Directory Overview

| Directory | Purpose | Loads When |
|---|---|---|
| `steering/` | Always-on context injected into every session | Automatically (every chat) |
| `agents/` | Thin wrappers that load `core/methodology/` files | On request ("write a song", "critique this") |
| `skills/` | On-demand knowledge (references core/ + references/) | When agent activates them or user requests |
| `hooks/` | Automated checks triggered by file events | On file create/save in matching patterns |
| `sops/` | Step-by-step procedures (canonical source is `core/methodology/`) | When user follows a workflow |
| `powers/` | Bundled capability packages | When activated via power system |
| `plugins/` | Suno Studio audio-effect plugins (post-render, applied to rendered audio in Suno Studio); not part of the Kiro agent/skill pipeline | Manually in Suno Studio (not by Kiro) |

---

## Steering Files (Always Active)

| File | What It Does | Customize? |
|---|---|---|
| `songwriting.md` | Core craft principles, 9-step workflow, quality gates | No — universal |
| `suno-formatting.md` | Suno AI field limits, tags, sliders, v5.5 features | No — universal |
| `output-preferences.md` | Song output format (Production Notes, layers, formulas) | **Yes** — your conventions |
| `concept-album.md` | Album continuity framework + setup guide | No — universal framework |

**To add album-specific steering:** Create a new file with `fileMatch` front-matter so it only loads when working on your album's files. See `examples/albums/` for the pattern.

---

## Agents (4 Thin Wrappers)

Each agent defines WHO it is and loads the methodology from `core/methodology/`:

| Agent | Invoke With | Loads |
|---|---|---|
| `songwriter` | "Write a song about X" | `core/methodology/songwriting.md` |
| `critic` | "Critique this" / "Score this" | `core/methodology/critique.md` |
| `suno-optimizer` | "Make this Suno-ready" | `core/methodology/suno-optimization.md` |
| `album-continuity` | "Check continuity" | `core/methodology/album-continuity.md` (**configure for YOUR album**) |

---

## Hooks (5 Automated Checks)

| Hook | Triggers On | Checks |
|---|---|---|
| `song-format-check.hook.json` | New file in `songs/` | All required sections present |
| `suno-char-count.hook.json` | Save in `songs/` | Style ≤1000, Lyrics ≤5000 |
| `prosody-lint.hook.json` | Save in `songs/` | Lines >12 syllables, stuffed phrases |
| `quick-score.hook.json` | On request | Fast 12-category scoring pass |
| `full-pipeline.hook.json` | On request | Complete pipeline flow |

**CLI alternative:** `python3 tools/validate-song.py songs/*.md` for deterministic checks without hooks.

---

## Skills (5 Knowledge Sets)

| Skill | Contains | Size |
|---|---|---|
| `song-critique` | 3-layer scoring framework, rubric definitions | Large |
| `suno-meta-tags` | Complete tag reference, v5.5, layers, sliders | Large |
| `music-theory` | 12 disciplines, 23-point framework, 18 advanced concepts | Very large |
| `character-voice` | Accent/dialect system, voice design template | Medium |
| `concept-album-blueprint` | Album continuity template (**configure for your album**) | Variable |

---

## SOPs (8 Procedures)

Step-by-step workflows that work with ANY AI assistant or manually:

| # | SOP | Use When |
|---|---|---|
| 01 | Writing a Song | Creating a new song from concept to Suno-ready |
| 02 | Critiquing a Song | Evaluating/scoring an existing song |
| 03 | Optimizing for Suno | Final formatting pass before rendering |
| 04 | Setting Up a Concept Album | Building your album blueprint, steering, and hooks |
| 05 | Extending an Album | Adding tracks to an existing album |
| 06 | Character Voice Design | Creating a voice for a specific character/accent |
| 07 | Full Pipeline | Complete write→critique→revise→optimize→verify flow |
| 08 | Contributing | Community setup guide and contribution rules |

---

## For kiro-cli Users

This system works identically in kiro-cli (headless mode). The steering files load automatically, agents are invocable, and hooks fire on file events. The only difference: creative sliders and Suno Personas are Suno UI features — you'll need to set those manually when rendering.

---

## Customization Priority

If you're new, customize in this order:
1. `steering/output-preferences.md` — Your format conventions
2. `agents/album-continuity.md` — Point `#[[file:]]` at YOUR album blueprint
3. Add a conditional steering file for your album (use `examples/` as template)
4. Add a continuity hook for your album

**To modify methodology:** Edit files in `core/methodology/` — agents will pick up changes automatically via `#[[file:]]` references.
