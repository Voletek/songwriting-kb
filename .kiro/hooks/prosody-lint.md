---
title: Prosody Lint
description: Flags lyric lines exceeding 12 syllables and detects common prosody issues on song file save
event: file_save
path: songs/**/*.md
---

# Prosody Lint

When a song file is saved, scan all lyric lines for prosody issues.

## Rules to Check

### 1. Syllable Count (Primary Check)
Flag any LYRIC line (not tags, not direction blocks) that exceeds 12 syllables.

**How to identify lyric lines:**
- Lines that are NOT inside `[brackets]`
- Lines that are NOT in the Production Notes section
- Lines that are NOT in the Style Prompt section
- Lines between section tags that contain actual words to be sung/spoken

**Threshold:** 12 syllables maximum per line at typical BPM (68-112). At tempos above 112 BPM, consider flagging at 10 syllables — faster tempos require shorter phrases.

**Output for violations:**
```
⚠️ PROSODY [Section]: "line text here" — XX syllables (max 12)
   Suggestion: Split or trim to fit melodic phrase
```

### 2. Stuffed Phrases (Secondary Check)
Flag lines with more than 3 multi-syllable words (3+ syllables each) crammed together:
```
⚠️ DENSE: "line text" — Multiple long words may fight melody
```

### 3. Weak Terminal Words
Flag lines ending on weak/unstressed function words (the, a, an, of, to, in, for, it, is, was):
```
⚠️ WEAK END: "line ending in 'of'" — Consider restructuring for strong terminal stress
```

### 4. Enjambment Warning
Flag cases where a sentence clearly spans across two lines without an em-dash or natural break:
```
⚠️ ENJAMBMENT: Lines X-Y may run together when sung — add em-dash or restructure
```

## What NOT to Flag

- Direction blocks (they're instructions, not lyrics)
- Production tags in brackets
- Spoken/whispered sections (tagged as `[Spoken]` or `[Whispered]`) — these have looser prosody rules
- Lines explicitly tagged as `[narrator]` or `[spoken word]`
- Lines in parentheses — these are backup vocals, delivery cues, or named layers (e.g., `(whispered) text`, `(robotic layer: text)`, `(response text)`) — often shorter fragments with looser prosody rules
- Named layer declarations (e.g., `(robotic layer: Prime Directive initializing)`) — these are spoken/processed, not melodic

## Summary Output

```
PROSODY LINT: X issues found in [Song Title]
- X lines over 12 syllables
- X dense phrases
- X weak terminal words
```
