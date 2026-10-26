---
inclusion: manual
description: Quick 12-category score of the song file you name (or the one under discussion). Invoke with /quick-score or #quick-score.
---

# Quick Score (manual command)

> Manual steering (`inclusion: manual`). Run it with `/quick-score` or `#quick-score`.
> It replaces the old user-triggered hook, since Kiro v1 has no manual hooks.
> Rubric definitions: `core/methodology/critique.md` (canonical). Read it if it is not already in context.

Quick-score the song file the user names (or the song currently under discussion):

1. Optional deterministic aids, if a shell is available:
   - `python3 tools/validate-song.py <file>`: character limits, required elements, V6 tag grammar.
   - `python3 tools/lyric-lint.py <file>`: syllables, rhyme types, scheme, section stability, clichés.
2. Score all 12 categories (1-10) from `core/methodology/critique.md`: Hook, Lyrics, Prosody, Arc,
   Structure, Originality, Singability, Commercial Viability, Genre Alignment, Arrangement/Production,
   Accent/Voice Coherence, Emotional Intelligence. Give one score and one sentence for each.
3. Calculate the core composite (average of 12) and state the decision gate:
   ≥8.5 optimize · 7.0-8.4 revise · <7.0 rethink.
4. Quote the strongest line.
5. Flag the single biggest issue with a concrete fix (2-3 alternative lines if it's a lyric issue).

Keep it concise. This is not the full critique report. For that, use the critic agent or
`.kiro/sops/02-critiquing-a-song.md`.
