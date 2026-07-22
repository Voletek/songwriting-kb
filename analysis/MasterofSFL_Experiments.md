# MasterofSFL Claims — Verification Experiments

> **Date:** July 2026
> **Purpose:** A/B testing to verify key claims from MasterofSFL's guide before full adoption.
> **Priority order:** Most impactful and cheapest tests first.

---

## Testing Protocol (All Experiments)

1. Use the SAME Suno account, same time of day if possible
2. Generate 2 takes per render (check reliability)
3. Keep ALL other variables constant (only ONE variable changes per test)
4. Note model version (v5.5)
5. Rate each render: did the tested variable produce an audible, reliable difference?
6. Log results below each experiment

---

## EXPERIMENT 1: Slider Settings (Our Previous 50/60 vs Their 60/90)

**Priority:** HIGHEST — cheapest to run, most universal impact
**Claim:** Higher Style Influence (85-90%) produces more genre-accurate results.
**Credits needed:** ~20 (4 renders x 2 takes, but reusing same lyrics)

### Setup

**Shared Style Prompt:**
```
1980s thrash metal, 180 BPM, E minor, palm-muted riffs, double bass drums, aggressive male vocal, raw lo-fi production
```

**Shared Lyrics:**
```
[Verse | aggressive, fast, palm-muted guitars]
Ripping through the silence with a scream
Nothing left to lose and nothing clean
Every wall they built comes crashing down
Ashes of the old world hit the ground

[Chorus | maximum power, gang vocals]
TEAR IT DOWN
BURN THE CROWN
WE ARE THE FIRE
WE ARE THE SOUND

[end]
```

### Renders

| Render | Weirdness | Style Influence | Audio | Preset Name |
|---|---|---|---|---|
| A | 50% | 55% | — | Our old default |
| B | 25% | 95% | — | God Mode "authentic recreation" |
| C | 60% | 90% | — | MasterofSFL "Genre Rebuilder" |
| D | 80% | 85% | — | MasterofSFL "The Rebirth" |

### Measurement
- Which sounds most like actual 80s thrash?
- Which is most generic?
- Does high Style Influence + low Weirdness = best genre accuracy?
- Does high Weirdness add interesting elements or just chaos?

### Results
_(To be filled after testing)_

---

## EXPERIMENT 2: Italian Tempo Markings vs BPM Numbers

**Priority:** HIGH — cheap, affects every song with tempo requirements
**Claim:** `[Tempo: Vivace]` works more consistently than `[Tempo: 140 BPM]` or `[Tempo: Fast]`
**Credits needed:** ~25 (5 renders x 2 takes)

### Setup

**Shared Style Prompt (base):**
```
Dark cinematic rock, D minor, aggressive, distorted guitar, heavy drums, male baritone, raw
```

**Shared Lyrics:**
```
[Intro | heavy guitars, building]

[Verse | driving rhythm, aggressive]
Breaking through the chains tonight
Every shadow runs from the light
Fire in my veins and ice in my hands
Standing at the edge of no man's lands

[Chorus | full power, maximum energy]
WE WILL NOT FALL
WE WILL NOT BREAK
EVERY WALL THEY BUILD
IS OURS TO TAKE

[end]
```

### Renders

| Render | Tempo Method | Added To |
|---|---|---|
| A | "140 BPM" | Style Prompt |
| B | "Vivace tempo" | Style Prompt |
| C | `[Tempo: Vivace]` | Lyrics field (before [Intro]) |
| D | "fast, driving tempo" | Style Prompt |
| E | "Vivace tempo, 140 BPM" | Style Prompt (BOTH) |

### Measurement
- Actual BPM of each render (use tap-tempo tool)
- Which method produces the most consistent/accurate tempo?
- Does doubling up (E) give better results than either alone?

### Results
_(To be filled after testing)_

---

## EXPERIMENT 3: Stress Pattern Steering (THE BIG ONE)

**Priority:** HIGH — the core thesis. Most complex to evaluate.
**Claim:** Lyrical meter (iambic vs spondee vs anapestic) steers Suno's musical delivery more than tags do.
**Credits needed:** ~20 (4 renders x 2 takes + 1 alt)

### Setup

**Shared Style Prompt:**
```
Dark rock, 100 BPM, E minor, male vocal, electric guitar, drums, aggressive energy
```

**Same concept:** A man walking down a dark road alone, determined.

### Renders

**Render A — Iambic (natural speech: da-DUM da-DUM):**
```
[Verse]
The night descends upon the empty road
A distant light begins to flicker low
The silence breaks beneath my heavy load
And shadows dance where no one dares to go
```

