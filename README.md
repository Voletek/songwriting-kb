# Songwriting Knowledge Base

A professional song production system combining Nashville/LA co-writing craft, academic music theory (13 disciplines), Suno AI V6 formatting expertise (legacy v5.5-era mechanics kept and labelled), and concept album continuity management — with a complete Kiro IDE automation layer and platform-neutral methodology usable by any AI assistant.

---

## Architecture

The system's methodology lives in `core/methodology/` as the **single source of truth**. Everything else consumes it:

```
core/methodology/  ← THE METHOD (complete, self-contained, canonical)
core/tenets.md     ← PRIORITIES (which rule wins when rules conflict)
       ↓ loaded by
.kiro/agents/      ← Kiro automation (thin wiring — persona + `resources:` front matter)
       ↓ also readable by
Any AI assistant   ← Just paste core/methodology/X.md into your assistant's context
       ↓ validated by
tools/             ← Deterministic checks (Python, no AI needed; run by hooks and CI)
```

When the method changes, you update ONE place (`core/methodology/`). Kiro agents inherit automatically. Non-Kiro users read the same source. When creative priorities conflict, check `core/tenets.md`.

---

## Quick Start

Clone this repo. Kiro users get automatic agent/skill/steering/hook wiring (hooks run in Kiro IDE 1.0+ and Kiro CLI V3; on Kiro Web, project agents are used for sub-agent delegation and hooks don't run — run the `tools/` scripts manually). Non-Kiro users read `core/methodology/` directly.

```bash
git clone https://github.com/Voletek/songwriting-kb.git
```

**Kiro users** — just talk naturally:
```
"Plan a song about..."        → Song-planner builds an approvable Song Brief first
"Help me plan a track"        → Song-planner activates
"Write a song about..."       → Songwriter asks for details, runs full pipeline
"I have an idea for a track"  → Songwriter activates
"Critique this song"          → Critic runs full evaluation in one pass
"Is this any good?"           → Critic activates
"Make this Suno-ready"        → Suno-optimizer formats and reports char counts
"Will this render?"           → Suno-optimizer activates
"Check album continuity"      → Album-continuity runs all checks, PASS/FAIL table
"Set up a new album"          → Builder walks you through blueprint creation
"Help me get started"         → Builder activates
/quick-score                  → Fast 12-category score (manual steering)
/full-pipeline                → Write → Critique → Revise → Optimize → Verify (manual steering)
```

**Guided / Collaborative Mode** — plan and write step-by-step, staying in the driver's seat. The song-planner walks the 12-section Song Brief and the songwriter drafts section-by-section; at each step the agent suggests a methodology-backed default, surfaces any concerns (via critique.md's full 12-category rubric during writing), and waits for you to confirm or override before moving on. Same collaborative loop across planning (brief decisions) and writing (lyric sections).

