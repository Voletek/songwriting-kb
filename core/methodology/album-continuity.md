# The Album Continuity Method

> **CANONICAL METHODOLOGY** -- This file is the single source of truth for concept album management.
> A non-Kiro user can read ONLY this file and set up a new album from scratch OR safely extend
> an existing album without breaking continuity.

---

## Overview

The album continuity system has two major workflows:

1. **Album Setup** -- Creating all documentation BEFORE writing any songs (5 phases, 12 steps)
2. **Album Extension** -- Safely adding new tracks to an existing album (12 steps)

Plus a **Continuity Verification Workflow** that runs on every track to catch errors before they become permanent.

---

## Part 1: Setting Up a Concept Album

### Prerequisites

- A story, theme, or concept that spans multiple songs
- A rough sense of how many tracks (8-17 is the sweet spot)
- Know your protagonist/speaker(s)

---

### PHASE 1: The Concept

#### Step 1 -- Write the Album Thesis

One sentence that captures the entire album's journey:

```
Album Thesis: "[The transformation this album tracks, in one sentence]"
```

Examples:
- "A man dissolves into his digital world and must rebuild himself from code and courage"
- "Grief does not end -- it transforms into something you can carry"
- "The monster under the bed was always just a frightened child"

#### Step 2 -- Define the Emotional Arc

Map the full journey in phases. Scale by album length:
- 8-10 tracks: 3-4 phases
- 12-17 tracks: 5-7 phases
- 17+ tracks: 7-9 phases (consider splitting into acts)

```
Phase 1 (Tracks 1-X): [emotional territory]
Phase 2 (Tracks X-X): [emotional territory]
Phase 3 (Tracks X-X): [emotional territory]
Final Track: [resolution/arrival point]
```

#### Step 3 -- Define the Sonic Evolution

How should the SOUND transform across the album?

```
Tracks 1-X:  [palette description -- instruments, textures, production style]
Tracks X-X:  [transition / pivot]
Tracks X-X:  [new palette]
Final Track: [sonic destination]
```

**Rule:** The sonic palette should MIRROR the emotional arc. If the character moves from trapped to free, the sound should move from claustrophobic to expansive.

---

### PHASE 2: The Track Registry

#### Step 4 -- Plan the Track List

Create a table with ALL planned tracks:

```
| # | Working Title | Key | BPM | Core Emotion | Sonic Palette |
|---|---|---|---|---|---|
| 01 | [title] | [key] | [bpm] | [emotion] | [instruments/texture] |
| 02 | [title] | [key] | [bpm] | [emotion] | [instruments/texture] |
```

**Guidelines:**
- Keys should relate to each other (see Step 5)
- BPM should vary (no three songs at same BPM in a row)
- Emotions should escalate, not repeat
- Adjacent tracks should contrast sonically

#### Step 5 -- Map Key Relationships

Plan how keys connect:
- Same key = related emotional territory (intentional callback)
- Relative major/minor = resolution potential (Am to C = hope)
- Tritone apart = maximum contrast/conflict
- Step up = energy lift
- Step down = weight/gravity

Document:
```
Key Map:
T1 [key] -- reasoning
T2 [key] -- relationship to T1
...
Final Track [key] -- how it resolves the harmonic journey
```

**Decisions to make:**
- Will there be a key change within a song? (Recommend one only, at climactic moment)
- Will there be a major key? (If yes: where? Make it EARNED through preceding minor material)
- Are any keys "reserved" for specific characters/emotions?

---

### PHASE 3: Rules & Constraints

#### Step 6 -- Write Your Hard Rules

These are the laws your album will never break. Aim for 8-12 rules.

**Categories to cover:**

| Category | Example Rules |
|---|---|
| Sonic boundaries | "No [instrument] after Track X" / "Only acoustic after the pivot" |
| Key/harmonic | "Only one key change" / "Major key only in Track X" |
| Phrase protection | "[Specific phrase] appears ONLY in Track X" |
| Character voice | "[Character] voice only appears in Tracks X and Y" |
| Motif rules | "[Motif] appears in T1-T5 then is absorbed" |
| Structural | "First [element] appears in Track X" |
| Vocal evolution | "Speaker's voice texture must change every track" |
| Palette enforcement | "No two tracks may share >70% instrument palette" |

Write each rule clearly:
```
1. [Rule] -- [reasoning]
2. [Rule] -- [reasoning]
...
```

