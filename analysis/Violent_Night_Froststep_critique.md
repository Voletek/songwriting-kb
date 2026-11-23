# Violent Night (Froststep Waltz take): Professional Critique

**Date:** November 23, 2026
**Version analyzed:** Froststep take. The v1 (original) words were sung over the user's uploaded Froststep Waltz instrumental using suno.com "add vocals" (Variety 4, v6, Nov 19). The take is formatted in `songs/standalones/Violent_Night_Froststep.md`.
**Analyzer:** Critic agent (SOP 02, Delta Critique: Layer 1 delta + Layer 2.5 + Recommendations)
**Album context:** Standalone seasonal single (dark Nordic Yule folk waltz, 5:59)
**Previous scores:** v1 Core 7.8 / Advanced 7.4 (`analysis/Violent_Night_critique.md`). v2 Core 8.3 (`analysis/Violent_Night_v2_critique.md`, Layer 2 not re-scored).

**Evidence used:** The `audio-analysis` and `audio-listen` results on the source take, as listed in the brief. `validate-song.py --strict` passed (Style 706/1000, Lyrics 4945/5000). `lyric-lint`: 101 lines, 3-9 syllables, 0 clichés. `estimate-runtime` (177 BPM, 3/4, 3 bars per line) gives 5:40. The lyric words match `Violent_Night.md` exactly, so the lyric categories carry over from the 7.8 critique and are **not re-scored**. Layer 2 (Advanced) is not re-scored, as the brief asked.

**Timing basis:** At 176.6 BPM in 3/4, one bar lasts about 1.02 s. The take sings roughly 2-3 bars per line: the short chorus lines get about 2 bars (the final chorus fits 12 lines into about 25 s), and the verse lines get about 3.

---

## Core 12-Category Scores (delta from v1)

| Category | v1 | Take | Δ | Basis | Notes |
|---|---|---|---|---|---|
| Hook | 8 | 8 | 0 | Carried | The pun and the chant are unchanged. The take's timing makes the hook later than v1 assumed. That cost is scored under Commercial so it isn't counted twice. |
| Lyrics | 8 | 8 | 0 | Carried | All five weak lines flagged in v1 are still in the take: "barely some," "watch beside," "valley, hill, and sea," "to see what he shall see," "both, you know." |
| Prosody | 8 | 8 | 0 | Carried | The v1 findings stand ("Bound in weathered hide" at 5 syllables, day-BREAK, done/some). The faster tempo of about 2-3 bars per line suits the common-meter verses. |
| Arc | 8 | 8 | 0 | Carried | The written arc is unchanged. The render drops the closing "ho ho ho" (see Voice/Accent). |
| Structure | 6 | 6 | 0 | Re-scored | At 177 BPM the 20 sung lines of Bridge plus Build pass in about 40 s instead of about 55 s, so the stretch with no hook is shorter. The bridge doesn't strip, though, so the song loses its one planned contrast, and the 33 s intro plus 5:59 total still carries the v1 bloat. |
| Originality | 8 | 8 | 0 | Carried | The Odin layer and the phrasing are unchanged. |
| Singability | 8 | 8 | 0 | Carried | "Hearthfires" and the fit of "VIOLENT" in the chant are unchanged. |
| Commercial | 7 | 7 | 0 | Re-scored | This is the only take with the waltz, and a brisk 177 BPM folk waltz with bowed strings, wooden flute and frame drums stands out for seasonal sync. Against that, the first chorus lands around 1:20-1:28 (33 s intro plus 16 lines), later than v1's estimate of 1:05-1:15, and the title still collides with the 2022 film. |
| Genre | 8 | 9 | +1 | Re-scored | Fabbri's formal, semiotic and behavioural rules are all met in the audio: 3/4 held, bowed folk strings, wooden flute, frame drums, drones, low male chant, and no pop jingle, electronics or growls. "Ancient Nordic folk waltz" is a genre Suno recognizes, which "cinematic Yule ballad" was not. |
| Arrangement | 8 | 7 | −1 | Re-scored | The gradual layering works, the instrumental breaks restate the waltz, and the final chorus is the biggest moment (about 4:52-5:17). The two designed contrasts both failed: the bridge builds instead of stripping, and the ending is ambience plus a bell with no whisper. The ~4:15 lift is also not a clear key change. |
| Voice/Accent | 8 | 8 | 0 | Re-scored | The deep bass-baritone, the low male chant layer and the Nordic instruments come from one cultural world, and there is no cartoon Santa (Moore, persona). The narrator-is-the-King reveal that v1 credited never sounds because the "ho ho ho" was dropped. The cultural fit is tighter than the text-only takes, so the score holds. |
| Emotional Intelligence | 8 | 8 | 0 | Carried | The v1 finding stands. |

