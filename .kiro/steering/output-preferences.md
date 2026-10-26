---
inclusion: always
description: Song output format conventions — Production Notes block, direction blocks, per-section tags, Exclude-field format, parenthetical layers, duet formatting, optional slider notes, hit formulas, and song thesis requirement.
---

# Output & Format Preferences

> Always loaded (`inclusion: always`). Recommended output format for all song files.
> Customize this file for your own conventions — see examples/preferences/ for a filled-in reference.

---

## Always Include: Production Notes Block

Every song output MUST include a detailed Production Notes section:

```
• Key: [Key] — [reasoning]
• Tempo: [X] BPM — [justification]
• Time Signature: [4/4 or 3/4 or 6/8]
• Chord Progression: [Nashville numbers] / [actual chords in key]
  (Different progressions for Verse, Pre-Chorus, Chorus, Bridge, Final Chorus)
• Vocal: [Type + delivery description]
• Instruments: [listed by prominence]
• Dynamics: [section-by-section energy with arrows]
• Hook Type: [Lyric/Title, Melodic, Rhythmic, or Instrumental/Production + placement notes]
• Rhyme Scheme: [per section, with the stability it creates (closed/open) and reasoning]
• Emotional Arc: [one-sentence narrative journey]
```

Chord notation shows BOTH Nashville numbers AND actual chords: `i – VI – III – iv (Em – C – G – Am)`

## Direction Blocks (Keep in Lyrics)

Always include these as consistency anchors:
- `[Production Direction: ...]` — overall tone, dynamics arc, what to avoid
- `[Vocal Direction: ...]` — voice type, delivery, emotional progression

These survive regenerations and keep Suno consistent across iterations.

## Artist Reference Conversion

Any artist name used as creative shorthand during writing (e.g., "in the style of Radiohead") must be converted to descriptive production language before appearing in the Style Prompt or Direction blocks. Translate to: genre + era + instruments + production characteristics + vocal style + structural habits. No artist names in final output.

## Per-Section Production Tags

Keep per-section tags — they guide instrument changes section-by-section. On V6 (default) use `[Instrument: X In]` / `[Instrument: X Out]` plus `[Dynamic: ...]` / `[Vocal: ...]` tags, 2-4 tags per section. (v5.5-era free-text cues like `[Sparse piano, room ambience]` are legacy — re-validate on V6.)

## Duet Format Preferences

- `[Male Vocal]` / `[Female Vocal]` — capitalized, standardized
- Duet: give-and-take alternating (Male then Female per exchange)
- Target 4 exchanges per section (8 lines) but flexible

## Parenthetical Layers (Inline Vocal Effects)

- **Backup/response vocals:** plain `(text)` — works when Style declares who sings them
- **Delivery cues:** `(whispered) text` / `(spoken) text` — changes performance of next line
- **Named layers:** `(robotic layer: text)` / `(echo layer: text)` / `(whisper layer: text)` — creates a distinct secondary vocal identity. MUST be declared in Style Prompt.
- **Whisper Rule pattern:** Declare at top of lyrics: `[Whisper Rule: Lyrics in parentheses are whispered intrusive thoughts, close and breathy.]`
- **Echo/Layer treatment notation:** `[deep echo layer]` or `[distant burr echo]` after parenthetical lines to specify production treatment of those layers
- Always add `vocal overlap confusion` to the Exclude field when using layers

## Character Limit Strategy

- Style 1000 chars → positives and core vocal rules FIRST
- Lyrics 5000 chars → must fit within limit (trim if needed)
- Exclude field = ONLY for negative prompts / exclusions (not overflow) — plain comma-separated text, no dash prefix, written under an `## EXCLUSIONS:` section in the song file:
  ```
  trap drums, beatboxing, vocal hums, bright synths
  ```

## Slider Recommendations (Optional)

Include creative-slider recommendations only if your Suno UI exposes sliders. Values are v5.5-era starting points (legacy — re-validate on V6); see `suno-formatting.md` → Legacy v5.5-era mechanics.

## Hit Formula Awareness

- **Formula 1 (Vulnerability):** 70-85 BPM, minor, minimal, confession hook, specific lyrics, imperfect vocal. Men's mental health territory.
- **Formula 2 (Anthem):** 90-110 BPM, minor→major lift, maximum production, chant hook, universal lyrics.
- Know which formula a song is using and don't mix their rules.

## Song Thesis

Every song should have a one-sentence thesis stated at the top of the file:
> *Song Thesis: The core truth this song expresses in a single sentence.*
