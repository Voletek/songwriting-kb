# Suno V6 Tag Reference — Master Tag Dictionary

> **The complete, de-duplicated V6 lyric-tag vocabulary.** Copy-paste dictionary for building
> V6 songs. This is the tag catalog; for HOW to use it (division of labor, production template,
> what's confirmed), see `references/V6_TAG_DISCOVERY.md`. For v5.5-era tags, see
> `references/SUNO_TAGS_REFERENCE.md`.
>
> **Working model (Sept 2026):** treat all tags below as functional per Suno V6 system output.

---

## How V6 Tags Divide (the core rule)

- **Style field = the WHAT (identity):** genre, key, tempo, vocal identity, production aesthetic. Sets the world.
- **Lyrics field = the HOW (arrangement):** section tags, instrument In/Out, dynamics, delivery, transitions. Choreographs the performance.
- **DO NOT include a `[Tag Vocabulary]` block in final output** — it does not get sung and is not needed. It is optional planning scaffolding only.

---

## STRUCTURE (15)

```
Intro · Verse · Pre-Chorus · Chorus · Post-Chorus · Bridge · Breakdown · Build · Drop · Instrumental Solo · Interlude · Key Change · Outro · Transition · End
```

## INSTRUMENTATION — each takes In / Out for entrance & exit control (CONFIRMED WORKING)

```
Piano · Felt Piano · Rhodes · Hammond Organ
Cello · Bowed Cello · Strings · Chamber Strings · Fiddle · Harmonica
Banjo · Acoustic Guitar · Electric Guitar · Slide Guitar · Muted Guitar
Upright Bass · Bass · Distorted Bass · Sub-Bass
Drums · Kick · Snare · Toms · Floor Tom · Cymbals · Percussion · Brushes
Boot Stomp · Hand Claps · Tambourine
Synth Pad · Synth Lead · Analog Synth · Arp
Room Tone · Drone · Vocal Chop · FX / Texture
```

Usage: `[Instrument: Banjo In]` ... `[Instrument: Banjo Out]`

## DYNAMICS (classical + named)

```
pp · p · mp · mf · f · ff · fff
Whisper (Hush) · Soft · Full · Fortissimo
Crescendo · Diminuendo · Swell · Drop · Full Impact
Fade In · Fade Out · Silence · Rest · Accent · Staccato · Sustain
```

## FEEL / TEMPO

```
Free Time · Rubato · Straight · Steady Stomp · Shuffle
Half-Time · Double-Time (Lift) · Bar Extension
Ritardando · Accelerando · Push · Hold
```
Plus explicit BPM and Italian markings (Adagio, Andante, Moderato, Allegro, etc.)

## VOCALS

```
Male Lead · Female Lead · Female Counter (Counterline / Counter-Voice)
Baritone · Tenor Lift · Falsetto
Whisper · Breathy · Dry / Close-Mic · Spoken Word · Half-Spoken
Raspy · Growl · Belt · Full Voice
Harmony · Unison · Layered Double · Gang Vocal
Call · Response · Ad-Lib
Reverb Tail · Vocal Out · Laugh · Breath
```

## TRANSITIONS

```
Entrance · Exit · Pickup · Turnaround
Riser · Drum Fill · Reverse Cymbal · Cymbal Rise
Stop-Time · Breath · Hit · Cut · Hard Cut
Key Change Up (Key Lift) · Filter Open · Filter Close · Glitch Cut
```
Compound transitions bundle simultaneous events: `[Transition: Crescendo, Snare In, Synth Riser]`

## PRODUCTION / FX

```
Vinyl Crackle · Tape Hiss · Room Tone
Filtered · Saturated · Detuned · Distorted
Stereo Widening · Delay · Reverb
Analog Warmth · Digital Cold
```

---

## Tag Syntax Forms Observed (all worked in V6 system output)

| Form | Example |
|---|---|
| Categorized bracket | `[Instrument: Banjo In]`, `[Vocal: Belt]`, `[Dynamic: Crescendo]` |
| Inline delivery detail | `[Male Lead: Whisper, dry close vocal]`, `[Female Lead: Call, lifted alto]` |
| Compound (bundled) | `[Transition: Crescendo, Snare In, Synth Riser]` |
| Call/response on own lines | `[Call] Higher!` then `[Response] Higher!` |
| Compact pipe vocabulary (planning only) | `[VOCABULARY:VOCALS=whisper\|belt\|gang\|...]` |

---

## Minimal V6 Song Skeleton (production-ready)

```
[Intro]
[Instrument: Piano In]
[Instrument: Cello In]
[Vocal: Whisper]
...lyric...

[Verse 1]
[Instrument: Drums In]
[Instrument: Bass In]
[Vocal: Male Lead]
...lyric...

[Pre-Chorus]
[Dynamic: Crescendo]
[Instrument: Banjo In]
...lyric...

[Chorus]
[Dynamic: Full]
[Vocal: Belt]
[Vocal: Gang Vocal]
...lyric...

[Bridge]
[Instrument: Drums Out]
[Dynamic: Diminuendo]
[Vocal: Spoken Word]
...lyric...

[Final Chorus]
[Transition: Key Lift]
[Dynamic: Fortissimo]
...lyric...

[Outro]
[Dynamic: Fade Out]
[Instrument: Piano Out]
[End]
```

(No `[Tag Vocabulary]` block. Style/identity lives in the Style field.)

---

*Living document. Note: v5.5-era tags and this V6 set coexist — use V6 tags for V6 renders.
Style prompts that pair with these tags are in `references/STYLE_LIBRARY.md`.*