### COMPOSITE SCORE: 7.8/10
(93/12 = 7.75. Δ 0.0 from v1)

The production gains (Genre) and losses (Arrangement) cancel out. Revision 2's lyric gains (Lyrics, Prosody, Arc and EI at 9) are not in this take.

**Projection, revision 2 words on this instrumental:** use the v2 lyric scores, this take's Genre 9, and Arrangement 9 if the bridge strip and whisper land (8 if they don't). That gives Hook 8, Lyrics 9, Prosody 9, Arc 9, Structure 7, Originality 8, Singability 8, Commercial 7, Genre 9, Arrangement 9, Voice 8, EI 9 = 100/12 = **8.3**, or 8.25 with Arrangement 8. The gap to 8.5 is in the same categories v2 identified: Hook, Singability, Structure and Commercial.

---

## Answers to the Key Questions

**1. Which version to build on.** Build on the **Froststep instrumental with the revision 2 words**. Don't revise this take's vocal line by line, and don't go back to text-only renders.
- The waltz is the song's identity. The Froststep take is the only one of five renders that held 3/4, because "add vocals" sings over the uploaded audio and the meter comes from the upload, not from the prompt. The text-only takes came out 4/4 on 3 of 4.
- Revision 2's lyric changes are worth +0.5 core, and none of them depend on the meter.
- Use a **new add-vocals run on the original Froststep Waltz upload** (on suno.com, not through the MCP). The MCP has no add-vocals tool. Its `reference_audio_ids` route is simple mode only and can't take a lyric sheet. `audio-covers-create` regenerates the instrumental, which is the one part that worked.
- Section-editing this take to the v2 words is a poor fit. The words change in 5 places (2 stanza cuts and 3 line swaps), which is exactly the limit; one more change and the whole song is re-sung as a cover. Cutting 8 lines from a vocal that sits on a fixed instrumental also leaves holes of about 16-24 s.
- Keep this take as the fallback keeper.

**2. How to get the bridge strip and the whispered ending.**
- **Run a free check first.** Run `audio-analysis` on the uploaded Froststep Waltz and ask `audio-listen` whether the instrumental itself rises from about 4:10 to 4:55. The measured lift at ~4:15 coincides with where the bridge starts at this tempo. If the upload rises there, no lyric tag or vocal re-run can strip it, because add vocals doesn't change the bed. That would also explain why `[Transition: Drums Out, Percussion Out, Diminuendo]` and the RAW sheet's "Instruments Pull Back" both failed.
- **Bridge:** After the v2 add-vocals run, do a **section edit** on the chosen take (`audio-create` with `reference_audio_ids` and a description; this regenerates only that time range). If you need certainty, a stems or DAW route is more reliable: split the instrumental, mute the drums and strings for the bridge window, then add vocals over the edited upload.
- **Ending:** Do a **section edit on the last ~15 s**. That is one lyric change, well inside the 5-place limit. The RAW sheet already contained "[Low Baritone — Almost Whispered] Ho... ho... ho...", and there was room after the final chorus (about 42 s for 9 lines). The model dropped the line rather than running out of space, so asking again in the same way is unlikely to fix it.
- **Not a cover.** A cover regenerates the instrumental and puts the 3/4 meter at risk.
- **Order:** add-vocals re-run first, then the section edits on the new keeper. Edits made to this take are lost when you switch to the v2 words.

