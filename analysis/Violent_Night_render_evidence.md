# Violent Night — Render Evidence (personal)

> Measured results of the four Violent Night takes (Nov 23, 2026), kept on the personal branch rather
> than in the community knowledge base. Measured with `audio-analysis` and `audio-listen` (SOP 10 Step 3).
> Song files: `songs/standalones/Violent_Night.md` (rev 1) and `Violent_Night_v2.md` (rev 2).
> Experiment logs: `experiments/suno/2026-11-23-v6-meter-from-style.yml`, `…-key-change-tag-vs-edit.yml`.

## Render rows (V6_TAG_DISCOVERY results-log format)

| Date | Model (v6/v6-wild/v6-mini) | Song / take | Tag(s) tested | Result (measured) | Render ID |
|---|---|---|---|---|---|
| 2026-11-23 | v6 | Violent Night rev 1, take A | Style "3/4 waltz at 132 BPM" | ❌ 4/4 (analysis), heard as a march; 134.9 BPM, D minor ✅ | `20a1b845-3d54-41df-a0b9-d66afc5fc131` |
| 2026-11-23 | v6 | Violent Night rev 1, take B | Style "3/4 waltz"; Style "D minor shifting to F major for the final refrain" (no lyric key tag) | ⚠️ 3/4 by beat tracker, 4/4 by ear; ✅ brief F major ~4:55-5:14 and back | `7a519480-c3f5-4bc2-9375-4222b00d8c3e` |
| 2026-11-23 | v6 | Violent Night rev 2, take A | `[Key Change: Relative major, F]`, `[Key Change: Back to D minor]`; `[Transition: Drums Out, Strings Out, Diminuendo]` + `[Instrument: Cello In]`; `[Dynamic: Full Impact]`; `[Vocal: Gang Vocal]`; `[Vocal: Whisper]`; `[Transition: Hit]` | ❌ no key change; ⚠️ bridge partly stripped (percussion stayed); ✅ biggest final chorus; ✅ gang vocals; ✅ whisper; ❌ no clear final hit; 4/4, 131 BPM | `bd5c3106-7f23-44b6-bc1b-bf0ebbf52cbc` |
| 2026-11-23 | v6 | Violent Night rev 2, take B | same as rev 2 take A | ❌ no key change (only "relative-major colour"); ✅ bridge strip (drums out, drone/cello + voice); ✅ final chorus; ✅ gang vocals; ✅ whisper; ❌ no final hit; 4/4, 133.2 BPM | `0578b38d-8eb2-4e71-9bc2-108f165fccfb` |
| 2026-11-23 | v6 | Violent Night, all 4 takes | Instruments outside the V6 list: `Bowed Lyre`, `Tagelharpa`, `Winter Bells`, `War Drums`, `Frame Drums` | ⚠️ lyre-like plucks heard in 3 of 4, "bowed folk strings" in 4, war/frame drums in 4, bells in 4; tagelharpa not identified as such | (above) |


## What these takes suggest for the tag-type ratings (one song only; not enough to change shared ratings)

| Tag type | This song | Note |
|---|---|---|
| `[Key Change: ...]` | ❌ 0/2 (rev 2) | `[Key Change: Relative major, F]` ignored on both takes. A rev 1 take with no key tag drifted to F briefly from the Style Prompt alone. Try a section edit next. |
| Meter from the Style Prompt (`3/4 waltz`) | ⚠️ 1/4 | 3 of 4 takes came out 4/4. Next: "6/8 lilting folk waltz" right after the genre. |
| `[Instrument: X Out]` (bridge drums out) | ⚠️ 1/2 | Full strip on one rev 2 take; percussion stayed on the other. |
| `[Dynamic: Full Impact]` final chorus | ✅ 2/2 | Biggest section on both rev 2 takes. |
| `[Vocal: Gang Vocal]` | ✅ 2/2 | |
| `[Vocal: Whisper]` | ✅ 2/2 | |
| `[Transition: Hit]` final strike | ⚠️ 2/4 | |
| Off-list instruments (Bowed Lyre, Tagelharpa, War/Frame Drums, Winter Bells) | ⚠️ | Lyre-like plucks in 3 of 4, bowed folk strings, war/frame drums and bells in 4 of 4; tagelharpa never identified. |


## Revision 2 words as a cover of the Froststep bed (Nov 23, 2026)

`audio-covers-create` on `72ccb1ed-1a21-4629-b06e-556b35ca6d64` (Audio Influence 0.8, Style Influence 0.75,
Weirdness 0.3, Variety 1). Takes `6fd78c03…` and `4cc83650…`, measured with `audio-listen`, word alignment and
`audio-analysis`.

| Element | Result |
|---|---|
| Waltz / triple meter | ✅ 2/2 (heard as 6/8 and 3/4; ~168 BPM) |
| Froststep melody and character | ✅ 2/2 |
| Key | moved C minor → G minor (cover regenerates the bed) |
| Bridge quieter, close vocal | ✅ 2/2 |
| Biggest final chorus | ✅ 2/2 |
| Low male chant harmonies (`[Vocal: Gang Vocal]`, with "choir" removed from Exclusions) | ✅ 2/2 |
| Whispered final ho ho ho | ✅ 2/2 (breathy, spoken) |
| All lyric lines sung | ✅ 2/2, 0 failed words |

Compared with the text-only renders (waltz 1/4, whisper not reliable): covering a 3/4 bed at high
Audio Influence carried the meter, and a cover could follow the bridge and ending cues written into the Style.
