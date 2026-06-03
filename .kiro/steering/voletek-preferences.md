# Voletek — Output & Format Preferences

> Auto-loaded. User-specific formatting and output requirements.

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
• Hook Type: [Title/Melodic/Rhythmic/Instrumental + placement notes]
• Rhyme Scheme: [per section with reasoning if unconventional]
• Emotional Arc: [one-sentence narrative journey]
```

Chord notation shows BOTH Nashville numbers AND actual chords: `i – VI – III – iv (Em – C – G – Am)`

## Direction Blocks (Keep in Lyrics)

Always include these as consistency anchors:
- `[Production Direction: ...]` — overall tone, dynamics arc, what to avoid
- `[Vocal Direction: ...]` — voice type, delivery, emotional progression

These survive regenerations and keep Suno consistent across iterations.

## Per-Section Production Tags

Keep per-section tags like `[Sparse piano, room ambience]` — these guide instrument changes section-by-section. Limit to 2-3 tags per section for best Suno parsing.

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
- Always include `‑vocal overlap confusion` in negatives when using layers

## Character Limit Strategy

- Style 1000 chars → positives and core vocal rules FIRST
- Lyrics 5000 chars → must fit within limit (trim if needed)
- Exclude field = ONLY for negative prompts / exclusions (not overflow)

## Hit Formula Awareness

- **Formula 1 (Vulnerability):** 70-85 BPM, minor, minimal, confession hook, specific lyrics, imperfect vocal. Men's mental health territory.
- **Formula 2 (Anthem):** 90-110 BPM, minor→major lift, maximum production, chant hook, universal lyrics.
- Know which formula a song is using and don't mix their rules.

## Song Thesis

Every song should have a one-sentence thesis stated at the top of the file:
> *Song Thesis: The core truth this song expresses in a single sentence.*
