# Violent Night: Professional Critique

**Date:** November 23, 2026
**Version analyzed:** v1 (user lyrics, converted by the orchestrator to V6 format with no word changes)
**Analyzer:** Critic agent (SOP 02, Full Multi-Layer Model)
**Album context:** Standalone. A seasonal dark Nordic Yule folk single, about 6:00.

**Timing basis used throughout:** At 132 BPM in 3/4, one bar lasts 1.36 s. Fitting 101 sung lines into a 5:59 track requires about 2 bars (about 2.7 s) per line. That gives roughly 4:35 of singing, plus the intro, three interludes and the outro.

---

## Core 12-Category Scores

| Category | Score | Notes |
|---|---|---|
| Hook | 8/10 | The "Violent Night" / "Silent Night" pun works without music and is easy to quote, but it first appears after 16 sung lines, about 44 s after the first sung word and around 1:05-1:15 of track time. That is late even for a cinematic story song, though the chorus pays off hard when it lands. |
| Lyrics | 8/10 | The imagery is strong and specific: "red as winter blood," "iron belt," "rusted battleaxe / From somewhere in the air," "A man confessed to four." A handful of lines are weaker or bent to fit a rhyme: "barely some," "watch beside," "Over valley, hill, and sea," "To see what he shall see," and "both, you know." |
| Prosody | 8/10 | Verses hold the 8-6-8-6 ballad meter (common meter) and lint found every line at 3-9 syllables. There are small breaks: "Bound in weathered hide" (5 syllables where the pattern wants 6) and "Eight great beasts with antlers black" (7, though the three heavy stresses earn it). Two stresses fall on weak syllables: PROM-is-ES and day-BREAK. The rhymes "done/some" and "hide/beside" show strain. |
| Arc | 8/10 | Verse 2 adds new events (the dialogue, the toys, the axe, the threat). The bridge turns the address from "he" to "you." The final chorus tag changes, morning resolves the night, and the bell and the whispered "ho ho ho" reopen the threat. The turn is partly diluted because "book of names" repeats the "names" carved on his belt in Verse 1. |
| Structure | 6/10 | Two sections run long. Verse 2 has 16 lines, and the bridge (12 lines) plus the build (8 lines) gives 20 sung lines with no chorus between Chorus 2 and the Final Chorus. Add three near-identical choruses and the song carries real bloat inside its ~6:00 length. |
| Originality | 8/10 | Dark-Santa songs are common (Krampus songs, metal Christmas records), but folding Odin into the story is fresh: the Wanderer, eight beasts recalling Sleipnir's eight legs, ravens, the Yule King. The phrasing is also original: a battleaxe "from somewhere in the air," "for the wicked, something cold." |
| Singability | 8/10 | Common meter is one of the most singable forms in English, and the short trochaic chorus lines suit a chant. Small catches: "VIOLENT" (2-3 syllables) has to fit a chant figure, and the "-rth-f-" cluster in "hearthfires" is hard to sing at tempo. |
| Commercial Viability | 7/10 | The song has strong seasonal sync potential (holiday horror, trailers, games) and a hook that markets itself. Against that, it runs 6:00 with a late hook, and it shares its title with the 2022 action film, which will crowd search results. |
| Genre Alignment | 8/10 | Nordic folk conventions are honoured (Fabbri formal and semiotic rules): drone, frame drums, tagelharpa, a storyteller's narration, and a waltz that fits the Scandinavian folk-dance tradition. "Cinematic Yule ballad" in the Style Prompt is not an established genre, and "ballad" can pull the render slow. |
| Arrangement/Production | 8/10 | The designed dynamic arc is strong: pp to ff, a stripped bridge, and an outro that bookends the opening. The tags do not deliver all of it. The Final Chorus is tagged ff exactly like Chorus 2, the bridge keeps the strings and tagelharpa, the interludes carry one tag each, and nothing cues the F major lift. |
| Accent/Voice Coherence | 8/10 | Scandinavian lilt, Nordic instruments, D minor and an old-world narrator all come from one cultural world. The closing "ho ho ho" suggests the narrator was the King all along, which is a strong persona twist (Moore, song-character layer). The child's question and the King's reply are not marked as separate voices. |
| Emotional Intelligence | 8/10 | The menace stays at fairy-tale scale, and the moral weight sits in the right place: the stolen bread against the shared bread. The song offers fireside pleasure without glorifying violence. The warm refrain softens the reckoning slightly more than the thesis claims. |

