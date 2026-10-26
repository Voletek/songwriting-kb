# SOP 03: Optimizing a Song for Suno

> Step-by-step procedure for taking a finished song and preparing it for Suno rendering.
> This does NOT change creative content -- it adds technical formatting only.

> **Note:** The canonical methodology for this workflow now lives in `core/methodology/suno-optimization.md`.
> This SOP is retained for Kiro-specific step formatting but the methodology file is the authoritative source.
> If content diverges, `core/methodology/` wins.

---

## ⚡ V6 Paradigm Callout (read first)

Suno V6 (v6 / v6-wild / v6-mini) is the current default and uses a DIFFERENT tag paradigm than the v5.5-era mechanics the numbered steps below were written for:

- **Style field = the WHAT:** genre, key, tempo, vocal identity, production aesthetic (sets the world)
- **Lyrics field = the HOW:** section tags + `[Instrument: X In/Out]` + dynamics + delivery + transitions (choreographs the performance)
- `[Instrument: X In]` / `[Instrument: X Out]` are the V6 arrangement controls for instrument entrances/exits — use them (working model, Sept 2026, user-confirmed; log render evidence in the `references/V6_TAG_DISCOVERY.md` results log)
- Do NOT include a `[Tag Vocabulary]` block in final output (planning aid only — not sung)
- The 12 numbered steps below are the **v5.5-era procedure (legacy)** — a Kiro-formatted version of the v5.5-era 13-step procedure (Steps 1–13 + 9b) in `core/methodology/suno-optimization.md`. Where they conflict with V6 (global tags, pipe notation, slider presets, tag-count limits, `[silence: sudden]`, obsolete-tag assumptions), re-validate against V6 before applying.
- Master tag list: `references/V6_TAG_REFERENCE.md` · How/why & division of labor: `references/V6_TAG_DISCOVERY.md`

---

## V6 Path (default)

Full procedure: `core/methodology/suno-optimization.md` → **V6 Procedure (default)**. Short version:

1. Split the song into **Style / Exclude / Lyrics** fields.
2. **Style = the WHAT:** genre first, key, tempo, vocal identity, production aesthetic; ≤1000 chars; no artist names; sound descriptors, not gear model names.
3. **Exclude:** negatives only, plain comma-separated text, no dash prefix (e.g. `trap drums, beatboxing, vocal hums, bright synths`); written under `## EXCLUSIONS:` in the song file.
4. **Lyrics = the HOW:** `[Title:]`, `[Production Direction:]`, `[Vocal Direction:]`, section tags, `[Instrument: X In/Out]` choreography, `[Dynamic:]` / `[Vocal:]` / `[Transition:]` / `[Key Change:]` tags, 2-4 tags per section; no pipe notation, no v5.5 global tags, no `[Tag Vocabulary]` block; end with `[End]`; ≤5000 chars.
5. Run `python3 tools/validate-song.py <file>` and `python3 tools/lyric-lint.py <file>`.
6. Render 3-4 takes, keep the best, and log results in the `references/V6_TAG_DISCOVERY.md` results log.

---

## Prerequisites

