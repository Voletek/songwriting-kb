# core/ — Canonical Methodology (Single Source of Truth)

> These files ARE the songwriting system. Everything else references them.

---

## What This Directory Contains

5 complete, self-contained methodology files. Each is independently followable — you do NOT need Kiro, any specific AI assistant, or any other file to execute the method (though `references/` files provide deeper data tables).

| File | What It Is | Lines |
|---|---|---|
| `methodology/critique.md` | The complete multi-layer song critique method (12 categories + 5 advanced + Suno optimization + album-context + calibration) | ~492 |
| `methodology/songwriting.md` | The complete Nashville-method song creation process (5 phases, 27 steps, quality gates) | ~465 |
| `methodology/suno-optimization.md` | The complete Suno rendering optimization process (12 steps, tags, sliders, compliance) | ~451 |
| `methodology/album-continuity.md` | The complete concept album continuity system (setup + extension + verification) | ~466 |
| `methodology/character-voice.md` | The complete character voice design process (11 steps, vocal + non-vocal templates) | ~300 |

---

## How These Are Used

### By Kiro (automatic)
`.kiro/agents/` files contain `#[[file:core/methodology/X.md]]` — Kiro loads the methodology into the agent's context automatically when invoked.

### By other AI assistants (manual)
Paste the relevant methodology file into your assistant's context window. See the main README's "Using Without Kiro" section for which files to combine per workflow.

### By humans (manual)
Read the methodology file as a step-by-step guide. Follow the procedure directly.

### By CLI tools (deterministic)
`tools/validate-song.py` implements the format/compliance checks from `suno-optimization.md` as deterministic code.

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
| `.kiro/agents/` | Loads `core/methodology/` via `#[[file:]]` (thin wrappers) |
| `.kiro/sops/` | Points to `core/methodology/` as canonical source (may become redundant) |
| `.kiro/steering/` | Contains always-on quick-reference SUBSETS derived from core methodology |
| `.kiro/skills/` | References `core/methodology/` + `references/` for on-demand deep loading |
| `references/` | Deep data tables (scoring rubrics, genre maps, tag lists) REFERENCED BY core methodology |
| `tools/` | Deterministic implementations of core methodology rules |
| `experiments/suno/` | Evidence logs for Suno-specific claims in core methodology |
