# Credits & Acknowledgments

---

## Creator & Maintainer

**Voletek** ([@Voletek](https://github.com/Voletek))
- System architecture, all methodology content, all songs, all critique frameworks
- Suno AI prompt engineering and testing
- Concept album design (Fractured Shadows, Keeper of the Light)
- Professional songwriting workflow development

---

## Contributors

### 21machines ([Suno profile](https://suno.com/@21machines))

First community user to adopt the system. Provided direct feedback that led to the v2.0 directory restructure:

- **Identified the songs/analysis separation problem** — flagged that developer example songs mixed with user songs creates confusion during `git pull`
- **Requested clean workspace directories** — directly led to moving all example content from `songs/` and `analysis/` into `examples/` so working directories are empty for users
- **Validated the platform-neutral approach** — confirmed the system works with Kiro for users who understand markdown
- **Conducted first Suno experiment proving timbre descriptors outperform gear model names** (acid house, June 2026). Evidence basis for the Instrument Sound Reference (`references/INSTRUMENT_SOUND_REFERENCE.md`).

---

### Brian Smith Clark ([@multi-lang](https://github.com/multi-lang))

Brian forked the repo, conducted a thorough methodology review, and submitted [PR #3](https://github.com/multi-lang/songwriting-kb/pull/3) proposing platform generalization. His contributions directly influenced the v2.0 architecture refactor:

- **Identified the fragmented source-of-truth problem** — the insight that methodology was duplicated across agents, SOPs, skills, and steering with no single canonical source
- **Proposed platform-neutral methodology** — the principle that songwriting knowledge should exist independently of any tool's config format
- **Suno version-dating concept** — the observation that Suno-specific claims need version labels and expiry dates
- **`tools/count-suno-fields.py`** — the original deterministic character counter (foundation for `tools/validate-song.py`)
- **`experiments/suno/` framework** — experiment template and promotion rules for Suno-versioned testing
- **Platform support matrix concept** — per-workflow file lists that informed context packet design
- **Methodology review document** — the most thorough external assessment the system received

---

### Omnisona ([Suno AI God Mode Manual v3.0](https://omnisona.com), March 2026)

Author of the comprehensive Suno AI God Mode Manual. Six contributions integrated into the knowledge base:

- **Performance Notation Symbols** -- 7 inline lyric formatting characters (~, -, ALL CAPS, ..., quotes, (), []) that affect vocal delivery
- **Anti-Pairs** -- genre combinations with near-zero compatibility (Gregorian Chant+Trap, Classical Baroque+Lo-fi Bedroom Pop, Opera+Mumble Rap)
- **Groove/Time-Feel Descriptors** -- optional 8th dimension for rhythmic specificity (medium swing, four-on-the-floor, syncopated, etc.)
- **Call-and-Response Instrument Technique** -- vocal/instrument conversational pattern using [instrumental break X] tags
- **Environmental/Ambient SFX Tags** -- 9 atmosphere tags ([Rain], [Thunder], [Birds chirping], [Wind], [Ocean waves], [City ambience], [Fire crackling], [Static], [Record scratch])
- **Probabilistic Generation Framing** -- tags shape probability not guarantees; generate 3-4 versions; treat Suno as collaborator

All contributions labeled [Tier 3: Community heuristic].

---

## Academic Sources

| Scholar/Source | Contribution |
|---|---|
| **Allan F. Moore** (*Song Means*, 2012) | 4 functional texture layers, soundbox theory, persona analysis |
| **Philip Tagg** (*Music's Meanings*, 2013) | Musemes, semiotic signification, cultural connotation of timbres |
| **Serge Lacasse** (2000, 2010) | Vocal staging, proxemic interaction in recorded song (composite framework: Hall proxemics theory + Lacasse vocal staging + Moore recorded song hermeneutics) |
| **William Moylan** (2014) | Recording analysis, timbral balance, spatial imaging |
| **Pat Pattison** (Berklee) | Prosody, phrase weight, stable/unstable systems |
| **Franco Fabbri** (1982) | Genre theory — 5 rules of genre membership |
| **Patrik Juslin** (2013) | BRECVEMA emotional mechanisms (8 pathways by which music induces emotion) |
| **Eerola, Friberg & Bresin** (2013, *Frontiers in Psychology* 4:487) | Emotional cue hierarchy (mode > tempo > register > dynamics > articulation > timbre) |
| **Christian Schubart** (1806) | Key characteristics and emotional associations |
| **Dodge et al.** (2025) | 6 universal evaluation criteria for popular music |
| **Gabrielsson & Lindstrom** (2010) | Emotional expression linearity in primary musical cues |
| **Tim Murphey** (1989, 1992) | Pop lyric corpus analysis -- temporal vagueness and "appropriability" |
| **Rebecca Wilson** (PhD, Queen's University Belfast, 2025) | 1291-song corpus stylistics, imaginative deixis in popular lyrics |
| **SD Jenkins** (Research Master, 2018) | Form, content, craft -- verse/chorus as rearrangement of time/space |
| **Kreyer & Mukherjee** (corpus linguistics) | Pop lyrics on boundary between speech and writing |
| **Werner** (register analysis) | Pop lyrics as simulated immediacy -- planned performance of conversational register |
| **Peter Stockwell** (*Cognitive Poetics*, 2002) | Temporal deixis, deictic shift theory, deictic centre |
| **Joanna Gavins** (*Text World Theory: An Introduction*, 2007) | Temporal parameters as world-building elements |
| **Voice & Whiteley** | Multimodal cognitive analysis of deixis in song |
| **Janiszewski & Uy** (precision anchoring) | Precise numbers anchor more strongly due to finer-resolution scale |
| **Mason, Lee, Wiley, Ames** | Precise offers perceived as more informed -- precision signals expertise |
| **Jack Perricone** (*Great Songwriting Techniques*, 2018) | Scenario development -- time grounds scene, prosodic interaction |
| **NSAI** (Nashville Songwriters Association) | "Be descriptive, but not so specific that your audience cannot relate" |

---

## Tools & Platforms

- **[Kiro](https://kiro.dev)** — IDE automation layer (agents, skills, hooks, steering, powers)
- **[Suno AI](https://suno.com)** — AI music generation platform (v4.5-v5.5)
- **Nashville/LA co-writing tradition** — structural methodology (chorus-first, quality gates)
- **Berklee Online** — songwriting craft education

---

## Community

The Suno prompt science sections incorporate community-tested research from:
- Suno community forums and Discord (2024-2026)
- beehiiv/roo research articles (2026) — prompt formula, era anchoring, genre combinations
- HowToPromptSuno.com — structural prompt methodology
- stayen/suno-reference (November 2025) — v5.0 meta-tag documentation
