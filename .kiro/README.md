# .kiro/ — Kiro Automation Layer

> This directory is the **Kiro automation adapter** for the songwriting methodology.
> The canonical methodology lives in `core/methodology/` — this directory wires it into Kiro's agent/skill/hook/steering system.
> Agents here are THIN: they define a persona and load the methodology through `resources:` front matter
> (e.g. `resources: ["file://core/methodology/songwriting.md"]`). The `#[[file:path]]` include syntax is used only in steering files.

---

## Architecture

```
core/methodology/  ← Source of truth (complete methods)
       ↓
.kiro/agents/      ← Thin loaders (persona + `resources: [file://core/methodology/X.md]`)
.kiro/steering/    ← Quick-reference rules (always / auto / manual inclusion)
.kiro/skills/      ← On-demand activation (reads core/ + references/ by path)
.kiro/hooks/       ← Kiro v1 JSON hooks that run the deterministic tools on song saves
.kiro/sops/        ← Step-by-step procedures (point to core/ as canonical)
```

---

## Directory Overview

| Directory | Purpose | Loads When |
|---|---|---|
| `steering/` | Context rules (3 always-on, 1 auto, 2 manual commands) | `always` = every chat; `auto` = when the request matches its description; `manual` = `/name` or `#name` |
| `agents/` | Thin wrappers that load `core/methodology/` files | On request ("write a song", "critique this") |
| `skills/` | On-demand knowledge (references core/ + references/) | When an agent activates them or the user requests |
| `hooks/` | Automated checks on file events (v1 JSON) | On agent-made create/save of matching song files (Kiro IDE 1.0+ / Kiro CLI V3) |
| `sops/` | Step-by-step procedures (canonical source is `core/methodology/`) | When user follows a workflow |
| `powers/` | Bundled capability package (`powers/songwriting/`) | When activated via the power system |
| `settings/` | Workspace settings | Automatically |

`plugins/` (at the repo root) holds Suno Studio audio-effect plugins (post-render, applied to rendered audio in Suno Studio); it is not part of the Kiro agent/skill pipeline.

---

## Steering Files (6)

| File | Inclusion | What It Does | Customize? |
|---|---|---|---|
| `songwriting.md` | `always` | Core craft principles, 9-step workflow, quality gates | No — universal |
| `suno-formatting.md` | `always` | Suno V6 rules (default) + legacy v5.5-era mechanics, field limits, Exclude format | No — universal |
| `output-preferences.md` | `always` | Song output format (Production Notes, layers, formulas) | **Yes** — your conventions |
| `concept-album.md` | `auto` | Album continuity framework + setup guide; loads on album-related requests | No — universal framework |
| `quick-score.md` | `manual` | `/quick-score` (or `#quick-score`): fast 12-category score of a song | No |
| `full-pipeline.md` | `manual` | `/full-pipeline` (or `#full-pipeline`): Write → Critique → Revise → Optimize → Verify | No |

Front matter must be the very first bytes of a steering file (no blank line before `---`).

**To add album-specific steering:** Create a new file with `inclusion: fileMatch` + `fileMatchPattern` so it only loads when your album's files are in context. See `examples/albums/<album>/steering.md` for the pattern.

---

## Agents (6 Thin Wrappers)

Each agent defines WHO it is and loads the methodology from `core/methodology/` via `resources:` front matter:

| Agent | Invoke With | Loads |
|---|---|---|
| `song-planner` | "Plan a song about X" / "Song brief" | `core/methodology/song-planning.md` |
| `songwriter` | "Write a song about X" | `core/methodology/songwriting.md` |
| `critic` | "Critique this" / "Score this" | `core/methodology/critique.md` |
| `suno-optimizer` | "Make this Suno-ready" | `core/methodology/suno-optimization.md` |
| `album-continuity` | "Check continuity" | `core/methodology/album-continuity.md` (**configure for YOUR album**) |
| `builder` | "Set up a new album" / "Help me get started" | `core/methodology/builder.md` |

On Kiro Web, project agents are available for sub-agent delegation only.

---

## Hooks (2 hook files + 2 manual steering commands)

Hooks use the Kiro v1 schema (`.kiro/hooks/*.json`: `version`, `hooks[]` with `name`, `trigger`, optional `matcher`, `action`).

| Hook file | Trigger | Runs |
|---|---|---|
| `song-validate.json` | `PostFileCreate` + `PostFileSave` on song files under `songs/` | `python3 tools/validate-song.py --hook {{filePath}}` — deterministic char counts, required elements, V6 tag checks, exclusions format |
| `prosody-lint.json` | `PostFileSave` on song files under `songs/` | `python3 tools/lyric-lint.py --hook {{filePath}}` — syllables, stress, rhyme type/scheme, section stability, clichés |

- Both skip `README.md` and `*.brief.md`.
- File-event hooks fire only for agent-made file changes.
- Hooks run in Kiro IDE 1.0+ and Kiro CLI V3. **Kiro Web sessions do not run hooks** — run the tools manually there.
- Kiro v1 has no manual hooks, so the former quick-score / full-pipeline hooks are now manual steering commands: `/quick-score` and `/full-pipeline`.
- Album continuity: example hooks live in `examples/albums/<album>/continuity-hook.json` (v1 schema, `agent` action). Copy one to `.kiro/hooks/<album>-continuity.json` and edit its matcher and prompt to enable it.

**CLI (any platform):**
```bash
python3 tools/validate-song.py songs/        # files or directories (recursive); --json, --strict
python3 tools/lyric-lint.py songs/my_song.md # --json; pip install pronouncing for dictionary accuracy
python3 tools/check-repo.py                  # repo integrity: include/resource paths, hooks, steering, JSON
```

---

## Skills (5 Knowledge Sets)

| Skill | Contains | Size |
|---|---|---|
| `song-critique` | 3-layer scoring framework, rubric definitions | Large |
| `suno-meta-tags` | V6 tag paradigm + full tag reference; v5.5-era tags, features, sliders as legacy | Large |
| `music-theory` | 13 disciplines, 23-point framework, 18 advanced concepts | Very large |
| `character-voice` | Accent/dialect system, voice design template | Medium |
| `concept-album-blueprint` | Album continuity template (**configure for your album**) | Variable |

Skills reference files by plain path with explicit "read X" instructions.

---

## SOPs (9 Procedures)

Step-by-step workflows that work with ANY AI assistant or manually:

| # | SOP | Use When |
|---|---|---|
| 01 | Writing a Song | Creating a new song from concept to Suno-ready |
| 02 | Critiquing a Song | Evaluating/scoring an existing song |
| 03 | Optimizing for Suno | Final formatting pass before rendering (V6 path + legacy v5.5-era steps) |
| 04 | Setting Up a Concept Album | Building your album blueprint, steering, and hooks |
| 05 | Extending an Album | Adding tracks to an existing album |
| 06 | Character Voice Design | Creating a voice for a specific character/accent |
| 07 | Full Pipeline | Complete write→critique→revise→optimize→verify flow |
| 08 | Contributing | Community setup guide and contribution rules |
| 09 | Planning a Song | Guided Song Brief before any lyrics are written |

---

## For Kiro CLI Users

Steering, agents, and skills work in Kiro CLI. Hooks fire on file events in Kiro CLI V3 (agent-made changes only); in other environments run the `tools/` scripts yourself. Suno UI settings (V6 model choice, and the legacy v5.5-era sliders and Personas if your Suno UI still offers them) are set manually when rendering.

---

## Customization Priority

If you're new, customize in this order:
1. `steering/output-preferences.md` — Your format conventions
2. `agents/album-continuity.md` — Point its `resources:` blueprint entry at YOUR album blueprint
3. Add a conditional steering file for your album (use `examples/albums/<album>/steering.md` as template)
4. (Optional) Add a continuity hook for your album (copy `examples/albums/<album>/continuity-hook.json` to `.kiro/hooks/<album>-continuity.json`)

**To modify methodology:** Edit files in `core/methodology/` — agents pick up changes automatically because they load those files via `resources:`.
