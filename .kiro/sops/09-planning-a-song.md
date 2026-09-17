# SOP 09: Planning a Song

> Guided procedure for producing an approvable **Song Brief** BEFORE any lyrics are written.

> **Note:** The canonical methodology for this workflow lives in `core/methodology/song-planning.md`.
> This SOP is retained for Kiro-specific step formatting, but the methodology file is the
> authoritative source. If content diverges, `core/methodology/` wins. Craft rules referenced here
> (prosody thresholds, hook timing, V2-new-info, bridge turn, Fabbri's 5 rules, the 70/30 rule,
> key-emotion mapping, BPM-emotion, Hit Formula F1/F2, the 12-category rubric) are defined in
> `core/methodology/songwriting.md` and `core/methodology/critique.md` -- this SOP references them,
> it does not restate them.

---

## Prerequisites

- A concept, theme, or prompt (even a single sentence works)
- Know your target: standalone single, album track, or experimental piece
- If album track: have the album blueprint and the adjacent tracks available

---

## Procedure

Run in **GUIDED MODE** (the default): for each brief section, present a methodology-backed
suggested default with one line of reasoning, then prompt the user to confirm or override before
moving to the next section. If the user asks for AUTO-PILOT ("surprise me", "you choose", "just
go", etc.), apply defaults across all sections in one pass and let them override afterward.

### Walk the 12 Brief Sections (suggest default -> confirm -> next)

**Step 1 -- Song Thesis.** Suggest one sentence capturing the core truth. Confirm/override. (No
thesis = a topic, not a song. See `core/methodology/songwriting.md`.)

**Step 2 -- Semantic Analysis.** Suggest subject, characters, setting, objects, actions. Confirm.
(See `core/methodology/songwriting.md` Step 2.)

**Step 3 -- Emotional Analysis.** Suggest the central affect, 2-3 BRECVEMA mechanisms, and the
start -> through -> arrive journey. Confirm. (See `core/methodology/songwriting.md` Step 3.)

**Step 4 -- Narrative Arc + The Turn.** Suggest the arc type and where the Turn is / what the
bridge reveals. Confirm. (Bridge-turn defined in `core/methodology/songwriting.md` Step 5/14.)

**Step 5 -- Voice / Accent.** Suggest register, dialect, and emotional state start vs end.
Confirm. (Character-driven? See `core/methodology/character-voice.md`.)

**Step 6 -- Genre Mapping.** Suggest primary genre, the 70/30 split (if fusion), a Fabbri 5-rules
check, and the instrument palette. Confirm. (Rules defined in `core/methodology/songwriting.md`
Step 7 and `references/SUNO_STYLE_GENRE_REFERENCE.md`.)

**Step 7 -- Key + BPM + Time Signature.** Suggest each with one-line reasoning drawn from Key
Selection and BPM-Emotion frameworks. Confirm. (See `SONGWRITING_KNOWLEDGE_BASE.md` and
`references/SUNO_STYLE_GENRE_REFERENCE.md`.)

**Step 8 -- Arrangement / Dynamics Sketch.** Suggest growth pattern, negative space, contrast
pairs, and where the hook lands. Confirm. (Hook timing defined in `core/methodology/songwriting.md`
Step 8.)

**Step 9 -- Structure Map + V6 Mode Label.** Suggest the section sequence and the mode label --
**Default/Roots** or **MODE C (Cinematic/Theatrical/Concept)**. Confirm. (Cite
`references/V6_TAG_DISCOVERY.md`.)

**Step 10 -- Hook Approach.** Suggest the hook type and a candidate hook line (a target phrase, not
finished lyrics). Confirm. (Hook types in `SONGWRITING_KNOWLEDGE_BASE.md`.)

**Step 11 -- Production / Commercial.** Suggest target audience, length, platform, solo/duet, and
standalone/album. Confirm. For album tracks, run the LIGHT continuity pre-check and prompt for
blueprint + adjacent tracks; point to the album-continuity agent for the full check. (Hit Formula
framing in `core/methodology/songwriting.md`.)

**Step 12 -- Open Questions / Decisions for the User.** List anything still open, defaulted but
unconfirmed, or deferred to writing.

### Candidate Style Prompt (optional, flexible template)

Offer a Candidate Style Prompt as a per-value template -- genre + 70/30 split, BPM (with Italian
tempo marking), key, vocal identity/range, production feel, mood, exclusions -- a suggested default
per value the user confirms or overrides. Output a filled-but-editable template, NOT a locked
string. (Assembly rules: `core/methodology/songwriting.md` Step 20.)

### Close: Stop or Flow

Ask the user: STOP at the brief (deliver and save it), or FLOW into writing (hand the approved
brief to the songwriter and begin Phase 2 of `core/methodology/songwriting.md`). Save the brief
either way.

---

## Song Brief Output Template

Fill this skeleton. Keep it CONCEPTUAL -- no verse lyrics anywhere.

```markdown
# [Song Title] -- Song Brief

> Status: [Draft | Approved]  |  Target: [Standalone | Album: <name>, track <n>]

## 1. Song Thesis
[One sentence -- the core truth this song expresses.]

## 2. Semantic Analysis
- Subject:
- Characters:
- Setting:
- Objects:
- Actions:

## 3. Emotional Analysis
- Central affect:
- BRECVEMA mechanisms (2-3):
- Journey (start -> through -> arrive):

## 4. Narrative Arc + The Turn
- Arc type:
- Where the Turn is / what the bridge reveals:

## 5. Voice / Accent
- Register:
- Dialect / accent:
- Emotional state (start vs end):

## 6. Genre Mapping
- Primary genre (70%):
- Texture genre (30%, if fusion):
- Fabbri 5-rules check:
- Instrument palette:

## 7. Key + BPM + Time Signature
- Key ( reasoning ):
- BPM ( reasoning ):
- Time signature ( reasoning ):

## 8. Arrangement / Dynamics Sketch
- Growth pattern:
- Negative space:
- Contrast pairs:
- Hook placement:

## 9. Structure Map + V6 Mode Label
- Section sequence:
- V6 mode label: [Default/Roots | MODE C (Cinematic/Theatrical/Concept)]

## 10. Hook Approach
- Hook type:
- Candidate hook line (conceptual target):

## 11. Production / Commercial
- Target audience:
- Target length:
- Platform:
- Solo / duet:
- Standalone / album ( + position ):

## 12. Open Questions / Decisions for the User
- [ ] ...
```

---

## Brief File Location Convention

Save the brief in the SAME folder as the eventual song file, using the pattern `SONGNAME.brief.md`
(next to `SONGNAME.md`). Examples:

- User work: `songs/My_Song.brief.md` (next to `songs/My_Song.md`)
- Example: `examples/songs/standalones/Three_In_The_Morning.brief.md` (next to
  `examples/songs/standalones/Three_In_The_Morning.md`)

---

## Output

A completed, user-approved **Song Brief** file (`SONGNAME.brief.md`) with all 12 conceptual
sections filled, saved next to the eventual song. Optionally, a Candidate Style Prompt template.
No verse lyrics.

---

## Time Estimate

| Step | Time |
|---|---|
| Guided walkthrough of the 12 sections | 15-25 min |
| Candidate Style Prompt (per-value confirm) | 5-10 min |
| Album pre-check (album tracks only) | 5 min |
| **Total** | **20-40 min** |
