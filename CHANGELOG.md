# Changelog

All notable changes to this project will be documented in this file.

---

## [Unreleased]

### Deep-review fixes (October 2026)

**Added**
- `references/RHYME_AND_LYRIC_CRAFT.md`, the lyric dictionary the KB's §4 title promised. It covers:
  - Pattison's rhyme ladder (perfect > family > additive/subtractive > assonance > consonance) and the consonant-family chart (plosives / fricatives / nasals; partners vs companions)
  - rhyme positions and compound rhymes; rhyme-scheme notation with the structural effect of each scheme
  - section stability (line count, line length, rhyme closure, stresses), power positions and title placement
  - poetic feet and musical meter (pickups, backbeat, syncopation, 3/4, 6/8, flow) and singability (vowel modification, diphthongs, consonants, sibilance)
  - rhetorical devices and cliché flipping
  - rhyming dictionaries and word tools: RhymeZone, B-Rhymes, MasterWriter, Datamuse, CMUdict, `pronouncing`, `prosodic`, and Hirjee & Brown's research
- `tools/lyric-lint.py`: a deterministic lyric readout. Per line: syllables and stress. Per end-rhyme pair: its rhyme type on the ladder. Per section: rhyme scheme (X = unrhymed) and stability. Also flags function-word endings, end punctuation, clichés and cliché rhyme pairs (`tools/data/cliches.txt`), and Verse 1 vs Verse 2 syllable mismatches. Uses CMUdict via the optional `pronouncing` package (`tools/requirements-optional.txt`) and falls back to a heuristic without it.
- `tools/check-repo.py`: repo integrity checks for `#[[file:]]` includes, relative links, agent `resources:`, Kiro v1 hook schema, steering front matter, skill names and JSON.
- `tools/songfile.py`: shared song-file parser.
- `tests/`: unittest suite with fixtures.
- `.github/workflows/ci.yml`: CI that runs the tests, check-repo, the validator on `examples/songs/` and `songs/`, and a lint smoke test.
- `.kiro/hooks/song-validate.json` and `.kiro/hooks/prosody-lint.json`: Kiro v1 hooks with `command` actions that run the deterministic tools.
- `.kiro/steering/quick-score.md` and `.kiro/steering/full-pipeline.md`: manual steering commands (`/quick-score`, `/full-pipeline`). Kiro v1 has no manual hooks.
- `examples/songs/standalones/I_Wear_It_Well_V6.md`: the first V6-format reference song, with a v5.5-to-V6 migration table.
- Root `CONTRIBUTING.md`.

**Changed**
- `tools/validate-song.py` rewritten. It now:
  - accepts heading variants and bare `STYLE PROMPT:` / `LYRICS:` labels
  - counts only pasteable text: it ignores count notes, code fences and separators, and stops at `[End]`
  - accepts `[End]` / `[end]` case-insensitively and `[Composition Direction]` as an alias for `[Production Direction]`
  - parses the Exclude field and warns on dash prefixes and mixed hyphen characters
  - matches genres on word boundaries
  - accepts layer declarations by alias (e.g. "AI voice" declares a robotic layer)
  - adds checks for V6 grammar, `[Tag Vocabulary]`, `[Instrument: X In/Out]`, mixed paradigms, obsolete tags, and production instructions inside `()` (which get sung)
  - adds directory scanning that skips README and `*.brief.md`, plus `--strict`, `--hook`, UTF-8 BOM handling and non-UTF-8 errors
  - downgrades missing blocks to WARN in archived songs marked `<!-- song-format: legacy -->`, and skips files marked `<!-- validate: skip -->`

  The examples went from 27 FAIL / 4 ERROR to 0 FAIL.