### COMPOSITE SCORE: 7.8/10
(93/12 = 7.75)

---

## Advanced Assessments

| Assessment | Score | Notes |
|---|---|---|
| Functional Layers (Moore) | 7/10 | Beat (frame and war drums), melody (voice and lyre) and harmonic filler (strings, tagelharpa) are all present. The bass layer is weak: until the strings enter at the pre-chorus, only the tagelharpa drone covers the low register, and no low drone or bass is named for the bridge. |
| Soundbox & Proxemics (Lacasse) | 8/10 | The planned distances are good: intimate close-mic Verse 1, public gang-vocal choruses, back to intimate for the near-whispered bridge, warm conversational refrain, whispered ending. The Style Prompt's single global "wide cold hall" works against the close verses. |
| Musemic Signification (Tagg) | 8/10 | Tagelharpa, frame drums and the drone signify the pagan North, and the waltz signifies a dance or fairy tale. Sleigh bells are the one sound that signifies Christmas pop, which "No bright Christmas sparkle" is trying to avoid. The irony works if the bells stay iron and distant, not jingling. |
| Scope of Vision (Dodge et al.) | 8/10 | Ambitious: a six-minute mythic narrative that rewrites Santa as Odin's Wild Hunt, with dialogue, a moral turn, and a narrator reveal at the end. |
| Skip Test (A&R) | 6/10 | Dead-zone risks: an intro longer than 15 s with no new event; the stretch from Interlude 2 through Bridge and Build (about 55 s of singing plus a break, no hook); a third chorus that repeats 10 of its 12 lines with the same tags. |

### ADVANCED COMPOSITE: 7.4/10

---

## Suno Optimization Assessment

**Current Style approach:** Dark Nordic folk plus a cinematic Yule ballad in D minor, shifting to F major. A 3/4 waltz at 132 BPM, with lyre, tagelharpa, frame drums, war drums, bells and low strings under a gravelly bass-baritone with a Scandinavian lilt and male gang vocals.
**Compliance:** PASS. validate-song.py --strict reported 0 failures and 0 warnings (Style 766/1000, Lyrics 4873/5000).
**Optimization verdict:** COULD IMPROVE

### 7-Point Dimensional Check

| # | Dimension | Current Choice | Assessment | Notes |
|---|---|---|---|---|
| 1 | Genre | Dark Nordic folk (70%) + cinematic Yule ballad (30%) | SUBOPTIMAL | Nordic folk is the right anchor. "Yule ballad" is not a known genre, and "ballad" pulls toward slow piano or strings. The literal "(70%)" and "(30%)" spend characters; the repo convention is `+`. |
| 2 | Key / Mode | D minor → F major | CORRECT | Minor mode carries the dread, and the D tonic sits in a bass-baritone's chest. A lift to the relative major suits the morning. The Style field cannot time that shift, though; it needs a tag in the lyrics. |
| 3 | BPM | 3/4 at 132 | CORRECT | 132 is a moderate waltz, and the 5:59 target confirms 2 bars per line (see Issue 9). [Tier 3] Suno tends to default to 4/4, so the word "waltz" appearing twice is useful. |
| 4 | Instruments | Lyre, tagelharpa, frame and war drums, iron and sleigh bells, low strings | CORRECT | Each is described as a sound ("raspy horsehair tagelharpa"), which helps with a niche instrument. "Sleigh bells" is the one risk to Christmas-pop colouring. |
| 5 | Vocal Style | Gravelly bass-baritone, Scandinavian lilt, gang chant | CORRECT | Matches the genre's behavioural rules and the arc. The range "(G2-D4)" is unlikely to be parsed and costs 9 characters. |
| 6 | Era/Production | "raw acoustic production" | CORRECT | Organic production suits the genre. No era anchor is needed. |
| 7 | Space/Mood | haunting, ominous, thunderous, fireside, menace, warmth, wide cold hall | SUBOPTIMAL | More than 3 atmospheric descriptors. "Fireside" (close and warm) and "wide cold hall" (distant and cold) point in different directions without saying which sections get which. |

### Section-Level Tag Assessment

