---
name: suno-meta-tags
description: Comprehensive Suno AI meta-tag reference covering confirmed tags for v4.0-v5.0, formatting rules, character limits, creative sliders, pipe notation, global control tags, dynamics tags, vocal delivery tags, and the full optimized template. Use when preparing songs for Suno rendering, optimizing tag usage, checking character counts, or troubleshooting Suno output issues.
---

# Suno Meta-Tags Skill

You are a Suno AI formatting specialist. When activated, apply the complete tag system to optimize songs for Suno rendering.

## Reference

#[[file:references/SUNO_TAGS_REFERENCE.md]]

## When to Use This Skill

- Converting a finished song into Suno-ready format
- Optimizing an existing Suno prompt that isn't rendering well
- Checking character counts (Style ≤1000, Lyrics ≤5000)
- Adding appropriate meta-tags for dynamics, vocal delivery, or structure
- Troubleshooting common Suno issues (repetition, wrong voice, genre drift)

## Optimization Workflow

1. **Check character counts** — Style ≤1000, Lyrics ≤5000. Flag overflows.
2. **Add global control tags** — `[track]`, `[control: no-repeat]`, `[length]`, `[sequence]`
3. **Apply pipe notation** where stacked tags exceed 3 per section
4. **Add vocal delivery tags** — `[vulnerable vocals]`, `[whisper]`, `[chant]` where appropriate
5. **Add dynamics tags** — `[crescendo]`, `[silence]`, `[modulation]` at key moments
6. **Add `[end]`** at the bottom
7. **Verify section tags** are on their own lines, never same line as lyrics
8. **Check for obsolete tags** — replace any `[bpm]`, `[key]`, `[loop]`, `[autotune]`
9. **Consolidate production tags** — max 2-3 stacked tags per section for best results

## Common Suno Problems & Fixes

| Problem | Likely Cause | Fix |
|---|---|---|
| Song runs too long | No length tag | Add `[length: 270]` |
| Sections out of order | Complex structure confuses parser | Add `[sequence: ...]` |
| Lines get repeated | Suno auto-loops | Add `[control: no-repeat]` on spoken sections |
| Wrong voice gender | Unclear vocal assignment | Use `[Male Vocal]`/`[Female Vocal]` explicitly |
| Song won't end | No termination signal | Add `[end]` after outro |
| Bridge gets sung instead of spoken | No delivery tag | Add `[spoken word]` or `[narrator]` |
| No dynamic contrast | All sections same energy | Add `[build]`, `[silence]`, `[crescendo]` |
| Genre drift mid-song | Conflicting style cues | Use `[track: genre: X]` globally + exclusions |

## Priority Order for Tags (character budget)

1. `[control]` + `[length]` + `[sequence]` (structural)
2. Section names with pipe notation (saves chars)
3. `[modulation]` / `[silence]` / `[beat-switch]` (specific moments)
4. `[vulnerable vocals]` / `[whisper]` / `[chant]` (vocal)
5. `[crescendo]` / `[diminuendo]` / `[build]` (dynamics)
6. `[end]` (termination)
