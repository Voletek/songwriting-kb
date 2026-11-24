# SOP 07: Full Pipeline (Write → Critique → Revise → Optimize → Verify)

> The complete end-to-end workflow for producing a finished, Suno-ready,
> quality-checked, continuity-verified song.

---

## Overview

```
WRITE → CRITIQUE → REVISE → OPTIMIZE → VERIFY → RENDER → FINISH
  ↑                                          |
  └──────── (if fails verification) ─────────┘
```

---

## Procedure

> **Starting from a song already on Suno?** Pull it into a song file first with SOP 11, then join at Stage 2 (critique) or Stage 4 (optimize).

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

**Output:** Revised draft saved as a NEW file (`<Title>_v2.md`, `_v3`, ...) next to the original. Never overwrite a version that has been critiqued or rendered: its critique and `## RENDERS` log refer to it. The highest version is canonical (`songs/README.md`).
**Time:** 15-30 min

**Exit criteria:**
- [ ] All flagged issues addressed
- [ ] No new prosody violations introduced
- [ ] Hook signal timing still works
- [ ] Character count still within limits

**Re-critique** (Stage 2, Layer 1 + 2.5 + delta) is **required** after structural revisions (sections cut, added or reordered) and optional for polish-only fixes where the original score was already 8.0-8.4. It is also recommended for songs targeting ≥8.5. Target: +0.5-1.0 improvement.

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
- [ ] (Optional) Slider recommendations — UI or Suno MCP `controls`; v5.5-era starting points to re-validate

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

### Stage 6: RENDER (SOP 10)

**Agent:** Renderer (through the Suno MCP), or a human in the suno.com UI
**Input:** Verified song file
**Process:** SOP 10 (`.kiro/sops/10-rendering-through-the-suno-mcp.md`):
1. Pre-flight: `validate-song.py --strict`, `lyric-lint.py`, `estimate-runtime.py`; check credits; **ask which saved voice to use** and confirm cost and settings (model, sliders) with the user; record them under `## RENDER SETTINGS`
2. Render: `python3 tools/suno-fields.py <file>` → `audio-create` (2 takes per call) → `audio-wait`. By hand: paste the same three fields into Custom Mode
3. Verify: `audio-analysis` (BPM, meter, key, sections) and `audio-listen` (tag-specific questions) against the Production Notes
4. Log: one row per take in the song file's `## RENDERS` section; tag results in the `references/V6_TAG_DISCOVERY.md` results log
5. Decide: keeper, section edit, extension, cover, more takes, or back to Stage 3

**Output:** Takes logged in `## RENDERS`, a keeper (or a decision on what to change)
**Time:** 10-20 min (plus Suno generation time)

**Exit criteria:**
- [ ] Every take logged with its measurements
- [ ] Planned elements marked landed / partial / missed
- [ ] Keeper chosen by the user, or the next change decided

---

### Stage 7: FINISH (SOP 10, Steps 6-7)

**Agent:** Renderer, then the user in Suno Studio or a DAW
**Process:**
1. Fix missed sections without a full re-render: section edit (`audio-create` with `reference_audio_ids`), extension + `audio-full-song`, or cover
2. Stems (`audio-stems-create`, 10 or 50 credits, ask first) → apply the stem-matched plugins in `plugins/` in Suno Studio, or mix in a DAW. Pitch-shifting one section is a DAW job
3. Optional MIDI (`audio-midi`, 10 credits) and download (`audio-download`; ask before spending a download credit)
4. Optional release checklist (SOP 10 Step 7): caption, word timings, shorter edit, solo/duet versions, publish only on request

**Album consistency tip:** For concept albums, take stems from every track's keeper and do final mixing/mastering in one place (Suno Studio or a DAW). That lets you level-match, apply consistent reverb and the same plugin chain, and keep the album cohesive even when individual renders differ.

---

## Pipeline Summary

| Stage | Agent | Time | Decision |
|---|---|---|---|
| 1. Write | Songwriter | 50-75 min | Always proceed |
| 2. Critique | Critic | 30-35 min | Score determines next step |
| 3. Revise | Songwriter | 15-30 min | Skip if ≥8.5 |
| 4. Optimize | Suno-Optimizer | 15-20 min | Always proceed |
| 5. Verify | Validators (5a) + Album-Continuity (5b) | 2 min + 10-15 min | 5a always; 5b only for album tracks |
| 6. Render | Renderer (or human) | 10-20 min | Always proceed |
| 7. Finish | Renderer + user (Studio/DAW) | varies | Optional |
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
