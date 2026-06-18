# SOP 04: Setting Up a Concept Album

> Step-by-step procedure for planning a multi-track concept album from scratch.
> Creates all documentation needed BEFORE writing any songs.

> **Note:** The canonical methodology for this workflow now lives in `core/methodology/album-continuity.md`.
> This SOP is retained for Kiro-specific step formatting but the methodology file is the authoritative source.
> If content diverges, `core/methodology/` wins.

---

## Prerequisites

- A story, theme, or concept that spans multiple songs
- A rough sense of how many tracks (8-17 is the sweet spot)
- Know your protagonist/speaker(s)

---

## Procedure

### PHASE 1: The Concept

**Step 1 — Write the Album Thesis**
One sentence that captures the entire album's journey:
```
Album Thesis: "[The transformation this album tracks, in one sentence]"
```

Examples:
- "A man dissolves into his digital world and must rebuild himself from code and courage"
- "Grief doesn't end — it transforms into something you can carry"
- "The monster under the bed was always just a frightened child"

**Step 2 — Define the Emotional Arc**
Map the full journey in phases. Scale by album length:
- 8-10 tracks: 3-4 phases
- 12-17 tracks: 5-7 phases
- 17+ tracks: 7-9 phases (consider splitting into acts)
```
Phase 1 (Tracks 1-X): [emotional territory]
Phase 2 (Tracks X-X): [emotional territory]
Phase 3 (Tracks X-X): [emotional territory]
...
Final Track: [resolution/arrival point]
```

**Step 3 — Define the Sonic Evolution**
How should the SOUND transform across the album?
```
Tracks 1-X:  [palette description — instruments, textures, production style]
Tracks X-X:  [transition / pivot]
Tracks X-X:  [new palette]
Final Track: [sonic destination]
```

**Rule:** The sonic palette should MIRROR the emotional arc. If the character moves from trapped → free, the sound should move from claustrophobic → expansive.

---

### PHASE 2: The Track Registry

**Step 4 — Plan the Track List**

Create a table with ALL planned tracks. Fill in keys where you're certain; mark "TBD" where you want flexibility. Aim for at least 60% of keys decided before moving on — you'll likely iterate between Steps 4 and 5.

**Note:** The per-track "Sonic Palette" column adds track-level specificity to Step 3's range-based evolution map. Step 3 = broad strokes by phase. Step 4 = individual track detail.

```
| # | Working Title | Key | BPM | Core Emotion | Sonic Palette |
|---|---|---|---|---|---|
| 01 | [title] | [key] | [bpm] | [emotion] | [instruments/texture] |
| 02 | [title] | [key] | [bpm] | [emotion] | [instruments/texture] |
| ... | | | | | |
```