- Hooks moved from the legacy `when`/`then`/`askAgent` format to the Kiro v1 schema (`version`, `hooks[]`, `trigger`, `matcher`, `action`). The five `*.hook.json` files are replaced, and the album `continuity-hook.json` examples are converted and list all 12 blueprint rules.
- Steering: `songwriting.md`, `suno-formatting.md` and `output-preferences.md` use `inclusion: always`, as the docs had claimed. `concept-album.md` uses `inclusion: auto` with `name`.
- Agents load files with documented `resources:` front matter instead of `#[[file:]]` (documented for steering only). The songwriter preloads only tenets, songwriting, critique and the rhyme reference, and reads the KB and the theory file on demand.
- Skills reference files by plain path.
- The critic follows `critique.md`'s layer table.
- Suno V6 is the default everywhere: steering, power, skills, agents, SOPs and README. The v5.5-era mechanics are labelled legacy (re-validate on V6): sliders, Personas/Stems, era tags, global tags, pipe notation, the 5-8 tag rule, Italian tempo and `[silence: sudden]`. `core/methodology/suno-optimization.md` gained a V6 Procedure.
- One exclusions format: the Exclude field takes plain comma-separated text with no dash prefix. Applied across the docs and the example songs.
- Canonical numbers reconciled across files:
  - syllables: 7-12 target, 13-15 review, 16+ Compression Test
  - hook timing: hook signal ~5-30 s of singing vs full chorus ~45-60 s of track time
  - rhyme scheme: no "PRO DEFAULT"
  - hook types: 4
  - bridge: 3-6 lines (up to 8)
  - runtime formula: corrected
- Craft corrections:
  - meter: the "spondaic" example is trochaic; dactyls are rolling rather than militaristic; corrected anapest example
  - rhyme examples: mosaic and home/alone
  - the reversed-stress example
  - "beats 1 and 3" now depends on the meter
  - 7 senses for object writing
  - a quotation wrongly attributed to Pattison
  - enjambment and function-word endings are no longer treated as errors
- Citation corrections:
  - Schubart key tables now give Schubart's actual characterisations alongside separate Tier 3 working associations
  - Fabbri: five rule types, not an "all five" checklist
  - Eerola et al.: perceived emotion; mode, not key
  - Juslin 2013 cited
  - Dodge et al. marked as having no primary citation yet
  - unsourced claims in `MUSIC_PRODUCTION_THEORY.md` are tier-labelled; accent-table myths fixed
- De-duplication:
  - the byte-identical blueprint copies in `references/` are removed; `examples/albums/*/BLUEPRINT.md` is canonical
  - KB §13 is condensed to a pointer, with its unique content moved into `SUNO_TAGS_REFERENCE.md` (now labelled legacy)
  - character-voice content is split into method (`core/methodology/character-voice.md`) and data (`CHARACTER_VOICE_REFERENCE.md`)
  - BPM tables now point to `SUNO_STYLE_GENRE_REFERENCE.md` §3.1
  - `critique.md` and `CRITIQUE_REFERENCE.md` are re-synced
- Counts fixed everywhere (6 agents, 9 SOPs, 7 methodology files, 6 steering files, 11 references, 13 disciplines, 18 Fractured Shadows tracks with T18 registered in the blueprint). Broken and stale paths fixed (builder include, SOP 02/04 paths, hook names, `docs/ARCHITECTURE_PLAN.md` status).
- Example songs:
  - `[end]` added where missing; missing `[Title:]` added
  - dash-prefixed exclusions converted to plain text
  - artist names replaced with descriptive language
  - four over-limit Style prompts trimmed under 1000 characters
  - Rikan and the Shapes duet brought under 5000 Lyrics characters (full direction kept in an Advanced Box section)
  - I Wear It Well's sung `(instrumental …)` lines converted to tags
- Plugins:
  - true bypass (passes the untouched input)
  - the always-on `g.tanh` safety stage (−2.4 dB and coloration at full scale) replaced with a transparent `g.clamp(-1, 1)` over-safety stage
  - the de-esser now has a soft knee, depth in dB, and a 2.5 kHz frequency floor
  - "Tier 1/2" renamed "Wave 1/2" to avoid clashing with the evidence tiers
  - `AUTHORING.md` assumptions brought up to date

