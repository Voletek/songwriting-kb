---
inclusion: manual
description: Runs the full song pipeline (Write → Critique → Revise → Optimize → Verify → Render plan) on the song you name. Invoke with /full-pipeline or #full-pipeline.
---

# Full Pipeline (manual command)

> Manual steering (`inclusion: manual`). Run it with `/full-pipeline` or `#full-pipeline`.
> It replaces the old user-triggered hook, since Kiro v1 has no manual hooks.
> Full procedure: `.kiro/sops/07-full-pipeline.md`. Read it if it is not already in context.

Run SOP 07 on the song the user names (or the song under discussion). If no song exists yet, start
with Stage 1 (write) using `core/methodology/songwriting.md`, or the song-planner brief if one exists.

1. **Critique.** Score the 12 categories from `core/methodology/critique.md` and compute the core composite.
2. **Decision gate:**
   - **≥ 8.5:** go straight to optimization.
   - **7.0-8.4:** list every issue by impact with fixes, revise (ask first unless the user said
     auto-pilot), then re-critique (Layer 1 + 2.5 + delta).
   - **< 7.0:** explain what isn't working and propose a new approach before rewriting.
3. **Optimize.** Follow the V6 Procedure in `core/methodology/suno-optimization.md` (the v5.5-era
   steps only for v5.5 renders).
4. **Verify.** If a shell is available, run `python3 tools/validate-song.py <file>` and
   `python3 tools/lyric-lint.py <file>`. Fix every FAIL and review every WARN. For album tracks,
   also run the album-continuity checks.
5. **Render plan.** Paste Style / Exclude / Lyrics into Suno, generate 3-4 takes, keep the best,
   and log tag behaviour in the `references/V6_TAG_DISCOVERY.md` results log.

Report the composite, the strongest line, the gate decision, the final character counts
(Style X/1000 · Lyrics X/5000), and the next action.
