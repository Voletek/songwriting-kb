---
title: Album Continuity Check
description: Verifies album continuity rules when song files in the album directories are saved — checks sonic palette, key relationships, and forbidden elements
event: file_save
path: songs/album_*/**/*.md
---

# Album Continuity Check

When any song in `songs/album_*/` directories is saved, verify it doesn't violate the 11 continuity rules.

## Checks to Run (5 Critical Rules — Automated)

> Note: This hook checks 5 of the 11 hard rules that are automatable via text scanning. For full 11-rule verification, invoke the album-continuity agent.

### 1. Sonic Palette Violation
Based on the track number (extracted from filename `XX_Title.md`):

| Track # | FORBIDDEN Elements |
|---|---|
| 08-17 | industrial, electronic percussion, cold synths, glitch effects, digital, cyber |
| 08 | (exception: "industrial undertones fading" is allowed as transition) |
| 09-17 | NO electronic/industrial at all |

**Check:** Scan Style Prompt, Production Direction, and instrument tags for forbidden terms.

```
🚨 CONTINUITY: Track XX contains "industrial synths" — forbidden after Track 8
```

### 2. Major Key Violation
Only Track 16 may use a major key. Track 17's final chorus may shift to C major.

**Check:** If the Production Notes key field contains "major" and track number is NOT 16 or 17:
```
🚨 CONTINUITY: Track XX uses major key — only T16 (D major) and T17 final chorus (C major) allowed
```

### 3. Key Change Violation
Only Track 17 may have a key change.

**Check:** If Style Prompt or Production Notes mention "key change" or "modulation" or "shifting" and track number is NOT 17:
```
🚨 CONTINUITY: Track XX contains key change — only T17 has the album's key change (Am→C)
```

### 4. AI/Electronic Voice After Track 7
The AI character (Prime Directive, robotic layer, digital voice) must NOT appear in Act 2.

**Check:** Scan for "robotic", "AI voice", "digital", "Prime Directive", "(robotic layer:" in tracks 8-17:
```
🚨 CONTINUITY: Track XX contains AI/robotic voice elements — AI stays in Act 1 only
```

### 5. Album Title Phrase Protection
"The fracture made the shadows" or "shadows made the dawn" must ONLY appear in Track 17.

**Check:** Scan lyrics for these phrases in any track except 17:
```
🚨 CONTINUITY: Album title phrase found in Track XX — reserved for T17 final chorus ONLY
```

## Pass Output

```
✅ CONTINUITY: Track XX passes all 5 checks — no violations detected
```

## Notes

- These checks are HARD rules — any violation should be addressed before committing
- For full continuity review (motifs, character voices, callbacks), invoke the concept-album-bible skill
