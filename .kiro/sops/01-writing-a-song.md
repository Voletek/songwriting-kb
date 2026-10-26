# SOP 01: Writing a Song

> Complete step-by-step procedure from concept to finished Suno-ready output.

> **Note:** The canonical methodology for this workflow now lives in `core/methodology/songwriting.md`.
> This SOP is retained for Kiro-specific step formatting but the methodology file is the authoritative source.
> If content diverges, `core/methodology/` wins.

---

## Prerequisites

- Concept, theme, or prompt (even a single sentence works)
- Know your target: standalone single, album track, or experimental piece
- If album track: have the concept-album-blueprint available

---

## Procedure

### PHASE 1: Analysis (Before writing a single word)

> **Planning is now its own workflow.** The authoritative source for Phase 1 planning is SOP 09
> (`.kiro/sops/09-planning-a-song.md`) and `core/methodology/song-planning.md`, which formalize this
> analysis into an approvable **Song Brief**. You can do Phase 1 three ways:
> - **Inline** — walk Steps 1-9 below as part of writing (fastest for simple songs).
> - **Via the planner** — run SOP 09 / the **song-planner** agent to produce a `SONGNAME.brief.md`
>   first, then flow into writing.
> - **Consume an existing brief** — if a `SONGNAME.brief.md` already exists next to the song, use it
>   directly as the completed Phase 1 plan and skip straight to Phase 2.
> The steps below remain as the inline reference; they mirror the brief's conceptual sections.

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
- Target syllables per line (7-12 [Tier 2]; 13-15 = review at tempo; 16+ = Compression Test)
- Where will breath points fall?
- Which vowels work for sustained notes in your key?
- Rhyme & stability plan per section — there is no universal default. ABCB (XAXA) is a common conversational option (less closure); choose stable/closed schemes for choruses and resolutions, unstable/open ones for pre-choruses and bridges. See `references/RHYME_AND_LYRIC_CRAFT.md`.

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
- Which of Fabbri's five genre-rule types (formal/technical, semiotic, behavioural, social/ideological, economic/juridical) carry the most weight in this genre, and does the song honor them? (Rule types, not a pass/fail checklist; ironic juxtaposition is itself a convention.)
- What instrumentation "belongs" in this genre?