**Non-Kiro users** — see [Using Without Kiro](#using-without-kiro) below.

**CLI validation** (any platform):
```bash
python3 tools/validate-song.py songs/            # format, limits, V6 tags, exclusions
python3 tools/lyric-lint.py songs/my_song.md      # syllables, stress, rhyme, section stability, clichés
python3 tools/check-repo.py                       # repo integrity
```

---

## Repository Structure

```
songwriting-kb/
├── core/
│   ├── methodology/           7 canonical method files (SINGLE SOURCE OF TRUTH)
│   └── tenets.md              7 creative decision-making principles (conflict resolution)
├── .kiro/
│   ├── steering/              6 files — 3 always, 1 auto (concept-album), 2 manual (/quick-score, /full-pipeline)
│   ├── agents/                6 thin agents — load core/methodology/ via `resources:` front matter
│   ├── skills/                5 skills — reference core/methodology/ + references/
│   ├── hooks/                 2 v1 JSON hooks — song-validate.json, prosody-lint.json
│   ├── powers/songwriting/    1 power — activatable master bundle
│   └── sops/                  9 SOPs — step-by-step procedures (point to core/)
├── tools/
│   ├── validate-song.py       Deterministic song validator (char counts, required elements, V6 tags, exclusions)
│   ├── lyric-lint.py          Deterministic lyric lint (syllables, stress, rhyme type/scheme, section stability, clichés)
│   ├── check-repo.py          Repo integrity (include/resource paths, hook schema, steering front matter, JSON)
│   ├── songfile.py            Shared song-file parser
│   ├── data/cliches.txt       Cliché list used by lyric-lint
│   └── requirements-optional.txt   Optional `pronouncing` (CMUdict) for dictionary-accurate syllables/rhymes
├── tests/                     unittest suite for the tools
├── .github/workflows/ci.yml   CI workflow (tests + repo/tool checks)
├── plugins/                   13 Suno Studio audio-effect plugins (post-render) + README/AUTHORING
├── experiments/
│   └── suno/                  Suno experiment logs (version-dated prompt tests)
├── docs/                      Architecture plans, implementation docs
├── references/                11 companion docs (see below)
├── examples/
│   ├── songs/                 Developer's example songs (concept albums, standalones)
│   ├── albums/                Album examples — BLUEPRINT.md, steering.md, continuity-hook.json per album
│   ├── analysis/              Example critique reports
│   └── preferences/           Output preference examples
├── songs/                     YOUR songs go here (empty — your workspace)
├── analysis/                  YOUR critique/continuity reports go here
├── CONTRIBUTING.md            Contribution guide (points to SOP 08)
├── SONGWRITING_KNOWLEDGE_BASE.md    Master craft reference (13 sections)
└── MUSIC_PRODUCTION_THEORY.md       Academic framework (13 disciplines)
```

**`references/` (11 files):** `CHARACTER_VOICE_REFERENCE.md`, `CRITIQUE_REFERENCE.md`, `CRITIQUE_REPORT_TEMPLATE.md`, `INSTRUMENT_SOUND_REFERENCE.md`, `RHYME_AND_LYRIC_CRAFT.md`, `STYLE_LIBRARY.md`, `SUNO_STYLE_GENRE_REFERENCE.md`, `SUNO_TAGS_REFERENCE.md`, `V6_TAG_DISCOVERY.md`, `V6_TAG_REFERENCE.md`, `YOUR_ALBUM_BLUEPRINT.md` (template). The example album blueprints live in `examples/albums/*/BLUEPRINT.md`.

---

## SOPs (Standard Operating Procedures)

The procedural layer — step-by-step HOW for every workflow:

| # | SOP | What It Covers | Time |
|---|---|---|---|
| **01** | [Writing a Song](/.kiro/sops/01-writing-a-song.md) | 27 steps: concept → analysis → writing → QA → formatting | 50-75 min |
| **02** | [Critiquing a Song](/.kiro/sops/02-critiquing-a-song.md) | 10 steps: read → 9-step analysis → score → Suno optimization → flag → recommend | 35-55 min |
| **03** | [Optimizing for Suno](/.kiro/sops/03-optimizing-for-suno.md) | V6 path (6 steps: split fields → Style → Exclude → V6 lyric tags → validate → render) + 12 v5.5-era legacy steps | 15-20 min |
| **04** | [Setting Up a Concept Album](/.kiro/sops/04-setting-up-concept-album.md) | 12 steps: concept → registry → rules → motifs → documentation | 2.5-3.5 hrs |
| **05** | [Extending an Album](/.kiro/sops/05-extending-an-album.md) | 12 steps: evaluate → scope → update blueprint → verify → write | 1-2 hrs |
| **06** | [Character Voice Design](/.kiro/sops/06-character-voice-design.md) | 11 steps: identify → accent → template → instruments → mode | 15-25 min |
| **07** | [Full Pipeline](/.kiro/sops/07-full-pipeline.md) | 6 stages: Write → Critique → Revise → Optimize → Verify → Render | 2-3 hrs |
| **08** | [Contributing](/.kiro/sops/08-contributing.md) | Community guide: setup → customize → add albums → submit | Variable |
| **09** | [Planning a Song](/.kiro/sops/09-planning-a-song.md) | Guided brief creation before writing — step through the 12-section Song Brief, save `SONGNAME.brief.md` alongside the song | 15-30 min |

### The Full Pipeline (SOP 07):

```
WRITE → CRITIQUE → REVISE → OPTIMIZE → VERIFY → RENDER
  ↑         (score ≥8.5? skip revise)         |
  └──────── (if fails verification) ──────────┘
```

---

## Agents (6 Roles)

| Agent | What It Does | Invoke With |
|---|---|---|
| **song-planner** | Produces an approvable Song Brief before lyrics via guided planning — steps through the 12-section brief, suggesting methodology-backed defaults and surfacing concerns for your confirmation. Loads `core/methodology/song-planning.md` | "plan a song", "song brief", "outline a track", "help me plan", "plan out a song", "brief for" |
| **songwriter** | Creates complete songs from concepts. Asks for missing parameters, runs full pipeline, outputs Suno-ready format with char counts. Offers a guided/collaborative mode that drafts section-by-section with per-section critic checks, and consumes an approved Song Brief when one exists. Loads `core/methodology/songwriting.md` | "Write a song about...", "compose", "make a track", "lyrics for...", "I have an idea" |
| **critic** | Multi-layer evaluation (12 craft + 5 advanced + Suno optimization + album-context). Runs full critique in one pass, reports scores and decision gate. Loads `core/methodology/critique.md` | "Critique this", "score", "rate", "review", "is this good?", "feedback", "what's wrong?" |
| **suno-optimizer** | Adds meta-tags, checks char counts, validates formatting. Reports counts, flags artist names for conversion. Loads `core/methodology/suno-optimization.md` | "Make this Suno-ready", "format for Suno", "check my char count", "will this render?" |
| **album-continuity** | Runs all continuity checks in one pass. PASS/FAIL table with fixes. Loads `core/methodology/album-continuity.md` | "Check continuity", "does this fit?", "album rules", "sonic palette check" |
| **builder** | Setup/configuration specialist. Walks through album blueprints, character voices, project structure, preferences interactively. Loads `core/methodology/builder.md` | "Set up a new album", "new project", "add a character", "configure", "help me get started" |

---

## Skills (On-Demand Knowledge)

| Skill | Contains | Activate When |
|---|---|---|
| **song-critique** | 12-category rubric, 5 advanced assessments, Suno optimization (7-point dimensional check + style alternatives), flag patterns | Evaluating any song |
| **suno-meta-tags** | V6 paradigm (Style=WHAT / Lyrics=HOW, `[Instrument: X In/Out]`) and canonical V6 vocabulary, plus 100+ v5.x tags (legacy), layers, and v5.5-era features/sliders/era tags | Formatting for Suno |
| **music-theory** | 13 disciplines, 23-point framework, 18 advanced concepts | Deep production analysis |
| **character-voice** | Accent/dialect system, voice design template (vocal + non-vocal), instrumentation maps | Writing for characters |
| **concept-album-blueprint** | Track registry, motifs, continuity rules (template; examples in `examples/albums/`) | Album work |

---

## Hooks (Automated Quality Checks)

Two Kiro v1 JSON hook files in `.kiro/hooks/` plus two manual steering commands:

| Hook / command | Fires On | Runs / Checks |
|---|---|---|
| **`song-validate.json`** | `PostFileCreate` + `PostFileSave` on song files under `songs/` | `python3 tools/validate-song.py --hook {{filePath}}` — deterministic char counts, required elements, V6 tag checks, exclusions format |
| **`prosody-lint.json`** | `PostFileSave` on song files under `songs/` | `python3 tools/lyric-lint.py --hook {{filePath}}` — syllables, stress, rhyme type/scheme, section stability, clichés |
| **`/quick-score`** | On request (manual steering, `.kiro/steering/quick-score.md`) | Fast 12-category scoring pass |
| **`/full-pipeline`** | On request (manual steering, `.kiro/steering/full-pipeline.md`) | Complete write→critique→revise→optimize→verify flow |

- Both hooks skip `README.md` and `*.brief.md`. File-event hooks fire only for agent-made file changes.
- Hooks run in Kiro IDE 1.0+ and Kiro CLI V3. Kiro Web sessions do not run hooks — run the tools manually there.
- Album continuity hooks: examples in `examples/albums/<album>/continuity-hook.json` (v1 schema, `agent` action) — copy to `.kiro/hooks/<album>-continuity.json` to activate.

**CLI alternative:** `python3 tools/validate-song.py songs/` and `python3 tools/lyric-lint.py songs/your_song.md` give the same deterministic checks without hooks.

---

## Steering (6 Files)

| File | Inclusion | Purpose |
|---|---|---|
| `songwriting.md` | `always` | Core principles + 9-step workflow + quality gates |
| `suno-formatting.md` | `always` | Suno V6 rules (default), limits, Exclude format, layers + legacy v5.5-era mechanics (sliders, v5.5 features, era tags, global tags, pipe notation) |
| `output-preferences.md` | `always` | Output format, layers, hit formulas (customize for your own) |
| `concept-album.md` | `auto` | Album continuity framework + setup guide (universal); loads on album-related requests |
| `quick-score.md` | `manual` | `/quick-score` — fast 12-category score |
| `full-pipeline.md` | `manual` | `/full-pipeline` — Write → Critique → Revise → Optimize → Verify |

---

## Suno AI Integration

### Suno V6 (current default)

**Suno V6** (models: `v6` / `v6-wild` / `v6-mini`) is the current default model, and it uses a different tag paradigm than v5.5. Status: working model (Sept 2026, user-confirmed); render evidence is logged in the `references/V6_TAG_DISCOVERY.md` results log.

- **Style field = the WHAT**: genre (first), key, tempo, vocal identity, production aesthetic (sets the world).
- **Lyrics field = the HOW**: section tags, `[Instrument: X In]` / `[Instrument: X Out]`, `[Dynamic: ...]`, `[Vocal: ...]` (or `[Male lead, inline adjective]`), `[Transition: ...]`, `[Key Change: ...]` — 2-4 tags per section, ending with `[End]` (choreographs the performance).
- **Exclude field**: negatives only, plain comma-separated text.
- Do **not** include a `[Tag Vocabulary]` block (planning scaffolding only), v5.5 global tags (`[track:]` / `[control:]` / `[sequence:]`), or compact pipe notation.
- Procedure: `core/methodology/suno-optimization.md` → **V6 Procedure (default)**; deterministic check: `python3 tools/validate-song.py <file>`.

Canonical V6 references:
- [`references/V6_TAG_REFERENCE.md`](references/V6_TAG_REFERENCE.md): master de-duplicated V6 tag dictionary.
- [`references/V6_TAG_DISCOVERY.md`](references/V6_TAG_DISCOVERY.md): how/why, division of labor, canonical grammar, results log.

### Field Limits
| Field | Limit | Notes |
|---|---|---|
| Style of Music | 1000 chars | Genre first, key, BPM, mood, instruments (sound descriptors), vocal, production |
| Lyrics | 5000 chars | Confirmed June 2026 (v5.5) — must fit, no overflow; V6 limit still being confirmed |
| Exclude | Dedicated field | Negative prompts ONLY — plain comma-separated text, no dash prefix (e.g. `trap drums, beatboxing, vocal hums, bright synths`); written under `## EXCLUSIONS:` in song files |

### Parenthetical Layers — `()` in Lyrics
| Pattern | Effect | Style Prompt Needed? |
|---|---|---|
| `(whispered) text` | Delivery cue — whispers next text | Usually works alone |
| `(spoken) text` | Spoken not sung | Usually works alone |
| `(robotic layer: text)` | Named secondary voice (AI/machine) | **YES — must declare** |
| `(echo layer: text)` | Delayed/echo treatment | **YES — must declare** |
| `(whisper layer: text)` | Background whisper texture | **YES — must declare** |
| `(response text)` | Backup vocal / duet response | Best with declaration |

### The Specificity Principle
The more dimensions you specify (genre, tempo, mood, vocal, instruments, space, key), the less Suno fills gaps with statistical averages. Our SOP system produces 7-dimension "precise" prompts by design. [Tier 3]

### Genre-Emotion Alignment (Critic Evaluates This)
The critic's **Suno Optimization Assessment** evaluates whether the Style Prompt's genre, key, BPM, and instrument choices are the BEST match for the song's emotional content — and provides complete alternative Style Prompts when they aren't. Key principles:

- **Mode is the strongest overall cue** (Eerola, Friberg & Bresin, 2013 — perceived emotion; mode contributed most overall, tempo most for arousal). Specific key "characters" are historical tradition (Schubart), not psychology; real key effects come from vocal tessitura, instrument resonance, and mode
- **Genre must SIGNIFY what the lyrics express** (Fabbri) — dark lyrics in an upbeat genre read as a semiotic mismatch unless the irony is intentional (ironic juxtaposition is itself a convention)
- **BPM serves two masters** — must satisfy genre convention AND emotional pacing
- **Instruments carry cultural meaning** (Tagg) — piano ≠ guitar ≠ synth even playing the same notes
- **70/30 Rule** — genre combinations: one dominant (70%) + one flavor (30%) [Tier 3]

Full reference: `references/SUNO_STYLE_GENRE_REFERENCE.md` (600+ lines covering key/mode-emotion mapping, BPM ranges, 30+ instrument significations, genre conventions, and Suno prompt science)

**Instrument Sound Reference:** For converting gear/model names to Suno-actionable sound descriptors, see `references/INSTRUMENT_SOUND_REFERENCE.md`. Describes what instruments SOUND like (not what they ARE) with 3 compression levels for character budget management. Generic category names (Rhodes, Hammond organ, Wurlitzer) are fine as tags; brand-model gear (TB-303, TR-808, Juno-60, Telecaster…) should be translated. [Tier 3]

### 5 Formatting Modes
| Mode | Use Case |
|---|---|
| **A** — Per-Line Vocal Tags | Intimate cinematic dialogue |
| **B** — Parenthetical () | Space-efficient call-and-response |
| **C** — Theatrical/Concept | Multi-layer concept albums (named layers) |
| **D** — Character Performance | Fantasy characters, accents |
| **E** — Solo Anthem/Intimate | Accessible solo tracks |

### Legacy v5.5-era (re-validate on V6)

Everything in this subsection is **v5.5-era (legacy) — re-validate on V6**. It is kept for v5.5 renders and as hypotheses to test on V6, not as current rules.

**Creative sliders** (optional — only if your Suno UI exposes them; values are v5.5-era starting points):

| Slider | Default | Starting Point | Effect |
|---|---|---|---|
| Weirdness | 50% | 50-55% | Safe (0%) ↔ Chaos (100%) — creative latitude |
| Style Influence | 50% | 50-60% (later v5.5 tests favoured 70-90%) | How much Style Prompt steers output |
| Audio Influence | ~45% | 45% | Reference track weight (Inspo only) |

**v5.5 features (UI — not text tags):**

| Feature | What It Does | Album Use |
|---|---|---|
| **Personas/Voices** | Lock vocal identity from your own sample | Same voice across all character tracks |
| **Stems (12-track)** | Extract vocals, drums, bass, guitar, keys, strings, synth, brass, perc, backing, FX, other | DAW mixing for album consistency |
| **Custom Models** | Train Suno on your completed tracks | Learn your sound for future songs |
| **My Taste** | AI learns your preferences over time | Better defaults on quick sessions |

**Era tags (production modifiers):** On v5.5, decade tags in the Style Prompt aggressively biased production style:
- `"1980s"` → gated reverb drums, synth textures, bright digital
- `"1970s"` → analog warmth, tape compression, live-room bleed
- **Separation Principle:** Want vintage instruments + modern production? Be explicit: `"modern production, vintage 1970s guitar tone"`
- **Era anchoring** ("early 2000s garage rock") was observed to beat bare genre labels [Tier 3]

**Other v5.5-era mechanics:** global tags (`[track:]` / `[control:]` / `[sequence:]`), lowercase `[end]` (the validator accepts both `[end]` and `[End]`), compact pipe notation `[Section | params]`, the 5-8 Style-descriptor sweet spot, the Italian-tempo preference, `[silence: sudden]` (unreliable even on v5.5), and performance-notation symbols (only ALL CAPS was reliable).

### Suno Studio Plugins

The `plugins/` folder holds **post-render audio-effect plugins for Suno Studio**: DSP processors applied to already-rendered audio inside Suno's in-app mixing environment. These are a separate concern from the prompt/lyric pipeline; they are NOT lyric tags and do NOT go in the Style or Lyrics fields. Use them in Suno Studio after a track has rendered, the way you would use effect plugins in a DAW.

Thirteen Wave 1 (built) plugins ship today. Six target the vocals stem: Intimate Proximity, De-Esser, Vintage / Lo-Fi Voicer, Digital Degrade / Glitch, Telephone / Radio Band, and Vocal Drive / Edge. Seven are stem-targeted for the instrumental / non-lead stems: Sub Tightener (bass), Warm Keys Voicer (keys), Guitar Grit / Warmth (guitar), String Air / Size (strings), Synth Cold / Glitch (synth), Backing Vocal Tucker (backing vocals), and Texture Filter / Degrade (FX / other). They are currently UNVERIFIED (not yet executed in Suno Studio). See [plugins/README.md](plugins/README.md) for details and [plugins/AUTHORING.md](plugins/AUTHORING.md) for the plugin schema.

---

## The 9-Step Professional Workflow

Applied to every song:

1. **SEMANTIC** — What is it literally about?
2. **EMOTIONAL** — Central affect? BRECVEMA mechanisms?
3. **PROSODIC** — Stresses, breaths, syllable counts (target 7-12 per line), rhyme & stability plan
4. **NARRATIVE** — Arc type? Where is the turn?
5. **VOICE** — Who speaks? Accent? Register?
6. **GENRE** — Which of Fabbri's genre-rule types carry the weight here? Fusion ratio (70/30)?
7. **ARRANGEMENT** — Growth pattern? Contrast? Negative space?
8. **PRODUCTION** — Timbre? Harmonic choices? Space?
9. **COMMERCIAL** — Audience? Platform? Length? Sync?

---

## Quality Standards

- [Tier 2] Hook signal within ~5-30 s of the first SUNG word (genre-dependent: pop earlier, cinematic/progressive later). Separately, the full chorus typically arrives by ~45-60 s of track time in pitch-ready commercial songs (pop average ~39 s) — two different metrics
- [Tier 2] Target 7-12 syllables per line; 13-15 = review stress density and singability at tempo; 16+ = apply the Compression Test (or justify as intentional)
- [Tier 2] Stresses land on the strong beats of the meter (square 4/4: usually 1 and 3; backbeat/syncopated styles: anticipations or 2 and 4; 3/4 and 6/8: the downbeat of each group; pickups carry unstressed syllables)
- [Tier 2] V2 usually adds new information or a new angle (unless reiteration is part of the form)
- [Tier 2] Bridge often works best when it creates contrast or a turn (semantic, musical, textural, or energetic); write 3-6 lines (up to 8 when the turn needs it)
- Hook passes "would someone text this line?" test
- Every word earns its place — no filler
- [Tier 2] No universal rhyme-scheme default: ABCB (XAXA) is a common conversational option (only even lines rhyme, so less closure). Choose per section — stable/closed for choruses and resolutions, unstable/open for pre-choruses and bridges
- [Tier 2] Use the strongest rhyme that doesn't bend meaning or syntax (Pattison's ladder: perfect > family > additive/subtractive > assonance > consonance) — perfect/family for closure (title lines, chorus resolutions), looser rhymes for motion. Never force syntax for a rhyme. Full detail: `references/RHYME_AND_LYRIC_CRAFT.md`
- Production choices must SIGNIFY correctly (Tagg semiotics)
- Named parenthetical layers must be declared in Style Prompt
- Artist references converted to descriptive production language before final output
- Era tags separated from production intent when mixing vintage + modern