**3. What in the formatted file would hurt a re-render on the same instrumental.** Each point is covered in detail below.
- "choir" in Exclusions targets the low male chant layer you want to keep (Issue 3).
- "sleigh-bell overload" puts the token "sleigh bell" into the Exclude field, against a song whose chorus sings "THE BELLS ARE RINGING" (Issue 3).
- The instrument In/Out, Transition and Feel tags can't act on a fixed upload. They use up 55 spare characters, and `[Feel: Double-Time]` is risky in a cover (Issue 4).
- The Style is missing the BPM that the file says was added, and it has more than 3 mood and space descriptors (7-point check).

---

## Suno Optimization Assessment

**Current Style approach:** Ancient Nordic folk waltz in C minor and 3/4 (no BPM stated), with tagelharpa, nyckelharpa, bowed lyre, wooden flutes, frame drums, iron sleigh bells and drones under a gravelly bass-baritone storyteller with layered low male harmonies on the choruses.
**Compliance:** PASS (strict validator: 0 failures, 0 warnings).
**Optimization verdict:** COULD IMPROVE

### 7-Point Dimensional Check

| # | Dimension | Current Choice | Assessment | Notes |
|---|---|---|---|---|
| 1 | Genre | Ancient Nordic folk waltz; "dark Viking Yule" | CORRECT | Putting "waltz" in the first genre phrase is right and matches the result. "Viking" with "thunderous" can pull toward folk-metal; the exclusions block screaming and growls but not distorted guitar. |
| 2 | Key | C minor | CORRECT | Matches the measured key of the instrumental. In add-vocals mode the stated key has to match the bed, or the vocal fights it. Any v2 file for this instrumental must drop revision 2's D minor/F major and its `[Key Change:]` tags, because a fixed bed can't modulate. The relative major would be E♭. |
| 3 | BPM | Not stated ("lilting 3/4 triple meter") | SUBOPTIMAL | The file header says the measured tempo was added to the Style, but it wasn't. Add-vocals doesn't need a BPM because the upload sets it. A cover regenerates the instrumental, so it does need one. |
| 4 | Instruments | Tagelharpa, nyckelharpa, bowed lyre, wooden flutes, frame drums, wooden percussion, iron sleigh bells, drones | CORRECT | Everything heard on the take is named (Tagg: each carries pagan-North connotations). The nyckelharpa wasn't identified in the audio, which is harmless. In add-vocals mode this list only orients the vocal style. |
| 5 | Vocal Style | Gravelly bass-baritone storyteller, staccato verses, layered low male harmonies | SUBOPTIMAL | The Style itself is correct. The problem is across fields: "choir" in Exclusions targets the harmony layer, which was heard as a choir/chant. The Style also has no cue for the whispered close or the near-whispered bridge, which are the two vocal moments that failed. |
| 6 | Era/Production | Organic live acoustic, unprocessed | CORRECT | Matches the take. |
| 7 | Space/Mood | spacious natural reverb, roomy, haunting, dark, ominous, festive, mischievous menace | SUBOPTIMAL | There are more than 3 atmospheric descriptors. "Spacious natural reverb" applies to the whole song, which works against the close bridge. "Festive" against "ominous" is a deliberate contrast and can stay; "haunting" repeats "ominous." |

### Section-Level Tag Assessment

"Inert" means the tag asks the instrumental to change, and an add-vocals run can't change the uploaded instrumental. Inert tags would act in a cover.