**Guidelines:**
- Keys should relate to each other (see Step 5)
- BPM should vary (don't put three 80 BPM songs in a row)
- Emotions should escalate, not repeat
- Adjacent tracks should contrast sonically

**Step 5 — Map Key Relationships**

Plan how keys connect:
- Same key = related emotional territory (intentional callback)
- Relative major/minor = resolution potential (Am→C = hope)
- Tritone apart = maximum contrast/conflict
- Step up = energy lift
- Step down = weight/gravity

Document:
```
Key Map:
T1 [key] — reasoning
T2 [key] — relationship to T1
...
Final Track [key] — how it resolves the harmonic journey
```

**Decisions to make:**
- Will there be a key change within a song? (Recommended: one only, at the climactic moment — but this is a strong choice, not a law)
- Will there be a major key? (If yes: where? Make it EARNED through preceding minor material)
- Are any keys "reserved" for specific characters/emotions?
- It's okay to focus on KEY relationships (T1↔final track, crisis track↔resolution) rather than exhaustively mapping every adjacent pair

**Theory help:** If modes/intervals/tritones are unfamiliar, see `MUSIC_PRODUCTION_THEORY.md` section on Harmonic Language (§9) for scale/mode reference.

---

### PHASE 3: Rules & Constraints

**Step 6 — Write Your Hard Rules**

These are the laws your album will never break. Aim for 8-12 rules.

**Categories to consider:**

| Category | Example Rules |
|---|---|
| **Sonic boundaries** | "No [instrument] after Track X" / "Only acoustic after the pivot" |
| **Key/harmonic** | "Only one key change" / "Major key only in Track X" |
| **Phrase protection** | "[Specific phrase] appears ONLY in Track X" |
| **Character voice** | "[Character] voice only appears in Tracks X and Y" |
| **Motif rules** | "[Motif] appears in T1-T5 then is absorbed" |
| **Structural** | "First [element] appears in Track X" |
| **Vocal evolution** | "Speaker's voice texture must change every track" |
| **Palette enforcement** | "No two tracks may share >70% instrument palette" |

Write each rule clearly:
```
1. [Rule] — [reasoning]
2. [Rule] — [reasoning]
...
```

**Step 7 — Define the Character Voice Registry**

For each speaking/singing character (include characters defined by ABSENCE — document what they DON'T do):

**For non-vocal presences** (ambient entities, environmental forces, cosmic beings): adapt the template below to describe sonic MANIFESTATION rather than vocal performance. What instruments/textures represent them? What registers? What delivery mode replaces "singing"?

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

---

### PHASE 4: Motifs & Continuity

**Step 8 — Plan Recurring Motifs**

Document every motif that will thread across songs:

```
| Motif | Type | First Appearance | Recurrences | Meaning | Evolution |
|---|---|---|---|---|---|
| [name] | musical/lyric/production | Track X | Tracks X, X, X | [what it signifies] | [how it changes] |
```

**Types of motifs:**
- **Lyric motif** — a recurring phrase/line
- **Musical motif** — a recurring melodic/rhythmic figure
- **Production motif** — a recurring sound/texture (e.g., a specific reverb, a pulse)
- **Timbral motif** — a specific instrument = a specific character/concept

**Rules for motifs:**
- Introduce in the first 25-30% of tracks (for 8 tracks: T1-2, for 17 tracks: T1-5)
- Recur 3-5 times across the album
- Each recurrence must EVOLVE in meaning
- Final appearance = most powerful

**Step 9 — Plan Callbacks & Transitions**

Document how tracks connect:
```
T1 → T2: [what carries over — sonic, lyric, thematic]
T2 → T3: [transition element]
...
```

Also document cross-album callbacks:
```
T7 references T1 by: [what and how]
T15 references T11 by: [what and how]
Final Track resolves: [which earlier threads]
```

---

### PHASE 5: Documentation

**Step 10 — Assemble the Album Bible**

Create `references/[YOUR_ALBUM]_BIBLE.md` containing all sections below.

**See `references/FRACTURED_SHADOWS_BIBLE.md` for a completed example** — use it as your format reference for section structure, detail level, and table formats.

Sections to include:

1. Album Thesis
2. Track Registry (full table)
3. Sonic Palette Evolution map
4. Key Relationships / Harmonic Map
5. Hard Rules (all of them, numbered)
6. Character Voice Registry
7. Recurring Motifs table
8. Callbacks/Transitions plan
9. Emotional Arc (full album)
10. Versioning Opportunities per track — *Alternative mixes/edits for each track (acoustic version, instrumental for sync, extended for streaming, clip for social media). Not every track needs one — identify the 3-5 with strongest standalone potential.*
11. Extension Protocol — *A 4-6 line safety checklist for anyone who wants to add tracks later. Include: (a) update bible first, (b) extend palette map, (c) review which rules carry forward, (d) commit documentation before writing, (e) verify sonic differentiation. See SOP 05 Steps 2-3 for full detail.*

**Step 11 — Create Your Steering File**

Create `.kiro/steering/[your-album-in-kebab-case].md` (e.g., `keeper-of-the-light.md`).

This is a CONDENSED version of the bible — loaded into every session for quick reference. Contains:
- Album title + track count
- Extension protocol reminder (4-line safety warning)
- Hard rules (all of them, numbered — same as bible but more scannable)
- Sonic palette by track range (table format)
- Character voices (quick reference — 1-2 lines each)
- Key motifs to track (name + which tracks)

**Multi-album repos:** Your steering file coexists alongside others. If the repo has `concept-album.md` (for another album), just create yours with your album's name. Both load, both apply to their respective songs.

**Step 12 — Configure Hooks (Optional)**

Hooks are checklist files that define what rules to verify when a song file is saved. In Kiro IDE, they can fire automatically. Without Kiro, they serve as manual review checklists.

If using Kiro, create `.kiro/hooks/[album]-continuity-check.md` with:
- What sonic palette violations to catch (list forbidden instruments per track range)
- What phrase protections to enforce (list protected phrases and which tracks own them)
- What key/structural rules to verify on save (key reservations, BPM locks, voice restrictions)

**Format:** Use checkbox lists (`- [ ]`) with specific, scannable rules. See `.kiro/hooks/continuity-check.md` for the existing example.

**Multi-album note:** If the repo already has another album's hook, create yours alongside it. They don't conflict — each watches its own `songs/[album_name]/` directory.

---

## Output Checklist

After completing this SOP, you should have:

- [ ] Album Thesis (one sentence)
- [ ] Emotional Arc (phases mapped)
- [ ] Sonic Evolution plan
- [ ] Track Registry (complete table)
- [ ] Key Relationship map
- [ ] 8-12 Hard Rules (written and reasoned)
- [ ] Character Voice Registry (per character)
- [ ] Motif plan (with first appearance + evolution)
- [ ] Callbacks/transitions documented
- [ ] Album Bible file created
- [ ] Steering file created
- [ ] (Optional) Hook configured

---

## What NOT to Do

| Don't | Do Instead |
|---|---|
| Start writing songs before the bible exists | Complete Steps 1-12 first |
| Define all 15 tracks in detail immediately | Start with rough emotional arc, refine as you write |
| Make rules you'll want to break | Make rules that SERVE the story |
| Plan rigid key for every track upfront | Plan relationships, let specific keys emerge during writing |
| Over-document before writing anything | 80% planning, 20% discovery — leave room for the songs to surprise you |

---

## Time Estimate

| Phase | Time |
|---|---|
| Concept (Steps 1-3) | 30-60 min |
| Track Registry (Steps 4-5) | 30-45 min |
| Rules & Constraints (Steps 6-7) | 20-30 min |
| Motifs & Continuity (Steps 8-9) | 20-30 min |
| Documentation (Steps 10-12) | 30-45 min |
| **Total** | **2.5-3.5 hours** |

This is the investment that makes the WRITING phase faster and the RESULTS coherent.
