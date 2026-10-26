# Suno AI — Power Steering

## ⚡ V6 Paradigm (current default)
V6 (v6 / v6-wild / v6-mini). Status: working model (Sept 2026, user-confirmed); log render evidence in the `references/V6_TAG_DISCOVERY.md` results log.
- **Style field = the WHAT:** genre (first), key, tempo, vocal identity, production aesthetic
- **Lyrics field = the HOW:** section tags + `[Instrument: X In/Out]` + dynamics + delivery + transitions
- `[Instrument: X In]` / `[Instrument: X Out]` control instrument entrances/exits — USE THEM
- Other event tags: `[Dynamic: ...]`, `[Vocal: ...]` (or `[Male lead, inline adjective]`), `[Transition: ...]`, `[Key Change: ...]`
- 2-4 tags per section; end with `[End]`
- Do NOT use: a `[Tag Vocabulary]` block (planning aid only, not sung), v5.5 global tags (`[track:]`/`[control:]`/`[sequence:]`), pipe notation `[Section | params]`
- Master tag list: `references/V6_TAG_REFERENCE.md` · How/why: `references/V6_TAG_DISCOVERY.md`
- Deterministic check: `python3 tools/validate-song.py <file>`

## Limits
- Style: 1000 chars | Lyrics: 5000 chars | Exclude field: negatives/exclusions ONLY

## Section Rules
- Tags on own line, never with lyrics
- Verses/choruses usually 4-8 lines; bridge 3-6 (up to 8 when the turn needs it)
- No end punctuation
- Each line = one phrase = one breath; target 7-12 syllables [Tier 2]

## Key V6 Tags
- `[Vocal: Whisper]` / `[Vocal: Breathy]` — confessional sections
- `[Vocal: Belt]` / `[Vocal: Gang Vocal]` — chorus lift
- `[Dynamic: Crescendo]` — pre-chorus ramp
- `[Instrument: Drums Out]` + `[Dynamic: Diminuendo]` — bridge strip
- `[Transition: Key Lift]` / `[Key Change: ...]` — key change
- `[Dynamic: Fade Out]` — outro
- `[End]` — always at bottom

## Parenthetical Layers — `()` in Lyrics
- `(whispered) text` — delivery cue (works alone)
- `(spoken) text` — speech delivery (works alone)
- `(robotic layer: text)` — named secondary voice (**Style must declare**)
- `(echo layer: text)` — echo treatment (**Style must declare**)
- `(whisper layer: text)` — whisper texture (**Style must declare**)
- `(response text)` — backup vocal / duet response (best with Style declaration)
- Always add `vocal overlap confusion` to the Exclude field when using layers

## Exclusions (Exclude field)
Plain comma-separated text, no dash prefix — under `## EXCLUSIONS:` in the song file:
```
trap drums, beatboxing, vocal hums, bright synths
```

---

## Legacy v5.5-era mechanics (re-validate on V6)

- **Global tags (v5.5 only):** `[track: genre: X, mood: X, length: 270]` / `[control: no-repeat, dynamic transitions]` / `[sequence: ...]`; terminator `[end]` (validator accepts `[end]` and `[End]`)
- **Pipe notation:** `[chorus | powerful, wide]` — v5.5 char-saver; not V6 canonical grammar
- **v5.5 tags:** `[vulnerable vocals]`, `[whisper]` / `[whispering]`, `[build]`, `[modulation: ascending]`, `[chant]`; `[silence: sudden]` was unreliable even on v5.5 (unverified on V6)
- **Creative sliders (optional — only if your Suno UI exposes them; v5.5-era starting points):** Weirdness 50-55%, Style Influence 50-60%, Audio Influence 45% if using Inspo
- **v5.5 features (UI):** Personas (lock vocal identity per character), Stems (12-track splits for DAW mixing), Custom Models (Pro/Premier)
- **Era tags:** decade tags ("1980s") biased production style on v5.5; separate era from mix: "modern production, vintage 1970s guitar tone"
- **5-8 descriptor sweet spot**, Italian tempo preference, performance-notation symbols (only ALL CAPS was reliable) — v5.5-era Tier 3 heuristics