**Render B — Spondee-heavy (STRESS STRESS — hard, pounding):**
```
[Verse]
Dark night. Cold road. No light. Dead end.
Hard ground. Dry throat. Raw hands. Cracked skin.
Long walk. Last chance. One shot. Don't break.
Stand tall. Push through. Fight back. Don't bend.
```

**Render B-alt — Spondee without ALL CAPS (isolates meter from formatting):**
```
[Verse]
Dark night. Cold road. No light. Dead end.
Hard ground. Dry throat. Raw hands. Cracked skin.
Long walk. Last chance. One shot. Don't break.
Stand tall. Push through. Fight back. Don't bend.
```

**Render C — Anapestic (da-da-DUM — galloping, fast):**
```
[Verse]
In the dead of the night when the cold starts to bite
And the road stretches far with no end still in sight
There's a fire in my chest and a weight on my back
But I'm running ahead and I'm never turning back
```

**Render D — Pyrrhic/flowing (unstressed-unstressed — light, airy):**
```
[Verse]
ever moving on the open way
barely touching where the shadows lay
gently fading into silver grey
only whispers at the end of day
```

### Measurement
- Does the MUSIC change character between renders?
- Does spondee produce heavier drums/delivery?
- Does anapestic produce galloping/faster rhythm?
- Does pyrrhic produce lighter instrumentation?
- Tags and style are IDENTICAL — only lyric rhythm changes. Any audible difference = the thesis has merit.

### Results
_(To be filled after testing)_

---

## EXPERIMENT 4: Chord Progression Tags

**Priority:** MEDIUM — affects harmonic control
**Claim:** `[Chord Progression: I-IV-V (C7, F7, G7)]` in the lyrics field guides harmonic content.
**Credits needed:** ~15 (3 renders x 2 takes)

### Setup

**Shared Style Prompt:**
```
Blues rock, 95 BPM, E major, electric guitar, organ, drums, warm gritty
```

### Renders

**Render A — No chord tag (baseline):**
```
[Verse]
Walking down that dusty road again
Sun is high and money's running low
Every step feels heavier than the last
But I keep moving cause it's all I know

[end]
```

**Render B — Standard blues progression tagged:**
```
[Chord Progression: I-IV-V (E7, A7, B7)]
[Verse]
Walking down that dusty road again
Sun is high and money's running low
Every step feels heavier than the last
But I keep moving cause it's all I know

[end]
```

**Render C — Unusual/minor progression tagged:**
```
[Chord Progression: i-bVI-bVII-i (Em, C, D, Em)]
[Verse]
Walking down that dusty road again
Sun is high and money's running low
Every step feels heavier than the last
But I keep moving cause it's all I know

[end]
```

### Measurement
- Does B sound more "standard blues" than A?
- Does C sound darker/minor compared to B?
- Can you hear the harmonic difference, or does Suno ignore the tag entirely?

### Results
_(To be filled after testing)_

---

## EXPERIMENT 5: Tag Sandwiching vs Pipe Notation

**Priority:** MEDIUM — affects tag precision
**Claim:** Focus tags BEFORE and AFTER the structure tag work better than all tags before.
**Credits needed:** ~15 (3 renders x 2 takes)

### Setup

**Shared Style Prompt:**
```
Cinematic orchestral rock, 110 BPM, D minor, epic, strings, brass, male vocal, powerful
```

**Same lyrics for all:**
```
Into the fire we march as one
No retreat and nowhere left to run
Through the smoke and through the flame
We will never be the same
```

### Renders

**Render A — Our pipe approach:**
```
[Verse | epic orchestral, building strings, brass accents, powerful male vocal, cinematic]
Into the fire we march as one
...
```

**Render B — Sandwiched:**
```
[Tempo: Allegro]
[Mood: Epic]
[Instrument: Strings, Brass]
[Verse]
[Vocals: Powerful male, baritone]
Into the fire we march as one
...
```

**Render C — Sandwiched with descriptive structure:**
```
[Tempo: Allegro]
[Mood: Epic, Building]
[Instrument: Strings, Brass Swells]
[Verse: Powerful, Cinematic, Building Intensity]
[Vocals: Male Baritone, Projected, Heroic]
Into the fire we march as one
...
```

### Measurement
- Does sandwiching produce more precise results (strings prominent, brass present, vocal powerful)?
- Or does pipe notation work equally well?
- Does C (descriptive structure + sandwich) outperform B (minimal structure + sandwich)?

### Results
_(To be filled after testing)_

---