---

## Creative Tenets (When Rules Conflict)

Seven priority-ordered principles for resolving creative conflicts. Full details in `core/tenets.md`.

1. **EMOTION OVER MECHANICS** — Serve the feeling, unless discipline makes the emotion hit harder
2. **SHOW OVER TELL** — Sensory imagery for scenes; direct statement permitted for hooks and bridge turns
3. **THE METHOD SERVES THE ARTIST** — Artist intent wins on creative choices; compliance constraints are non-negotiable
4. **ONE SOURCE OF TRUTH** — Canonical definition in one place; context-appropriate summaries acceptable
5. **RENDER-READY OR NOT DONE** — Final song output must paste into Suno's three fields; intermediate work is exempt
6. **UNIVERSAL RESONANCE** — Specificity creates universality; album tracks should resonate without requiring the full album
7. **PLATFORM-NEUTRAL CRAFT** — Craft method is portable; platform optimization is a layer, not embedded

**Academic basis:** Pattison (prosody as relationship), Juslin (BRECVEMA emotion mechanisms), Dodge et al. (authenticity + innovation), Fabbri (genre as process), Moore (non-prescriptive analysis), Nashville A&R (format constraints).

---

## Knowledge Base

### SONGWRITING_KNOWLEDGE_BASE.md (13 Sections)
1. Song Structure & Form
2. The Hook (4 types, 6 principles)
3. Lyric Writing Mastery
4. Rhyme & Prosody (summary — full lyric dictionary in `references/RHYME_AND_LYRIC_CRAFT.md`)
5. Chord Progressions & Music Theory
6. Emotional Arc & Storytelling
7. Genre Conventions
8. Co-Writing & Nashville Method
9. Pitching & Industry Standards
10. Songwriter's Workflow & Exercises
11. Quick Reference Cheat Sheets
12. Suno AI — Formatting, Style Prompts & Production (V6 default; duet modes, layers, hit formulas, specificity)
13. Suno AI — Legacy v5.x Advanced Meta-Tags (summary: v5.x tags, pipe notation, controls, sliders, stems, personas — re-validate on V6)