**Step 8 — Arrangement Design**
Plan the dynamic arc:
- Growth pattern (additive? subtractive? explosive? bloom?)
- Where is negative space?
- What contrast pairs exist? (quiet/loud, sparse/dense, human/machine)
- Where does the hook land? [Tier 2] (Aim for a hook signal within the first 5-30s of singing; genre-dependent -- instrumental intros don't count against this clock)

**Hook timing guidance:** Measured from the first SUNG word to the beginning of the hook phrase. An 8-second instrumental intro followed by a 12-second verse means the hook must land by second 12 of singing, not second 20 of the track. Pop tends toward earlier hooks; progressive and cinematic genres allow more setup.

**Runtime estimate:** `runtime_s ≈ (sung_lines × bars_per_line + instrumental_bars) × beats_per_bar × 60 / BPM`. At 92 BPM in 4/4 one bar ≈ 2.6 s; a sung line usually takes 1-2 bars including the breath. Example: 32 sung lines × 1.5 bars + 16 instrumental bars = 64 bars ≈ 2:47.

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

> **Option — Guided / collaborative section-by-section walkthrough.** Instead of writing all sections
> in one pass, you can co-write them with the user via the songwriter agent's **GUIDED /
> COLLABORATIVE MODE** (triggers: "write with me", "guide me", "step through the lyrics", "section by
> section", "help me write it"). It walks the same Nashville order below and, for EACH section:
> (1) proposes a draft, (2) self-flags concerns against `core/methodology/critique.md`'s 12-category
> rubric — surfacing the section-relevant subset first — then (3) WAITS for the user to confirm or
> override before the next section. The authoritative per-section emphasis mapping lives in the
> **songwriter** agent's GUIDED / COLLABORATIVE MODE (`.kiro/agents/songwriter.md`), which references
> `core/methodology/critique.md`'s categories 1-12; it is intentionally NOT re-listed here to avoid
> drift. This is an interaction mode only; the craft steps below are unchanged.

**Step 10 — Write the Chorus FIRST**
This is your destination. Write it before anything else.
- Must contain the hook (identify your hook TYPE first: lyric/title, melodic, rhythmic, or instrumental/production)
- If lyric hook: it must be in the chorus lyrics
- If melodic/production hook: the chorus must still contain the emotional peak
- Must be singable (test: can you hum it?)
- Target 7-12 syllables per line [Tier 2]
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
- Target 7-12 syllables per line [Tier 2]
- Use em-dashes for breath within lines

**Step 13 — Write Verse 2**
4-8 lines that ADD NEW INFORMATION. [Tier 2]
- Usually should not restate V1 (unless reiteration is part of the form -- blues, hymnal, chant)
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
- Intro: 2-4 lines max, sets mood. For instrumental intros, write a brief parenthetical description: `(sea-wash, 4 bars → concertina enters with melody)`. In the V6 Suno output, use the section tag plus event tags on their own lines: `[Intro]` / `[Instrument: Concertina In]` / `[Dynamic: Soft]` (v5.5-era equivalent, legacy: `[intro | atmospheric, warm, sparse]`)
- Outro: 2-4 lines max, resolves or fades
- Neither should introduce major new content

---

### PHASE 3: Quality Check

**Step 17 — Prosody Audit**
Go line by line:
- [ ] Lines target 7-12 syllables? 13-15 reviewed for stress density and singability at tempo? 16+ compressed or justified? [Tier 2]
- [ ] Stressed syllables on the strong beats of the meter? (square 4/4: usually beats 1 and 3; backbeat/syncopated styles: anticipations or 2 and 4; 3/4 and 6/8: the downbeat of each group; pickups carry unstressed syllables)
- [ ] Open vowels on any sustained notes?
- [ ] No stuffed phrases (3+ long words crammed)?
- [ ] Function words at line end (the, a, of, to, in, for, it, is, was) only where they're sung STRESSED ("that's the way it IS") — not unstressed on a held note?
- [ ] Enjambment used deliberately (forward motion), with real breath points kept?
- [ ] Run `python3 tools/lyric-lint.py <file>` (syllables, stress, rhyme type, rhyme scheme, section stability, clichés)

**Step 18 — Structure Check**
- [ ] Hook signal within ~5-30 s of the first SUNG word (genre-dependent)? [Tier 2]
- [ ] V2 adds genuinely new information?
- [ ] Bridge contains a real turn?
- [ ] Total lyrics estimatable under 5000 chars?
- [ ] Target runtime appropriate for platform?

**Step 19 — Quality Gates**
- [ ] Every word earns its place (no filler)?
- [ ] No clichés (unless subverted)?
- [ ] Hook passes "would someone text this?" test?
- [ ] Rhyme strength fits the job — perfect/family where you want closure (title lines, chorus resolutions), looser rhymes where you want motion — and no syntax bent for a rhyme?
- [ ] Each section's stability (line count, line length, rhyme closure) matches the rhyme & stability plan from Step 4?

---

### PHASE 4: Formatting (Suno-Ready Output — V6 default)

> V6 is the default format (Style = the WHAT, Lyrics = the HOW). Full rules: `.kiro/steering/suno-formatting.md` and
> `core/methodology/suno-optimization.md` → V6 Procedure. v5.5-era mechanics are noted as legacy below.

**Step 20 — Assemble Style Prompt (the WHAT)**
Write comma-separated descriptors, genre first: Genre, Key, BPM, Mood, Instruments (as sound descriptors, not gear model names), Vocal identity, Production aesthetic / space. No artist names.
- Check: ≤1000 characters?

**Step 21 — Write Exclusions**
Plain comma-separated text, no dash prefix, under an `## EXCLUSIONS:` section in the song file:
```
trap drums, beatboxing, vocal hums, bright synths
```
Paste into Suno's dedicated Exclude field (NOT in Style or Lyrics).

**Step 22 — Add the Title Tag (no global tags on V6)**
At the top of the Lyrics field: `[Title: Song Title]`. V6 uses no global tags and no `[Tag Vocabulary]` block.

*v5.5-era (legacy — re-validate on V6):* v5.5 renders used global tags at the top of the Lyrics field — `[track: genre: X, mood: X, length: XXX]`, `[control: no-repeat, dynamic transitions]`, `[sequence: ...]` — with `length` taken from the Step 8 runtime estimate in seconds.

**Step 23 — Add Direction Blocks**
```
[Production Direction: ...]
[Vocal Direction: ...]
```

**Step 24 — Format Lyrics with Section Tags (the HOW)**
- Section tags on their own lines (`[Verse 1]`, `[Chorus]`, `[Bridge]`, …)
- Choreograph the arrangement with `[Instrument: X In]` / `[Instrument: X Out]`
- Add `[Dynamic: ...]`, `[Vocal: ...]` (or `[Male lead, inline adjective]`), `[Transition: ...]`, `[Key Change: ...]` at key moments — 2-4 tags per section
- No pipe notation, no v5.5 global tags
- End with `[End]` (v5.5-era: `[end]`)

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

**Step 26 — Final Character Count + Validation**
- Style Prompt: ___/1000
- Lyrics field: ___/5000
- If over: trim (don't overflow — there's no overflow box)
- Run `python3 tools/validate-song.py <file>` (deterministic char counts, required elements, V6 tag checks, exclusions format) and `python3 tools/lyric-lint.py <file>`

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
6. (Optional) Creative slider recommendations — only if your Suno UI exposes sliders; values are v5.5-era starting points

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
| V2 restates V1 | [Tier 2] Ask "what's NEW?" -- different angle, deeper, progression (unless reiteration is part of form) |
| Bridge restates chorus | [Tier 2] The bridge often works best when it reveals something the chorus hasn't said |
| Lines of 13+ syllables | [Tier 2] 13-15: check stress density and singability at tempo; 16+: apply the Compression Test (split/trim, or justify as intentional) |
| Hook signal later than ~30 s after the first sung word (for a pop target) | Shorten V1 or move the hook earlier (cinematic/progressive forms may justify more setup) |
| Rhyme forcing meaning or syntax | Drop to a looser rhyme (family, assonance) or restructure the line — never bend syntax for a rhyme |