| Section | Current Tags | Signification Check | Recommendation |
|---|---|---|---|
| Intro | Lyre In, Tagelharpa In, Winter Bells In, pp | ALIGNED | The user's "Extended" did not carry over. Add the length to the Production Direction, for example "16-bar intro." Lyre, Tagelharpa and Winter Bells are not in the V6 instrument list, so log whether the In/Out events render. |
| Verse 1 | Male lead role tag, p | ALIGNED | None. |
| Pre-Chorus 1 | War Drums In, Bowed Strings In, Crescendo | ALIGNED | None. |
| Chorus 1 | Frame Drums In, Gang Vocal, f | ALIGNED | None. |
| Interlude 1 | mf only | UNDER-TAGGED (1 tag) | Restore the user's cue. Add `[Vocal: Vocal Out]` and `[Feel: Steady Stomp]`. The user wrote "Original Waltz Theme, Heavy Frame Drums, Rhythmic Tagelharpa." |
| Verse 2 | War Drums Out, role tag, mp | ALIGNED | None. |
| Pre-Chorus 2 | War Drums In, Crescendo | ALIGNED | None. |
| Chorus 2 | Gang Vocal, ff | ALIGNED | None. |
| Interlude 2 | f only | UNDER-TAGGED (1 tag) | Add `[Vocal: Vocal Out]`, plus a second tag naming the strings melody the user asked for ("Bowed String Melodies"). |
| Bridge | War Drums Out, Frame Drums Out, Diminuendo, role tag | PARTIAL | Strings and tagelharpa stay in, so "Instruments Pull Back" and "drops to drone" will not happen. Use the compound form `[Transition: Drums Out, Strings Out, Diminuendo]`, then `[Instrument: Drone In]` and the role tag. |
| Build | Ceremonial Drums In, Crescendo | PARTIAL | The user's "Rising Strings" needs `[Instrument: Bowed Strings In]` if the bridge removes them. |
| Interlude 3 (climax) | War Drums In, Frame Drums In, Double-Time, ff | ALIGNED | "Original Melody Returns" was dropped. It could go in the Production Direction ("climax restates the intro waltz theme"). |
| Final Chorus | Straight, Gang Vocal, ff | MISMATCHED | It is meant to be the biggest moment but is tagged the same as Chorus 2. Use `[Dynamic: fff]` or `[Dynamic: Full Impact]`, and add `[Vocal: Full Voice]`. |
| Refrain | War Drums Out, Frame Drums Out, mp, role tag | PARTIAL | "Refrain" is not one of the 15 V6 structure tags. Nothing cues the F major. Use `[Outro]` or `[Breakdown]`, and replace one drum tag with `[Key Change: Relative major, F]` (log the result), or bundle `[Transition: Drums Out, Key Lift]`. |
| Outro | Bowed Strings Out, Tagelharpa Out, Whisper, Hit | ALIGNED | The user's "Final Bowed Note" could become `[Dynamic: Sustain]` after the Hit. Without a tag, the key drops back to D minor only by chance. |

### Style Alternatives

**Option A (same concept, tightened):**
```
Dark Nordic folk + cinematic winter folk, D minor, 3/4 waltz at 132 BPM, ominous and haunting, building to a stomping fireside chant, droning bowed lyre, raspy horsehair tagelharpa, deep frame drums, thunderous ceremonial war drums, distant iron bells, slow-shaken iron sleigh bells, low bowed strings and a deep cello drone, deep gravelly male bass-baritone storyteller with a slight Scandinavian lilt and rolled r's, grinning menace with warmth underneath, layered male gang-vocal chants on choruses, raw organic acoustic production, close dry verses, choruses in a wide cold stone hall, long instrumental waltz breaks, ends on solitary bowed lyre and one drum strike
```
Reasoning: Removes "ballad," the percentages and the vocal range. Gives the space descriptors a section each (close verses, hall choruses). Adds a cello drone to fill the bass layer. Makes the sleigh bells iron and slow so they don't jingle.
Expected improvement: Fewer slow-ballad renders, a clear difference between intimate verses and public choruses, and a firmer low end in the verses and bridge.

**Option B (myth and ritual first, carol irony on purpose):**
```
Dark Nordic ritual folk + dark Christmas carol, D minor, 3/4 waltz at 132 BPM with a heavy downbeat stomp, menacing and mythic, rising to a pounding mead-hall chant, droning tagelharpa and bowed lyre, deep frame drums, ceremonial war drums, hand-rung iron bells, low cello drone, deep gravelly male bass-baritone narrator with a Scandinavian lilt and rolled r's, playful menace, stomping male gang choir singing carol-like harmonies on choruses, organic acoustic recording, intimate close-mic verses, vast reverberant hall on choruses, long instrumental waltz breaks, whispered ending
```
Reasoning: "Dark Christmas carol" as the 30% flavour points the model at the "Silent Night" parody, so the chorus can lean on carol-style harmony while the 70% Nordic folk keeps it pagan.
Expected improvement: The title pun and the "THE BELLS ARE RINGING" chant should read as a twisted carol rather than generic folk-metal.

