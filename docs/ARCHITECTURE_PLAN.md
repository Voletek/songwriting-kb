# Architecture Refactor Plan: Methodology as Source of Truth

**Date:** June 2026
**Status:** Phases 1-3 implemented (June 2026)
**Triggered by:** multi-lang/songwriting-kb PR #3 review + internal discussion

---

## Credits & Acknowledgments

This restructuring was catalyzed by **Brian Smith Clark** ([@multi-lang](https://github.com/multi-lang)) who forked the repo, conducted a thorough methodology review, and submitted [PR #3](https://github.com/multi-lang/songwriting-kb/pull/3) proposing platform generalization. While our final implementation differs from his PR's approach, the core insights that drove this refactor came directly from his work:

- **The fragmented source-of-truth problem** — Brian identified that the same methodology was duplicated across agents, SOPs, skills, and steering with no single canonical source. This is the central problem this refactor solves.
- **The platform-neutral methodology concept** — The principle that songwriting knowledge should exist independently of any tool's config format originated from his review.
- **Suno version-dating** — His observation that Suno-specific claims are mixed across versions without clear labels directly led to our version status table approach.
- **Deterministic validation tooling** — His `tools/count-suno-fields.py` script demonstrated that character counting and format validation should be code, not AI interpretation. Our `tools/validate-song.py` will be built from this foundation.
- **Experiment logging for Suno** — His `experiments/suno/` structure (README + TEMPLATE) is being adopted with minor simplifications.
- **Context packet concept** — The file-path-per-workflow lists in his `README_PLATFORM_SUPPORT.md` are the direct basis for our `docs/context-packets/` design.

The review document itself (`RESEARCH_METHODOLOGY_REVIEW_AND_GENERALIZATION_PLAN.md`) is the most thorough external assessment this system has received. It validated the methodology's strengths ("creatively sophisticated and operationally useful") while honestly identifying gaps we're now addressing.

Brian's work pushed this project forward. Credit where it's due.

---

## The Problem

The methodology currently lives fragmented across multiple layers:

```
.kiro/sops/           ← Step-by-step procedures (detailed)
.kiro/agents/         ← Agent prompts (contain COPIES of procedures)
.kiro/skills/         ← Skill files (contain ANOTHER summary)
.kiro/steering/       ← Always-on rules (contain format rules)
references/           ← Deep reference data (scoring rubrics, genre tables)
```

**Consequences:**
- When the method updates, 3-5 files need manual syncing
- Agents can miss rules that exist in steering but weren't loaded (e.g., the `[Title]` tag incident)
- Non-Kiro users have no clear path to follow the methodology
- The "source of truth" for any given rule is ambiguous

---

## The Solution

Make `core/methodology/` the **single canonical source** for all methodology content. Everything else REFERENCES it rather than duplicating it.

### Proposed Architecture

```
songwriting-kb/
├── core/
│   └── methodology/
│       ├── songwriting.md          ← THE writing method (complete, self-contained)
│       ├── critique.md             ← THE critique method (complete, self-contained)
│       ├── suno-optimization.md    ← THE Suno optimization method (complete, self-contained)
│       ├── album-continuity.md     ← THE continuity method (complete, self-contained)
│       └── character-voice.md      ← THE character voice method (complete, self-contained)
├── references/
│   ├── CRITIQUE_REFERENCE.md       ← Deep scoring rubric details (referenced BY critique.md)
│   ├── CRITIQUE_REPORT_TEMPLATE.md ← Output format (referenced BY critique.md)
│   ├── SUNO_STYLE_GENRE_REFERENCE.md ← Genre/style data (referenced BY suno-optimization.md)
│   ├── SUNO_TAGS_REFERENCE.md      ← Tag reference (referenced BY suno-optimization.md)
│   └── CHARACTER_VOICE_REFERENCE.md ← Voice data (referenced BY character-voice.md)
├── .kiro/
│   ├── agents/
│   │   ├── critic.md               ← THIN — loads core/methodology/critique.md via #[[file:]]
│   │   ├── songwriter.md           ← THIN — loads core/methodology/songwriting.md
│   │   ├── suno-optimizer.md       ← THIN — loads core/methodology/suno-optimization.md
│   │   └── album-continuity.md     ← THIN — loads core/methodology/album-continuity.md
│   ├── steering/                   ← Quick-reference rules (derived FROM core/methodology/)
│   ├── skills/                     ← On-demand deep knowledge (references core/ + references/)
│   ├── hooks/                      ← Automated checks (references core/ rules)
│   └── sops/                       ← Step-by-step procedures (CAN be replaced by core/ if redundant)
├── docs/
│   └── context-packets/
│       ├── critique-packet.md      ← "Non-Kiro: give your AI THESE files"
│       ├── songwriting-packet.md
│       ├── suno-optimize-packet.md
│       └── album-continuity-packet.md
├── tools/
│   └── count-suno-fields.py        ← Deterministic char counter (platform-agnostic)
├── experiments/
│   └── suno/
│       ├── README.md               ← How to log Suno experiments
│       └── TEMPLATE.yml            ← Experiment log template
└── (existing: songs/, analysis/, examples/, etc.)
```

### The Flow

```
core/methodology/  ← THE METHOD (what to do, why, complete procedure)
       ↓ references for deep data
references/        ← SUPPORTING DATA (scoring tables, genre maps, templates)
       ↓ consumed by (Kiro users)
.kiro/agents/      ← THIN WIRING — points at core/ via #[[file:]]
.kiro/steering/    ← QUICK RULES — derived from core/ (subset for always-on loading)
.kiro/skills/      ← ON-DEMAND — loads core/ + references/ when activated
       ↓ consumed by (non-Kiro users)
docs/context-packets/ ← "Load THESE files into your AI to get the same result"
       ↓ consumed by (manual/CLI users)
tools/             ← Deterministic validation scripts
```

### The Rule

> **When the method changes, you update `core/methodology/`. Everything downstream inherits.**
> 
> `.kiro/` agents become thin loaders. They say WHO you are and WHAT to load — not HOW to do the work. The HOW lives in `core/methodology/`.

---

## What Each Layer Does

| Layer | Purpose | Size | Updates When |
|---|---|---|---|
| `core/methodology/` | THE canonical method | Fat (complete) | Method changes |
| `references/` | Deep supporting data | Fat (reference tables) | Data changes |
| `.kiro/agents/` | Kiro wiring — loads the right files | Thin (pointers) | Rarely |
| `.kiro/steering/` | Quick-reference always-on rules | Medium (derived subset) | Method changes |
| `.kiro/skills/` | On-demand deep knowledge activation | Medium (pointers + context) | Method changes |
| `.kiro/sops/` | MAY become redundant (core/ replaces them) OR stays as Kiro-specific step format | TBD | TBD |
| `docs/context-packets/` | Non-Kiro access instructions | Small (file lists + prompts) | Method changes |
| `tools/` | Deterministic validation | Code | When rules change |
| `experiments/suno/` | Suno version-dated test logs | Growing over time | Each test |

---

## Migration Plan

### Phase 1: Build `core/methodology/` (without breaking `.kiro/`)

1. Write `core/methodology/critique.md` — the FULL critique method, self-contained
2. Write `core/methodology/songwriting.md` — the FULL writing method
3. Write `core/methodology/suno-optimization.md` — the FULL Suno optimization method
4. Write `core/methodology/album-continuity.md` — the FULL continuity method
5. Write `core/methodology/character-voice.md` — the FULL voice design method

Each file should be COMPLETE ENOUGH to follow without any other file — but can reference `references/` for deep data tables.

### Phase 2: Rewire `.kiro/` to point at `core/`

1. Make agents thin — replace duplicated methodology content with `#[[file:core/methodology/X.md]]`
2. Make skills reference `core/` — skill activation loads the methodology file
3. Evaluate SOPs — if `core/methodology/` fully replaces them, SOPs become redundant. If SOPs add Kiro-specific steps (like "save to analysis/"), keep them as thin wrappers.
4. Steering stays as quick-reference rules (derived FROM core/ but kept lean for always-on loading)

### Phase 3: Add non-Kiro access

1. Write context packets for each workflow
2. Add `tools/count-suno-fields.py` (cherry-pick from Brian's PR)
3. Add `experiments/suno/` template (cherry-pick from Brian's PR)
4. Update README with "Using Without Kiro" section

### Phase 4: Verify nothing broke

1. Test: Kiro agents still load correctly and produce the same quality output
2. Test: Non-Kiro users can follow `core/methodology/` independently
3. Test: Context packets work with ChatGPT/Claude/other assistants
4. Test: `count-suno-fields.py` runs correctly on existing songs

---

## Relationship to multi-lang/songwriting-kb PR #3

**What we're adopting from their PR:**
- The PRINCIPLE of platform-neutral methodology as source of truth
- `tools/count-suno-fields.py` (deterministic validation)
- `experiments/suno/README.md` + `TEMPLATE.yml` (Suno experiment logging)
- The concept of version-dating Suno claims

**What we're doing differently:**
- `core/methodology/` files will be COMPLETE methods, not thin pointers to `.kiro/` SOPs
- `.kiro/` becomes the consumer, not the source
- No claim registry YAML (overkill — version notes in the methodology files themselves)
- No `README_PLATFORM_SUPPORT.md` as a separate file — integrated into main README
- No renaming of the project identity — this remains a Kiro-powered system with accessibility options

---

## Open Questions

1. **Do SOPs survive?** If `core/methodology/critique.md` contains the full step-by-step, does `.kiro/sops/02-critiquing-a-song.md` still need to exist? Or does the agent just load the methodology file directly?

2. **Steering overlap:** Steering files contain quick rules derived from the methodology. Do we keep them as a performance optimization (Kiro loads less), or do we consolidate into the methodology files?

3. **How fat is "fat enough"?** The methodology files need to be self-contained enough to follow independently — but how much detail? Do they include the full 12-category scoring rubric inline, or reference `CRITIQUE_REFERENCE.md` for that?

4. **Context packets vs README section:** Is a separate `docs/context-packets/` directory needed, or is a README section with "for critique, load these 3 files" sufficient?

---

---

## Cherry-Pick Assessment: multi-lang/songwriting-kb PR #3

Detailed evaluation of each file from Brian's PR for adoption into our restructuring.

### ✅ ADOPT: `tools/count-suno-fields.py` (with enhancements)

**What's good:**
- Clean Python, well-structured, proper argparse
- JSON output mode (useful for CI or hook integration)
- WARN threshold at 90% (catches "you're close" before you're over)
- Exit code 1 on failure (works in pipelines)
- Handles multiple files at once

**What needs fixing for OUR format:**
- Regex patterns assume `## STYLE PROMPT:` / `## LYRICS:` headers — our songs use inconsistent formats
- Doesn't account for `[Exclusions:]` block (should be EXCLUDED from lyrics count since it goes in Suno's Exclude field)
- Doesn't check for required tags (`[Title:]`, `[Production Direction:]`, `[Vocal Direction:]`)
- Doesn't separate Style Prompt from exclusions line

**Plan:** Adopt the structure, rewrite detection logic for our format. Expand into `tools/validate-song.py` — broader than just char counting. Add required-tag checks.

---

### ✅ ADOPT: `experiments/suno/README.md` (minor path edits)

**What's good:**
- Clear promotion rule (don't promote to universal guidance without evidence)
- Simple workflow (copy template → fill in → record → conclude)

**Changes needed:**
- Remove reference to `core/claims/claim-registry.yml` (not adopting)
- Update path references to our methodology file locations
- Otherwise adopt as-is

---

### ✅ ADOPT: `experiments/suno/TEMPLATE.yml` (simplify)

**What's good:**
- Structured fields: date, model version, settings, expected behavior, observations, conclusion
- Per-render observations with `supports_claim: yes/no/partial`
- Retest date forces revisiting

**Simplifications:**
- Remove `claim_under_test.claim_id` (assumes formal registry we don't have) — replace with plain description
- Consider converting from JSON-in-.yml to actual YAML
- Keep `persona_or_voice` and `custom_model` fields (forward-thinking for v5.5)

---

### ❌ REJECT: `core/claims/claim-registry.yml`

**Concept is useful, implementation is overkill:**
- 90 lines of YAML for 5 claims = absurd overhead
- CRAFT-001 and CRAFT-002 are established Pattison/Berklee practice, not volatile claims needing a registry
- PLATFORM-001 is their own PR thesis encoded as a "claim" — advocacy disguised as evidence
- Assumes a claims-management workflow nobody will maintain

**What to do instead:** Add a simple version-date table to `references/SUNO_STYLE_GENRE_REFERENCE.md`:

```markdown
## Suno Version Status

| Claim | Verified On | Suno Version | Confidence | Retest By |
|---|---|---|---|---|
| Style Prompt ≤1000 chars | June 2026 | v5.5 | High | Sept 2026 |
| [control: no-repeat] works | June 2026 | v5.5 | Medium | Sept 2026 |
| Pipe notation parsed | June 2026 | v5.5 | High | Dec 2026 |
| Era tags bias production | June 2026 | v5.5 | High | Dec 2026 |
| Genre must be first | June 2026 | v5.5 | High | Dec 2026 |
| 5-8 tags optimal | June 2026 | v5.5 | Medium | Sept 2026 |
```

10 lines instead of 90. Same purpose. No maintenance nightmare.

---

### ❌ REJECT: `core/claims/source-bibliography.md`

**Why:** Just maps internal file paths to source IDs. Our methodology files will cite sources inline. This adds indirection without value.

---

### 🔄 SAVE FOR LATER: `README_PLATFORM_SUPPORT.md` (content useful, file format wrong)

**What's useful:**
- The per-workflow file path lists are essentially context packets pre-written:
  - Critique: `.kiro/sops/02`, `.kiro/agents/critic.md`, `references/CRITIQUE_REFERENCE.md`
  - Songwriting: `.kiro/sops/01`, `.kiro/agents/songwriter.md`, `SONGWRITING_KNOWLEDGE_BASE.md`
  - Suno: `.kiro/sops/03`, `tools/count-suno-fields.py`, `references/SUNO_TAGS_REFERENCE.md`
- The "Reading order by use case" (full automation / assistant use / manual) is clean thinking
- Three-path approach matches our context packet concept exactly

**What's wrong:**
- Separate file will drift from README
- References files that don't exist yet
- Claims hooks that may not exist in our repo

**Plan:** Don't create this as a separate file now. Use the file-path-per-workflow concept as the basis for our `docs/context-packets/` in Phase 3. The matrix content gets integrated into the README "Using Without Kiro" section.

---

### ❌ REJECT: `core/methodology/*.md` (5 thin pointer files)

**Already discussed.** Our methodology files will be FAT (complete, self-contained methods), not thin pointers back to `.kiro/` SOPs. These 5 files are the wrong implementation of the right idea.

---

### ❌ REJECT: `docs/PLATFORM_GENERALIZATION_IMPLEMENTATION_PLAN.md`

**Why:** Their project management doc for their own PR. Not useful to us.

---

### ❌ REJECT: `docs/RESEARCH_METHODOLOGY_REVIEW_AND_GENERALIZATION_PLAN.md`

**Why:** Interesting read, surfaced real gaps, but not actionable as a repo file. The insights that matter are already captured in our architecture plan.

---

## Implementation Priority (Cherry-Picks)

When we reach Phase 3 of the migration, cherry-pick in this order:

1. **`tools/count-suno-fields.py`** → Rewrite as `tools/validate-song.py` with our format detection
2. **`experiments/suno/TEMPLATE.yml`** → Simplify and adopt
3. **`experiments/suno/README.md`** → Edit paths and adopt
4. **Suno version table** → Add to `references/SUNO_STYLE_GENRE_REFERENCE.md` (not a separate registry)
5. **Context packet file lists** → Derived from their platform support matrix, built during Phase 3

---

## Notes for Implementation

- This branch (`refactor/methodology-as-source-of-truth`) is the staging area
- Phase 1 is the heavy lift — writing the fat methodology files
- Phase 2 is the rewiring — making `.kiro/` thin
- Phase 3 is the accessibility layer — context packets + tools + experiments
- Don't merge to main until Phase 1 + 2 are complete and tested

---

## Future Improvements

### Audio Render Analysis Tool (`tools/analyze-render.py`)

**Status:** Planned — not yet implemented

**Purpose:** Quantitative verification of Suno renders against Production Notes. Closes the loop between what we asked for and what Suno actually produced.

**What it would measure:**

| Measurement | Library | What It Verifies |
|---|---|---|
| Actual BPM vs requested | librosa.beat.beat_track | Tempo accuracy |
| Actual key vs requested | librosa.feature.chroma_cqt | Key/harmony compliance |
| Dynamic range per section | librosa.feature.rms | Arrangement arc matches Production Direction |
| Functional layers present | Demucs (source separation) | Moore's 4 layers: drums/bass/harmony/melody |
| Hook timing | Self-similarity matrix + onset detection | When does the first repeated phrase appear |
| Vocal presence per section | Source separation → vocal energy | Confirms instrumental sections are actually instrumental |
| Song length vs requested | librosa.get_duration | Duration compliance |
| Spectral genre fingerprint | Spectral centroid + MFCCs | Genre alignment verification |
| Section contrast ratio | RMS energy between adjacent sections | Bridge actually stripped? Chorus actually bigger? |
| ALL CAPS = louder (verified) | Compare RMS of marked sections | Quantify the emphasis effect |

**Critic categories it could partially automate:**

- Hook (timing of first repeated melodic phrase)
- Arc (dynamic energy curve over time)
- Structure (section boundary detection via novelty)
- Genre (spectral fingerprint comparison)
- Arrangement (layer presence/absence, contrast ratios)
- Functional Layers - Moore (via Demucs source separation)
- Soundbox/Proxemics (reverb estimation, stereo width, vocal level)

**Dependencies:** Python 3.9+, librosa, numpy, matplotlib, Demucs (for separation), CREPE (for pitch)

**Integration:** Would accept an mp3/wav + the song's Production Notes (as JSON). Reports MATCH/MISMATCH for each parameter. Could feed into the critic's Suno Optimization Assessment.

**Prerequisite:** Needs local execution (GPU recommended for Demucs). Cannot run in Kiro Web sandbox.