#### Step 7 -- Define the Character Voice Registry

For each speaking/singing character:

```
CHARACTER: [Name]
- Register: [range]
- Texture: [description]
- Delivery: [how they sound]
- Appears in: [which tracks]
- Production treatment: [reverb, effects, etc.]
- Evolution: [how their voice changes across tracks]
- Rule: [any voice-specific constraints]
```

For non-vocal presences (ambient entities, environmental forces): adapt the template to describe sonic MANIFESTATION rather than vocal performance. See `core/methodology/character-voice.md` for the full voice design procedure.

---

### PHASE 4: Motifs & Continuity

#### Step 8 -- Plan Recurring Motifs

Document every motif that will thread across songs:

```
| Motif | Type | First Appearance | Recurrences | Meaning | Evolution |
|---|---|---|---|---|---|
| [name] | musical/lyric/production/timbral | Track X | Tracks X, X, X | [what it signifies] | [how it changes] |
```

**Types of motifs:**
- **Lyric motif** -- a recurring phrase/line
- **Musical motif** -- a recurring melodic/rhythmic figure
- **Production motif** -- a recurring sound/texture (e.g., a specific reverb, a pulse)
- **Timbral motif** -- a specific instrument = a specific character/concept

**Rules for motifs:**
- Introduce in the first 25-30% of tracks (for 8 tracks: T1-2, for 17 tracks: T1-5)
- Recur 3-5 times across the album
- Each recurrence must EVOLVE in meaning
- Final appearance = most powerful

#### Step 9 -- Plan Callbacks & Transitions

Document how tracks connect:
```
T1 -> T2: [what carries over -- sonic, lyric, thematic]
T2 -> T3: [transition element]
...
```

Also document cross-album callbacks:
```
T7 references T1 by: [what and how]
Final Track resolves: [which earlier threads]
```

---

### PHASE 5: Documentation

#### Step 10 -- Assemble the Album Blueprint

Create `references/[YOUR_ALBUM]_BLUEPRINT.md` (or fill in the template `references/YOUR_ALBUM_BLUEPRINT.md`) containing the sections below. Completed examples: `examples/albums/fractured-shadows/BLUEPRINT.md` and `examples/albums/keeper-of-the-light/BLUEPRINT.md`.

1. Album Thesis
2. Track Registry (full table)
3. Sonic Palette Evolution map
4. Key Relationships / Harmonic Map
5. Hard Rules (all numbered)
6. Character Voice Registry
7. Recurring Motifs table
8. Callbacks/Transitions plan
9. Emotional Arc (full album)
10. Versioning Opportunities per track (alternative mixes, sync edits, acoustic versions)
11. Extension Protocol (safety checklist for future additions)

#### Step 11 -- Create Your Steering File

