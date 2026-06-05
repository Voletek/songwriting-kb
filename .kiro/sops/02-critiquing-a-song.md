# SOP 02: Critiquing a Song

> Step-by-step procedure for evaluating any song using the multi-layer critique model
> (Core 12-category craft rubric + 5 Advanced Assessments + Suno Optimization Assessment + Album-Context Module).
> Academic sources: Moore, Tagg, Lacasse, Moylan, Pattison, Fabbri, Juslin, Schubart, Dodge et al.
> Suno sources: Community-tested prompt science (2025-2026), era anchoring, genre-first principle.

---

## Prerequisites

- A complete song (lyrics + production notes, or at minimum lyrics + genre/tempo info)
- Access to the Critique Reference (`references/CRITIQUE_REFERENCE.md`) — this contains the full multi-layer scoring framework (Core 12 rubric definitions + Advanced 5 assessment scales + Suno Optimization methodology + Album-Context checks). Required for consistent scoring.
- Access to the Style & Genre Reference (`references/SUNO_STYLE_GENRE_REFERENCE.md`) — required for evaluating genre/key/BPM/instrument choices against emotional content and providing Style Prompt alternatives.
- If album track: access to the Album Bible for this track's intended role, emotion, and palette
- If the song has an existing self-score: note it but do NOT let it anchor your assessment. Self-critiques inflate by ~1.0 point on average.

---

## Procedure

### Step 1 — Read Completely (No Scoring Yet)

Read the entire song once without evaluating. Just absorb:
- What is this trying to be?
- What's the intended context (single, album track, concept piece)?
- What's the emotional thesis?

### Step 2 — Apply the 9-Step Analysis

Work through each quickly (1-2 sentences each). This is your internal scaffolding — it doesn't appear verbatim in the final report, but it informs the one-sentence justification per score in Step 3.

1. **Semantic** — What's it literally about?
2. **Emotional** — Central affect? What should I feel?
3. **Prosodic** — Count syllables on 3-4 lines. Any over 12? Stress alignment?
4. **Narrative** — What's the arc? Where's the turn?
5. **Voice** — Who's singing? Does the voice match the material?
6. **Genre** — What genre is this? Does it honor conventions?
7. **Arrangement** — What's the dynamic plan? Contrast present?
8. **Production** — Do the timbres signify correctly?
9. **Commercial** — Who's this for? Right length/platform?

### Step 3 — Score Each Category (1-10)

Score using the rubric definitions in `references/CRITIQUE_REFERENCE.md` — the 1-10 scale meanings there are required for consistent scoring. Do not guess at score boundaries. For each category, write ONE sentence justifying the score.

**⚠️ CONTEXT RULE:** Score relative to the song's INTENDED context. A concept album track is scored against concept album standards, not radio singles. A folk ballad is scored against folk conventions, not pop hooks. For album tracks, "Commercial" assesses whether the track serves its position in the album's emotional arc, not standalone chart potential.

| Category | Question to Answer |
|---|---|
| 1. Hook | Can I remember it after one read? Does it arrive within 15s of first vocal? |
| 2. Lyrics | Is it physical/sensory? Show-don't-tell? Specific? |
| 3. Prosody | Lines ≤12 syllables? Stresses on strong beats? Open vowels on holds? |
| 4. Arc | Does the song's INTERNAL arc move? Does V2 add new info? Does bridge TURN? |
| 5. Structure | Right length? Negative space? Contrast? |
| 6. Originality | Fresh angle? Or territory I've heard covered this way? |
| 7. Singability | Can I hum it? Consistent phrase rhythm? Melody-ready? |
| 8. Commercial | Right for its platform/context? Hook speed? Sync-ready? |
| 9. Genre | Fabbri's 5 rules satisfied? |
| 10. Arrangement | Dynamic range? Timbre choices signify? |
| 11. Voice/Accent | Accent coherent? Cultural ecosystem aligned? |
| 12. Emotional Intelligence | Authentic→Transcendent? Not exploitative? |

### Step 4 — Calculate Composite

Average all 12 scores. This is the composite.

### Step 5 — Suno Optimization Assessment

Evaluate whether the Style Prompt and tag choices are OPTIMAL for the song's emotional content. Use `references/SUNO_STYLE_GENRE_REFERENCE.md` as the evaluation reference.

**5a. 7-Point Dimensional Check:**

For each dimension, assess CORRECT / SUBOPTIMAL / WRONG:

| # | Dimension | Check Against |
|---|---|---|
| 1 | Genre | Fabbri's 5 rules — does this genre SIGNIFY what the lyrics express? |
| 2 | Key | Juslin's cue hierarchy — mode is #1 emotional cue. Does key character match dominant emotion? |
| 3 | BPM | Genre convention table + BPM-Emotion mapping. Correct for BOTH? |
| 4 | Instruments | Tagg musemes — does each instrument carry the correct cultural connotation? |
| 5 | Vocal style | Moore persona + Fabbri behavioral — delivery matches genre AND lyric arc? |
| 6 | Era/Production | Would era anchoring improve specificity? Is era separated from instrumentation? |
| 7 | Space/Mood | Atmospheric descriptors aligned, non-contradictory, ≤3 total? |

