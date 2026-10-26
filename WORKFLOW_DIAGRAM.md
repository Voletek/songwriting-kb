# Songwriting KB — System Workflow Diagram

---

## How Everything Connects

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            USER REQUEST                                     │
│                                                                             │
│ "Plan a song..." "Write a song..." "Critique this" "Optimize" "Continuity"  │
└──────┬───────────────┬─────────────────┬──────────────┬──────────────┬──────┘
       │               │                 │              │              │
       ▼               ▼                 ▼              ▼              ▼
┌──────────────┐┌───────────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐
│ SONG-PLANNER ││   SONGWRITER      │ │   CRITIC     │ │ SUNO-        │ │ ALBUM-           │
│ AGENT (thin) ││   AGENT (thin)    │ │   AGENT      │ │ OPTIMIZER    │ │ CONTINUITY       │
│              ││                   │ │   (thin)     │ │ (thin)       │ │ (thin)           │
│ Loads:       ││ Loads:            │ │ Loads:       │ │ Loads:       │ │ Loads:           │
│ core/method- ││ core/methodology/ │ │ core/method- │ │ core/method- │ │ core/method-     │
│ ology/song-  ││ songwriting.md    │ │ ology/       │ │ ology/suno-  │ │ ology/album-     │
│ planning.md  ││                   │ │ critique.md  │ │ optimization │ │ continuity.md    │
└──────┬───────┘└────────┬──────────┘ └──────┬───────┘ └──────┬───────┘ └────────┬─────────┘
       │                 │                   │                │                  │
       │ Produces:       │ Also refs:        │ Also refs:     │ Also refs:       │ Also refs:
       │ [Song Brief,    │ • KB files        │ • CRITIQUE_REF │ • SUNO_TAGS_REF  │ • ALBUM_BLUEPRINT
       │  user-approved] │ • MUSIC_THEORY    │ • STYLE_GENRE  │ • STYLE_GENRE    │
       │ SONGNAME.brief  │ • critique.md     │                │                  │
       │  (feeds writer) │ (per-section      │                │                  │
       │       └────────▶│  checks)          │                │                  │
       │                 │                   │                │                  │
       │                 ▼                   ▼                ▼                  ▼
