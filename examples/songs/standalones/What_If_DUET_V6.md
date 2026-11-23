# What If — Duet (Mode B) — V6 Format

> Song Thesis: *The same two words that trap you in fear can free you into hope — if someone holds
> your hand through the question.*

> **V6 migration of `What_If_DUET.md`** (the v5.5-era original, Duet Mode B: main voice + `()`
> response). Same words, same Style Prompt, same direction blocks and Production Notes, re-tagged in
> the canonical V6 grammar from `references/V6_TAG_REFERENCE.md`. The 8-step analysis, 23-point
> checklist and rubric stay in the original. Status: not yet rendered on V6. Log results in
> `## RENDERS` below and in the `references/V6_TAG_DISCOVERY.md` results log.

## What changed from the v5.5-era version

| v5.5-era original | V6 version | Why |
|---|---|---|
| `[Fingerpicked acoustic guitar, gentle, intimate]` | `[Instrument: Acoustic Guitar In]` + `[Dynamic: Soft]` | V6 honours entrances and exits on cue |
| Arrangement described only in Production Direction and Production Notes | Piano + bass in at Pre-Chorus 1, brushes in at Chorus 1, out for Verse 2, back in at Pre-Chorus 2 | Same entry points as the original's Dynamics notes, namespaced |
| `[Piano only, intimate, both voices close]` | Acoustic guitar, bass and brushes out + `[Vocal: Close-Mic]` | Explicit exits leave piano alone |
| `[Full band, warm strings, both voices strong]` | `[Transition: Crescendo, Acoustic Guitar In, Bass In, Brushes In]` + `[Instrument: Strings In]` + `[Dynamic: Full]` + `[Female response, equal strength]` | Compound transition keeps the section at 4 tags |
| `[Acoustic guitar alone, gentle]` | Piano, bass, brushes and strings out | Guitar is left alone |
| Voice roles only in Style and Vocal Direction | `[Male lead, ...]` / `[Female response, ...]` role tags at key sections | V6 role form; the Style declaration still does the Mode B work |
| `[end]` | `[End]` | V6 terminator |
| `[Exclusions: ...]` inside the Style section | `## EXCLUSIONS:` section, plain comma-separated, plus `vocal overlap confusion` | Exclude field format; `()` layer rule |
| No render settings | `## RENDER SETTINGS` (voice left empty) | SOP 10 Step 1: ask which voice(s) before rendering |

Kept on purpose: every lyric word, the `()` response layer, the Style Prompt's vocal-assignment
declaration (male tenor for the main lines, female mezzo-soprano for the lines in parentheses, which
is what makes Mode B work), the `[Production Direction:]` / `[Vocal Direction:]` blocks, and the
Production Notes block.

---

## STYLE PROMPT:

Indie pop, acoustic pop, 100 BPM, warm hopeful, fingerpicked acoustic guitar, piano, brushed drums, male tenor vocals breathy and vulnerable for main sections, female mezzo-soprano vocals warm and grounding for response sections in parentheses, intimate close-mic production, organic warmth, building emotional arc, G major, clear vocal separation, no hums, no beatboxing, no vocal overlap

---

## EXCLUSIONS:

trap drums, beatboxing, vocal hums, heavy distortion, dark ambient, industrial sounds, screaming, rap, EDM drops, autotune, vocal overlap confusion

---

## RENDER SETTINGS

voice_id:
model: v6
controls:

Before rendering, the renderer must ask the user which voice(s) to use (SOP 10 Step 1).

---

## LYRICS:

[Title: What If]

[Production Direction: Warm, intimate, and organic. Start near-empty with solo acoustic guitar and bloom gradually into full warm band by final chorus. Never aggressive, never cold. Bridge strips to piano only — let the words carry everything. Production should feel like a warm kitchen at midnight — two people at a table, one spiraling, one holding space. Final chorus adds light strings for emotional lift but stays grounded. The sound of being HELD, not performed at.]

[Vocal Direction: Lead male tenor — warm, slightly breathy, intimate, the anxious voice. Conversational in verses, opens emotionally in chorus. Response female mezzo-soprano in parentheses — warm, clear, gentle strength, like a hand on a shoulder. Present but not overpowering. By final chorus both voices at equal strength. Clear vocal separation, no overlap confusion, no hums, no beatboxing.]

[Intro]
[Instrument: Acoustic Guitar In]
[Dynamic: Soft]

[Verse 1]
[Dynamic: p]
[Male lead, breathy, close-mic, conversational]
What if I fall apart before I even start
What if every step I take just leads me somewhere dark
What if they were right and I've been wrong this whole time
What if I'm the only one who can't read the signs

[Pre-Chorus]
[Instrument: Piano In]
[Instrument: Bass In]
[Dynamic: Crescendo]
These walls I built from questions keep getting taller
And I'm running out of air in here