### MUSIC_PRODUCTION_THEORY.md
- 13 Academic Disciplines (incl. #13 Cognitive Poetics & Deixis)
- 23-Point Song Development Framework
- 18 Advanced Concepts
- Vocal Accent & Dialect Phonetics (real-world + fantasy)

---

## Example Albums (Reference Implementations)

### Fractured Shadows — Digital→Fantasy Concept (18 tracks: Acts 1–2 complete, Act 3 in progress)

> "The fracture made the shadows — but the shadows made the dawn."

**Act 1 — Digital Dissolution → Transfer (Tracks 1-7)**

| # | Title | Key | Emotion |
|---|---|---|---|
| 01 | Ghost In The System | F#m | Burnout |
| 02 | Signal Loss | Dm | Isolation |
| 03 | Residual Self | Em | Identity searching |
| 04 | Human Exception | Dm | AI fascination |
| 05 | Prime Directive | Dm | AI possession |
| 06 | Fracture Protocol | Fm | Consciousness torn |
| 07 | Rikan | Fm→Ab | Terrified awakening |

**Act 2 — Survival → Integration (Tracks 8-17)**

| # | Title | Key | Emotion |
|---|---|---|---|
| 08 | First Blood | Bm | Violence as discovery |
| 09 | The Shard | Em | Prophecy |
| 10 | Fractured Plains | Dm | Epic journey |
| 11 | The Custodian | Am | Mentor |
| 12 | Fall of Dawnwatch | Fm | War, loss |
| 13 | Shadow Weaver | Ebm | Villain revealed |
| 14 | Ghost of Draeven | Cm | Self-confrontation |
| 15 | The Sword Remembers | Gm | Grief |
| 16 | Campfire | **D major** | Found family |
| 17 | Both Names | Am→**C major** | Integration |

**Act 3 — In Progress (Track 18+)**

| # | Title | Key | Emotion |
|---|---|---|---|
| 18 | Edge of the Rift | Em | Resolute hope, awe at scale |

**Sonic Evolution:** Industrial/Glitch → Tribal/Primal → Cinematic Orchestral → Folk Rock → Full Orchestra + Key Change → (Act 3) Cinematic Folk-Rock

Blueprint: `examples/albums/fractured-shadows/BLUEPRINT.md`

---

### Keeper of the Light — Folk-Horror/Sea-Shanty Concept (8 tracks)

> "The light was never a beacon — it was a lullaby, and she's been singing something terrible to sleep her entire life."

| # | Title | Key | Emotion |
|---|---|---|---|
| 01 | The Keeper's Morning | D Mixolydian | Devotion, solitude |
| 02 | Sixty Years of Light | G Dorian | Ritual, quiet loneliness |
| 03 | What the Logbook Says | Em | Unease, first dread |
| 04 | The Depth Hymn | Bm | Revelation, awe-horror |
| 05 | The Night the Light Died | F#m | Panic, guilt, chaos |
| 06 | Something Stirs Below | Cm | Cosmic dread, paralysis |
| 07 | It Remembers the Sun | Fm | Ancient sorrow, terrible beauty |
| 08 | Lullaby for Leviathan | D Mixolydian (underwater) | Acceptance, transformation |

**Sonic Evolution:** Warm acoustic folk → Darkened folk → Dark ambient → Storm chaos → Near-silence → Massive choir → Transformed return

**Unique features:** Non-vocal entity character design, harmonic circle (starts/ends in D Mixolydian), the sea as ever-present instrument evolving across 8 tracks.

Blueprint: `examples/albums/keeper-of-the-light/BLUEPRINT.md` (one example track: `examples/songs/keeper_of_the_light/01_The_Keepers_Morning.md`)

---

## Community Use

This system is designed for sharing. The architecture separates **universal** from **personal**:

### Universal (works for anyone — ~70% of system):
- All knowledge base files
- All SOPs
- Song-planner, Songwriter, Critic, Suno-Optimizer, Builder agents
- All skills (except album-blueprint content)
- `song-validate` and `prosody-lint` hooks, `/quick-score` and `/full-pipeline` commands, and the `tools/` scripts
- All reference docs (except your album blueprint)

### Personal (customize for your projects — ~30% of system):
- `output-preferences.md` → edit with YOUR format preferences
- Album blueprint → replace `references/YOUR_ALBUM_BLUEPRINT.md` with your own (examples live in `examples/albums/*/BLUEPRINT.md`)
- Album-continuity agent → configure YOUR rules
- Add conditional steering + continuity hooks for YOUR albums (see `examples/`)

### Getting Started (Community):
```bash
git clone https://github.com/Voletek/songwriting-kb.git
cd songwriting-kb
# See SOP 08 for full setup guide
# See SOP 04 to create your own concept album
# See examples/ for complete reference implementations
```

---

## Using Without Kiro

The methodology in this repository works with **any AI assistant** - not just Kiro. The `core/methodology/` files are the complete, self-contained methods.

### Quick Start (Any AI)

Load the relevant methodology file(s) into your AI's context, then ask it to follow the procedure:

| Workflow | Load These Files |
|---|---|
| **Critique a song** | `core/methodology/critique.md` + `references/CRITIQUE_REFERENCE.md` + `references/SUNO_STYLE_GENRE_REFERENCE.md` |
| **Plan a song** | `core/methodology/song-planning.md` |
| **Write a song** | `core/methodology/songwriting.md` + `SONGWRITING_KNOWLEDGE_BASE.md` + `references/RHYME_AND_LYRIC_CRAFT.md` |
| **Optimize for Suno** | `core/methodology/suno-optimization.md` + `references/V6_TAG_REFERENCE.md` (+ `references/SUNO_TAGS_REFERENCE.md` for legacy v5.x renders) |
| **Album continuity** | `core/methodology/album-continuity.md` + your album blueprint |
| **Character voice** | `core/methodology/character-voice.md` + `references/CHARACTER_VOICE_REFERENCE.md` |

### Example Prompts

**For ChatGPT/Claude/etc:**
```
I've loaded the critique methodology. Please critique the following song 
using the full 3-layer model (Core 12 + Advanced 5 + Suno Optimization).
Score each category 1-10 with one-sentence justification.

[paste your song here]
```

```
I've loaded the songwriting methodology. Write a song about [topic]. 
Follow the Nashville Method (chorus first) and output in full Suno-ready format.
```

### Deterministic Validation

For checks that don't need AI judgment, use the scripts in `tools/` (Python 3, no AI needed):

```bash
python3 tools/validate-song.py songs/                 # files or directories (recursive); skips README.md and *.brief.md
python3 tools/validate-song.py --json songs/          # machine-readable output
python3 tools/validate-song.py --strict songs/        # WARN → non-zero exit
python3 tools/lyric-lint.py songs/my_song.md          # syllables, stress, rhyme type/scheme, section stability, clichés (--json)
python3 tools/check-repo.py                           # repo integrity: include/resource paths, hook schema, steering front matter, JSON
```

`validate-song.py` checks character counts, required elements, V6 tag compliance, and the exclusions format. `lyric-lint.py` uses CMUdict through the optional `pronouncing` package (`pip install pronouncing`, see `tools/requirements-optional.txt`) for dictionary-accurate syllables and rhymes; without it a heuristic fallback runs.

### How This Differs from Kiro

| Aspect | With Kiro | Without Kiro |
|---|---|---|
| Methodology loading | Automatic via agents | Manual file loading |
| Format validation | Hooks run the tools on agent-made saves (Kiro IDE 1.0+ / CLI V3; not Kiro Web) | Run `tools/validate-song.py` and `tools/lyric-lint.py` manually |
| Album continuity | Agent checks on edit | Load methodology + blueprint, ask AI to check |
| Steering rules | Loaded automatically (always / auto / manual) | Include in your system prompt |
| Skills | Activated on demand | Load the relevant methodology file |

---

## Sources

- Berklee Online, Pat Pattison (Berklee Professor)
- Pat Pattison, *Songwriting: Essential Guide to Rhyming* and *Writing Better Lyrics* (rhyme ladder, consonant families, section stability, power positions)
- Andrea Stolpe, *Popular Lyric Writing: 10 Steps to Effective Storytelling* (Berklee Press)
- Sheila Davis, *The Craft of Lyric Writing* (rhetorical devices, lyric forms)
- Jimmy Webb, *Tunesmith: Inside the Art of Songwriting* (the perfect-rhyme position)
- CMU Pronouncing Dictionary (CMUdict), via the optional `pronouncing` Python package (used by `tools/lyric-lint.py`)
- Franco Fabbri, "A theory of musical genres: two applications" (1982) — five types of genre rules
- Philip Tagg (music semiotics — musemes, cultural connotation of timbres)
- Patrik Juslin (2013), "From everyday emotions to aesthetic emotions: towards a unified theory of musical emotions", *Physics of Life Reviews* 10(3) — BRECVEMA (8 mechanisms of induced emotion)
- Eerola, Friberg & Bresin (2013), *Frontiers in Psychology* 4:487 — emotional cue hierarchy for perceived emotion
- Allan F. Moore (functional texture layers, soundbox theory, style vs genre)
- Serge Lacasse (vocal staging, proxemic distance)
- Christian Schubart, *Ideen zu einer Aesthetik der Tonkunst* (written 1784-85, published 1806; English in Rita Steblin, *A History of Key Characteristics*) — historical key characteristics
- Dodge et al. (2025) — six evaluation criteria for popular music; primary citation (journal/DOI) not yet recorded, see PR Newswire, Feb 2026
- stayen/suno-reference (November 2025 — v5.0 meta-tags, legacy)
- Suno AI official documentation + community testing (2025-2026)
- Suno community research (v5.5-era, legacy): prompt formula (genre-first, 5-8 tags), era anchoring, genre combinations (70/30 rule), slider behavior, v5.5 features
- V6 working model (Sept 2026, user-confirmed render tests) — `references/V6_TAG_DISCOVERY.md`
- Battle-tested prompt engineering (real Suno playlist prompts)
- iZotope, The Song Foundry, American Songwriter, Nashville Guitar Studios

---

## License

This knowledge base is free to use, customize, and share. Attribution appreciated but not required.
