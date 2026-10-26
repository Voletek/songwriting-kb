# User Preferences — Power Steering

## Always Output: Production Notes Block

Every song must include:
- Key (+ reasoning)
- Tempo (BPM + justification)
- Time Signature
- Chord Progression (Nashville numbers AND actual chords, per section)
- Vocal description
- Instruments (by prominence)
- Dynamics arc (section arrows)
- Hook Type (Lyric/Title, Melodic, Rhythmic, or Instrumental/Production + placement)
- Rhyme Scheme (per section, with the stability it creates)
- Emotional Arc (one sentence)

## Format Conventions
- `[Production Direction:]` and `[Vocal Direction:]` blocks in lyrics (consistency anchors)
- Per-section cues (V6 default): `[Instrument: X In]` / `[Instrument: X Out]` + `[Dynamic: ...]` / `[Vocal: ...]`, 2-4 tags per section; end with `[End]`
- `[Male Vocal]` / `[Female Vocal]` capitalized
- Duet: alternating lines, 4 exchanges per section
- Em dashes (—) for phrasing/breath within lines

## Parenthetical Layers
- Backup/response vocals: plain `(text)` — Style must declare who sings them
- Delivery cues: `(whispered) text`, `(spoken) text` — changes next-line performance
- Named layers: `(robotic layer: text)`, `(echo layer: text)`, `(whisper layer: text)` — MUST declare in Style Prompt
- Layer treatment tags: `[deep echo layer]` after parenthetical lines for production treatment
- Always add `vocal overlap confusion` to the Exclude field when using layers

## Exclude Field
- Plain comma-separated text, no dash prefix, under `## EXCLUSIONS:` in the song file: `trap drums, beatboxing, vocal hums, bright synths`

## Sliders
- Optional — only if your Suno UI exposes them; values are v5.5-era starting points (legacy)

## Song Thesis
Every song starts with:
> *Song Thesis: [one sentence core truth]*