[Chorus]
[Instrument: Brushes In]
[Dynamic: mf]
[Male lead, opening up]
[Female response, warm, grounding]
What if we just try
What if the ground holds when we step outside
(What if it works — what if you fly)
What if the answer's been here the whole time
(I'll be right beside you either way)
What if — what if — what if we're okay

[Verse 2]
[Instrument: Brushes Out]
[Dynamic: mp]
[Male lead, conversational]
What if I say the wrong thing and it all comes down
What if the silence after is the loudest sound
What if I've been so afraid of what I'd lose
I forgot to count the things I never chose

(What if we just shift it — turn the lens around)
(What if what you're scared of is the safest ground)

[Pre-Chorus]
[Instrument: Brushes In]
[Dynamic: Crescendo]
[Male lead, emotional strain]
I've been holding all these questions like a fist
What if I just — open it

[Chorus]
[Dynamic: f]
[Vocal: Harmony]
[Female response, stronger]
What if we just try
What if the ground holds when we step outside
(What if it works — what if you fly)
What if the answer's been here the whole time
(I'll be right beside you either way)
What if — what if — what if we're okay

[Bridge]
[Instrument: Acoustic Guitar Out]
[Instrument: Bass Out]
[Instrument: Brushes Out]
[Vocal: Close-Mic]
I've spent so long asking what goes wrong
(What if I asked you — what if it goes right)
Same two words but everything has changed
(You don't have to know — you just have to stay)

[Final Chorus]
[Transition: Crescendo, Acoustic Guitar In, Bass In, Brushes In]
[Instrument: Strings In]
[Dynamic: Full]
[Female response, equal strength]
What if we just try
What if the ground holds when we step outside
(What if it works — what if we fly)
What if together is the answer to the question
(I was always right beside you anyway)
What if — what if — what if we're okay
(We're okay)

[Outro]
[Instrument: Piano Out]
[Instrument: Bass Out]
[Instrument: Brushes Out]
[Instrument: Strings Out]
What if

[End]

---

## PRODUCTION NOTES:

• **Title:** What If
• **Song Thesis:** *The same two words that trap you in fear can free you into hope — if someone holds your hand through the question.*
• **Key:** G major — bright, warm, guitar-friendly, accessible, universally hopeful without being saccharine. Open string resonance on acoustic guitar. Accommodates both male tenor and female mezzo comfortably.
• **Tempo:** 100 BPM — walking pace, not moping, not manic. The tempo of someone gathering courage. Fits indie/acoustic pop sweet spot.
• **Time Signature:** 4/4
• **Chord Progression (Nashville Numbers + Key of G):**
  - Verse: I – V – vi – IV (G – D – Em – C) — the universal progression, familiar = safe for the listener while the lyric creates unease
  - Pre-Chorus: vi – IV – I – V (Em – C – G – D) — starts darker, resolves upward
  - Chorus: I – V – IV – I – IV – V – I (G – D – C – G – C – D – G) — open, resolved, triumphant simplicity
  - Bridge: vi – IV – I – V (Em – C – G – D) — reflective, turning
  - Final Chorus: I – V – IV – I (G – D – C – G) — same but fuller, warmer, certain
• **Vocal:**
  - Lead: Male tenor, warm, slightly breathy, intimate — the anxious voice. Range approximately B2–E4. Delivery is conversational in verses, opens emotionally in chorus.
  - Response (parenthetical): Female mezzo-soprano, warm, clear, grounding — the wisdom voice. Range approximately A3–D5. Delivery is steady, gentle, like a hand on a shoulder. Present but not overpowering.
• **Instruments (by prominence):**
  1. Fingerpicked acoustic guitar (foundation — honesty, folk-truth)
  2. Piano (warmth, emotion, enters pre-chorus)
  3. Brushed drums (gentle pulse, enters chorus, heartbeat reliability)
  4. Warm bass (enters pre-chorus, supports without driving)
  5. Light strings/pad (final chorus only — emotional lift, community feeling)
• **Dynamics:**
  - Intro: Solo acoustic (2/10)
  - Verse 1: Acoustic + voice (3/10)
  - Pre-Chorus 1: + piano + bass hint (5/10)
  - Chorus 1: + brushed drums + response vocal (7/10)
  - Verse 2: Acoustic + piano (4/10)
  - Pre-Chorus 2: Building, drums hint (6/10)
  - Chorus 2: Full arrangement (7.5/10)
  - Bridge: Piano + both voices only (3/10)
  - Final Chorus: Full band + strings + both voices strong (9/10)
  - Outro: Solo acoustic + single voice (2/10)
• **Hook Type:** Title hook / Question-as-confession — "What if" is both the fear and the hope, recontextualized through the song
• **Rhyme Scheme:**
  - Verse: AABB (couplets — tight, anxious, spiraling)
  - Pre-Chorus: Free/AB (breaking the pattern = breaking free)
  - Chorus: ABCBDB (loose, conversational, meaning over rhyme)
  - Bridge: ABCB (resolving into clarity)
• **Emotional Arc:** Paralyzed by fear → weighted by "what ifs" → a second voice offers reframe → the same question becomes hope → choosing to try together → shared courage
• **Duet Mode:** Mode B (Parenthetical) — Main male vocal carries the anxious narrative; female response in () provides the grounding counterpoint. Style prompt declares roles explicitly.

---

## RENDERS

| Date | Model | Clip ID | Settings | Measured | Verdict |
|---|---|---|---|---|---|