**5b. Section-Level Tag Check:**
- Does each section's production cue tag signify correctly for THAT section's content? (Tagg applied)
- Do tags contrast between adjacent sections?
- Are tags ≤3 per section?

**5c. Compliance Checklist:**
- Required elements present? (`[Title:]`, `[Production Direction:]`, `[Vocal Direction:]`, `[end]`)
- Character limits respected? (Style ≤1000, Lyrics ≤5000)
- Genre first in Style Prompt? Tag count 5-8? No contradictions?
- Named `()` layers declared? Exclusions in Exclude field?

**5d. Overall Verdict:**
- **OPTIMAL** — All dimensions correct. No changes needed.
- **COULD IMPROVE** — 1-3 dimensions suboptimal. Provide 2 alternative Style Prompts.
- **MISMATCHED** — 1+ dimensions wrong OR 4+ suboptimal. Revision strongly recommended.

**5e. Style Alternatives (if not OPTIMAL):**
Provide 2 complete alternative Style Prompts (ready to paste into Suno) with:
- Full rewritten prompt text
- Reasoning (why this serves the emotional content better)
- Expected improvement in render quality
- Slider recommendation (Weirdness % / Style Influence % / Audio Influence %)

### Step 6 — Identify Strongest Line

Find the ONE line you'd build the whole song around. Quote it. Explain in 1-2 sentences WHY it works (imagery? rhythm? meaning? surprise?).

### Step 7 — Flag ALL Issues

For each issue found (do not limit to a fixed number — report everything that needs fixing):
1. Name the problem (specific — not "could be better")
2. Quote the current line (for lyric issues) OR describe the specific moment/decision (for structural/production issues)
3. Explain WHY it's a problem (prosody? forced rhyme? abstract? redundant? predictable? static?)
4. Provide a fix:
   - **For lyric issues:** 2-3 alternative lines that solve it
   - **For structural issues:** describe the structural change (e.g., "extend bridge to 6 lines" or "add a 2-bar silence before final chorus")
   - **For production/arrangement issues:** describe the production fix (e.g., "introduce a counter-melody in V2" or "break the additive bloom with a subtractive moment")

**Rule:** Alternatives/fixes must SOLVE THE STATED PROBLEM while maintaining the song's thesis and voice — not just be different for difference's sake.

### Step 8 — Write Priority Recommendations

ALL identified issues, ordered by impact (biggest improvement first). Each recommendation should target a different LEVEL of the song where possible (one lyric-level, one structural/arrangement, one polish) — but if the song's problems cluster at one level, that's fine. Impact ordering takes precedence over category diversity.

1. The ONE change that would improve the song most
2. The second-highest-impact fix
3. The third-highest-impact fix

### Step 9 — Save the Report

Save the critique to `analysis/[song-filename]_critique.md`

Naming convention:
- Song: `songs/album_act2/08_First_Blood.md`
- Report: `analysis/08_First_Blood_critique.md`
- Song: `songs/experimental/The_Wound_Speaks.md`
- Report: `analysis/The_Wound_Speaks_critique.md`
- Song: `songs/keeper_of_the_light/01_The_Keepers_Morning.md`
- Report: `analysis/KOTL_01_The_Keepers_Morning_critique.md`

**Multi-album naming:** If your repo has multiple albums with potentially overlapping track numbers, prefix the filename with an album abbreviation (e.g., `FS_` for Fractured Shadows, `KOTL_` for Keeper of the Light).

**Re-critiques:** If critiquing a revised version (post-SOP 07 revision cycle), append `_v2` to the filename: `analysis/KOTL_01_The_Keepers_Morning_critique_v2.md`. Keep the original for comparison.

### Step 10 — Format Output

**Use the standardized report template for ALL critique outputs:**

#[[file:references/CRITIQUE_REPORT_TEMPLATE.md]]

The template defines the exact structure, section ordering, conditional inclusion rules (when to include Album-Context, Revision Delta Table, Summary), and format guidelines. Follow it precisely — it is the single source of truth for critique report formatting.

---

## Principles

- Be honest but constructive — identify what WORKS before what doesn't
- The strongest line matters more than the weakest line (build from strength)
- Prosody issues are FIXABLE — don't catastrophize them
- If emotional intelligence is high (9-10), the song has a soul — everything else is polish
- A 7.5/10 concept album track may be PERFECT for its role
- Self-critiques inflate by ~1.0 point — if you're self-critiquing, subtract 1

---

## Time Estimate

| Step | Time |
|---|---|
| Read completely | 2-3 min |
| 9-step analysis | 5-7 min |
| Score 12 categories | 10-15 min |
| Suno Optimization Assessment | 5-10 min |
| Strongest line + flags | 5-7 min |
| Recommendations + format | 5 min |
| **Total (standalone song)** | **35-45 min** |
| **Total (concept album track with production notes)** | **45-55 min** |