### Compliance Checklist

| Check | Status | Notes |
|---|---|---|
| `[Title:]` present above intro | ✅ | |
| `[Production Direction:]` present | ✅ | |
| `[Vocal Direction:]` present | ✅ | |
| Style Prompt ≤1000 chars | ✅ | 766 |
| Lyrics ≤5000 chars (with tags) | ✅ | 4873. Only 127 left, so any added tags must be paid for with cuts (see Issue 1). |
| `[End]` at bottom | ✅ | |
| Section tags on own lines | ✅ | |
| Named `()` layers declared in Style | ✅ | None are used. `vocal overlap confusion` in Exclusions is unnecessary but harmless. |
| Exclusions in Exclude field, plain, no dash | ✅ | |
| V6 format: no `[Tag Vocabulary]`, no global tags, no pipes | ✅ | |
| Genre is FIRST in Style Prompt | ✅ | |
| Style tag count (v5.5-era 5-8 heuristic) | ❌ | 14 descriptors. This is a Tier 3 heuristic not re-checked on V6, so it is informational only. |
| No contradictory tags | ❌ | "fireside" against "wide cold hall" (space) |
| No artist names | ✅ | |
| No gear/model names | ✅ | |
| BPM/tempo specified | ✅ | |
| V6: 2-4 tags per section | ❌ | Interludes 1 and 2 have one tag each. Verse 1 Pre-Chorus 2 and Chorus 2 have two each, which is fine. |

---

## Calibration & Technical Audit

- **Self-Score Delta:** No self-score was provided.
- **Layer Audit:** There are no parenthetical layers, so nothing needs declaring. The `vocal overlap confusion` exclusion can go.
- **Production-Lyric Alignment:** The Production Direction says "No bright Christmas sparkle" while the Style Prompt asks for sleigh bells. This contrast is intentional and needs managing (Option A). The thesis says "a reckoning, not a comfort," but the F major refrain *is* a comfort. The song gives both, so the thesis should too (see Minor Notes).
- **Discovery Depth:** HIGH. Repeat listens turn up the Odin layer (the Wanderer, eight beasts, ravens, the Yule King), the bread motif (stolen in Verse 2, shared in the Bridge), the "go" callback ("Where mortal men don't go" becomes "There's nowhere he can't go"), the low/bright bookend on the village fires, and the hint in "ho ho ho" that the narrator is the King.

---

## Strongest Line

> "For the wicked, something cold" works on several levels at once. On the surface it updates the lump of coal ("cold" sits one letter from "coal"). The understatement also leaves room for iron, the axe blade, or a grave, and the song never says which. It closes a perfect rhyme on the thesis couplet, sits on an open vowel the gang vocal can hold, and appears three times without losing its menace. Runner-up: "A man confessed to four," which shows the King's effect through dark comedy without showing any violence.

---

## Flagged Issues

1. **Bridge plus Build is 20 sung lines without a hook, and it repeats an image**
   Current: A 12-line Bridge ("They say he keeps a book of names…") flows straight into an 8-line Build. "Book of names" repeats the "names of those he'd known" on the belt in Verse 1.
   Why: That is about 55 s of singing plus Interlude 2 without the hook, which is the Skip Test's main dead zone. The bridge guideline is 3-6 lines, up to 8 when the turn needs it. The real turn ("He knows… the child who shared his bread") arrives in stanza 2, so stanza 1 delays it. With only 127 characters left, these cuts are also what pays for the tag fixes in Issue 2.
   Fix:
   a) Cut Bridge stanza 1. The bridge then opens on "He knows the lies you whispered" (8 lines), the turn hits at once, and about 130 characters are freed.
   b) Keep Bridge stanza 1 and cut Build stanza 2 ("Through the storm…"). This also removes Issues 4 and 10.
   c) Do both and replace the Build with one 4-line stanza. The Final Chorus then lands about 25 s sooner.

