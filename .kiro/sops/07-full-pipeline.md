# SOP 07: Full Pipeline (Write → Critique → Revise → Optimize → Verify)

> The complete end-to-end workflow for producing a finished, Suno-ready,
> quality-checked, continuity-verified song.

---

## Overview

```
WRITE → CRITIQUE → REVISE → OPTIMIZE → VERIFY → RENDER
  ↑                                          |
  └──────── (if fails verification) ─────────┘
```

---

## Procedure

### Stage 1: WRITE (SOP 01)

**Agent:** Songwriter
**Input:** Concept/prompt + album context (if applicable)
**Process:** Full SOP 01 (analysis → writing → quality check → formatting)
**Output:** Complete first draft (lyrics + style + production notes + Suno formatting)
**Time:** 50-75 min

**Exit criteria:**
- [ ] Song thesis stated
- [ ] All sections written
- [ ] Production notes complete
- [ ] Suno format applied (full formatting from SOP 01 Phase 4)

---

### Stage 2: CRITIQUE (SOP 02)

**Agent:** Critic
**Input:** The completed first draft
**Process:** Full SOP 02 (9-step analysis → 12-category scoring → flags → recommendations)
**Output:** Critique report with scores, strongest line, flagged issues, priorities

**Time:** 30-35 min

**Exit criteria:**
- [ ] All 12 categories scored
- [ ] Composite score calculated
- [ ] All issues flagged with alternatives
- [ ] Priority recommendations given (all issues, ordered by impact)
- [ ] Report formatted per `references/CRITIQUE_REPORT_TEMPLATE.md`
- [ ] Report saved to `analysis/[song-filename]_critique.md`

**Decision gate:**
- If composite ≥8.5: Proceed to Stage 4 (Optimize) — skip revision
- If composite 7.0-8.4: Proceed to Stage 3 (Revise)
- If composite <7.0: Return to Stage 1 with new approach (concept may need rethinking)

**⚠️ Score source:** The decision gate uses the SOP 02 CRITIQUE composite score. Self-scores from SOP 01 (which use a different rubric) are for the writer's reference only — they do not drive pipeline decisions.

---

### Stage 3: REVISE

**Agent:** Songwriter (with critique in hand)
**Input:** Original draft + critique report
**Process:**
1. Address Priority 1 recommendation first (highest impact)
2. Fix all flagged issues using provided alternatives (or write better ones)
3. Address Priority 2 and 3
4. Re-check prosody (every line ≤12 syllables)
5. Re-check structure (hook timing, V2 new info, bridge turn)
6. Update Production Notes if changes affect key/chords/dynamics

**Output:** Revised draft (v2)
**Time:** 15-30 min

**Exit criteria:**
- [ ] All flagged issues addressed
- [ ] No new prosody violations introduced
- [ ] Hook timing still works
- [ ] Character count still within limits

**Optional:** Run through Critique again (Stage 2) for a revised score. Target: +0.5-1.0 improvement. Recommended for songs targeting ≥8.5 or when revisions were structural. Optional for polish-only fixes where the original score was already 8.0-8.4.

**Note:** Revision is defined here (not as a standalone SOP) because it always requires critique output as input. The critique report IS the revision brief.

---

### Stage 4: OPTIMIZE (SOP 03)

**Agent:** Suno-Optimizer
**Input:** Revised (or first draft if skipping revision)
**Process:** Full SOP 03 (char count → global tags → validation → delivery tags → dynamics → termination)
**Output:** Suno-ready version with all meta-tags applied

**Note:** For songs written with SOP 01 (which includes Phase 4 Suno formatting), this stage functions primarily as VERIFICATION. Run all SOP 03 checks to confirm compliance and catch any formatting disrupted during revision (Stage 3). Expect minimal changes for well-formatted songs.

**Time:** 15-20 min

**Exit criteria:**
- [ ] Style ≤1000 chars
- [ ] Lyrics ≤5000 chars
- [ ] Global control tags present ([track], [control], [sequence])
- [ ] [end] at bottom
- [ ] All pipe params validated (adjectives only)
- [ ] No obsolete tags
- [ ] Slider recommendations documented
- [ ] Exclude field content prepared

---

### Stage 5: VERIFY (Album tracks only)

**Agent:** Album-Continuity
**Input:** Optimized song + Album Bible
**Authority:** All verification checks reference the Album Bible (`references/[ALBUM]_BIBLE.md`) as the single source of truth.
**Process:**
1. Run all hard rules against the track
2. Check sonic palette compliance
3. Verify motif usage (correct? evolved?)
4. Check character voice (matches registry? different from adjacent?)
5. Verify key relationship (makes sense in harmonic map?)
6. Check callbacks (accurate references?)
7. Confirm emotional arc position

**Output:** Continuity report (PASS/FAIL with details)
**Time:** 10-15 min

**Exit criteria:**
- [ ] All rules pass
- [ ] Palette compliant
- [ ] Motifs correct
- [ ] Voice differentiated
- [ ] Key fits map
- [ ] Arc position correct

**If FAIL:** Return to Stage 3 (Revise) with continuity notes. Fix violation. Re-optimize (Stage 4). Re-verify.

**⚠️ Conflict resolution:** If continuity rules conflict with critique recommendations (e.g., critique says "add harmony vocals" but album rule forbids harmony before Track 7): continuity rules always win. Achieve the critique's INTENT through rule-compliant means. Document the conflict and resolution.

---

### Stage 6: RENDER

**Human action** (not agent):
1. Open Suno (Custom Mode)
2. **Select Persona** (if using v5.5 Voices): Choose the character's vocal model for album consistency
3. Paste Style Prompt into "Style of Music" field
4. Paste Exclusions into "Exclude" field
5. Paste Lyrics (from `[track:]` through `[end]`) into "Lyrics" field
6. Set Creative Sliders per recommendations
7. Generate 3-4 versions
8. Evaluate renders against the Production Notes vision
9. Select best render OR identify what to adjust and re-render
10. **Extract Stems** (if using v5.5): Get 12-track stems from best render for DAW mixing/mastering

**Album consistency tip:** For concept albums, extract stems from all tracks and do final mixing/mastering in a DAW. This lets you level-match, apply consistent reverb, and ensure the album sounds cohesive even if individual Suno renders have different production characteristics.

---

## Pipeline Summary

| Stage | Agent | Time | Decision |
|---|---|---|---|
| 1. Write | Songwriter | 50-75 min | Always proceed |
| 2. Critique | Critic | 30-35 min | Score determines next step |
| 3. Revise | Songwriter | 15-30 min | Skip if ≥8.5 |
| 4. Optimize | Suno-Optimizer | 15-20 min | Always proceed |
| 5. Verify | Album-Continuity | 10-15 min | Only for album tracks |
| 6. Render | Human | 10-20 min | Always proceed |
| **TOTAL** | | **2-3 hours** | Per song |

---

## When to Skip Stages

| Scenario | Skip |
|---|---|
| Standalone song (not album) | Skip Stage 5 |
| Score ≥8.5 on first critique | Skip Stage 3 |
| Song is experimental/non-Suno | Skip Stage 4 |
| Quick draft / idea capture | Stop after Stage 1 |
| Just need feedback | Stop after Stage 2 |
| Song already Suno-formatted from SOP 01 | Stage 4 is verification only (still run, expect minimal changes) |
| Album track but non-Suno | Skip Stage 4, keep Stage 5 |
