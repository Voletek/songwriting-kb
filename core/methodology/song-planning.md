# The Song Planning Method

> **CANONICAL METHODOLOGY** -- This file is the single source of truth for PLANNING a song:
> the procedure that runs BEFORE any lyrics are written, and the approvable deliverable it
> produces -- the **Song Brief**. A non-Kiro user can read ONLY this file and produce a complete,
> reviewable Song Brief.
>
> This file describes the PLANNING PROCEDURE and the DELIVERABLE. It does NOT restate craft
> definitions. Every craft rule (prosody thresholds, hook timing, V2-new-info, bridge turn,
> Fabbri's 5 rules, the 70/30 fusion rule, key-emotion mapping, BPM-emotion, Hit Formula F1/F2)
> lives in its canonical source and is pulled in BY REFERENCE only. See
> `core/methodology/songwriting.md`, `SONGWRITING_KNOWLEDGE_BASE.md`, and
> `references/SUNO_STYLE_GENRE_REFERENCE.md`.

---

## Overview: Planning Is Phase 1, Made Reviewable

Planning is the elevation of what `core/methodology/songwriting.md` calls **Phase 1: Analysis
(Steps 1-9)** into a first-class, approvable artifact produced BEFORE writing a single word.

```
PLAN (this file)  -->  WRITE (songwriting.md Phase 2)  -->  CRITIQUE / OPTIMIZE / VERIFY
   |
   produces the SONG BRIEF (approved by the user) which becomes the writer's contract
```

The Song Brief is **CONCEPTUAL**. It plans the song -- thesis, emotion, arc, genre, key, BPM,
structure, hook approach. **It does NOT write verses.** Lyric writing happens later, in the
writing phase, and consumes the approved brief as its brief-of-record.

---

## Three-Tier Evidence Labeling System

Claims in this methodology carry one of three evidence tiers:

| Label | Meaning |
|---|---|
| **[Tier 1: Scholarship-backed]** | Documented academic framework with primary sources and peer-reviewed research. |
| **[Tier 2: Professional heuristic]** | Widely-used craft guidance supported by professional practice but not empirically validated as universal law. |
| **[Tier 3: Community/platform heuristic]** | Empirical observation from practitioner testing (e.g., Suno community experiments). Unverified, version-dependent. |

Unlabeled claims are general craft consensus or structural descriptions that do not require tiering.

---

## GUIDED MODE Is the Default Posture

Planning runs in **GUIDED MODE by default**. The planner does not silently make every decision
and hand back a finished brief. For EACH brief decision it runs a small loop:

```
1. SUGGEST  -- present a methodology-backed default for this decision, with one line of reasoning
2. PROMPT   -- ask the user to CONFIRM the default or OVERRIDE it
3. RECORD   -- write the confirmed value into the brief
4. NEXT     -- move to the next decision
```

The suggested default is never invented. It is derived from the canonical decision frameworks
(see "Decision Frameworks the Plan Draws On" below) so that a user who simply confirms every
default still ends up with a methodology-sound brief. The user stays in control: any default can
be overridden, and the planner re-derives downstream suggestions from the override (e.g., a genre
override changes the suggested instrument palette and BPM range).

### AUTO-PILOT Mode (still available, not the default)

If the user signals they do not want to be prompted -- "surprise me", "you choose", "you decide",
"just go", "auto-pilot", "make the best choices", "I trust you", "don't ask" (or similar intent) --
the planner switches to AUTO-PILOT: it applies the methodology-prescribed default for every
decision without prompting, fills the whole brief in one pass, and states each choice with a
one-line reason so the user can review and override afterward. AUTO-PILOT uses the SAME decision
frameworks as GUIDED MODE; only the prompting differs. This mirrors the songwriter agent's
AUTO-PILOT trigger list (see `.kiro/agents/songwriter.md`).

---

## The SONG BRIEF (Deliverable Spec)

The Song Brief has **12 sections, in this exact order**. In GUIDED MODE each section is one
suggest-default-then-confirm step. The brief is conceptual throughout -- no verse lyrics appear in
any section.

### (1) Song Thesis
One sentence that captures the core truth of the song. This is the destination everything else
serves. If you cannot write this sentence, you have a topic, not a song. See the Song Thesis
requirement in `core/methodology/songwriting.md`.

### (2) Semantic Analysis
What is this literally about? Subject, characters, setting, objects, actions. See
`core/methodology/songwriting.md` Step 2.

### (3) Emotional Analysis
The central affect (specific, not "sad"), the 2-3 **BRECVEMA** mechanisms to target, and the
emotional journey stated as **start -> through -> arrive** ("starts at X, moves through Y, arrives
at Z"). BRECVEMA and the emotion mechanisms are defined in `core/methodology/songwriting.md`
Step 3 and `SONGWRITING_KNOWLEDGE_BASE.md`.

### (4) Narrative Arc + The Turn
The arc type (e.g., confession -> panic -> release) and, explicitly, **where the Turn is** and
**what the bridge reveals**. The bridge-turn concept is defined in `core/methodology/songwriting.md`
Step 5 and Step 14 -- reference it, do not restate the rule.

### (5) Voice / Accent
Who is singing: register, dialect/accent, and the emotional state at the START versus the END of
the song. If character-driven, point to the Character Voice Template in
`core/methodology/character-voice.md`. See `core/methodology/songwriting.md` Step 6.

### (6) Genre Mapping
Primary genre and, if fusion, the texture genre expressed as a **70/30 split**; a **Fabbri 5-rules**
sanity check; and the instrument palette that "belongs" to the genre. The 70/30 fusion rule,
Fabbri's 5 rules, and the Genre-Instrument palette are defined in `core/methodology/songwriting.md`
Step 7 and `references/SUNO_STYLE_GENRE_REFERENCE.md` -- reference them, do not restate.

### (7) Key + BPM + Time Signature (with reasoning)
The chosen key, BPM, and time signature, each with a one-line reason. Derive from the
key-emotion mapping and BPM-emotion interaction; do NOT restate the mappings here. See the Key
Selection and BPM-Emotion frameworks in `SONGWRITING_KNOWLEDGE_BASE.md` and
`references/SUNO_STYLE_GENRE_REFERENCE.md`, and `core/methodology/songwriting.md` Step 9.

### (8) Arrangement / Dynamics Sketch
The growth pattern (additive / subtractive / explosive / bloom), where the **negative space** is,
the contrast pairs, and where the **hook lands**. Hook-timing guidance (a hook signal within the
first 5-30s of the first sung vocal, genre-dependent) is defined in `core/methodology/songwriting.md`
Step 8 -- reference it, do not restate. This is a SKETCH; it is formalized as Production Notes
during writing.

### (9) Structure Map + V6 Mode Label
The section sequence (e.g., intro -> V1 -> PC -> C -> V2 -> PC -> C -> bridge -> final C -> outro)
and the **V6 mode label**: either **Default/Roots** (folk, blues, mountain-gothic) or
**MODE C (Cinematic/Theatrical/Concept)** for concept-album / cinematic material. The mode label
and its technique inventory are defined in `references/V6_TAG_DISCOVERY.md` (V6 Technique
Inventory) -- cite that file; do not restate its technique list here.

### (10) Hook Approach
The hook TYPE (title / lyric / melodic / rhythmic / production) and a **candidate hook line** to
aim for. Hook types are defined in `SONGWRITING_KNOWLEDGE_BASE.md` and `core/methodology/songwriting.md`.
A candidate line is a conceptual target, not finished chorus lyrics.

### (11) Production / Commercial
Target audience, target length, platform fit, solo vs duet, and standalone vs album. If album, note
the album and track position (see album-vs-standalone pre-check below). Reference the Hit Formula
awareness (F1 Vulnerability / F2 Anthem) in `core/methodology/songwriting.md` to keep the
commercial framing coherent -- do not restate the F1/F2 table.

### (12) Open Questions / Decisions for the User
The list of decisions that are still open, defaulted-but-unconfirmed, or deliberately deferred to
writing. This is where GUIDED MODE surfaces anything the user skipped or asked to revisit.

> **The brief is CONCEPTUAL and does NOT write verses.** No section above contains lyric lines.
> A candidate hook line (section 10) is a conceptual target phrase, not a written chorus.

---

## Decision Frameworks the Plan Draws On (Pointers, Not Restatements)

Every suggested default in GUIDED MODE is derived from a canonical framework. The planner POINTS
TO these; it never forks or restates their contents.

| Framework | Feeds Brief Section | Canonical Source (reference only) |
|---|---|---|
| Genre-Emotion Alignment | (6) Genre mapping | `SONGWRITING_KNOWLEDGE_BASE.md`, `references/SUNO_STYLE_GENRE_REFERENCE.md` (used by the songwriter agent's AUTO-PILOT mode) |
| Key Selection (mode = #1 emotional cue) | (7) Key | `SONGWRITING_KNOWLEDGE_BASE.md`, `references/SUNO_STYLE_GENRE_REFERENCE.md` |
| BPM-Emotion Interaction | (7) BPM | `SONGWRITING_KNOWLEDGE_BASE.md`, `references/SUNO_STYLE_GENRE_REFERENCE.md` |
| Fabbri's 5 Rules of genre membership | (6) Genre mapping | `core/methodology/songwriting.md` Step 7 |
| 70/30 fusion rule | (6) Genre mapping | `core/methodology/songwriting.md` Step 7 / Step 20 |
| Hook timing (5-30s), hook types | (8), (10) | `core/methodology/songwriting.md` Step 8, `SONGWRITING_KNOWLEDGE_BASE.md` |
| Prosody thresholds (7-12 syllables) | informs (7), (8) | `core/methodology/songwriting.md` Step 4 / Step 17 |
| Hit Formula F1 (Vulnerability) / F2 (Anthem) | (11) Production/commercial | `core/methodology/songwriting.md` "Hit Formula Awareness" |
| V6 mode label + technique inventory | (9) Structure map | `references/V6_TAG_DISCOVERY.md` |
| 12-category critique rubric (quality lens) | brief self-check | `core/methodology/critique.md` |

---

## The Candidate Style Prompt (Flexible Template, Not a Locked String)

The planner MAY emit a **Candidate Style Prompt** as part of the brief. It is a **FLEXIBLE
TEMPLATE**, never a locked, finished string. It prompts for EACH value, shows a methodology-backed
suggested default per value, and the user confirms or overrides each one. The output is a
filled-but-editable style template that the writing/optimization phase finalizes.

Prompt for each of these values (suggest a default for each; user confirms/overrides):

- Genre + the 70/30 split (if fusion)
- BPM (with Italian tempo marking, per `core/methodology/songwriting.md` Step 20)
- Key
- Vocal identity / range (register, accent, delivery)
- Production feel / era anchor
- Mood
- Exclusions (what must NOT appear)

The full Style Prompt assembly rules (7-dimension formula, 5-8 tags, artist-reference conversion,
instrument sound descriptors, character limits) are defined in `core/methodology/songwriting.md`
Step 20 -- the planner references them and does not restate them.

---

## Album vs Standalone Prompt

The planner asks whether this is a **standalone** track or an **album** track.

- **Standalone:** proceed with the brief as-is.
- **Album:** run only a **LIGHT album continuity pre-check** at planning time:
  - Does the planned key fit the album's harmonic map?
  - Does the planned palette DIFFER sufficiently from adjacent tracks?
  Then prompt the user for the album blueprint and the adjacent (neighbor) tracks. The pre-check is
  intentionally light. The FULL continuity verification (all hard rules, motif usage, callbacks,
  >70% palette differentiation, Rule 11) is out of scope for planning and is owned by the
  **album-continuity agent** and `core/methodology/album-continuity.md` -- point the user there.

---

## Stop-at-Brief vs Flow-into-Writing Prompt

At the end of the brief, the planner asks the user what to do next:

- **STOP at the brief** -- deliver the approved Song Brief as the artifact and stop. Save it with
  the eventual song as `SONGNAME.brief.md` (see location convention below).
- **FLOW into writing** -- hand the approved brief to the writing phase (songwriter) as the
  brief-of-record and begin Phase 2 of `core/methodology/songwriting.md`.

Either way, the approved brief is saved next to the song file it belongs to.

---

## Brief File Location Convention

Save the Song Brief in the SAME folder as the eventual song file, using the naming pattern
`SONGNAME.brief.md` (the brief sits next to `SONGNAME.md`). For example, a standalone song at
`examples/songs/standalones/Three_In_The_Morning.md` has its brief at
`examples/songs/standalones/Three_In_The_Morning.brief.md`. A user's own work lives under `songs/`.

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Writing verses in the brief | The brief is conceptual -- plan, don't draft lyrics |
| Restating craft rules in the brief | Reference the canonical source (songwriting.md / critique.md / KB) |
| Skipping the thesis | Without a one-sentence thesis you have a topic, not a song |
| Handing back a finished brief without prompting | GUIDED MODE is default -- suggest, then confirm each decision |
| Emitting a locked style string | The Candidate Style Prompt is a flexible, per-value template |
| Running the full album check at planning time | Only a LIGHT pre-check here; full check is the album-continuity agent's job |

---

## Time Estimate

| Step | Time |
|---|---|
| Guided walkthrough of the 12 brief sections | 15-25 min |
| Candidate Style Prompt (per-value confirm) | 5-10 min |
| Album pre-check (album tracks only) | 5 min |
| **Total** | **20-40 min** |

---

## References

- `core/methodology/songwriting.md` -- canonical craft method; Phase 1 Steps 1-9, prosody, hook timing, Fabbri, 70/30, Hit Formula F1/F2, Style Prompt assembly
- `core/methodology/critique.md` -- the 12-category scoring rubric and advanced A1-A5 checks (quality lens for the brief)
- `core/methodology/character-voice.md` -- Character Voice Template (brief section 5, if character-driven)
- `core/methodology/album-continuity.md` -- full album continuity system (brief section 11, album tracks)
- `SONGWRITING_KNOWLEDGE_BASE.md` -- Genre-Emotion Alignment, Key Selection, BPM-Emotion, hook types
- `references/SUNO_STYLE_GENRE_REFERENCE.md` -- genre / key / BPM / instrument reference tables
- `references/V6_TAG_DISCOVERY.md` -- V6 Technique Inventory and the Default/Roots vs MODE C mode label