| Section | Current Tags | Signification Check | Recommendation |
|---|---|---|---|
| Intro | Tagelharpa In, Bowed Lyre In, Vocal Out, pp (4) | Vocal Out ALIGNED; the instrument tags are INERT | Keep `[Vocal: Vocal Out]` (the take's first vocal arrived at 0:33, so silence held). Cut the two instrument tags (about 50 characters). |
| Verse 1 | Role tag, p | ALIGNED | None. |
| Pre-Chorus 1 | Frame Drums In, Bells In, Crescendo | INERT apart from Crescendo | Cut the instrument tags. A crescendo can shape the vocal. |
| Chorus 1 / 2 | Harmony, f / ff | ALIGNED | `[Vocal: Harmony]` produced the low male layer. Keep it, and make sure no exclusion cancels it. |
| Interludes 1-2 | Vocal Out, Steady Stomp, mf / Vocal Out, f | Vocal Out ALIGNED; Feel INERT | Keep Vocal Out. Cut the Feel tag. |
| Verse 2 | Role tag, mp | ALIGNED | The role tag ("playful menace, wry humor") is a delivery cue that does reach the vocal. |
| Pre-Chorus 2 | Percussion In, Crescendo | Percussion INERT | Cut it. |
| Bridge | Transition: Drums Out, Percussion Out, Diminuendo; Drone In; near-whisper role tag | MISMATCHED on this take | The transition can't strip a fixed bed, and a near-whisper over a rising bed gets buried (see the Production-Lyric Alignment note). Fix with a section edit or the stems route (Issue 1). Otherwise retag the voice to ride the rise. |
| Build | Frame Drums In, Strings In, Crescendo | INERT apart from Crescendo | Cut the instrument tags. |
| Interlude 3 | Vocal Out, Double-Time, ff | Double-Time RISKY | In a cover, Double-Time at 177 BPM implies about 354 BPM, and the model is likely to resolve that as a fast 4/4 march, which loses the waltz. Cut it. |
| Final Chorus | Straight, Harmony, Full Impact | ALIGNED (Straight inert) | The take already delivered the biggest final chorus. Cut `[Feel: Straight]`. |
| Breakdown | Drums Out, mp, warm-tender role tag | Drums Out INERT | Keep the mp and role tags. |
| Outro | Strings Out, pp, Whisper, Transition: Hit, Sustain (4) | Whisper ALIGNED but missed; the rest INERT | The take ended on its own bell stroke. Keep `[Vocal: Whisper]` and fix the ending with a section edit if the re-run drops it again. |

Cutting the inert tags frees roughly 300 characters. That makes room for revision 2's cues, for `[Vocal: Half-Spoken]` on the child's line, and for an intro note about the bell figure.

### Style Alternatives

**Option A: re-run add vocals on the Froststep upload with the revision 2 words (recommended)**
```
Ancient Nordic folk waltz, C minor, brisk lilting 3/4 at 177 BPM, organic live acoustic character; deep weathered male bass-baritone, gravelly, commanding ancient storyteller, close dry rhythmic narrative verses with staccato phrasing and warm dark humor, powerful sustained choruses with layered low male unison chant harmonies, low near-whispered bridge, almost whispered final ho ho ho; tagelharpa, bowed lyre, Nordic wooden flutes, deep hide frame drums, iron bells and resonant acoustic drones; dark Yule, ominous mischievous menace
```
Reasoning: The bed is fixed, so this version puts its words into the vocal. It names both vocal moments that failed (the bridge near-whisper and the final whisper), calls the harmony layer "low male unison chant" so it matches what rendered, and states the measured BPM. Mood and space go down to ominous, mischievous menace and close dry verses, with the global reverb phrase removed. About 530 characters.
Expected improvement: A better chance of getting the close bridge vocal and the final whisper. The chorus harmony layer stays, and the vocal key and tempo stay locked to the upload.
Slider recommendation (v5.5-era starting points, re-check on V6): Weirdness 30% / Style Influence 70% / Audio Influence 75% (the add-vocals upload weight on suno.com) / Variety Normal (1). The source take used Variety 4 (Max), which reinterprets the style tags the most. Lowering it is a deliberate change made for tag adherence, so log it as a variable.

**Option B: cover of this take with the revision 2 words (`audio-covers-create`; only if add vocals is unavailable)**
```
Ancient Nordic folk waltz, C minor, brisk 3/4 waltz at 177 BPM with a strong one-two-three sway, gradual instrumental layering, organic live acoustic recording; deep weathered male bass-baritone, gravelly commanding ancient storyteller, close dry rhythmic verses with warm dark humor, powerful choruses with layered low male unison chant harmonies; tagelharpa, nyckelharpa, bowed lyre, Nordic wooden flutes, deep hide frame drums, iron bells and acoustic drones; bridge drops to drone and close near-whispered voice, thunderous final chorus, quiet outro on solo bowed lyre and a bell, almost whispered ho ho ho; ominous mischievous menace
```
Reasoning: A cover regenerates the instrumental, so this version states the meter twice ("3/4 waltz," "one-two-three sway") along with the BPM, and it puts the bridge strip and the ending into the Style, where the regenerated bed can follow them. Pass the full lyrics in `lyrics`, or the cover comes out instrumental.
Expected improvement: The bridge can actually strip, because the bed is newly generated. The source audio's 3/4 pulls the cover toward the waltz, but the meter is no longer guaranteed.
Slider recommendation: Weirdness 30% / Style Influence 75% / Audio Influence 80% (`controls.audio_influence: 0.8`, which in a cover sets how close the result stays to the source) / Variety Normal (1).

**Exclusions (both options):**
```
pop Christmas jingles, cartoon Santa vocals, children's choir, female vocals, metal screaming, death growls, distorted guitar, EDM, electronic effects, orchestral brass, autotune
```
This drops "choir," "sleigh-bell overload" and "overly polished pop vocals," and adds "children's choir," "female vocals," "distorted guitar" and "autotune."

### Compliance Checklist

| Check | Status | Notes |
|---|---|---|
| `[Title:]` present above intro | ✅ | |
| `[Production Direction:]` present | ✅ | It says the intro is about 38 s; the measured first vocal is at 0:33. It also describes a bridge strip that a fixed bed can't perform. |
| `[Vocal Direction:]` present | ✅ | |
| Style Prompt ≤1000 chars | ✅ | 706 |
| Lyrics ≤5000 chars | ✅ | 4945 (55 spare). Revision 2's cuts plus the inert-tag cuts would bring this to about 4,400-4,450; re-run the validator to confirm. |
| `[End]` at bottom | ✅ | |
| Section tags on own lines | ✅ | |
| Named `()` layers declared | ✅ | None used. |
| Exclusions in Exclude field | ✅ | Content issues are covered in Issue 3. |
| Genre is FIRST | ✅ | |
| Tag count 5-8 | ❌ | 19 descriptors. Informational only; this v5.5-era heuristic hasn't been re-checked on V6. |
| No contradictory tags | ❌ | "choir" (Exclude) against "layered low male harmonies" (Style). |
| BPM/tempo specified | ❌ | Meter only. |
| Per-section tags ≤3 | ❌ | Intro and Outro have 4 each. That is within V6's 2-4, and most of those tags are inert. |

---

## Calibration & Technical Audit

- **Self-Score Delta:** No self-score was provided.
- **Layer Audit:** There are no parenthetical layers. The harmony layer is driven by `[Vocal: Harmony]` and the Style, and "choir" in Exclusions works against it.
- **Production-Lyric Alignment:**
  - Mismatch at the bridge. "Close dark near-whisper" and "He knows the lies you whispered" sit on a rising bed, so the most intimate words get the loudest backing they've had so far (Lacasse: the vocal distance and the bed point in opposite directions).
  - Accidental alignment at the end. The bell stroke illustrates "A bell rang through the night." Without the "ho ho ho" the bell becomes the last word. That is a defensible ending, but it loses the persona reveal.
  - Aligned in the final chorus, where "LET THE HEAVENS SHAKE" lands on the biggest moment.
- **Timing check:** The estimate-runtime figure of a first chorus at ~57 s doesn't account for the take's 33 s intro. From 0:33, 16 lines at about 3 bars each put the chorus around 1:20-1:28. Run `audio-lyrics-alignment` (free) on the take to get the exact time and to confirm that all 20 Bridge and Build lines were sung in the roughly 40 s before 4:52.
- **Discovery Depth:** HIGH (carried). The waltz adds a further layer: a dance under a threat, which is how a fairy tale works.

---

## Strongest Line

> "For the wicked, something cold" (carried from v1). It updates the lump of coal, leaves the punishment unnamed, and closes the thesis couplet with a perfect rhyme on an open vowel. In this take it falls in the AABB couplet that the low male chant layer carries, three times, and it doesn't wear out.

---

## Flagged Issues

1. **The bridge builds instead of stripping, probably because the instrumental itself rises there**
   Current: `[Transition: Drums Out, Percussion Out, Diminuendo]` plus `[Male lead, close dark near-whisper]` over a bed that lifts at about 4:15.
   Why: Add vocals keeps the uploaded instrumental, so lyric tags can't remove drums from it. The song's only subtractive moment is lost (Moore: no texture-layer subtraction), and the near-whisper gets buried.
   Fix:
   a) Confirm the cause for free with `audio-analysis` and `audio-listen` on the Froststep upload, covering about 4:10-4:55.
   b) After the v2 re-run, do a section edit on the keeper. Example description: *"In Violent Night, redo the bridge (about 4:12–4:40) as a quiet passage: drums and strings drop out, only a low drone and a close, near-whispered bass-baritone, keeping the 3/4 waltz pulse, then rise back into the build."* Use the real times from the new take's analysis.
   c) For a guaranteed result, take stems of the upload (10 credits), mute the drums and strings in the bridge window in a DAW, re-upload, and run add vocals on that version.
   d) Or accept the rise. Retag the bridge as `[Male lead, low intense, rising]` and let the 12 lines of v2's Bridge and Build ride one continuous build.