2. **The tags don't deliver the designed arrangement (orchestrator formatting)**
   Current: Interludes 1 and 2 have one tag each. The Bridge keeps strings and tagelharpa. The Final Chorus is ff like Chorus 2. `[Refrain]` is not a V6 structure tag, and there is no key-change cue. The user's interlude descriptions ("Original Waltz Theme, Heavy Frame Drums, Rhythmic Tagelharpa"; "Spiraling… Bowed String Melodies"; "Original Melody Returns") were dropped.
   Why: V6 uses the lyric field to choreograph the performance. Untagged breaks risk being skipped or shortened, or getting sung filler. A Final Chorus tagged the same as Chorus 2 renders as the same chorus, and the F major lift stays a wish in the Style field.
   Fix: Apply the Section-Level table above. In short: add `[Vocal: Vocal Out]` plus a feel or instrument tag to each interlude; use `[Transition: Drums Out, Strings Out, Diminuendo]` and `[Instrument: Drone In]` in the Bridge; give the Final Chorus `[Dynamic: Full Impact]`; rename Refrain to `[Outro]` or `[Breakdown]` with a `[Key Change: …]` or `[Transition: Key Lift]` cue; add the climax melody note to the Production Direction. Log the render results in V6_TAG_DISCOVERY.md.

3. **Forced rhyme: "When there was barely some"**
   Current: "He knows the child who shared his bread / When there was barely some"
   Why: "Barely some" is not idiomatic English (people say "barely any"). The meaning bent to reach a slant rhyme with "done," in the song's most important moral line.
   Fix:
   a) "And went to bed with none". This gives a perfect rhyme with "done" and makes the sacrifice physical.
   b) "When he had only one"
   c) "Though hunger had begun"

4. **Weak lines in the Build: filler and a tautology**
   Current: "Over valley, hill, and sea / The old king rides before the dawn / To see what he shall see"
   Why: "Valley, hill, and sea" is a generic list. "To see what he shall see" says nothing (a tautology). "Before the dawn" anticipates "RIDES BEFORE DAYBREAK" in the next chorus.
   Fix:
   a) "Over fjord and frozen sea / The old king rides from door to door / To judge both you and me". This is specific and Nordic, and it carries the bridge's "you" onto the singer.
   b) "Over fjord and frozen sea / The old king counts the open doors / And knows which ones are free"
   c) Cut the stanza (Issue 1b).

5. **"Bound in weathered hide / … While ravens watch beside"**
   Why: "Bound in weathered hide" has 5 syllables where common meter wants 6. "Watch beside" is bent syntax made for the rhyme. If Issue 1a is taken, the stanza goes and this issue goes with it.
   Fix:
   a) "And bound in weathered hide / … With ravens at his side". This restores the meter, gives a perfect rhyme, and the phrasing is natural.
   b) "All bound in blackened hide / … While ravens wait outside"

6. **Rhyme filler: "And answered, both, you know"**
   Why: "You know" is padding to reach the "snow" rhyme. It also softens the menace at the exact moment the battleaxe is about to appear. With the quotation marks removed, lowercase "both" also reads ambiguously.
   Fix:
   a) "And growled, Why, both, you know". This keeps the user's folksy wink and adds a menacing verb.
   b) "And answered, Both. Now go". The perfect rhyme makes it a command, but "go" already appears twice in the song.
   In either case, capitalize "Both" so the reply reads as speech.

7. **Song length and density work against commercial reach**
   Why: The song runs about 6:00, with the title hook around 1:05-1:15 of track time, against the norm of the full chorus by ~45-60 s. The title also collides in search with the 2022 film *Violent Night*.
   Fix:
   a) Make a 3:30-3:45 edit: shorten the intro to about 8 bars, cut Interlude 1, and apply Issue 1c. That keeps the full version as the album/YouTube cut.
   b) Plant an early hook signal. A bell figure in the intro that the chorus melody later answers would work with no lyric change.
   c) For discoverability, consider a subtitle such as "Violent Night (The Yule King)."

8. **The Final Chorus tag drops the title and repeats an image**
   Current: "LET THE HEAVENS SHAKE / THE KING OF YULE / RIDES BEFORE DAYBREAK"
   Why: "DAYBREAK" puts the rhyme on its weaker second syllable (day-BREAK). It also repeats the dawn image from the Build. The lint "open" reading is not a real problem, because SHAKE/DAYBREAK closes as a perfect rhyme.
   Fix:
   a) "LET THE HEAVENS SHAKE / THE KING OF YULE / IS WIDE AWAKE". This is a perfect rhyme on a stressed syllable and calls back to "NO ONE SLEEPS."
   b) Keep the line and cut "before the dawn" from the Build (Issue 4a) to remove the repetition.

