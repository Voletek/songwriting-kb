# SOP 05: Extending an Album

> Step-by-step procedure for safely adding new tracks to an existing album.
> Prevents continuity errors from undocumented extensions.

> **Note:** The canonical methodology for this workflow now lives in `core/methodology/album-continuity.md`.
> This SOP is retained for Kiro-specific step formatting but the methodology file is the authoritative source.
> If content diverges, `core/methodology/` wins.

---

## Prerequisites

- A completed Album Bible for the existing tracks
- The new concept/story material that justifies extension
- Clear understanding of WHERE the new tracks fit (sequel act? inserted? appendix?)

---

## Procedure

### Step 1 — STOP. Ask: Should This Be a New Album?

Before extending, ask:
- Does the new material continue the SAME character arc?
- Does it share the same album thesis?
- Will the sonic palette evolution make sense with additional tracks?
- Is there a narrative reason these belong TOGETHER vs separately?

**If NO to 2+ questions:** Start a new album (go to SOP 04).
**If YES:** Continue below.

### Step 2 — Define the Extension Scope

Document:
```
Extension: Act [X] — Tracks [XX-XX]
Reason: [why the story continues]
Position: [sequel / prequel / inserted between / parallel]
New track count: [X]
```

**Numbering convention by position:**
- **Sequel (after existing tracks):** Continue sequential numbering (T9, T10, T11...)
- **Prequel (before existing tracks):** Use prefix numbering (P01, P02, P03) to avoid renumbering existing tracks and invalidating number-based rules
- **Inserted between:** Use decimal notation (T3a, T3b) or renumber with act headers
- **Parallel (same timeline, different POV):** Use prefix (S01 for "side" or character-initial)

**Why not renumber?** Existing rules, motif tables, and cross-references all use track numbers. Renumbering creates cascading updates and risks missed references. Prefix numbering preserves all existing documentation.

### Step 3 — Update the Track Registry

Add new rows to the Album Bible's track table:
```
| # | Working Title | Key | BPM | Core Emotion | Sonic Palette |
|---|---|---|---|---|---|
| [new] | [title] | [key] | [bpm] | [emotion] | [palette] |
```