- A complete song (lyrics + style concept + production notes)
- Song has been through critique/revision (don't optimize a first draft)
- Know your target Suno model version (V6 is the current default — use the V6 Path above; v5.5 and earlier for legacy renders — use the procedure below)
- Access to `references/SUNO_TAGS_REFERENCE.md` for tag validation

**Note:** If the song was written with SOP 01 (which includes Phase 4 formatting), this SOP functions as a VERIFICATION pass. Run all steps to confirm compliance — document "no changes needed" or list corrections made.

---

## Procedure — v5.5-era (legacy — re-validate on V6)

### Step 1 — Character Count Audit

**Measure Style Prompt:**
- Copy everything from your genre/BPM/mood description
- Count characters (use any text tool)
- Must be ≤1000 characters
- If over: move negatives/exclusions to Exclude field first, then trim least essential descriptors

**Measure Lyrics Field:**
- Count the whole Lyrics field (V6: `[Title:]` through `[End]`; v5.5-era: `[track:]` through `[end]`), including ALL tags, direction blocks, section tags — or let `python3 tools/validate-song.py <file>` count it
- Must be ≤5000 characters
- If over: trim direction blocks (keep essential intent), reduce section production tags, shorten outro
- If still over after trimming: overflow additional direction to Suno's Advanced Settings box

**Record counts:**
```
Style: ___/1000 chars
Lyrics: ___/5000 chars
```

### Step 2 — Add Global Control Tags

If missing, add these at the TOP of Lyrics field (before the first section/content tag):

```
[track: genre: [your genre], mood: [your mood], length: [seconds]]
[control: no-repeat, dynamic transitions]
[sequence: [list all sections in order]]
```

**Length calculation:** `runtime_s ≈ (sung_lines × bars_per_line + instrumental_bars) × beats_per_bar × 60 / BPM`. At 92 BPM in 4/4 one bar ≈ 2.6 s; a sung line usually takes 1-2 bars including the breath. Example: 32 sung lines × 1.5 bars + 16 instrumental bars = 64 bars ≈ 2:47 (167 s). Round to the nearest 15 seconds.

**Sequence:** List EVERY section tag that appears, in order:
```
[sequence: intro, verse, pre-chorus, chorus, verse, pre-chorus, chorus, bridge, final chorus, outro]
```

### Step 3 — Validate [control] Parameters

Only these values were observed to work on v5.x (legacy — `[control:]` is not part of the V6 grammar; see `references/SUNO_TAGS_REFERENCE.md`):
- `no-repeat` ✅
- `dynamic transitions` ✅
- `instrumental` ✅

**Invalid** (remove if present): `build across sections`, custom phrases, unconfirmed terms.

**Discovered a new working parameter?** Contribute it via SOP 08.

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
- ✅ Valid: adjectives/descriptors (powerful, intimate, wide, dark, stripped, rising, sparse, full, layered, driving)
- ✅ Valid: vocal delivery (vulnerable vocals, close-mic, whispered, spoken)
- ❌ Invalid: instrument instructions ("cello enters low", "drums enter soft", "guitar picks up tempo")
- ❌ Invalid: custom phrases ("maximum width", "build across sections")

**Practical limit:** Recommend 2-4 pipe parameters per section tag. Beyond 5, Suno may deprioritize later descriptors.

**Move invalid pipe params** to Production Direction block or standalone tags.

### Step 5 — Add Vocal Delivery Tags

Per-section vocal tags SUPPLEMENT the global Vocal Direction block — they specify WHERE a delivery change happens. The Vocal Direction block sets the baseline; section tags mark departures from it.

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

At key moments, add explicit tags. Dynamics can be expressed as **standalone tags** (`[build]` before a section) OR as **pipe parameters** (`[section | building, rising]`). Use standalone tags for mid-section dynamic events (e.g., sudden silence in the middle of a verse). Use pipe parameters when the dynamic applies to the entire section.

| Moment | Standalone Tag | Pipe Alternative |
|---|---|---|
| Pre-chorus building | `[build]` | `[pre-chorus \| building, rising tension]` |
| Dramatic silence | `[silence: sudden]` | N/A (use standalone — mid-section event) |
| Key change | `[modulation: ascending]` or `[modulation: sudden]` | N/A |
| Volume increasing | `[crescendo]` | `[section \| swelling, crescendo]` |
| Volume decreasing | `[diminuendo]` | `[section \| fading, pulling back]` |
| Rhythm change | `[beat-switch: half-time]` | N/A |
| Grand ending | `[big finish]` | `[final chorus \| powerful, big finish]` |
| Held note | `[fermata]` | N/A |

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
- [ ] No prohibited end punctuation on lyric lines (no periods, commas, semicolons, exclamation marks, question marks). Em-dashes (—) ARE allowed for phrasing/breath. Apostrophes (') and hyphens (-) are fine.
- [ ] Each line = one melodic phrase
- [ ] 4-8 lines per section maximum (for sections with sung/spoken lyrics — instrumental sections with only a tag and no lyrics are valid)
- [ ] No lyrics on same line as tags
- [ ] Tags on their own line
- [ ] `[track:]` tag is present with genre, mood, and length
- [ ] Production Direction block present
- [ ] Vocal Direction block present

### Step 10 — Set Creative Sliders (optional)

Only if your Suno UI exposes sliders. Values are v5.5-era starting points (legacy — re-validate on V6). Recommend slider values based on song type:

| Song Type | Weirdness | Style Influence | Audio (if Inspo) |
|---|---|---|---|
| Radio pop/rock | 35-45% | 55-65% | 40-50% |
| Concept album | 50-55% | 50-60% | 45% |
| Dark cinematic | 50-60% | 55-65% | 45-55% |
| Intimate ballad | 45-55% | 50-60% | 40-50% |
| Epic orchestral | 50-55% | 60-70% | 45-55% |
| Experimental | 60-75% | 40-50% | 30-40% |

**Album consistency note:** For album tracks, document slider values per track. If a render captures the intended palette well, note the settings as a baseline for adjacent tracks with similar sonic palettes. Consistency across an album matters more than per-track optimization.

### Step 11 — Prepare Exclude Field Content

Format exclusions for the dedicated Exclude field in Suno's UI (same on V6 and v5.5):
```
trap drums, beatboxing, vocal hums, bright synths
```

**Format:** Plain comma-separated text — no dash prefix (neither `-` nor `‑`); the field itself implies exclusion. In the song file, put them under an `## EXCLUSIONS:` section (preferred); a legacy `[Exclusions: ...]` line inside the Style section is still parsed and never counted toward Style chars. Dash-prefixed negatives were a v5.5-era technique for negation INSIDE the Style field — don't use them in the Exclude field.

**Note:** This goes in the EXCLUDE field in Suno's UI — NOT in Style Prompt or Lyrics.

### Step 12 — Final Output

Document the optimized version with:
```
## SUNO-OPTIMIZED VERSION

### Changes Made:
- [list of specific additions/changes]
- (If no changes: "Verification pass — all checks passed, no changes needed")

### Character Counts:
- Style: XXX/1000
- Lyrics: XXXX/5000

### Slider Recommendations (optional — only if your Suno UI exposes sliders):
- Weirdness: XX%
- Style: XX%
- Audio: XX% (if applicable)

### Exclude Field:
[content for Exclude]

### [Full optimized song]
```

---

## Common Suno Problems This Prevents (v5.5-era procedure)

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