2. **No whispered "ho ho ho"; the take ends on ambience and a bell**
   Why: The narrator-is-the-King reveal (Moore, song-character layer) goes missing. The RAW sheet asked for it and there was room for it, so the model dropped it.
   Fix: Do a section edit on the last ~15 s of the chosen take. Example description: *"In Violent Night, add an almost whispered 'ho… ho… ho' in the low male voice just before the final bell."* This is one change and costs 2 songs. Keep `[Vocal: Whisper]` in the file for the re-run.

3. **Exclusions that work against the sound you want**
   Current: "choir," "sleigh-bell overload."
   Why: The harmony layer the user wants was heard as a choir/chant. The take kept it while the exclusions were only prose in the description, but in the actual Exclude field "choir" gets more weight. The Exclude field also can't apply "overload": "sleigh-bell" reads as an excluded sound in a song built on bells.
   Fix: Use the exclusions string in the Style Alternatives section ("children's choir" and "female vocals" in place of "choir"; "sleigh-bell overload" dropped, since "pop Christmas jingles" already covers it).

4. **Tags a fixed instrumental can't follow, with only 55 characters spare**
   Current: Instrument In/Out tags in 6 sections, `[Transition: … Out]` in the Bridge and Breakdown, `[Feel: Steady Stomp / Double-Time / Straight]`.
   Why: In add vocals these tags at best do nothing and use up the budget the vocal cues need. In a cover, Double-Time at 177 BPM is likely to turn the waltz into a fast 4/4.
   Fix: For the add-vocals file, keep only the structure, vocal, role and dynamic tags, as listed in the section table. For a cover file, keep the instrument tags but drop Double-Time.