**Verify:**
- [ ] No key duplicates without intentional reason
- [ ] BPM varies from adjacent tracks
- [ ] Emotions progress (don't repeat)
- [ ] Sonic palette follows the evolution map

### Step 4 — Extend the Sonic Palette Map

Add the new range to the evolution:
```
[For sequels:]
Existing Tracks 1-8: [existing palette evolution]
New Tracks 9-XX: [what the palette does now — continues? transforms? returns?]

[For prequels:]
Prequel (P1-P3): [ancient/primitive palette description]
Existing (T1-T8): [existing palette — unchanged]
Note: The prequel's final track must sonically ARRIVE at T1's established palette.
The listener should feel "transition" between the prequel's end and the original album's start.
```

**Rule 11 check:** Does any new track share >70% palette with an existing track? If yes, document the differentiation.

**Prequel palette principle:** The prequel's sonic evolution should LEAD TO the existing T1's sound. The audience's journey is: unfamiliar → recognizable. The final prequel track is the sonic bridge.

### Step 5 — Review Existing Rules

For each Hard Rule, answer:
- Does this rule still apply to the new tracks? (Y/N)
- Does it need modification? (If yes, what?)
- Are new rules needed for the extension?

**⚠️ Number-reference check:** If any rule references a track NUMBER (e.g., "Track 3," "T1 and T8 only"), determine whether it means:
- The track CONTENT (the specific song, regardless of position) — most common
- The track POSITION (first, third, last in the running order)

For resilience, update number-referenced rules to include track TITLES alongside numbers: "D Mixolydian = T1 (The Keeper's Morning) and T8 (Lullaby for Leviathan) ONLY." This prevents ambiguity when new tracks are added before or between existing ones.

Document:
```
Rules carrying forward: [list numbers]
Rules that are act-specific (no longer apply): [list numbers]
Rules with number-references clarified: [list numbers + title additions]
New rules for Act X: [list new rules]
```

### Step 6 — Update Character Voice Registry

For returning characters:
- How has their voice EVOLVED since last appearance?
- What new vocal texture distinguishes this act?

For new characters:
- Fill out full Character Voice Template (use SOP 06, Step 6 for the template format)
- Specify which tracks they appear in
- Define their production treatment

### Step 7 — Plan New Motifs + Existing Motif Fate

**For SEQUELS — existing motifs:**
- Which continue into the new act?
- Which have completed their arc (don't use again)?
- Which transform into something new?

**For PREQUELS — existing motifs (reverse logic):**
- Which existing motifs can be SEEDED here (their origin point in the story)?
- Which must be ABSENT (they don't exist yet in the story timeline)?
- Which can appear as DRAMATIC IRONY (audience knows the future significance, characters don't)?

**New motifs (all extension types):**
- What new recurring elements are introduced?
- Where do they first appear?
- How do they evolve across the new tracks?
- For prequels: do any new prequel motifs BECOME existing motifs (showing their origin)?

### Step 8 — Verify Key Relationships

Map the new keys against the existing harmonic architecture:
- Do the new keys create meaningful relationships to the old ones?
- If the album had a key change (e.g., T17 Am→C), does the extension respect that resolution or deliberately depart from it?
- Are there harmonic callbacks that strengthen cross-act continuity?

**For prequels specifically:** The final prequel track's key should create natural harmonic gravity toward the existing T1's key — the listener should feel "arrival" when the original album begins. Consider dominant→tonic relationships, or relative major/minor pairings that resolve into T1.

**For sequels:** The first new track's key should either continue the harmonic trajectory or deliberately break it (if the extension represents a new phase).

### Step 9 — Update the Album Bible

Open `references/[ALBUM]_BIBLE.md` and update:
- [ ] Track Registry (new rows)
- [ ] Sonic Palette Evolution (extended)
- [ ] Key Relationships (new entries)
- [ ] Rules (reviewed, new ones added)
- [ ] Character Voice Registry (evolved/new)
- [ ] Motifs (status updated, new ones added)
- [ ] Emotional Arc (extended)
- [ ] Extension Protocol (note that this extension happened)

### Step 10 — Update Steering File

Open `.kiro/steering/[album].md` and update:
- [ ] Track count
- [ ] Rules (if changed)
- [ ] Palette table (extended)
- [ ] Character voices (if new ones)
- [ ] Verify all number-referenced rules still have correct numbers (or add title disambiguation)

### Step 11 — Commit BEFORE Writing

**Commit all bible/steering updates to version control BEFORE writing any new songs.**

This ensures:
- The documentation is the source of truth
- The hooks can check against updated rules
- Anyone else working on the album has the current state
- If songs violate rules, the rules existed first (not retrofitted)

### Step 12 — Write New Tracks

NOW proceed to SOP 01 (Writing a Song) for each new track, with the updated bible available.

**Note:** This SOP is the expanded procedure referenced by "Album Extension Protocol" sections in album bibles. If your bible has an extension protocol checklist, this SOP fulfills and supersedes those steps.

---

## Common Extension Mistakes

| Mistake | Consequence | Prevention |
|---|---|---|
| Writing songs before updating bible | Continuity violations discovered too late | Step 11: commit documentation FIRST |
| Keeping all old rules unchanged | New context may need different constraints | Step 5: review each rule explicitly |
| Same sonic palette as earlier tracks | Album sounds repetitive, no progression | Step 4 + Rule 11: differentiate |
| Ignoring motif completion | Motifs that were "resolved" get resurrected cheaply | Step 7: check motif status |
| Not evolving character voices | Characters sound static across acts | Step 6: mandate evolution |
| Number-referenced rules not updated | Rules become ambiguous after renumbering | Step 5: add title disambiguation |
| Prequel uses motifs that don't exist yet | Breaks story-timeline logic | Step 7: prequel motif check |
| Renumbering existing tracks | Cascading documentation invalidation | Step 2: use prefix numbering instead |

---

## Time Estimate: 1-2 hours (documentation updates before writing begins)