Create a condensed version of the blueprint for quick reference (Kiro: `.kiro/steering/<your-album>.md` with `inclusion: fileMatch` and a `fileMatchPattern` for your album's song folder; examples in `examples/albums/<album>/steering.md`), containing:
- Album title + track count
- Extension protocol reminder
- Hard rules (all numbered, scannable)
- Sonic palette by track range (table format)
- Character voices (quick reference, 1-2 lines each)
- Key motifs to track (name + which tracks)

#### Step 12 -- Configure Hooks (Optional)

Define what rules to verify when a song file is saved:
- Sonic palette violations (forbidden instruments per track range)
- Phrase protections (protected phrases and which tracks own them)
- Key/structural rules (key reservations, BPM locks, voice restrictions)

**Kiro:** hooks are v1 JSON files in `.kiro/hooks/`. Copy `examples/albums/<album>/continuity-hook.json` to `.kiro/hooks/<album>-continuity.json`, set its `matcher` (regex on the file path) to your album's song folder, and list your rules in the `agent` action's prompt. File-event hooks fire only for agent-made file changes and run in Kiro IDE 1.0+ / Kiro CLI V3 (not Kiro Web). **Without Kiro:** use the rule list as a manual review checklist.

**Commit all documentation BEFORE writing any songs.** The documentation is the source of truth.

---

## Part 2: The Extension Protocol (Adding Tracks Safely)

### Pre-Extension Gate

Before extending, ask:
- Does the new material continue the SAME character arc?
- Does it share the same album thesis?
- Will the sonic palette evolution make sense?
- Is there a narrative reason these belong TOGETHER?

**If NO to 2+ questions:** Start a new album. **If YES:** Continue.

---

### Step 1 -- Define the Extension Scope

```
Extension: Act [X] -- Tracks [XX-XX]
Reason: [why the story continues]
Position: [sequel / prequel / inserted between / parallel]
New track count: [X]
```

### Step 2 -- Choose Numbering Convention

| Position | Convention | Rationale |
|---|---|---|
| Sequel (after existing) | Continue sequential (T9, T10...) | Natural extension |
| Prequel (before existing) | Prefix numbering (P01, P02...) | Avoids renumbering existing tracks |
| Inserted between | Decimal (T3a, T3b) or act headers | Preserves existing numbering |
| Parallel (same timeline, different POV) | Prefix (S01 for "side" or character-initial) | Avoids collisions |

**Never renumber existing tracks.** Existing rules, motif tables, and cross-references all use track numbers. Renumbering creates cascading documentation invalidation.

### Step 3 -- Update the Track Registry

Add new rows to the Album Blueprint's track table. Verify:
- No key duplicates without intentional reason
- BPM varies from adjacent tracks
- Emotions progress (do not repeat)
- Sonic palette follows the evolution map

### Step 4 -- Extend the Sonic Palette Map

Add the new range to the evolution. For sequels: what does the palette do now? For prequels: the final prequel track must sonically ARRIVE at T1's established palette.

**Rule 11 check:** Does any new track share >70% palette with an existing track? If yes, document the differentiation.

### Step 5 -- Review Existing Rules

For each Hard Rule, answer:
- Does this rule still apply to new tracks? (Y/N)
- Does it need modification?
- Are new rules needed for the extension?

**Number-reference check:** If any rule references a track NUMBER, add track TITLES alongside numbers for disambiguation: "D Mixolydian = T1 (The Keeper's Morning) and T8 (Lullaby for Leviathan) ONLY."

### Step 6 -- Update Character Voice Registry

For returning characters: How has their voice EVOLVED? What new vocal texture distinguishes this act?

For new characters: Fill out full Character Voice Template (see `core/methodology/character-voice.md`).

### Step 7 -- Plan New Motifs + Existing Motif Fate

**For sequels -- existing motifs:**
- Which continue into the new act?
- Which have completed their arc (do not use again)?
- Which transform into something new?

**For prequels -- reverse logic:**
- Which existing motifs can be SEEDED here (their origin point)?
- Which must be ABSENT (they do not exist yet in the timeline)?
- Which can appear as DRAMATIC IRONY?

**New motifs (all extension types):**
- What new recurring elements are introduced?
- Where do they first appear?
- How do they evolve across the new tracks?

### Step 8 -- Verify Key Relationships

Map new keys against existing harmonic architecture:
- Do new keys create meaningful relationships to old ones?
- For prequels: final prequel track's key should create harmonic gravity toward T1
- For sequels: first new track's key should continue OR deliberately break the trajectory

### Step 9 -- Update the Album Blueprint

Update all sections: Track Registry, Sonic Palette, Key Relationships, Rules, Character Voices, Motifs, Emotional Arc, Extension Protocol.

### Step 10 -- Update Steering File

Update: track count, rules (if changed), palette table, character voices (if new).

### Step 11 -- Commit BEFORE Writing

**Commit all documentation updates BEFORE writing any new songs.** This ensures the documentation is the source of truth, not a retrofit.

### Step 12 -- Write New Tracks

NOW proceed to songwriting (see `core/methodology/songwriting.md`) for each new track, with the updated blueprint available.

---

## The Continuity Verification Workflow (8 Checks)

Run this on every album track (new or edited):

| # | Check | What to Verify | Result |
|---|---|---|---|
| 1 | **Track Position** | What number is this? Where does it sit in the arc? | Document position |
| 2 | **Hard Rules** | Verify against ALL documented rules | PASS / VIOLATION |
| 3 | **Sonic Palette** | Are instruments/textures legal for this track range? | PASS / VIOLATION |
| 4 | **Motif Usage** | Are recurring motifs used correctly? Meaning evolved? | CORRECT / ISSUE |
| 5 | **Character Voice** | Does the vocal match the registry? | PASS / MISMATCH |
| 6 | **Key Relationship** | Does this key make sense in the harmonic map? | PASS / CONFLICT |
| 7 | **Callback Verification** | Any cross-track references? Are they accurate? | CORRECT / ERROR |
| 8 | **Emotional Arc** | Does this track's emotion fit its position? | PASS / MISMATCH |

**Output format for verification:**
```
## CONTINUITY REPORT: Track XX -- [Title]

### Hard Rules Check
| Rule | Status | Notes |
|---|---|---|
| [Rule description] | PASS/VIOLATION | ... |

### Sonic Palette: PASS/VIOLATION
### Motif Usage: CORRECT/ISSUE
### Character Voices: PASS/MISMATCH
### Key Relationship: PASS/CONFLICT
### Callbacks: CORRECT/ERROR
### Emotional Arc Position: PASS/MISMATCH

### VERDICT: PASS / FAIL (X violations)
```

---

## Universal Album Rules

These apply to ANY concept album regardless of genre:

1. **No two adjacent tracks should share >70% instrument palette** -- sonic differentiation is mandatory
2. **Recurring phrases must evolve in meaning** -- same words, different weight each time
3. **Character voices must be consistent** -- same production treatment for the same character across tracks
4. **The sonic pivot (if present) must be clean** -- no bleed between sonic worlds
5. **Reserved keys/modes should be protected** -- if a key belongs to a character or moment, do not borrow it elsewhere
6. **Named parenthetical layers must be confined to their declared tracks** -- no voice leakage

---

## Common Extension Mistakes

| Mistake | Consequence | Prevention |
|---|---|---|
| Writing songs before updating blueprint | Continuity violations discovered too late | Commit documentation FIRST |
| Keeping all old rules unchanged | New context may need different constraints | Review each rule explicitly |
| Same sonic palette as earlier tracks | Album sounds repetitive | Rule 11 + palette differentiation |
| Ignoring motif completion | Resolved motifs get resurrected cheaply | Check motif status before reuse |
| Not evolving character voices | Characters sound static across acts | Mandate evolution per act |
| Number-referenced rules not updated | Rules become ambiguous after changes | Add title disambiguation |
| Prequel uses motifs that don't exist yet | Breaks story-timeline logic | Prequel motif check |
| Renumbering existing tracks | Cascading documentation invalidation | Use prefix numbering instead |
| No transition consciousness | Tracks just stop without gravity toward next | Plan endings that pull forward |
| Over-documenting before writing | Creativity stifled | 80% planning, 20% discovery |

---

## Output Formats

### Album Blueprint Sections

The Album Blueprint (`references/[ALBUM]_BLUEPRINT.md`; bundled examples in `examples/albums/<album>/BLUEPRINT.md`) contains these sections:
1. Album Thesis
2. Track Registry (table)
3. Sonic Palette Evolution
4. Key Relationships / Harmonic Map
5. Hard Rules (numbered)
6. Character Voice Registry
7. Recurring Motifs (table)
8. Callbacks/Transitions
9. Emotional Arc
10. Versioning Opportunities
11. Extension Protocol

### Continuity Report Format

Save to: `analysis/[album-prefix]_[song-filename]_continuity.md`

---

## Time Estimates

| Task | Time |
|---|---|
| Full album setup (Steps 1-12) | 2.5-3.5 hours |
| Extension documentation (Steps 1-11) | 1-2 hours |
| Per-track continuity verification | 10-15 minutes |

---

## Theoretical Foundation

| Principle | Source |
|---|---|
| Sonic palette as narrative | Film scoring tradition -- timbre carries meaning across scenes |
| Key relationships as emotional architecture | Classical sonata form -- tonal relationships create expectation |
| Motif evolution | Wagnerian leitmotif -- recurring themes gain meaning through context |
| Proxemic arc across album | Lacasse -- vocal distance tells its own spatial story |
| Genre coherence with variation | Fabbri -- genre rules apply at album level, not just track level |
| Contrast and pacing | Sequencing craft (DJ/mastering tradition) -- energy management |

---

## References

- `references/YOUR_ALBUM_BLUEPRINT.md` -- Template for album blueprint structure
- `examples/albums/fractured-shadows/BLUEPRINT.md` -- Complete example album blueprint (17 tracks in Acts 1-2 + Act 3 in progress)
- `examples/albums/keeper-of-the-light/BLUEPRINT.md` -- Complete example album blueprint (8 tracks)
- `examples/albums/<album>/steering.md` and `examples/albums/<album>/continuity-hook.json` -- Example conditional steering and continuity hook
- `core/methodology/character-voice.md` -- Full character voice design procedure
- `core/methodology/songwriting.md` -- Song creation procedure (use after album is documented)
