# Suno AI — Power Steering

## Limits
- Style: 1000 chars | Lyrics: 5000 chars | Exclude field: negatives/exclusions ONLY

## Creative Sliders (UI Settings)
- **Weirdness:** 50-55% for our songs (Safe↔Chaos, default 50%)
- **Style Influence:** 50-60% for our songs (how much Style Prompt steers)
- **Audio Influence:** 45% if using Inspo (how much reference affects output)

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
