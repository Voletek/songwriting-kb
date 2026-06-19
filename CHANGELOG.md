# Changelog

All notable changes to this project will be documented in this file.

---

## [Unreleased]

---

## [2.0.0] — June 2026

### Architecture Refactor: Methodology as Source of Truth

**Breaking change:** Song and analysis files moved from working directories to examples.

#### Added
- `core/methodology/` — 5 canonical methodology files (2,174 lines total) as single source of truth
  - `critique.md` (492 lines) — complete multi-layer critique model
  - `songwriting.md` (465 lines) — complete Nashville-method song creation
  - `suno-optimization.md` (451 lines) — complete Suno rendering optimization
  - `album-continuity.md` (466 lines) — complete concept album continuity
  - `character-voice.md` (300 lines) — complete character voice design
- `tools/validate-song.py` — deterministic Python CLI validator (char counts, required tags, format checks)
- `experiments/suno/` — Suno experiment logging framework (README + TEMPLATE.yml)
- `docs/ARCHITECTURE_PLAN.md` — full architecture documentation with credits
- `core/README.md` — explains the source-of-truth structure
- `examples/songs/` — all example songs organized by album/category
- `examples/analysis/` — all example critique reports
- "Using Without Kiro" section in README — platform-neutral access instructions
- Suno Version Status table in `references/SUNO_STYLE_GENRE_REFERENCE.md`

#### Changed
- `.kiro/agents/` — all 4 agents rewritten as thin wrappers (load `core/methodology/` via `#[[file:]]`)
- `.kiro/skills/` — all 5 skills rewired to reference `core/methodology/`
- `.kiro/sops/` — all 6 relevant SOPs have deprecation notes pointing to canonical source
- `README.md` — new Architecture section, updated repo structure, dual quick-start (Kiro + non-Kiro)
- `.kiro/README.md` — reframed as "Kiro Automation Layer" with architecture diagram
- `WORKFLOW_DIAGRAM.md` — updated for thin-agent architecture
- `.kiro/powers/songwriting/POWER.md` — updated architecture description

#### Moved
- `songs/*` → `examples/songs/` (songs/ is now empty user workspace)
- `analysis/*` → `examples/analysis/` (analysis/ is now empty user workspace)

#### Credits
- Architecture refactor catalyzed by Brian Smith Clark ([@multi-lang](https://github.com/multi-lang))
- Directory restructure (songs/ and analysis/ separation) driven by community feedback from 21machines

---

## [1.5.0] — June 2026

### Suno Optimization Assessment + Genre Research

#### Added
- `references/SUNO_STYLE_GENRE_REFERENCE.md` — 600+ line comprehensive reference
- Suno Optimization Assessment module integrated into critic
- `references/CRITIQUE_REPORT_TEMPLATE.md` — standardized template for all critique outputs

#### Changed
- Critic agent, skill, SOP, and reference updated for Suno Optimization Assessment
- Steering files: added `inclusion: auto` frontmatter for Kiro auto-loading

---

## [1.4.0] — June 2026

### Album Universalization

#### Changed
- All Act 2 + Act 3 tracks (11 songs) revised to remove book-specific lore
- Replaced plot-exposition lyrics with emotional-experience lyrics

#### Added
- Act 2 Book Specificity Analysis

---

## [1.3.0] — June 2026

### Critique System Upgrade

#### Added
- 3-layer critique model (Core 12 + Advanced 5 + Album-Context)
- Academic framework integration (Moore, Tagg, Lacasse, Moylan, Pattison, Fabbri, Juslin, Dodge)
- `references/CRITIQUE_REFERENCE.md` — full scoring rubric
- Decision gate system (8.5 threshold)

---

## [1.2.0] — May-June 2026

### Concept Album Development

#### Added
- Fractured Shadows (17 tracks, 3 acts)
- Keeper of the Light (8 tracks, folk-horror)
- Album bible system + character voice design

---

## [1.1.0] — May 2026

### Suno v5.5 Integration

#### Added
- v5.5 features (Personas, Stems, Custom Models)
- Era tags, creative sliders, advanced meta-tags
- Parenthetical layer system

---

## [1.0.0] — May 2026

### Initial Release

#### Added
- Complete songwriting knowledge base (13 sections)
- Music production theory (12 disciplines)
- 4 agents, 5 skills, 8 SOPs, 4 steering files, 3 hooks
- Songwriting power bundle