5. **The hook arrives late and the radio edit is harder**
   Why: The first chorus at about 1:20-1:28 is about 15 s later than v1 assumed, and in add-vocals mode the 33 s intro is part of the fixed upload.
   Fix:
   a) Trim the upload's intro to about 16 bars (about 16 s) in Studio or a DAW before the add-vocals run. The chorus then lands near 1:05.
   b) Leave the full take as the YouTube cut and make a shorter edit from the keeper later (SOP 10, Step 7).
   c) For search, release it as "Violent Night (The Yule King)."

### Minor Notes
- The file header says "measured key and tempo added," but only the key was added. Add "at 177 BPM" (Option A) or correct the header.
- Change "Instrumental intro of about 38 s" in the Production Direction to about 33 s, which is what was measured.
- The Production Notes' "first chorus planned at 1:28" is the take's plan. Replace it with the `audio-lyrics-alignment` result once that has run.
- Log in `references/V6_TAG_DISCOVERY.md`: `[Vocal: Harmony]` rendered as a low male chant layer under add vocals; the bridge transition failed on a fixed bed; the whisper was dropped even with an explicit cue.
- A v2-on-Froststep file needs its own Production Notes. Revision 2's D minor chord chart and its F major Breakdown don't apply to a C minor bed. Chart the bed with `audio-midi` (10 credits) if you want Nashville numbers.