┌──────┴──────────────────────────────────────────────────────────────────────┐
│                         OUTPUT: songs/*.md                                  │
│  (song-planner also writes SONGNAME.brief.md alongside the song)            │
│                                                                             │
│  Triggers hooks on agent-made create/save (Kiro IDE 1.0+ / Kiro CLI V3):    │
│  • song-validate.json ─── tools/validate-song.py: char counts, required     │
│      elements, V6 tag checks, exclusions format (create + save)             │
│  • prosody-lint.json ─── tools/lyric-lint.py: syllables, stress, rhyme,     │
│      section stability, clichés (save)                                      │
│  • <album>-continuity.json ─── hard-rule check (if copied from examples/)   │
│  (README.md and *.brief.md are skipped; Kiro Web: run the tools manually)   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## The Full Pipeline (SOP 07)

```
┌──────────┐   ┌───────────┐   ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐     ┌───────────┐
│   PLAN   │──▶│ [Song     │──▶│  WRITE   │────▶│ CRITIQUE  │────▶│  REVISE  │────▶│ OPTIMIZE │────▶│  VERIFY   │
│  SOP 09  │   │  Brief,   │   │ (guided) │      │  SOP 02  │      │          │      │  SOP 03  │     │ Continuity│
│ (guided) │   │ approved] │   │  SOP 01  │      │          │      │          │      │          │     │           │
└──────────┘   └───────────┘   └──────────┘      └─────┬────┘      └──────────┘      └──────────┘     └───────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  DECISION GATE  │
              │                 │
              │  ≥8.5 ──────────────────────────────────▶ Skip to OPTIMIZE
              │  7.0-8.4 ─────▶ REVISE (fix top 3 issues, re-critique)
              │  <7.0 ─────────▶ Return to WRITE (new approach)
              │                 │
              │  Album FAIL ────▶ REVISE regardless of score
              └─────────────────┘
```

---

## Guided / Collaborative Mode (PLAN → WRITE seam)

One shared interaction loop drives both the song-planner (brief decisions) and the
songwriter (lyric sections). It is an INTERACTION MODE over the existing methodology
and critique rubric — never new craft rules.

```
   PLANNING (song-planner, SOP 09)              WRITING (songwriter, SOP 01)
   ─────────────────────────────                ──────────────────────────────
   For each of the 12 brief sections:           For each lyric section:
                                                
   ┌───────────────────────────────┐            ┌───────────────────────────────┐
   │ 1. SUGGEST a methodology-      │            │ 1. PROPOSE a draft section     │
   │    backed default              │            │    (seeded by the Song Brief)  │
   │        │                       │            │        │                       │
   │        ▼                       │            │        ▼                       │
   │ 2. SURFACE concerns / options  │            │ 2. SELF-FLAG against           │
   │    (from song-planning.md)     │            │    critique.md's FULL 12-      │
   │        │                       │            │    category rubric             │
   │        ▼                       │            │        │                       │
   │ 3. USER confirms / overrides   │            │ 3. USER confirms / overrides   │
   │        │                       │            │        │                       │
   │        ▼                       │            │        ▼                       │
   │ 4. NEXT section                │            │ 4. NEXT section                │
   └───────────────┬───────────────┘            └───────────────┬───────────────┘
                   │                                             │
                   ▼                                             ▼
       [Song Brief, user-approved]  ───────feeds───────▶  Completed lyrics
       saved as SONGNAME.brief.md                         → CRITIQUE → OPTIMIZE
       alongside the song
```

Full pipeline seam:
`PLAN (guided) → [Song Brief, user approves] → WRITE (guided, per-section critic checks) → CRITIQUE → OPTIMIZE`

---

## SOP 01: Writing a Song (Songwriter Agent)

```
PHASE 1: ANALYSIS (Steps 1-9)              PHASE 2: WRITING (Steps 10-16)
─────────────────────────────               ──────────────────────────────
                                           
 1. Song Thesis (one sentence)              10. Write CHORUS first ◀── destination
 2. Semantic (what's it about?)             11. Write Pre-Chorus (builds into chorus)
 3. Emotional (central affect)              12. Write Verse 1 (sets up chorus)
 4. Prosodic (syllable/rhyme plan)          13. Write Verse 2 (NEW information)
 5. Narrative Arc (choose arc type)         14. Write Bridge (THE TURN)
 6. Voice/Accent (who sings?)              15. Write Final Chorus (variation)
 7. Genre (70/30 fusion?)                   16. Write Intro/Outro
 8. Arrangement (dynamic plan)             
 9. Production & Commercial                
                                           
         ┌──────────────────────────────────────────────────────────────┐
         │  KEY DECISIONS MADE BEFORE WRITING A SINGLE WORD:            │
         │  • Thesis • Affect • Syllable targets • Arc type             │
         │  • Hook timing • Key • BPM • Audience • Runtime              │
         └──────────────────────────────────────────────────────────────┘

PHASE 3: QUALITY CHECK (Steps 17-19)       PHASE 4: FORMATTING (Steps 20-26)
────────────────────────────────────       ──────────────────────────────────

 17. Prosody Audit (+ lyric-lint.py)        20. Assemble Style Prompt (≤1000)
     □ 7-12 syl target; 13-15 review?       21. Write Exclusions (Exclude field)
     □ Stresses on meter's strong beats?    22. Add [Title:] (V6: no global tags)
     □ No stuffed phrases?                  23. Add Direction Blocks
     □ Line-end function words stressed?    24. V6 section + [Instrument: X In/Out]
 18. Structure Check                            tags, end with [End]
     □ Hook signal ~5-30s after 1st sung    25. Write Production Notes
       word?                                26. Final Character Count
     □ V2 adds new info?                        + validate-song.py
     □ Bridge turns?                       PHASE 5: ALBUM (Step 27)
 19. Quality Gates                         ──────────────────────────
     □ Every word earns its place?          27. Continuity Check
     □ Hook passes "text" test?                 □ Key fits harmonic map?
     □ Rhyme strength fits the job?             □ Palette matches range?
     □ Section stability matches plan?          □ Motifs correct?
                                                □ >70% differentiation?
```

---

## SOP 02: Critiquing a Song (Critic Agent)

```
┌─────────────┐    ┌─────────────┐   ┌─────────────────┐    ┌──────────────┐
│ Step 1:     │    │ Step 2:     │   │ Step 3:         │    │ Step 4:      │
│ READ        │──▶│ 9-STEP      │──▶│ SCORE 12        │──▶│ CALCULATE    │
│ (no scoring)│    │ ANALYSIS    │   │ CATEGORIES      │    │ COMPOSITE    │
└─────────────┘    └─────────────┘   └─────────────────┘    └──────┬───────┘
                                                                   │
┌─────────────┐   ┌─────────────┐   ┌─────────────────┐            │
│ Step 8:     │   │ Step 7:     │   │ Step 5:         │            │
│ PRIORITY    │◀──│ FLAG ALL    │◀──│ SUNO            │◀─────────┘
│ RECOMMEN-   │   │ ISSUES      │   │ OPTIMIZATION    │
│ DATIONS     │   │ (with fixes)│   │ ASSESSMENT      │
└──────┬──────┘   └─────────────┘   └─────────────────┘
       │
       ▼
┌─────────────────────────────────────────┐
│ LAYERS (choose based on context):       │
│                                         │
│ Layer 1: Core 12 categories ──── Quick  │
│ Layer 2: + Advanced 5 ────────── Full   │
│ Layer 2.5: + Suno Optimization ── Suno  │
│ Layer 3: + Album-Context 6 ──── Album   │
│ + Calibration audit ─────────── Always  │
└─────────────────────────────────────────┘
```

---

## Context Loading Architecture

```
SESSION START
     │
     ▼
┌─────────────────────────────────────┐
│ STEERING                            │
│ always (EVERY session):             │
│ • songwriting.md (principles)       │
│ • suno-formatting.md (V6 rules)     │
│ • output-preferences.md (format)    │
│ auto (album-related requests):      │
│ • concept-album.md (framework)      │
│ manual (/quick-score, /full-pipe-   │
│ line): quick-score.md,              │
│ full-pipeline.md                    │
│ fileMatch: <album>.md (if added)    │
└──────────────────┬──────────────────┘
                   │
          User invokes an agent
                   │
     ┌─────────────┼─────────────┐
     │             │             │
     ▼             ▼             ▼
┌─────────┐   ┌─────────┐  ┌─────────┐
│Songwriter│  │ Critic  │  │Optimizer│     ◀── ON INVOKE (thin wrapper loads core/ via resources:)
│ loads:   │  │ loads:  │  │ loads:  │
│ core/    │  │ core/   │  │ core/   │
│ method-  │  │ method- │  │ method- │
│ ology/   │  │ ology/  │  │ ology/  │
│ song-    │  │ crit-   │  │ suno-   │
│ writing  │  │ ique    │  │ opt     │
└────┬────┘   └────┬────┘  └────┬────┘
     │             │            │
     │       Agent needs deeper data
     │             │
     ▼             ▼
┌─────────────────────────────┐
│ REFERENCES (on demand)      │           ◀── WHEN NEEDED (deep data tables)
│                             │
│ • CRITIQUE_REFERENCE (+15k) │
│ • SUNO_STYLE_GENRE (+12k)   │
│ • V6_TAG_REFERENCE/DISCOVERY│
│ • SUNO_TAGS_REFERENCE (+10k)│
│   (v5.x, legacy)            │
│ • RHYME_AND_LYRIC_CRAFT     │
│ • CHARACTER_VOICE (+5k)     │
│ • MUSIC_PRODUCTION (+15k)   │
│ • SONGWRITING_KB (+15k)     │
└─────────────────────────────┘
```

---

## Hook Triggers

```
┌──────────────────────────────────┬──────────────────────────────┬───────────────┐
│ EVENT                            │ HOOK / COMMAND               │ TYPE          │
├──────────────────────────────────┼──────────────────────────────┼───────────────┤
│ New .md in songs/                │ song-validate.json           │ hook (auto)   │
│ Save .md in songs/               │ song-validate.json           │ hook (auto)   │
│ Save .md in songs/               │ prosody-lint.json            │ hook (auto)   │
│ Save .md in songs/<album>/       │ <album>-continuity.json      │ hook (opt-in) │
│ User runs /quick-score           │ quick-score.md               │ manual steer. │
│ User runs /full-pipeline         │ full-pipeline.md             │ manual steer. │
└──────────────────────────────────┴──────────────────────────────┴───────────────┘
```

- Hooks are Kiro v1 JSON (`.kiro/hooks/*.json`); file-event hooks fire only for agent-made changes and skip `README.md` / `*.brief.md`.
- Hooks run in Kiro IDE 1.0+ and Kiro CLI V3; Kiro Web sessions don't run hooks — run `python3 tools/validate-song.py` / `python3 tools/lyric-lint.py` manually.
- `<album>-continuity.json` = a copy of `examples/albums/<album>/continuity-hook.json` placed in `.kiro/hooks/`.

---

## File Authority Hierarchy

```
     core/methodology/ wins (SINGLE SOURCE OF TRUTH)
         │
         │  Complete, self-contained methods
         │  Update HERE — everything downstream inherits
         │
         ▼
     AGENT (thin wrapper — loads core/ via `resources:` front matter)
         │
         │  Defines persona + loads methodology
         │  Does NOT duplicate content
         │
         ▼
     STEERING (derived subset — always / auto / manual / fileMatch)
         │
         │  Quick-reference rules (3 always-on files every session)
         │  Does NOT load large reference docs
         │
         ▼
     SKILLS (on-demand deep knowledge)
         │
         │  References core/ + references/
         │  Activated by agents when needed
         │
         ▼
     REFERENCES (deep data tables)
         │
         │  Scoring rubrics, genre maps, tag lists
         │  REFERENCED BY core/methodology/ — not the source
         │
         ▼
     TOOLS (deterministic validation)
         │
         │  tools/validate-song.py — format, char, V6-tag, exclusions checks
         │  tools/lyric-lint.py — syllables, stress, rhyme, stability, clichés
         │  tools/check-repo.py — repo integrity
         │  No AI interpretation needed
         │
         ▼
     HOOKS (automated quality enforcement)
              Run the tools on agent-made file saves (Kiro IDE / CLI V3)
              Catch violations after the fact
```
