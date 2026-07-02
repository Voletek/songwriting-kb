# The Critique Method

> **CANONICAL METHODOLOGY** -- This file is the single source of truth for song critique.
> A non-Kiro user can read ONLY this file and execute the complete multi-layer critique model.
> For the full scoring rubric tables, see `references/CRITIQUE_REFERENCE.md`.
> For the output template, see `references/CRITIQUE_REPORT_TEMPLATE.md`.

---

## Overview: The Multi-Layer Critique Model

The critique system operates in layers, each answering a different question:

```
Layer 1: CORE 12 CATEGORIES (Craft)        -- "Is it well-made?"
Layer 2: ADVANCED 5 ASSESSMENTS (Depth)     -- "Is it meaningful and rewarding?"
Layer 2.5: SUNO OPTIMIZATION (Render)       -- "Will Suno produce its best version?"
Layer 3: ALBUM-CONTEXT MODULE (Continuity)  -- "Does it serve its role?" (concept albums only)
+ CALIBRATION & TECHNICAL AUDIT             -- "Are the systems working correctly?"
```

**Which layers to apply:**

| Scenario | Layers |
|---|---|
| Quick feedback / "is this good?" | Layer 1 only + Strongest Line + 2 flags |
| Full pipeline critique (Stage 2) | Layers 1 + 2 + 2.5 + Recommendations |
| Concept album track | All layers (1 + 2 + 2.5 + 3) + Calibration |
| Standalone single / experimental | Layers 1 + 2 + 2.5 + Calibration (skip Layer 3) |
| Re-critique after revision | Layer 1 + 2.5 + delta from previous score |
| Suno render check only | Layer 2.5 only (skip all scoring) |

---

## Three-Tier Evidence Labeling System

Claims in this methodology carry one of three evidence tiers:

| Label | Meaning |
|---|---|
| **[Tier 1: Scholarship-backed]** | Documented academic framework with primary sources and peer-reviewed research. |
| **[Tier 2: Professional heuristic]** | Widely-used craft guidance supported by professional practice but not empirically validated as universal law. |
| **[Tier 3: Community/platform heuristic]** | Empirical observation from practitioner testing (e.g., Suno community experiments). Unverified, version-dependent. |

Unlabeled claims are general craft consensus or structural descriptions that do not require tiering.

---

## Prerequisites

- A complete song (lyrics + production notes, or at minimum lyrics + genre/tempo info)
- Access to the Style & Genre Reference for evaluating genre/key/BPM/instrument choices
- If album track: access to the Album Blueprint for this track's intended role, emotion, and palette
- If the song has an existing self-score: note it but do NOT let it anchor your assessment

---

## The Complete Critique Procedure

### Step 1 -- Read Completely (No Scoring Yet)

Read the entire song once without evaluating. Absorb:
- What is this trying to be?
- What is the intended context (single, album track, concept piece)?
- What is the emotional thesis?

### Step 2 -- Apply the 9-Step Analysis

Work through each quickly (1-2 sentences each). This is internal scaffolding -- it informs scoring but does not appear verbatim in the final report.

| # | Step | Question to Answer |
|---|---|---|
| 1 | **Semantic** | What is it literally about? (subject, characters, setting, actions) |
| 2 | **Emotional** | Central affect? Which BRECVEMA mechanisms targeted? |
| 3 | **Prosodic** | Stresses, breaths, rhymes, syllable counts, phrase lengths, singable vowels |
| 4 | **Narrative** | Does it escalate, collapse, confess, transform? Where is the turn? |
| 5 | **Voice** | Who is speaking? Vowel placement, rhythm, instrumentation match? |
| 6 | **Genre** | Fabbri's 5 rules satisfied? Fusion balanced (70/30)? |
| 7 | **Arrangement** | Growth pattern, contrast pairs, negative space, repetition calibration |
| 8 | **Production** | Timbre palette (Tagg musemes), harmonic choices, soundbox design, proxemic distance |
| 9 | **Commercial** | Audience, platform, length, sync readiness, 7-second rule, skip test scan |