### Added
- Suno Studio audio-effect plugins: new `plugins/` folder holding post-render audio processors applied to rendered audio inside Suno's in-app mixing environment. These are Suno Studio effects, NOT lyric tags, and are separate from the Style/Lyrics text-prompt pipeline. Delivered as single JSON files (`plugins/<name>/<name>.plugin.json`) carrying embedded JavaScript DSP.
- Six Tier-1 plugins: Intimate Proximity, De-Esser, Vintage / Lo-Fi Voicer, Digital Degrade / Glitch, Telephone / Radio Band, and Vocal Drive / Edge. Built with a confirmed `g.*` primitive set only (effects needing an unconfirmed primitive, such as the digital-degrade amplitude quantizer, are approximated and documented in the code header). Status UNVERIFIED: not yet executed in Suno Studio, pending in-Suno testing.
- Seven stem-targeted instrumental Suno Studio plugins, each meant to be dropped onto a specific stem: Sub Tightener (bass), Warm Keys Voicer (keys), Guitar Grit / Warmth (guitar), String Air / Size (strings), Synth Cold / Glitch (synth), Backing Vocal Tucker (backing vocals), and Texture Filter / Degrade (FX / other). Built with confirmed `g.*` primitives only; the synth and texture degrade reuses the digital-degrade fixed-depth 8-level amplitude quantizer rather than inventing a new primitive. Status UNVERIFIED: not yet executed in Suno Studio, pending in-Suno testing.
- Plugin documentation: `plugins/README.md` (Suno Studio / post-render framing, use cases, and file shape) and `plugins/AUTHORING.md` (plugin schema and confirmed `g.*` primitive reference for authoring new plugins).
- Song-planner package — elevates SOP 01 Phase 1 planning into a reviewable, approvable Song Brief before any lyrics are written. `core/methodology/song-planning.md` (canonical planning methodology with the 12-section SONG BRIEF spec and GUIDED MODE as default), `.kiro/agents/song-planner.md` (thin agent; trigger phrases "plan a song", "song brief", "outline a track", "help me plan", "plan out a song", "brief for"), `.kiro/sops/09-planning-a-song.md` (guided procedure + fillable template + the `SONGNAME.brief.md` convention that saves the brief alongside the song), plus a sample brief (`examples/songs/standalones/Three_In_The_Morning.brief.md`). The package references `songwriting.md`/`critique.md` for craft logic rather than duplicating it — planning is a new interaction layer over existing methodology, not new craft rules.
- Guided lyric-writing mode — added a GUIDED / COLLABORATIVE MODE to the songwriter agent (`.kiro/agents/songwriter.md`): drafts section-by-section, self-flags each draft against critique.md's full 12-category rubric, and waits for user confirmation before continuing. Added a Song Brief consumption seam so an approved brief seeds the write. Establishes a shared "Collaborative / Guided Mode" framing across the planner (brief decisions) and writer (lyric sections): suggest a methodology-backed default → surface concerns → user confirms/overrides → next step. Pipeline seam: PLAN(guided) → [Song Brief, user approves] → WRITE(guided, per-section critic checks) → CRITIQUE → OPTIMIZE.
- Adopted the Suno V6 tag paradigm as the current default model (models v6 / v6-wild / v6-mini): Style field = the WHAT (genre, key, tempo, vocal identity, production aesthetic), Lyrics field = the HOW (section tags, [Instrument: X In]/[Instrument: X Out], dynamics, delivery, transitions). [Instrument: X In/Out] confirmed working for instrument entrances/exits; no [Tag Vocabulary] block in final output (planning scaffolding only). v5.5-era mechanics flagged "re-validate for V6".
- Three new V6 reference files: `references/V6_TAG_REFERENCE.md` (master de-duplicated V6 tag dictionary), `references/V6_TAG_DISCOVERY.md` (how/why, division of labor, confirmed behaviors), and `references/STYLE_LIBRARY.md` (paired style prompts).
- Toolkit-wide V6 pointer integration across agents, steering, SOP, and methodology (`.kiro/agents/suno-optimizer.md`, `.kiro/steering/suno-formatting.md`, `.kiro/powers/songwriting/steering/suno.md`, `.kiro/sops/03-optimizing-for-suno.md`, `core/methodology/suno-optimization.md`).
- Surfaced Suno V6 in user-facing docs (README.md, SONGWRITING_KNOWLEDGE_BASE.md) with links to the canonical V6 references.
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
