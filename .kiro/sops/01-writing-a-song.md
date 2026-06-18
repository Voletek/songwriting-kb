# SOP 01: Writing a Song

> Complete step-by-step procedure from concept to finished Suno-ready output.

> **Note:** The canonical methodology for this workflow now lives in `core/methodology/songwriting.md`.
> This SOP is retained for Kiro-specific step formatting but the methodology file is the authoritative source.
> If content diverges, `core/methodology/` wins.

---

## Prerequisites

- Concept, theme, or prompt (even a single sentence works)
- Know your target: standalone single, album track, or experimental piece
- If album track: have the concept-album-bible available

---

## Procedure

### PHASE 1: Analysis (Before writing a single word)

**Step 1 — State the Song Thesis**
Write ONE sentence that captures the core truth of this song.
```
Song Thesis: [The single truth this song expresses]
```
If you can't write this, you don't have a song yet — you have a topic.

**Step 2 — Semantic Analysis**
Answer: What is this literally about? Name:
- Subject (what's happening)
- Characters (who's involved)
- Setting (where/when)
- Objects (physical things in the world)
- Actions (what occurs)

**Step 3 — Emotional Analysis**
Answer: What should the listener FEEL?
- Name the central affect (specific, not "sad" — try "hollow resignation" or "defiant grief")
- Identify 2-3 BRECVEMA mechanisms to target
- Map the emotional journey: "starts at X, moves through Y, arrives at Z"

**Step 4 — Prosodic Planning**
Decide before writing:
- Target syllables per line (7-12 at your tempo)
- Where will breath points fall?
- Which vowels work for sustained notes in your key?
- What's your default rhyme scheme? (ABCB unless you have reason to deviate)

**Step 5 — Narrative Arc**
Choose your arc type:
- Confession → panic → release
- Fear → rage → empowerment
- Numbness → memory → grief
- Isolation → collapse → acceptance
- Other (name it)

Identify WHERE THE TURN IS. What does the bridge reveal?

**Step 6 — Voice/Accent**
Answer: Who is singing?
- What's their register?
- Any accent/dialect?
- What's their emotional state at song start vs end?
- If character-driven: fill out the Character Voice Template (activate character-voice skill)

**Step 7 — Genre Mapping**
Decide:
- Primary genre (70%)
- Texture genre (30%) — if fusion
- Does this honor Fabbri's 5 rules for the chosen genre?
- What instrumentation "belongs" in this genre?

**Step 8 — Arrangement Design**
Plan the dynamic arc:
- Growth pattern (additive? subtractive? explosive? bloom?)
- Where is negative space?
- What contrast pairs exist? (quiet/loud, sparse/dense, human/machine)
- Where does the hook land? (Must be within 15s of first sung vocal — instrumental intros don't count against this clock)

**Hook timing rule:** 15 seconds is measured from the first SUNG word to the beginning of the hook phrase. An 8-second instrumental intro followed by a 12-second verse means the hook must land by second 12 of singing, not second 20 of the track.

**Runtime estimation formula:** (total lyric lines × 60/BPM × 2) + intro seconds + outro seconds. At 92 BPM: each line ≈ 2.5s with breath. Typical: 24 lines + 8s intro + 8s outro ≈ 3:15.

**Note:** This step is a SKETCH — you'll formalize it as Production Notes in Step 25. Don't over-document here.

**Step 9 — Production & Commercial**
Decide:
- Key (with reasoning)
- BPM (with reasoning)
- Target audience
- Target length
- Platform fit

---

### PHASE 2: Writing (Nashville Method)

**Step 10 — Write the Chorus FIRST**
This is your destination. Write it before anything else.
- Must contain the hook (identify your hook TYPE first: lyric, melodic, rhythmic, or production)
- If lyric hook: it must be in the chorus lyrics
- If melodic/production hook: the chorus must still contain the emotional peak
- Must be singable (test: can you hum it?)
- Every line ≤12 syllables
- Check: would someone text this line to a friend?

**Step 11 — Write the Pre-Chorus**
2-4 lines that BUILD into the chorus.
- Creates tension the chorus resolves
- Rising energy
- Should make the listener LEAN FORWARD

**Note for narrative songs:** You may find it easier to sketch V1's TOPIC first (what scene/world it sets), then write the pre-chorus that builds FROM that world into the chorus. The key principle: the chorus is your destination — everything else serves it.

**Step 12 — Write Verse 1**
4-8 lines that SET UP the chorus.
- Establish the situation/character/world
- Show don't tell (imagery, physical, sensory)
- Every line ≤12 syllables
- Use em-dashes for breath within lines

**Step 13 — Write Verse 2**
4-8 lines that ADD NEW INFORMATION.
- Must NOT restate V1
- Deepens, complicates, or progresses the narrative
- New images, new details, new perspective
- Same syllable discipline

**Step 14 — Write the Bridge (The Turn)**
3-6 lines that CHANGE THE MEANING.
- Must reveal something new
- Must make the final chorus hit differently
- Strip the production here (contrast)
- This is where the strongest single line should live

**Step 15 — Write Final Chorus (Variation)**
Same structure as Chorus 1 but:
- At least 1-2 lines changed
- Meaning has shifted because of the bridge
- Production should be fuller/different
- This is the emotional climax

**Step 16 — Write Intro/Outro**
- Intro: 2-4 lines max, sets mood. For instrumental intros, write a brief parenthetical description: `(sea-wash, 4 bars → concertina enters with melody)`. In the Suno output, use the section tag with pipe notation: `[intro | atmospheric, warm, sparse]`
- Outro: 2-4 lines max, resolves or fades
- Neither should introduce major new content

---

### PHASE 3: Quality Check

**Step 17 — Prosody Audit**
Go line by line:
- [ ] Every line ≤12 syllables?
- [ ] Stressed syllables on strong beats?
- [ ] Open vowels on any sustained notes?
- [ ] No stuffed phrases (3+ long words crammed)?
- [ ] No weak terminal words (the, of, to, in)?

**Step 18 — Structure Check**
- [ ] Hook within 15s of first vocal?
- [ ] V2 adds genuinely new information?
- [ ] Bridge contains a real turn?
- [ ] Total lyrics estimatable under 5000 chars?
- [ ] Target runtime appropriate for platform?

**Step 19 — Quality Gates**
- [ ] Every word earns its place (no filler)?
- [ ] No clichés (unless subverted)?
- [ ] Hook passes "would someone text this?" test?
- [ ] Near/slant rhymes (no forced perfect)?

---

### PHASE 4: Formatting (Suno-Ready Output)

**Step 20 — Assemble Style Prompt**
Write comma-separated descriptors: Genre, BPM, Mood, Instruments, Vocal, Production Direction
- Check: ≤1000 characters?

**Step 21 — Write Exclusions**
```
[Exclusions: ‑item, ‑item, ‑item]
```
Place in dedicated Exclude field (NOT in Style or Lyrics).

**Step 22 — Add Global Meta-Tags**
At top of Lyrics field:
```
[track: genre: X, mood: X, length: XXX]
[control: no-repeat, dynamic transitions]
[sequence: intro, verse, pre-chorus, chorus, ...]
```

**Length calculation:** Use your runtime estimate from Step 8. Minutes × 60 = seconds. Example: 3:45 target = 225 seconds.

**Step 23 — Add Direction Blocks**
```
[Production Direction: ...]
[Vocal Direction: ...]
```

**Step 24 — Format Lyrics with Section Tags**
- Tags on own lines
- Use pipe notation where appropriate
- Add dynamics tags at key moments ([build], [silence], [modulation])
- Add [end] at bottom

**Step 25 — Write Production Notes**
Include ALL of:
- Key (+ reasoning)
- Tempo (BPM + justification)
- Time Signature
- Chord Progression (Nashville + actual, per section)
- Vocal description
- Instruments (by prominence)
- Dynamics arc
- Hook Type (+ placement)
- Rhyme Scheme (per section)
- Emotional Arc (one sentence)

**Step 26 — Final Character Count**
- Style Prompt: ___/1000
- Lyrics field: ___/5000
- If over: trim (don't overflow — there's no overflow box)

---

### PHASE 5: Album Integration (If applicable)

**Step 27 — Continuity Check**
If this is an album track:
- [ ] Key fits the harmonic map?
- [ ] Sonic palette matches track range?
- [ ] No forbidden instruments?
- [ ] Vocal texture different from adjacent tracks?
- [ ] Motifs used correctly?
- [ ] Callbacks reference correct source tracks?
- [ ] Rule 11: >70% palette differentiation from similar tracks?

**For Track 1 (album opener):** Focus on establishing motifs correctly, setting up future callbacks, and verifying no forbidden elements are present. Adjacency check is forward-only (does T2's planned palette differ sufficiently?). No backward callbacks to verify.

**For the Final Track:** Focus on resolution — do motifs reach their final form? Are callbacks to earlier tracks accurate? Does the harmonic resolution feel earned?

**If this track introduces a recurring phrase:** Test it forward — write out ALL planned future uses and verify the phrase is flexible enough to carry each meaning. Fix now if it only works in one context.

---

## Output

A complete file containing:
1. Song Thesis
2. Style Prompt (≤1000 chars)
3. Exclude field content
4. Lyrics with all tags + direction blocks
5. Production Notes (complete)
6. Creative Slider recommendations

---

## Time Estimate

| Phase | Time |
|---|---|
| Analysis (Steps 1-9) | 10-15 min |
| Writing (Steps 10-16) | 20-30 min |
| Quality Check (Steps 17-19) | 5-10 min |
| Formatting (Steps 20-26) | 10-15 min |
| Album Integration (Step 27) | 5 min |
| **Total** | **50-75 min** |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Writing V1 first | Write CHORUS first (Nashville method) |
| No thesis before writing | Can't build without a destination |
| V2 restates V1 | Ask "what's NEW?" — different angle, deeper, progression |
| Bridge restates chorus | The bridge must REVEAL something the chorus hasn't said |
| Lines over 12 syllables | Split or trim — no exceptions |
| Hook after 30s | Shorten intro or V1 |
| Rhyme forcing meaning | Use slant rhyme or restructure |
