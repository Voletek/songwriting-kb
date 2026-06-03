# SOP 03: Optimizing a Song for Suno

> Step-by-step procedure for taking a finished song and preparing it for Suno rendering.
> This does NOT change creative content — it adds technical formatting only.

---

## Prerequisites

- A complete song (lyrics + style concept + production notes)
- Song has been through critique/revision (don't optimize a first draft)
- Know your target Suno model version (v4.5 or v5.0)

---

## Procedure

### Step 1 — Character Count Audit

**Measure Style Prompt:**
- Copy everything from your genre/BPM/mood description
- Count characters (use any text tool)
- Must be ≤1000 characters
- If over: move negatives/exclusions to Exclude field first, then trim least essential descriptors

**Measure Lyrics Field:**
- Count from `[Title:]` through `[end]` (including ALL tags, direction blocks, section tags)
- Must be ≤5000 characters
- If over: trim direction blocks (keep essential intent), reduce section production tags, shorten outro

**Record counts:**
```
Style: ___/1000 chars
Lyrics: ___/5000 chars
```

### Step 2 — Add Global Control Tags

If missing, add these at the TOP of Lyrics field (before `[Title:]`):

```
[track: genre: [your genre], mood: [your mood], length: [seconds]]
[control: no-repeat, dynamic transitions]
[sequence: [list all sections in order]]
```

**Length calculation:** Target minutes × 60 = seconds (e.g., 4:30 = 270)

**Sequence:** List EVERY section tag that appears, in order:
```
[sequence: intro, verse, pre-chorus, chorus, verse, pre-chorus, chorus, bridge, final chorus, outro]
```

### Step 3 — Validate [control] Parameters

Only these values are confirmed valid:
- `no-repeat` ✅
- `dynamic transitions` ✅
- `instrumental` ✅

**Invalid** (remove if present): `build across sections`, custom phrases, unconfirmed terms.

### Step 4 — Optimize Section Tags

**Check stacked tags:** If any section has >3 production tags stacked:
```
❌ Too many:
[Heavy drums]
[Distorted bass]
[Staccato guitar]
[Cave reverb]
[Choir pad]

✅ Convert to pipe notation:
[chorus | powerful, wide, heavy drums, distorted bass]
[Staccato guitar] [Cave reverb]
```

**Validate pipe parameters:**
- ✅ Valid: adjectives/descriptors (powerful, intimate, wide, dark, stripped, rising)
- ✅ Valid: vocal delivery (vulnerable vocals, close-mic, whispered, spoken)
- ❌ Invalid: instrument instructions ("cello enters low", "drums enter soft")
- ❌ Invalid: custom phrases ("maximum width", "build across sections")

**Move invalid pipe params** to Production Direction block or standalone tags.

### Step 5 — Add Vocal Delivery Tags

Scan each section. Where appropriate, add:

| If the section is... | Add this tag |
|---|---|
| Confessional/grief/intimate | `[vulnerable vocals]` in pipe or standalone |
| Lead vocal whispered | `[whisper]` before the line |
| Background whisper atmosphere | `[whispering]` as texture tag |
| Spoken/non-sung | `[spoken word]` or `[narrator]` |
| Repeated hook/mantra | `[chant]` |
| Dialogue/call-response | `[call-and-response]` |

### Step 6 — Add Dynamics Tags

At key moments, add explicit tags:

| Moment | Tag |
|---|---|
| Pre-chorus building | `[build]` (or in pipe: `[pre-chorus \| build, rising tension]`) |
| Dramatic silence | `[silence: sudden]` |
| Key change | `[modulation: ascending]` or `[modulation: sudden]` |
| Volume increasing | `[crescendo]` |
| Volume decreasing | `[diminuendo]` |
| Rhythm change | `[beat-switch: half-time]` |
| Grand ending | `[big finish]` |
| Held note | `[fermata]` |

### Step 7 — Add Termination

At the very bottom of lyrics, add:
```
[end]
```

If the song should fade rather than cut:
```
[fade: layered]
[end]
```

### Step 8 — Check for Obsolete Tags

Scan for and REMOVE any of these:
- `[bpm: X]` → put BPM in Style Prompt text
- `[key: X]` → put key in Style Prompt text
- `[loop]` → remove entirely (unsupported)
- `[autotune]` → remove (deprecated)
- `[mix]` / `[master]` → remove (ineffective)
- `[volume]` → use dynamics tags instead
- `[filter]` → describe in Production Direction
- `[section: X]` → use specific section names

### Step 9 — Verify Suno Compatibility

Final checklist:
- [ ] No end punctuation on lyric lines (no periods, commas, semicolons)
- [ ] Each line = one melodic phrase
- [ ] 4-8 lines per section maximum
- [ ] No lyrics on same line as tags
- [ ] Tags on their own line
- [ ] `[Title:]` is present and matches song name
- [ ] Production Direction block present
- [ ] Vocal Direction block present

### Step 10 — Set Creative Sliders

Recommend slider values based on song type:

| Song Type | Weirdness | Style Influence | Audio (if Inspo) |
|---|---|---|---|
| Radio pop/rock | 35-45% | 55-65% | 40-50% |
| Concept album | 50-55% | 50-60% | 45% |
| Dark cinematic | 50-60% | 55-65% | 45-55% |
| Intimate ballad | 45-55% | 50-60% | 40-50% |
| Epic orchestral | 50-55% | 60-70% | 45-55% |
| Experimental | 60-75% | 40-50% | 30-40% |

### Step 11 — Prepare Exclude Field Content

Format exclusions for the dedicated Exclude field:
```
‑trap drums, ‑beatboxing, ‑vocal hums, ‑[genre-specific exclusions]
```

**Note:** This goes in the EXCLUDE field in Suno's UI — NOT in Style Prompt or Lyrics.

### Step 12 — Final Output

Document the optimized version with:
```
## SUNO-OPTIMIZED VERSION

### Changes Made:
- [list of specific additions/changes]

### Character Counts:
- Style: XXX/1000
- Lyrics: XXXX/5000

### Slider Recommendations:
- Weirdness: XX%
- Style: XX%
- Audio: XX% (if applicable)

### Exclude Field:
[content for Exclude]

### [Full optimized song]
```

---

## Common Suno Problems This Prevents

| Problem | This SOP Prevents It By |
|---|---|
| Song runs too long | Step 2: `[length: XXX]` |
| Sections out of order | Step 2: `[sequence: ...]` |
| Lines get auto-repeated | Step 2: `[control: no-repeat]` |
| Song won't end | Step 7: `[end]` tag |
| No dynamic contrast | Step 6: dynamics tags |
| Genre drift | Step 2: `[track: genre: X]` |
| Bridge gets sung not spoken | Step 5: `[spoken word]` tag |
| Over character limit | Step 1: audit FIRST |

---

## Time Estimate: 15-20 minutes per song
