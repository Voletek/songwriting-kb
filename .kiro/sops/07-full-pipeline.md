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
4. Re-check prosody (stress density and singability checked at tempo; `python3 tools/lyric-lint.py <file>`)
5. Re-check structure (hook signal within ~5-30 s of the first sung word, V2 new info, bridge turn)
6. Update Production Notes if changes affect key/chords/dynamics

**Output:** Revised draft (v2)
**Time:** 15-30 min

**Exit criteria:**
- [ ] All flagged issues addressed
- [ ] No new prosody violations introduced
- [ ] Hook signal timing still works
- [ ] Character count still within limits

**Optional:** Run through Critique again (Stage 2) for a revised score. Target: +0.5-1.0 improvement. Recommended for songs targeting ≥8.5 or when revisions were structural. Optional for polish-only fixes where the original score was already 8.0-8.4.

**Note:** Revision is defined here (not as a standalone SOP) because it always requires critique output as input. The critique report IS the revision brief.

---

### Stage 4: OPTIMIZE (SOP 03)

**Agent:** Suno-Optimizer
**Input:** Revised (or first draft if skipping revision)
**Process:** SOP 03 — the V6 Path by default (Style / Exclude / Lyrics split → V6 section, instrument, dynamic and vocal tags → `[End]` → char counts); the v5.5-era steps only for legacy renders
**Output:** Suno-ready version with all tags applied

**Note:** For songs written with SOP 01 (which includes Phase 4 Suno formatting), this stage functions primarily as VERIFICATION. Run all SOP 03 checks to confirm compliance and catch any formatting disrupted during revision (Stage 3). Expect minimal changes for well-formatted songs.

**Time:** 15-20 min

**Exit criteria:**
- [ ] Style ≤1000 chars
- [ ] Lyrics ≤5000 chars
- [ ] `[Title:]`, `[Production Direction:]`, `[Vocal Direction:]` present
- [ ] V6 section tags + `[Instrument: X In/Out]` choreography, 2-4 tags per section
- [ ] `[End]` at bottom (v5.5-era: `[end]`)
- [ ] No `[Tag Vocabulary]` block, no v5.5 global tags, no pipe notation (V6)
- [ ] No obsolete tags
- [ ] Exclude field content prepared (plain comma-separated, no dash prefix)
- [ ] (Optional) Slider recommendations — only if your Suno UI exposes sliders; v5.5-era starting points

---

### Stage 5: VERIFY

#### 5a — Deterministic checks (every song)

Run:
```bash
python3 tools/validate-song.py songs/<album_or_category>/<song>.md   # char counts, required elements, V6 tag checks, exclusions format
python3 tools/lyric-lint.py songs/<album_or_category>/<song>.md      # syllables, stress, rhyme type/scheme, section stability, clichés
```
Add `--strict` to make the validator fail on warnings. In Kiro IDE / CLI V3 the `song-validate` and `prosody-lint` hooks run these on agent-made saves; on Kiro Web, run them manually. FAIL → back to Stage 4 (format) or Stage 3 (prosody).

#### 5b — Continuity (album tracks only)

**Agent:** Album-Continuity
**Input:** Optimized song + Album Blueprint
**Authority:** All verification checks reference the Album Blueprint (`references/[ALBUM]_BLUEPRINT.md`, or `examples/albums/<album>/BLUEPRINT.md` for the bundled examples) as the single source of truth.
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
2. **Select Persona / Voice** (v5.5-era feature, legacy — use it if your Suno UI offers it): Choose the character's vocal model for album consistency
3. Paste Style Prompt into "Style of Music" field
4. Paste Exclusions into "Exclude" field
5. Paste Lyrics (V6: from `[Title:]` through `[End]`; v5.5-era: from `[track:]` through `[end]`) into "Lyrics" field
6. (Optional) Set creative sliders — only if your Suno UI exposes them; recommendations are v5.5-era starting points
7. Generate 3-4 versions
8. Evaluate renders against the Production Notes vision
9. Select best render OR identify what to adjust and re-render; log V6 tag behaviour in the `references/V6_TAG_DISCOVERY.md` results log
10. **Extract Stems** (v5.5-era feature, legacy — if available in your Suno UI): Get stems from the best render for DAW mixing/mastering

**Album consistency tip:** For concept albums, extract stems (where your Suno plan/UI offers them) from all tracks and do final mixing/mastering in a DAW. This lets you level-match, apply consistent reverb, and ensure the album sounds cohesive even if individual Suno renders have different production characteristics.

---

## Pipeline Summary

| Stage | Agent | Time | Decision |
|---|---|---|---|
| 1. Write | Songwriter | 50-75 min | Always proceed |
| 2. Critique | Critic | 30-35 min | Score determines next step |
| 3. Revise | Songwriter | 15-30 min | Skip if ≥8.5 |
| 4. Optimize | Suno-Optimizer | 15-20 min | Always proceed |
| 5. Verify | Validators (5a) + Album-Continuity (5b) | 2 min + 10-15 min | 5a always; 5b only for album tracks |
| 6. Render | Human | 10-20 min | Always proceed |
| **TOTAL** | | **2-3 hours** | Per song |

---

## When to Skip Stages

| Scenario | Skip |
|---|---|
| Standalone song (not album) | Skip Stage 5b (still run 5a) |
| Score ≥8.5 on first critique | Skip Stage 3 |
| Song is experimental/non-Suno | Skip Stage 4 |
| Quick draft / idea capture | Stop after Stage 1 |
| Just need feedback | Stop after Stage 2 |
| Song already Suno-formatted from SOP 01 | Stage 4 is verification only (still run, expect minimal changes) |
| Album track but non-Suno | Skip Stage 4, keep Stage 5b (lyric-lint from 5a still useful) |
