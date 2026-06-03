---
title: Suno Character Count Check
description: Checks Style Prompt ≤1000 chars and Lyrics field ≤5000 chars on song file save, flags overflows with specific counts
event: file_save
path: songs/**/*.md
---

# Suno Character Count Validation

When a song file in `songs/` is saved, check character counts against Suno's limits.

## Limits

| Field | Limit | What Counts |
|---|---|---|
| Style Prompt | 1000 chars | Everything from "STYLE PROMPT:" to `[Exclusions:]` (inclusive) |
| Lyrics | 5000 chars | Everything from `[Title:]` through `[end]` or last lyric line, including all section tags, direction blocks, and production cue tags |

## Measurement Rules

- Count the **Style Prompt** section: from the line after "STYLE PROMPT:" through the `[Exclusions: ...]` line
- Count the **Lyrics** section: from `[Title: ...]` through the final lyric/tag (before Production Notes)
- Direction blocks (`[Production Direction: ...]`, `[Vocal Direction: ...]`) count toward lyrics
- Section tags (`[Verse 1]`, `[Chorus]`, etc.) count toward lyrics
- Production cue tags (`[Sparse piano]`, `[Heavy drums]`) count toward lyrics

## Output

If OVER limit:
```
🚨 STYLE PROMPT: XXX/1000 chars (OVER by XX) — Move negatives to Exclude field
🚨 LYRICS: XXXX/5000 chars (OVER by XXX) — Trim direction blocks or reduce section tags
```

If UNDER limit:
```
✅ Style: XXX/1000 chars | Lyrics: XXXX/5000 chars — Within Suno limits
```

If CLOSE (within 10%):
```
⚠️ Style: XXX/1000 chars (XX remaining) — Consider trimming if adding more
⚠️ Lyrics: XXXX/5000 chars (XXX remaining) — Tight budget
```