---

## Priority Recommendations

1. **Create `Violent_Night_v2_Froststep.md`:** the revision 2 words, C minor, no `[Key Change:]` tags, the inert tags removed, the Option A Style and the revised Exclusions. Re-run add vocals on the Froststep upload on suno.com (one generation, 2 takes). Expected impact: core about 7.8 → 8.25-8.3, and the waltz is kept.
2. **Before spending credits, run the free checks:** `audio-analysis` and `audio-listen` on the upload for about 4:10-4:55, and `audio-lyrics-alignment` on this take. These decide between section edit, stems or accepting the rise for the bridge, and they give the real hook time.
3. **Section-edit the bridge strip on the new keeper** (Issue 1b), or use the stems route (1c). Expected impact: Arrangement +1-2 and Structure +0-1.
4. **Section-edit the whispered "ho ho ho" ending** (Issue 2). Expected impact: Arrangement +1, and the persona reveal is back.
5. **Trim the upload's intro for a hook around 1:05 and add the subtitle** (Issue 5). Expected impact: Commercial +1. Together with revision 2's open Hook and Singability fixes, this is the most likely route past 8.5.

---

## Decision Gate

**Core composite 7.8/10. Falls in the 7.0-8.4 revision band.**

→ **Proceed to Revise (Stage 3), with the revision 2 words moved onto the Froststep instrumental** (Priority 1), then fix sections through SOP 10 Step 5a and re-critique the new keeper.

This take settles the meter question: the waltz holds when it comes from the upload and fails when it comes from the prompt. Revision 2 settles the lyric question. Combining them is the shortest path. Even combined, the projected 8.3 still needs the Hook, Commercial and Singability work to clear 8.5. No album-context override applies.

---

## Addendum (Nov 23, 2026): follow-up checks change Issues 1 and 2

The free checks from Priority 2 were run after this report:

- **Bridge (Issue 1):** `audio-listen` on the Froststep bed (`72ccb1ed-1a21-4629-b06e-556b35ca6d64`) says the bed itself **pulls back** at ~3:40–4:18 (sparse, percussion largely out) and builds again from ~4:18. Word alignment puts the take's bridge at 3:47–4:20, inside that window, and a targeted listen on the take confirms the bridge is quieter and sparser than the choruses, with drums out until ~4:04. **The bridge strip landed.** The "~4:15 lift" is the bed's build starting, under the Build lyrics (from 4:20).
- **Ending (Issue 2):** alignment places "Ho... ho... ho..." at 5:51.7–5:53.2, and a targeted listen hears it clearly: **present, but low, raspy and spoken rather than whispered.** The fix is smaller than proposed: a delivery tweak (section edit of the last ~10 s, "softer, almost whispered"), or accept it.
- **Hook timing (Issue 5):** first chorus at 1:38 of track time, 65 s after the first sung word (alignment), later than the 1:20–1:28 estimated above.
- The first broad `audio-listen` answer was wrong on two points. Targeted questions plus `audio-lyrics-alignment` corrected it.

**Effect on scores:** Arrangement returns to 8 (both designed contrasts are present; the whisper delivery is the remaining gap). Core composite ≈ 7.8 → 7.9 (94/12). Priority 1 (revision 2 words on the Froststep upload) is still the main recommendation, and Priority 3 (bridge section edit) is no longer needed.
