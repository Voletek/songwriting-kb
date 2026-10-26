# core/ — Canonical Methodology (Single Source of Truth)

> These files ARE the songwriting system. Everything else references them.

---

## What This Directory Contains

7 complete, self-contained methodology files plus `tenets.md` (7 creative tenets — which rule wins when rules conflict). Each methodology file is independently followable — you do NOT need Kiro, any specific AI assistant, or any other file to execute the method (though `references/` files provide deeper data tables).

| File | What It Is | Lines |
|---|---|---|
| `methodology/critique.md` | The complete multi-layer song critique method (12 categories + 5 advanced + Suno optimization + album-context + calibration) | ~520 |
| `methodology/songwriting.md` | The complete Nashville-method song creation process (5 phases, 27 steps, quality gates) | ~670 |
| `methodology/song-planning.md` | The guided Song Brief planning method (12 brief sections, guided vs auto-pilot, stop-or-flow) | ~270 |
| `methodology/suno-optimization.md` | The complete Suno rendering optimization process (V6 Procedure (default) + v5.5-era 13-step procedure (legacy), tags, compliance) | ~720 |
| `methodology/album-continuity.md` | The complete concept album continuity system (setup + extension + verification) | ~470 |
| `methodology/character-voice.md` | The complete character voice design process (11 steps, vocal + non-vocal templates) | ~290 |
| `methodology/builder.md` | The interactive setup method (albums, blueprints, steering, hooks, character voices, preferences, experiment logs) | ~250 |

---

## How These Are Used

### By Kiro (automatic)
`.kiro/agents/` files list the methodology in their `resources:` front matter (e.g. `file://core/methodology/critique.md`) — Kiro loads it into the agent's context when the agent is invoked.

### By other AI assistants (manual)
Paste the relevant methodology file into your assistant's context window. See the main README's "Using Without Kiro" section for which files to combine per workflow.

### By humans (manual)
Read the methodology file as a step-by-step guide. Follow the procedure directly.

### By CLI tools (deterministic)
- `tools/validate-song.py` implements the deterministic parts of `suno-optimization.md`: character counts (Step 1), termination (Step 7), obsolete tags (Step 8), artist/gear-name flags (Steps 9/9b), required elements, the Exclude-field format, and the V6 tag checks (V6 Procedure).
- `tools/lyric-lint.py` covers the prosody/rhyme side of `songwriting.md` and `critique.md`: syllables per line, stress, rhyme type, rhyme scheme, section stability, clichés.
- Craft judgement (hook, arc, imagery, emotional intelligence) stays with the critic.

---

## The Rule

> **When the method changes, update the file in `core/methodology/`. Everything downstream inherits.**
>
> Do NOT update `.kiro/agents/` with methodology content — they are thin loaders only.
> Do NOT duplicate methodology in `.kiro/sops/` — SOPs point here as the canonical source.

---

## Relationship to Other Directories

| Directory | Relationship to `core/` |
|---|---|
| `.kiro/agents/` | Loads `core/methodology/` via `resources:` front matter (thin wrappers) |
| `.kiro/sops/` | Kiro-formatted step lists that point to `core/methodology/` as canonical; if they diverge, `core/` wins |
| `.kiro/steering/` | Contains quick-reference SUBSETS derived from core methodology |
| `.kiro/skills/` | References `core/methodology/` + `references/` for on-demand deep loading |
| `references/` | Deep data tables (scoring rubrics, genre maps, tag lists, rhyme craft) REFERENCED BY core methodology |
| `tools/` | Deterministic implementations of core methodology rules |
| `experiments/suno/` | Evidence logs for Suno-specific claims in core methodology |
| `plugins/` | Suno Studio audio-effect plugins (post-render audio processors), a separate concern from the methodology; not consumed by `core/` |