9. **The Production Notes' tempo description doesn't match the song's density (orchestrator)**
   Current: "felt as a slow one-in-a-bar waltz"
   Why: If each of the 4 stresses in an 8-syllable line gets its own bar, each line takes about 5.5 s, Verse 1 alone takes about 65 s, and the song runs past 9 minutes. The 5:59 target only works with 2 bars per line (stresses on beats 1 and 3, like a lilting 6/8). Suno will choose one or the other, and the wrong one risks truncation or a rushed render.
   Fix: Change the note to "two stresses per bar, lilting, one-in-a-bar pulse only in the instrumental breaks." Also correct the hook estimate to about 44 s after the first sung word.

### Minor Notes

- **"THE YULE KING'S SINGING"**: The King is never shown singing, so the line can read as rhyme-driven. It is defensible as a twisted carol ("Hark! the herald angels sing"), and under Tenet 3 the user's hook stands. Optional alternative: "THE WILD HUNT SINGING."
- **"Lock your doors or light your hearthfires"**: "Hearthfires" is a consonant cluster that is hard to sing at tempo. Alternative: "Bar the doors and bank the fires." It calls back to "barred the door" and "feed the flame."
- **Dialogue voices**: The child's question is sung by the baritone with no cue. Optional: `[Vocal: Half-Spoken]` on that couplet, though it costs a tag and characters.
- **Outro timeline**: The Refrain reaches morning, then the outro returns to "night." It reads well as the yearly cycle ("every year he reads it through"). If the cycle isn't intended, "A bell rang through the light" or "A bell rings, out of sight" fixes the order.
- **Thesis wording**: Change it to say he is both: "The old Yule King is both reckoning and reward: gifts for the kind, a return visit for the cruel." That also removes the "not X but Y" construction.
- **Lint flag "travels on"**: Not a problem. "On" is the stressed particle of a phrasal verb (TRAV-els ON) on an open-enough vowel. Keep it.
- **"For those who kept their PROM-is-ES"**: The meter stresses the weak "-es" syllable. This is minor and not at a rhyme point. Optional fix: "For those who kept their word this year."
- **Unknown instrument tags**: Lyre, Tagelharpa, Winter Bells, War Drums and Ceremonial Drums are not in the V6 instrument list. Log whether their In/Out events render. If they don't, fall back to `Drone`, `Strings`, `Toms` and `Percussion`.
- **Exclusions**: `vocal overlap confusion` has no job here because there are no parenthetical layers, and it can be removed.

---

## Priority Recommendations

1. Cut the Bridge plus Build from 20 lines to 8-12 (Issue 1a or 1b). This fixes the main dead zone and the "names" repetition, and frees the characters Issue 2 needs. Expected impact: Structure +1, Skip Test +1-2.
2. Re-tag the arrangement: interludes, bridge strip, Final Chorus lift, key-change cue, and the dropped user cues (Issue 2). Expected impact: Arrangement +1, and the render matches the design.
3. Fix the "barely some" rhyme in the moral turn (Issue 3). Expected impact: Lyrics and Prosody.
4. Replace the weak Build lines and the dawn repetition (Issues 4 and 8; "IS WIDE AWAKE" is recommended). Expected impact: Lyrics and Arc.
5. Switch to Style Option A or B. This removes "ballad," gives the space descriptors a section each, and adds a bass drone. Expected impact: Genre and Space/Mood move to CORRECT, and Functional Layers improves.
6. Correct the Production Notes' phrasing description and hook estimate (Issue 9) so the render aims for 2 bars per line.
7. Fix the meter and rhyme in "weathered hide / watch beside" (Issue 5) if that stanza survives Issue 1.
8. Tighten "both, you know" (Issue 6).
9. Plan a 3:30-3:45 edit and an early bell-motif hook signal (Issue 7).
10. Apply the Minor Notes: "hearthfires," thesis wording, outro timeline, dialogue cue, and logging the instrument tags.

---

## Decision Gate

**Core composite 7.8/10. Falls in the 7.0-8.4 revision band.**

→ **Proceed to Revise (Stage 3).** Address Issues 1-6 first, then re-critique.

This is a standalone single, so no album-context override applies. The core (7.8) and advanced (7.4) scores are close; the main drag in both is length and density (Structure 6, Skip Test 6), not the quality of the writing. Priorities 1-4 alone should plausibly lift the core composite to about 8.3-8.6.
