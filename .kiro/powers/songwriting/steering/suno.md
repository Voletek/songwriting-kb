# Suno AI — Power Steering

## ⚡ V6 Paradigm (current default)
V6 (v6 / v6-wild / v6-mini) uses a DIFFERENT tag paradigm than v5.5:
- **Style field = the WHAT:** genre, key, tempo, vocal identity, production aesthetic
- **Lyrics field = the HOW:** section tags + `[Instrument: X In/Out]` + dynamics + delivery + transitions
- `[Instrument: X In]` / `[Instrument: X Out]` control instrument entrances/exits — USE THEM
- Do NOT put a `[Tag Vocabulary]` block in final output (planning aid only, not sung)
- v5.5 sliders/features below are NOT assumed to apply to V6 — re-validate
- Master tag list: `references/V6_TAG_REFERENCE.md` · How/why: `references/V6_TAG_DISCOVERY.md`

## Limits
- Style: 1000 chars | Lyrics: 5000 chars | Exclude field: negatives/exclusions ONLY

## Creative Sliders (UI Settings)
- **Weirdness:** 50-55% for our songs (Safe↔Chaos, default 50%)
- **Style Influence:** 50-60% for our songs (how much Style Prompt steers)
- **Audio Influence:** 45% if using Inspo (how much reference affects output)

## v5.5 Features (UI, not text tags)
- **Personas:** Lock vocal identity per character. Select before generating.
- **Stems:** Extract 12-track splits for DAW mixing. Use for album consistency.
- **Custom Models:** Train on your tracks to learn your style (Pro/Premier).

## Era Tags (Style Prompt)
Decade tags ("1980s") aggressively bias production style. To get vintage instruments with modern production: "modern production, vintage 1970s guitar tone" — separate era from mix.

## Always Include
```
[track: genre: X, mood: X, length: 270]
[control: no-repeat, dynamic transitions]
[sequence: intro, verse, pre-chorus, chorus, ...]
```

## Section Rules
- Tags on own line, never with lyrics
- 4-8 lines per section
- No end punctuation
- Each line = one phrase = one breath

## Key Tags
- `[vulnerable vocals]` — confessional sections
- `[whisper]` — lead whispered / `[whispering]` — background layer
- `[build]` — pre-chorus ramp
- `[silence: sudden]` — dramatic pause
- `[modulation: ascending]` — key change
- `[chant]` — repeated hook/mantra
- `[end]` — always at bottom

## Parenthetical Layers — `()` in Lyrics
- `(whispered) text` — delivery cue (works alone)
- `(spoken) text` — speech delivery (works alone)
- `(robotic layer: text)` — named secondary voice (**Style must declare**)
- `(echo layer: text)` — echo treatment (**Style must declare**)
- `(whisper layer: text)` — whisper texture (**Style must declare**)
- `(response text)` — backup vocal / duet response (best with Style declaration)
- Always add `‑vocal overlap confusion` to exclusions when using layers

## Exclusions
```
[Exclusions: ‑beatboxing, ‑vocal hums, ‑trap drums, ...]
```
