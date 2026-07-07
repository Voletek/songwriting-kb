# Changelog

All notable changes to this project will be documented in this file.

---

## [Unreleased]

### Added
- Documented future improvement: audio render analysis tool for quantitative Suno render verification
- Performance notation symbols user-tested on Suno v5.5: ALL CAPS confirmed working (louder/forceful delivery); tilde unreliable; quotes no effect; dash = word separator not syllable stretcher; ellipsis marginal (reinforces existing behavior only). Updated across all reference files with tested status and warnings. Experiment log: `experiments/suno/2026-07-02-performance-notation-symbols.yml`
- Performance Notation Symbols (inline lyric formatting) integrated into tags reference and knowledge base -- 7 symbols that affect Suno vocal delivery. [Tier 3: Community heuristic] Credit: Omnisona (Suno AI God Mode Manual v3.0, March 2026)
- Anti-Pairs (genre combinations that do NOT work) added to style/genre reference, suno-optimization, and critique flag patterns -- Gregorian Chant+Trap, Classical Baroque+Lo-fi Bedroom Pop, Opera+Mumble Rap. [Tier 3: Community heuristic] Credit: Omnisona
- Groove/Time-Feel Descriptors (optional 8th dimension) added to style/genre reference, suno-optimization, songwriting production notes template, and steering -- 8 groove types for rhythmic specificity beyond BPM. [Tier 3: Community heuristic] Credit: Omnisona
- Call-and-Response Instrument Technique added to tags reference and knowledge base -- vocal/instrument conversational pattern. [Tier 3: Community heuristic] Credit: Omnisona
- Environmental/Ambient SFX Tags added to tags reference and knowledge base -- 9 atmosphere tags ([Rain], [Thunder], etc.). [Tier 3: Community heuristic] Credit: Omnisona
- Probabilistic Generation Framing (Render Strategy) added to suno-optimization, steering, and songwriter agent -- tags shape probability, generate 3-4 versions, treat Suno as collaborator. [Tier 3: Community heuristic] Credit: Omnisona
- Instrument Sound Reference added (`references/INSTRUMENT_SOUND_REFERENCE.md`) -- gear-to-sound translation table with 3 compression levels, character budget guidance. Gear-name detection added to validator. Tier 3, evidence from 21machines' acid house experiment.
- Temporal Specificity guideline (times, dates, numbers in lyrics) added to songwriting methodology, knowledge base, production theory, critique reference, and Suno rendering guide -- backed by 13 academic/professional sources (Pattison, Murphey, Werner, Perricone, Wilson, Jenkins, Stockwell, Gavins, Voice & Whiteley, Janiszewski & Uy, Mason et al., Kreyer & Mukherjee, NSAI)
- `core/tenets.md` — 7 creative decision-making principles with academic basis (Pattison, Juslin, Dodge, Fabbri, Moore, Nashville A&R). Priority-ordered for resolving conflicts when methodology rules fight each other or artistic intent. Wired into songwriter + critic agents.
- Artist Reference Conversion rule -- artist names in creative direction must be converted to descriptive production language (genre + era + instruments + production characteristics + vocal style + structural habits) before final output. Applied across all methodology, steering, reference, template, validator, and knowledge base files. Requested by 21machines.
- Builder agent (`core/methodology/builder.md` + `.kiro/agents/builder.md`) -- interactive setup/configuration specialist for albums, character voices, directory structure, experiments, preferences, and track addition
- Behavioral Directives section in all 5 agents (songwriter, critic, suno-optimizer, album-continuity, builder) -- explicit behavioral rules for autonomous execution without unnecessary permission-asking
- Songwriter auto-pilot mode — 30+ trigger phrases ("you choose", "surprise me", "just do it", etc.) that skip questions and use methodology decision frameworks for all choices
- Songwriter interactive mode — expanded parameter prompts (BPM, key, vocal staging, length, album position) matching community-requested fields
- Three-Tier Evidence Labeling System ([Tier 1: Scholarship-backed], [Tier 2: Professional heuristic], [Tier 3: Community/platform heuristic]) applied across all methodology files
- The Compression Test -- decision framework for handling lines exceeding singable density (songwriting.md Phase 3)
- Eerola, Friberg & Bresin (2013) properly attributed for emotional cue hierarchy

### Changed
- Renamed "bible" to "blueprint" across entire repository -- all files, references, skill names, and documentation updated (case-preserving: BIBLE->BLUEPRINT, Bible->Blueprint, bible->blueprint)
- Expanded trigger keywords in all agent description fields and POWER.md keywords array for better activation matching
- Emotional cue hierarchy attribution corrected from Juslin/Gabrielsson to Eerola, Friberg & Bresin (2013, Frontiers in Psychology 4, Article 487)
- Fabbri rule labels corrected to exact terminology (formal and technical rules, semiotic rules, behaviour rules, social and ideological rules, economical and juridical rules)
- Lacasse proxemics -- noted "dissolved" as system adaptation; credited composite framework (Hall + Lacasse + Moore)
- Moore 4 layers -- added caveat: generalized descriptions, not prescriptive rules
- Tagg musemes -- corrected to interobjective comparison methodology
- Quality gate language softened from absolute rules to professional heuristic checks [Tier 2]: syllable limits, hook timing, V2 novelty, bridge turn, ABCB scheme
- Suno-specific claims labeled [Tier 3] with version notes: 5-8 tags, genre-first, era anchoring
- Key-emotion mapping split: mode effects [Tier 1], specific key character [Tier 2 historical tradition]

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
- Album blueprint system + character voice design

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