### Step 3 -- Score Each Core Category (Layer 1: 1-10 Each)

Score using the rubric definitions below. For each category, write ONE sentence justifying the score.

**CONTEXT RULE:** Score relative to the song's INTENDED context. A concept album track is scored against concept album standards, not radio singles. A folk ballad is scored against folk conventions, not pop hooks. For album tracks, "Commercial" assesses whether the track serves its position in the album's emotional arc, not standalone chart potential.

---

## The 12-Category Scoring Rubric

### 1. Hook (Memorable? Singable? Hook signal within first 5-30s?)

| Score | Meaning |
|---|---|
| 9-10 | Instantly memorable, arrives early, works a cappella, textable, melodically distinct |
| 7-8 | Strong phrase, good repetition, slightly late arrival or relies on context |
| 5-6 | Functional but not sticky, arrives too late, or too generic |
| 3-4 | Weak -- forgettable, buried, or unclear what the hook IS |
| 1-2 | No identifiable hook |

**Hook timing verification:** [Tier 2] At the song's BPM, count ~2-3 seconds per sung line with breath. (Total lines before hook x 2.5s) + intro seconds = time to hook. Aim for 5-30s from first sung vocal (genre-dependent).

### 2. Lyrics (Imagery? Specificity? Visual/cinematic writing?)

| Score | Meaning |
|---|---|
| 9-10 | Every line earns its place, physical/sensory imagery, show-don't-tell, original phrasing |
| 7-8 | Strong imagery with occasional abstract lines, mostly specific |
| 5-6 | Mix of good and generic, some tell-not-show, functional |
| 3-4 | Mostly generic/abstract, cliches present, diary-trap |
| 1-2 | Entirely generic, no imagery, pure abstraction |

### 3. Prosody (Stress alignment? Phrase length? Breath placement?)

| Score | Meaning |
|---|---|
| 9-10 | Every stressed syllable on strong beat, consistent phrase lengths, natural breath points, singable vowels on sustained notes |
| 7-8 | Mostly aligned with 1-2 stuffed lines, generally singable |
| 5-6 | Inconsistent -- some lines sing well, others are prose crammed into melody |
| 3-4 | Many lines fight the meter, reversed stresses, breath-hostile |
| 1-2 | Written as prose with no consideration for singing |

**Prosody check method:** Count syllables per line (target 7-12). Identify stressed syllables -- do they land on beats 1 and 3? Check for open vowels on sustained/high notes. Verify em-dashes create actual breath points. Flag any line over 12 syllables. For flagged lines, apply the Compression Test (see songwriting.md) to determine whether to compress, keep as spoken, or rewrite.

### 4. Arc (Transformation? Turn? V2 adds new info?)

| Score | Meaning |
|---|---|
| 9-10 | Clear emotional journey, genuine turn in bridge, final chorus means something different than first, V2 adds new information |
| 7-8 | Good movement with one static section or slightly weak turn |
| 5-6 | Some development but largely same emotional state throughout |
| 3-4 | Flat -- same feeling start to finish, no transformation |
| 1-2 | No discernible arc |

### 5. Structure (Length appropriate? Negative space? Contrast?)

| Score | Meaning |
|---|---|
| 9-10 | Perfect length for platform, effective silence/space, dynamic contrast between sections, nothing excess |
| 7-8 | Good structure with one slightly long section or missed contrast opportunity |
| 5-6 | Functional but predictable, some bloat, limited contrast |
| 3-4 | Over-long, no breathing room, or too short to develop |
| 1-2 | Structurally broken |

### 6. Originality (Fresh angle? Unique phrasing?)

| Score | Meaning |
|---|---|
| 9-10 | Concept, imagery, and phrasing feel genuinely fresh -- "I have never heard it said this way" |
| 7-8 | Mostly fresh with one or two familiar phrases |
| 5-6 | Solid but you have heard similar songs explore this territory |
| 3-4 | Relies heavily on common tropes/phrases without subversion |
| 1-2 | Entirely derivative |

### 7. Singability (Syllable density? Vowel placement? Melodic potential?)

