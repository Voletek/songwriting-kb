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
- **Conducted the first Suno experiment reporting that timbre descriptors outperform gear model names** (acid house, June 2026, Suno v5.5). Evidence basis for the Instrument Sound Reference (`references/INSTRUMENT_SOUND_REFERENCE.md`) [Tier 3: not yet reproduced in this repo or re-tested on V6].
- **Logged the performance-notation-symbols experiment** (`experiments/suno/2026-07-02-performance-notation-symbols.yml`, v5.5).

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

- **Performance Notation Symbols** (v5.5-era, legacy) -- 7 inline lyric formatting characters (~, -, ALL CAPS, ..., quotes, (), []) that affect vocal delivery
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
| **William Moylan** (*Understanding and Crafting the Mix*, 3rd ed., 2014) | Recording analysis, timbral balance, spatial imaging |
| **Pat Pattison** (Berklee) | Prosody, phrase weight, stable/unstable systems (books listed under Rhyme & Lyric Craft) |
| **Franco Fabbri** (1982), "A Theory of Musical Genres: Two Applications" | Genre as musical events (real or possible) governed by socially accepted rules of five types: formal & technical, semiotic, behavioural, social & ideological, economical & juridical |
| **Patrik N. Juslin** (2013), "From everyday emotions to aesthetic emotions: towards a unified theory of musical emotions", *Physics of Life Reviews* 10(3) | BRECVEMA: 8 mechanisms by which music induces (felt) emotion |
| **Eerola, Friberg & Bresin** (2013), "Emotional expression in music: contribution, linearity, and additivity of primary musical cues", *Frontiers in Psychology* 4:487 | Perceived-emotion cue hierarchy (mode > tempo > register > dynamics > articulation > timbre; tempo strongest for arousal) |
| **C. F. D. Schubart**, *Ideen zu einer Ästhetik der Tonkunst* (written 1784-85, publ. 1806); English in **Rita Steblin**, *A History of Key Characteristics in the Eighteenth and Early Nineteenth Centuries* (1983; 2nd ed. 2002) | Historical key characteristics (aesthetics under unequal temperaments, not psychology) |
| **Dodge et al.** (2025) | Evaluation criteria for popular music from expert raters with transparent criteria (innovation, beauty, scope of vision, technical prowess, generosity of spirit, authenticity). Primary citation (journal/DOI) not yet recorded; see PR Newswire, Feb 2026, "Academic Study Proposes New Standards for Evaluating Popular Music". Treated as Tier 2 until the primary source is added |
| **Gabrielsson & Lindstrom** (2010) | Emotional expression linearity in primary musical cues |
| **Tim Murphey** (1989, 1992) | Pop lyric corpus analysis -- temporal vagueness and "appropriability" |
| **Rebecca Wilson** (PhD, Queen's University Belfast, 2025; citation unverified) | 1291-song corpus stylistics, imaginative deixis in popular lyrics |
| **SD Jenkins** (Research Master, 2018) | Form, content, craft -- verse/chorus as rearrangement of time/space |
| **Kreyer & Mukherjee** (corpus linguistics) | Pop lyrics on boundary between speech and writing |
| **Werner** (register analysis) | Pop lyrics as simulated immediacy -- planned performance of conversational register |
| **Peter Stockwell** (*Cognitive Poetics*, 2002) | Temporal deixis, deictic shift theory, deictic centre |
| **Joanna Gavins** (*Text World Theory: An Introduction*, 2007) | Temporal parameters as world-building elements |
| **Matthew Voice & Sara Whiteley** (2019), "'Y'all don't wanna hear me, you just wanna dance': A cognitive approach to listener attention in OutKast's 'Hey Ya!'", *Language and Literature* 28(1) | Cognitive analysis of listener attention to lyrics and deixis in song |
| **Janiszewski & Uy** (precision anchoring) | Precise numbers anchor more strongly due to finer-resolution scale |
| **Mason, Lee, Wiley, Ames** | Precise offers perceived as more informed -- precision signals expertise |
| **Jack Perricone** (*Great Songwriting Techniques*, 2018) | Scenario development -- time grounds scene, prosodic interaction |
| **NSAI** (Nashville Songwriters Association) | "Be descriptive, but not so specific that your audience cannot relate" |

---

## Rhyme & Lyric Craft

| Source | Contribution |
|---|---|
| **Pat Pattison**, *Writing Better Lyrics* (2nd ed., 2009) and *Songwriting: Essential Guide to Rhyming* (Berklee Press) | Rhyme ladder (perfect > family > additive/subtractive > assonance > consonance), consonant families, section stability, prosody |
| **Andrea Stolpe** (Berklee) | Article on rhyme types and their relative strength |
| **Sheila Davis**, *The Craft of Lyric Writing* (1985) | Lyric forms, rhetorical devices, cliche avoidance |
| **Jimmy Webb**, *Tunesmith: Inside the Art of Songwriting* (1998) | The perfect-rhyme (standards/Broadway) school, contrasted with Pattison's family/slant approach |
| **Julia Cameron**, *The Artist's Way* (1992) | Morning pages (daily free-writing) |
| **CMU Pronouncing Dictionary** (Carnegie Mellon University, BSD-licensed) | Pronunciations and stress marks used for syllable/stress/rhyme checks in `tools/lyric-lint.py` |
| **`pronouncing`** (Python library by Allison Parrish) | Simple interface to CMUdict (optional dependency of `tools/lyric-lint.py`) |
| **Datamuse API** | Word-finding API (rhymes, near rhymes, sounds-like) recommended as a rhyme tool |
| **Hussein Hirjee & Daniel G. Brown** (ISMIR 2009; *Empirical Musicology Review* 2010) | Rhyme Analyzer and automatic detection of internal and imperfect rhymes in rap lyrics |

---

## Tools & Platforms

- **[Kiro](https://kiro.dev)** — IDE automation layer (agents, skills, hooks, steering, powers)
- **[Suno AI](https://suno.com)** — AI music generation platform (v4.5-v5.5 legacy; V6 model family v6 / v6-wild / v6-mini, the default since Sept 2026)
- **Nashville/LA co-writing tradition** — structural methodology (chorus-first, quality gates)
- **Berklee Online** — songwriting craft education

---

## Community

The Suno prompt science sections incorporate community-tested research from:
- Suno community forums and Discord (2024-2026)
- beehiiv/roo research articles (2026) — prompt formula, era anchoring, genre combinations
- HowToPromptSuno.com — structural prompt methodology
- stayen/suno-reference (November 2025) — v5.0 meta-tag documentation