## EXPERIMENT 6: Return Tags After Breaks

**Priority:** MEDIUM-LOW — practical fix, quick to test
**Claim:** Without "return to" tags after solos/breaks, Suno can't find its way back to the song.
**Credits needed:** ~15 (3 renders x 2 takes)

### Setup

**Shared Style Prompt:**
```
Hard rock, 120 BPM, A minor, distorted guitar, drums, male vocal, driving
```

### Renders

**Render A — No return tag:**
```
[Verse]
Breaking through the walls tonight
Nothing gonna hold me down

[Guitar Solo]

[Chorus]
We are the fire in the dark
We are the ones who never fall

[end]
```

**Render B — Simple return tag:**
```
[Verse]
Breaking through the walls tonight
Nothing gonna hold me down

[Guitar Solo]
[Solo ends]
[Return to main song]

[Chorus]
We are the fire in the dark
We are the ones who never fall

[end]
```

**Render C — Detailed return (longer solo):**
```
[Verse]
Breaking through the walls tonight
Nothing gonna hold me down

[Guitar Solo | blues scale, 16 bars]
[Band syncs]
[Return to main riff]

[Chorus]
We are the fire in the dark
We are the ones who never fall

[end]
```

### Measurement
- Does Render A drift after the solo (different key, different feel)?
- Do B and C return to verse/chorus feel more cleanly?
- Is the difference more noticeable with longer solos (C)?

### Results
_(To be filled after testing)_

---

## EXPERIMENT 7: Percentage Genre Weighting

**Priority:** LOW — marginal expected difference
**Claim:** `Thrash Metal (80%), EDM (20%)` produces controllable genre blending.
**Credits needed:** ~15 (3 renders x 2 takes)

### Setup

**Shared Lyrics:**
```
[Verse | aggressive, driving]
Circuits overload and the system burns
Every warning sign that the world ignores
Digital decay in a concrete maze
Running out of time in electric haze

[Chorus | powerful, anthem]
OVERRIDE THE SIGNAL
BREAK THE CODE
WE ARE THE VIRUS
IN THE MACHINE'S ABODE

[end]
```

### Renders

**Render A — Our descriptive approach:**
```
Style: Thrash metal with EDM undertones, 160 BPM, aggressive, double bass drums, synth layers
```

**Render B — Percentage explicit:**
```
Style: Thrash Metal (80%), EDM (20%), 160 BPM, aggressive, double bass drums, synth layers
```

**Render C — Narrative blend:**
```
Style: 80s Era Thrash Metal (80%), Influenced by 90s Era EDM (20%), EDM vibes layered behind thrash metal sound, 160 BPM, aggressive
```

### Measurement
- Does the percentage syntax give MORE control over the blend ratio?
- Does narrative description (C) work better than numbers (B)?
- Is there any audible difference vs our descriptive approach (A)?

### Results
_(To be filled after testing)_

---

## Summary: Execution Order (Optimized for Cost/Impact)

| Order | Experiment | Credits | Expected Impact |
|---|---|---|---|
| 1 | Sliders (Exp 1) | ~20 | Universal — affects every future song |
| 2 | Italian Tempo (Exp 2) | ~25 | High — affects every song with tempo needs |
| 3 | Stress Patterns (Exp 3) | ~20 | Potentially game-changing — the big thesis |
| 4 | Return Tags (Exp 6) | ~15 | Practical fix, quick to confirm |
| 5 | Chord Progressions (Exp 4) | ~15 | Moderate — harmonic control |
| 6 | Sandwiching (Exp 5) | ~15 | Interesting but pipe format already works |
| 7 | Percentage Weighting (Exp 7) | ~15 | Low — marginal difference expected |
| **TOTAL** | | **~125** | |

---

## Post-Testing Actions

**If Experiment 3 confirms meter-steering:**
- Elevate Step 4b (Rhythmic Design) from [Experimental] to [Tier 3: Confirmed]
- Add meter selection to the critique framework scoring
- Develop genre-specific meter templates (what meters work best for indie? metal? folk?)

**If Experiment 1 confirms higher Style Influence:**
- Remove "50-60%" language entirely from all docs
- Set new default recommendation at 70-80% for standard work

**If Italian tempo markings work (Exp 2):**
- Make Italian marking the PRIMARY tempo method, BPM the secondary/human-reference
- Add to the 7-Dimension Formula as the preferred format for Dimension 2

**If any experiment FAILS to show a difference:**
- Mark the claim as [Tier 3: Unconfirmed] and note negative result
- Do not remove from methodology — leave as optional technique with honest assessment