| Score | Meaning |
|---|---|
| 9-10 | Every line sits naturally in the voice, open vowels on holds, consistent phrase rhythm, could be hummed |
| 7-8 | Mostly singable with 1-2 dense passages |
| 5-6 | Mix of singable and prose-like lines, inconsistent |
| 3-4 | Many lines resist melody, consonant clusters, irregular rhythm |
| 1-2 | Reads as prose/poetry, not lyrics |

### 8. Commercial Viability (Platform fit? Sync ready? 7-second rule?)

| Score | Meaning |
|---|---|
| 9-10 | Hits target platform perfectly, hook signal early, right length, sync-placeable |
| 7-8 | Good fit with minor adjustments needed (slightly long, hook slightly late) |
| 5-6 | Works for its context but limited broader appeal |
| 3-4 | Too niche, too long, or structurally uncommercial |
| 1-2 | No commercial pathway |

**Context rule:** For album tracks, "Commercial" means: does this track serve its position in the album's emotional arc, not standalone chart potential.

### 9. Genre Alignment (Conventions honored? Fusion balanced?)

| Score | Meaning |
|---|---|
| 9-10 | Perfectly serves genre expectations (Fabbri's 5 rules) while adding freshness |
| 7-8 | Mostly aligned with one genre drift or missed convention |
| 5-6 | General genre fit but does not fully commit or honor specific conventions |
| 3-4 | Genre confused -- conflicting signals |
| 1-2 | No discernible genre coherence |

**Fabbri's 5 Rules:** formal and technical rules (structural conventions), semiotic rules (what the genre signifies), behaviour rules (performance conventions), social and ideological rules (community values), economical and juridical rules (marketplace expectations).

### 10. Arrangement/Production (Dynamics? Timbre? Contrast?)

| Score | Meaning |
|---|---|
| 9-10 | Every production choice signifies correctly (Tagg), dynamic range exceptional, contrast pairs effective, negative space used |
| 7-8 | Strong design with one missed opportunity |
| 5-6 | Functional but predictable, limited dynamic range |
| 3-4 | Production choices do not support the lyric meaning |
| 1-2 | No production consideration |

### 11. Accent/Voice Coherence (Dialect? Cultural instrumentation?)

| Score | Meaning |
|---|---|
| 9-10 | Voice, accent, instrumentation, and mode all from same cultural ecosystem, dialect in lyrics reinforces, persona is clear and distinct |
| 7-8 | Coherent voice with minor inconsistencies |
| 5-6 | Generic voice -- correct but not character-driven |
| 3-4 | Voice conflicts with instrumentation or genre |
| 1-2 | No vocal identity consideration |

**Persona distinction (Moore):** Three layers: real person, performer's public identity, song character. The Voice/Accent score assesses whether the SONG CHARACTER's voice is coherent and believable.

### 12. Emotional Intelligence (Authentic? Transcendent? Responsible?)

| Score | Meaning |
|---|---|
| 9-10 | Expresses without exploiting, offers companionship not solutions, handles darkness responsibly, achieves transcendence, generous to the listener |
| 7-8 | Authentic and thoughtful with one slightly forced moment |
| 5-6 | Genuine but does not push beyond surface emotion |
| 3-4 | Manipulative, glorifying, or dismissive of real pain |
| 1-2 | Exploitative or harmful |

**Generosity of spirit (Dodge):** Does the song GIVE something to the listener? Companionship in pain, beauty in darkness, recognition of experience?

---

### Step 4 -- Calculate Composite

Average all 12 scores. This is the core composite.

---

## The 5 Advanced Assessments (Layer 2: 1-10 Each)

These go DEEPER than craft. They assess whether the song is meaningful, spatially designed, semiotically correct, artistically ambitious, and temporally rewarding.

### A1. Functional Layer Completeness (Moore)

Based on Moore's 4 functional texture layers (described as generalized descriptions, not prescriptive rules -- not all will be present in every example): explicit beat (percussion), functional bass (bass-register harmonic foundation), harmonic filler (keyboards/guitars/pads), melodic layer (voice + melodic instruments).

| Score | Meaning |
|---|---|
| 9-10 | All 4 layers present, perfectly balanced, each serves the song without competing. Layers breathe (thin when needed, full when earned). |
| 7-8 | All layers present, one slightly over/under-represented but song still works |
| 5-6 | One layer missing or competing -- texture feels thin or cluttered |
| 3-4 | Two layers weak or absent -- song feels unmoored or claustrophobic |
| 1-2 | Textural chaos or emptiness -- layers fight, overlap, or are not considered |

### A2. Soundbox & Proxemic Design (Moore + Lacasse + Moylan)

The soundbox is the virtual 3D space (left-right, close-far, high-low). Proxemics measures perceived distance between vocalist and listener.

**Proxemic distances:**
- **Intimate:** Dry, close-mic, breath audible, near-whisper. Secrets, vulnerability.
- **Conversational:** Light room reverb, natural delivery. Storytelling, connection.
- **Social:** Moderate reverb, some projection. Performance, address.
- **Public:** Heavy reverb, projected, vast space. Declaration, anthem.
- **Dissolved:** Underwater/infinite reverb, voice=environment. Transcendence. *(Note: "Dissolved" is our adaptation extending the framework beyond Lacasse's original categories. The proxemics model here is composite: Hall's proxemics theory + Lacasse's vocal staging semiotics + Moore's recorded song hermeneutics.)*

| Score | Meaning |
|---|---|
| 9-10 | Soundbox is vivid and intentional. Proxemic distance matches emotional content perfectly and CHANGES meaningfully across the song. |
| 7-8 | Good spatial design with one section where distance does not match emotion |
| 5-6 | Generic space -- sounds like "a recording" rather than a specific place |
| 3-4 | Distance contradicts content (intimate lyrics in stadium reverb) |
| 1-2 | No spatial consideration -- flat, dimensionless |

### A3. Musemic Signification (Tagg)

A museme = the smallest meaningful musical unit. It carries cultural connotations inferred through culturally-informed interobjective comparison. The question: do the sounds MEAN what they should?

| Score | Meaning |
|---|---|
| 9-10 | Every timbre, riff, and texture carries the correct cultural connotation. A listener with no lyrics would still FEEL the intended emotion from music alone. |
| 7-8 | Mostly correct with one timbral choice that is neutral (does not help or hurt) |
| 5-6 | Some musemes carry mixed signals -- instrumentation is "fine" but does not signify |
| 3-4 | Key musemes contradict lyric intent (upbeat production on grief, chirpy sounds on dread) |
| 1-2 | Complete semiotic mismatch -- music and lyrics say opposite things |

### A4. Scope of Vision (Dodge et al.)

Measures artistic ambition -- not just craft execution but REACH.

| Score | Meaning |
|---|---|
| 9-10 | Attempts something genuinely difficult and succeeds -- conceptual depth, structural innovation, emotional range. "This could not have been easy to write." |
| 7-8 | Ambitious scope with strong execution -- reaches beyond convention in at least one dimension |
| 5-6 | Competent but plays it safe -- stays within well-mapped territory. No artistic risk. |
| 3-4 | Formulaic -- follows templates without adding vision |
| 1-2 | No discernible artistic intent beyond basic completion |

**Key insight:** A daring song that partially fails may score HIGHER here than a safe song that fully succeeds. This category rewards AMBITION.

### A5. Skip Test -- Dead Zone Scan (A&R Industry)

Mentally scan every ~15-second window. In each window, is there: new information, contrast, a hook/surprise/reward, or forward momentum? If ANY window answers "no" to all four: dead zone.

| Score | Meaning |
|---|---|
| 9-10 | Zero dead zones -- every moment earns attention |
| 7-8 | One brief moment (~5-8 seconds) that could lose a casual listener |
| 5-6 | One full 15-second dead zone (overly long intro, identical repeated chorus) |
| 3-4 | Multiple dead zones -- listener would check remaining time |
| 1-2 | Fundamental engagement failure from the start |

**Common dead zones:** Intro longer than 15s without sonic interest. Repeated chorus with identical lyrics AND production. Bridge that restates without turning. Outro that just fades.

Calculate **advanced composite** (average of 5). This does NOT replace the core composite -- it is a separate depth-score.

---

## The Suno Optimization Assessment (Layer 2.5)

Evaluates whether the Style Prompt and tag choices are OPTIMAL for the song's emotional content.

### 5a. The 7-Point Dimensional Check

For each dimension, assess CORRECT / SUBOPTIMAL / WRONG:

| # | Dimension | Framework | Check Against |
|---|---|---|---|
| 1 | **Genre** | Fabbri (5 rules) | Does this genre SIGNIFY what the lyrics express? |
| 2 | **Key** | Eerola, Friberg & Bresin (cue hierarchy) | Mode is #1 emotional cue. Does key character match dominant emotion? |
| 3 | **BPM** | Genre + emotion mapping | Correct for BOTH genre conventions AND emotional pacing? |
| 4 | **Instruments** | Tagg (musemes) | Does each instrument carry the correct cultural connotation? Described as SOUNDS, not gear names? Character budget efficient? |
| 5 | **Vocal style** | Moore (persona) + Fabbri (behavioral) | Delivery matches genre AND serves the lyric arc? |
| 6 | **Era/Production** | Suno era-anchoring | Would a specific sonic period improve specificity? Era separated from instrumentation? |
| 7 | **Space/Mood** | Tagg + Lacasse | Atmospheric descriptors aligned, non-contradictory, <=3 total? |

### 5b. Section-Level Tag Evaluation

- Does each section's production cue tag signify correctly for THAT section's content? (Tagg applied)
- Do tags contrast between adjacent sections?
- Are tags <=3 per section?
- Do tags support the proxemic arc? (Sparse = intimate, full = public)

### 5c. Compliance Checklist

Binary pass/fail checks:
- Required elements present? (`[Title:]`, `[Production Direction:]`, `[Vocal Direction:]`, `[end]`)
- Character limits respected? (Style <=1000, Lyrics <=5000)
- Genre first in Style Prompt? Tag count 5-8? No contradictions?
- Named `()` layers declared in Style Prompt?
- Exclusions in dedicated Exclude field (not in Style or Lyrics)?
- No artist names present in Style Prompt or Production Direction? (converted to descriptive production language)
- No gear/model names present in Style Prompt or Production Direction? (converted to sound descriptors) [Tier 3]

### 5d. Overall Verdict

- **OPTIMAL** -- All 7 dimensions CORRECT. No changes needed.
- **COULD IMPROVE** -- 1-3 dimensions SUBOPTIMAL. Provide 2 alternative Style Prompts.
- **MISMATCHED** -- 1+ dimensions WRONG or 4+ SUBOPTIMAL. Revision strongly recommended.

### 5e. Style Alternatives (if not OPTIMAL)

Provide 2 complete alternative Style Prompts (ready to paste into Suno) with:
- Full rewritten prompt text
- Reasoning (why this serves the emotional content better)
- Expected improvement in render quality
- Slider recommendation (Weirdness % / Style Influence % / Audio Influence %)

---

## The Album-Context Module (Layer 3: Concept Albums Only)

Skip entirely for standalone songs. For concept album tracks, run all 6 checks:

| # | Check | Question | Result Options |
|---|---|---|---|
| C1 | **Position Awareness** | Does this track know WHERE it sits in the arc? An opener establishes; a climax delivers; a denouement resolves. | PASS / CONCERN / FAIL |
| C2 | **Intention vs Delivery** | Compare the blueprint's stated "Core Emotion" against what the song ACTUALLY delivers. | MATCH / PARTIAL / MISS |
| C3 | **Transition Consciousness** | Does the ending create harmonic/timbral/emotional gravity toward the next track? | STRONG / ADEQUATE / WEAK |
| C4 | **Dramatic Irony Management** | Does the song give the AUDIENCE more information than the CHARACTER has? Is irony planted without being on-the-nose? | PRESENT & EFFECTIVE / PRESENT BUT HEAVY / ABSENT |
| C5 | **Motif & Callback Accuracy** | Are recurring motifs used correctly per the blueprint? In the right tracks? With the right meaning evolution? | CORRECT / MINOR ISSUE / VIOLATION |
| C6 | **Sonic Differentiation** | Does this track sound sufficiently DIFFERENT from adjacent tracks? (<70% palette overlap) | PASS / BORDERLINE / FAIL |

---

## Calibration & Technical Audit

Run after all scoring is complete:

| Check | What to Do |
|---|---|
| **Self-Score Delta** | If existing self-score: note gap. Self-critiques inflate by ~1.0 point. Delta <0.5 = well-calibrated. Delta >1.0 = significant overestimation. |
| **Parenthetical Layer Audit** | If `()` layers used: Are named layers declared in Style Prompt? Is density appropriate for emotional moments? Serving or cluttering? |
| **Production-Lyric Alignment** | Explicit Tagg check: Do production choices REINFORCE or CONTRADICT lyric meaning? Flag mismatches (e.g., "silence" lyric + busy production). |
| **Discovery Depth** | Would a second listen reveal something new? Rate: HIGH (multiple hidden layers) / MEDIUM (some texture) / LOW (what you hear first is what you get). |

---

## Post-Scoring Steps

### Step 5 -- Identify Strongest Line

Find the ONE line you would build the whole song around. Quote it. Explain in 1-2 sentences WHY it works (imagery? rhythm? meaning? surprise? multi-level operation?).

### Step 6 -- Flag ALL Issues

For each issue found (do not limit to a fixed number -- report everything):
1. Name the problem (specific -- not "could be better")
2. Quote the current line (for lyric issues) OR describe the specific moment/decision
3. Explain WHY it is a problem (prosody? forced rhyme? abstract? redundant? predictable?)
4. Provide a fix:
   - For lyric issues: 2-3 alternative lines that solve it
   - For structural issues: describe the structural change
   - For production/arrangement issues: describe the production fix

**Rule:** Fixes must SOLVE THE STATED PROBLEM while maintaining the song's thesis and voice.

### Step 7 -- Write Priority Recommendations

ALL identified issues, ordered by impact (biggest improvement first). At least one should address lyrics/content and one should address structure/arrangement/production -- but impact ordering takes precedence over category diversity.

### Step 8 -- Save the Report

Use the standardized report template from `references/CRITIQUE_REPORT_TEMPLATE.md`. Save to `analysis/[song-filename]_critique.md`.

---

## Decision Gate Rules

The **core 12-category composite** drives the pipeline decision:

| Composite | Action |
|---|---|
| >= 8.5 | Skip revision, proceed to Optimize |
| 7.0 - 8.4 | Revise, then re-critique |
| < 7.0 | Return to concept/writing with new approach |

**Override rule:** If the core composite passes (>=8.5) but Album-Context checks show FAIL on Position Awareness, Intention vs Delivery, or Motif Accuracy -- flag for revision regardless. Album continuity failures override craft scores.

**Advanced composite** is informational -- it identifies depth issues that may not surface in craft scoring alone. A song with Core 8.5 but Advanced 6.0 is well-crafted but shallow. A song with Core 7.5 but Advanced 9.0 is ambitious and meaningful but needs craft polish.

---

## Common Flag Patterns

| Pattern | What to Flag | Fix |
|---|---|---|
| Stuffed line | >12 syllables at tempo | Trim or split |
| Reversed stress | Weak word on strong beat | Reorder words |
| Abstract where physical needed | "feeling sad" vs "hands won't stop shaking" | Replace with sensory |
| Rhyme forcing | Meaning bent to serve rhyme | Use slant rhyme or restructure |
| V2 repeats V1 | No new information in second verse | Add narrative progression |
| Bridge restates | Bridge says what chorus already said | Find the TURN |
| Over-explanation | Imagery + thesis statement of same idea | Trust the imagery, cut the thesis |
| Generic hook | Could be in any song | Make specific to THIS song's world |
| Prose bridge | 12+ lines of non-melodic content | Trim to 6-8, impose syllable discipline |
| Soundbox static | Same spatial depth entire song | Vary proxemic distance per section |
| Layer missing | No harmonic filler or bass presence | Add mid-range texture or bass foundation |
| Musemic contradiction | Bright sounds on dark lyrics | Align timbral connotation to content |
| Anti-pair genre combo | Genre A + Genre B in Style Prompt are known incompatible (Cinematic+Dark, Opera+Melodic, D&B+Funk) [Tier 3: Omnisona] | Replace one genre or use compatible combination |
| Dead zone | 15+ seconds with no new information | Add contrast, cut length, or introduce variation |
| Proxemic mismatch | Intimate lyrics at public distance | Match reverb/mic treatment to emotional content |

---

## Quality Principles

1. Be honest but constructive -- identify what WORKS before what does not
2. The strongest line matters more than the weakest (build from strength)
3. Prosody issues are FIXABLE -- do not catastrophize them
4. If emotional intelligence is high (9-10), the song has a soul -- everything else is polish
5. A 7.5/10 concept album track may be PERFECT for its role -- context matters
6. Self-critiques inflate by ~1.0 point -- note the delta
7. Every alternative must be BETTER than the original, not just different
8. Flag the PATTERN, not just the instance
9. Advanced assessments reward ambition -- a daring partial success may outscore a safe full success
10. The Skip Test is ruthless but honest -- if YOU would skip, the listener will too
11. Album-context checks can surface issues invisible to craft-only scoring
12. Production-lyric alignment failures create unease the listener cannot name
13. Suno Optimization is NOT gate-blocking -- it does not prevent passing the 8.5 threshold, but determines render quality
14. Genre-Emotion Alignment is the highest-impact Suno choice -- wrong genre = the entire sound fights the lyrics
15. Key is the #1 emotional cue (Eerola, Friberg & Bresin, 2013) -- evaluate key choice with the same seriousness as lyric quality

---

## Output Format

Use the standardized report template: `references/CRITIQUE_REPORT_TEMPLATE.md`

The template defines exact structure, section ordering, conditional inclusion rules (when to include Album-Context, Revision Delta Table), and format guidelines. Follow it precisely.

---

## Theoretical Foundation

| Scholar/System | Contribution |
|---|---|
| **Allan F. Moore** (*Song Means*, 2012) | 4 functional texture layers, soundbox theory, persona analysis (real/performer/character) |
| **Philip Tagg** (*Music's Meanings*, 2013) | Musemes (smallest meaningful musical units), semiotic signification |
| **Serge Lacasse** | Vocal staging, proxemic distance (intimate to public). Part of a composite framework: Hall (proxemics theory) + Lacasse (vocal staging semiotics) + Moore (hermeneutics of recorded song). "Dissolved" is our extension. |
| **William Moylan** | Recording analysis, timbral balance, spatial imaging |
| **Pat Pattison** (Berklee) | Prosody as relationship between form and content |
| **Franco Fabbri** | Genre theory (5 rules of genre membership) |
| **Patrik Juslin** | BRECVEMA emotional mechanisms (8 pathways by which music induces emotion) |
| **Eerola, Friberg & Bresin** (2013, *Frontiers in Psychology* 4:487) | Emotional cue hierarchy (mode > tempo > register > dynamics > articulation > timbre) |
| **Christian Schubart** | Key characteristics and emotional associations |
| **Dodge et al.** (2025) | 6 universal criteria: innovation, beauty, scope of vision, technical prowess, generosity of spirit, authenticity |
| **Nashville A&R** | Melody memorability, "cut" potential, market fit, 7-second emotional truth, skip test |
| **Suno community research** (2025-2026) | Prompt formula, era anchoring, genre-first principle, 5-8 tag sweet spot, slider behavior |

---

## References

- `references/CRITIQUE_REFERENCE.md` -- Full scoring rubric tables with detailed scale definitions and all assessment frameworks
- `references/CRITIQUE_REPORT_TEMPLATE.md` -- Standardized output template for all critique reports
- `references/SUNO_STYLE_GENRE_REFERENCE.md` -- Genre/key/BPM/instrument evaluation tables for Suno Optimization Assessment
