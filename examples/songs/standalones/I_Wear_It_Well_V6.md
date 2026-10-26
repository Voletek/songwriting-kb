# I Wear It Well — V6 Format (migration example)

> **Reference example of the Suno V6 lyric format.** Same song, same words and same Style Prompt as
> `I_Wear_It_Well.md` (the v5.5-era original), re-tagged in the canonical V6 grammar from
> `references/V6_TAG_REFERENCE.md`. Use it as the model for new songs, and compare the two files to
> see what changes when you migrate a v5.5-era song. Status: not yet rendered on V6. Log results in
> the `references/V6_TAG_DISCOVERY.md` results log.

## What changed from the v5.5-era version

| v5.5-era original | V6 version | Why |
|---|---|---|
| `[track: ...]`, `[control: ...]`, `[sequence: ...]` global tags | Removed | V6 doesn't use v5.5 global tags; genre and mood live in the Style field |
| `[Tempo: Moderato]` | Removed (tempo is in Style) | Style = the WHAT (key, tempo, identity) |
| Pipe notation `[Verse 1 \| composed formal diction, close-mic, elegant]` | `[Verse 1]` + `[Male lead, composed formal diction, close-mic]` | V6 canonical grammar: separate role/inline-adjective tags |
| `[build]` / `[diminuendo]` | `[Dynamic: Crescendo]` / `[Dynamic: Diminuendo]` | Namespaced dynamics |
| Arrangement described only in Production Direction | `[Instrument: X In]` / `[Instrument: X Out]` at each section | V6 honours instrument entrances and exits on cue |
| `[fade: layered]` + `[end]` | `[Dynamic: Fade Out]` + `[End]` | V6 terminator |
| `[Exclusions: ...]` inside the Style section | `## EXCLUSIONS:` section, plain comma-separated | Exclude field format (no dash prefix) |

Kept on purpose: the `[Production Direction:]` / `[Vocal Direction:]` blocks and the `[Whisper Rule:]`
(consistency anchors between regenerations), the `()` whispered layer, and the Production Notes block.

---

## STYLE PROMPT:

Alternative rock (70%), Victorian bluegrass-EDM hybrid (30%), Moderato, restrained and composed turning to precise anthemic release, electric bass-led groove, plucked banjo and bowed cello over pulsing four-on-the-floor synth, chamber strings, clean locked modern production with parlor-room warmth, smooth warm commanding male baritone (G2-E4) with a slight East Tennessee Appalachian lilt surfacing on the raw lines, soft twang and dropped g's leaking through the formal composure, layered rhythmic textures building additively, restrained instrumental intro to full precise final chorus, instrumental outro fade, elegant restraint cracking under modern exhaustion

---

## EXCLUSIONS:

distortion, screaming vocals, trap drums, mumble rap, autotune, aggressive metal guitar, chiptune, vocal overlap confusion, cheerful major-key brightness, lo-fi tape hiss

---

## LYRICS:

[Title: I Wear It Well]

[Production Direction: Restrained instrumental intro — composure intact — plucked banjo and bowed cello over a soft pulsing synth, electric bass leading the groove. Build ADDITIVELY across sections: each part adds one rhythmic layer so the arrangement mirrors the emotional pressure rising under the mask. Clean, locked, modern production with parlor-room warmth. Strip the bridge almost bare — the mask slips here. Final chorus is the biggest, most PRECISE moment, full band four-on-the-floor, chamber strings and banjo locked tight. End on an instrumental outro that fades. Contrast is the engine: elegant restraint against modern burnout.]

[Vocal Direction: Smooth warm commanding male baritone, composed and mannered like a period-drama role — always IN CONTROL on the surface even while admitting collapse. Underneath is an East Tennessee man wearing borrowed elegance. On the FORMAL performed lines, diction stays crisp and clean — the mask holds. On the RAW confessional lines and all whispered parentheticals, a slight Appalachian lilt leaks through — soft twang on vowels, dropped g's, mountain phrasing. NOT exaggerated country — just the real man showing through the cracks. Close-mic, no vibrato wobble. Parenthetical lines are whispered intrusive thoughts, close and breathy — the truth under the performance, heaviest accent here. Bridge is the most vulnerable moment, the mask fully slips and the mountain shows all the way through, voice thinning but never breaking. Final chorus is commanding and full, the mask at its most powerful even as the twang bleeds under it.]

[Whisper Rule: Lyrics in parentheses are whispered intrusive thoughts, close and breathy, with the heaviest East Tennessee accent — the real man under the performance]

[Intro]
[Instrument: Banjo In]
[Instrument: Bowed Cello In]
[Instrument: Synth Pad In]
[Dynamic: pp]

[Verse 1]
[Instrument: Bass In]
[Dynamic: mp]
[Male lead, composed formal diction, close-mic]
Good evening — yes I'm keeping fine
Cufflinks straight and the parting clean
I hold my composure like a coat
Buttoned to the throat where it can't be seen

(ain't slept in a week)

I answer every letter that I owe
And I never let the tremor reach my hand

[Pre-Chorus]
[Dynamic: Crescendo]
[Male lead, accent leaking in]
But the candle's burnin' low
and I'm runnin' on empty for the show

[Chorus]
[Instrument: Kick In]
[Dynamic: mf]
[Male lead, warm and precise, twang under the composure]
I wear it well — I'm not alright
A gentleman's decline in evening light
I bow and I smile and I hold the line
(I'm comin' apart)
I wear it well — I'm not alright

[Verse 2]
[Instrument: Percussion In]
[Dynamic: mp]
[Male lead, composed formal diction]
They say a man should carry it with grace
So I keep the collar high and the jaw set stone
I toast to your good health across the room
And I'm the loneliest gentleman you've ever known

(smilin' through it)

I perform the word alright like it's a role
And nobody claps to see the curtain shake

[Pre-Chorus]
[Dynamic: Crescendo]
[Male lead, accent leaking in]
Still the candle's burnin' low
and I'm runnin' on empty for the show

[Chorus]
[Dynamic: f]
[Male lead, warm and precise, twang under the composure]
I wear it well — I'm not alright
A gentleman's decline in evening light
I bow and I smile and I hold the line
(I'm comin' apart)
I wear it well — I'm not alright

[Bridge]
[Instrument: Kick Out]
[Instrument: Percussion Out]
[Dynamic: Diminuendo]
[Male lead, the mask slips, heaviest accent]
Behind the collar and the crown
there's a boy that this town near broke
Take the medal off my chest
and you'll find there ain't a thing holdin' on

(I'm so tired)
(I'm so tired of bein' fine)

[Final Chorus]
[Instrument: Kick In]
[Instrument: Chamber Strings In]
[Dynamic: f]
[Male lead, commanding, twang bleeding under]
I wear it WELL — I'm not alright
A gentleman's decline in evening light
I bow and I smile and I hold the line
(I'm comin' apart)
The mask is the only thing still holdin' tight
I wear it well — I'm not alright

[Outro]
[Instrument: Synth Pad Out]
[Instrument: Bass Out]
[Dynamic: Fade Out]
[End]

---

## PRODUCTION NOTES

```
• Key: E minor — minor mode carries the burnout/grief valence (Eerola: mode is
  the #1 emotional cue), while E minor sits perfectly in the baritone's warm
  chest range (G2-E4) so the "commanding" surface reads as effortless control
  even as the words admit collapse. No lift to major = the mask never truly wins.

• Tempo: 116 BPM (Moderato) — a steady midtempo build. Fast enough for the
  four-on-the-floor EDM pulse to drive, controlled enough to feel composed and
  mannered rather than frantic. The steadiness IS the composure.

• Groove/Time-Feel: Straight eighth-note pulse, electric-bass-led, four-on-the-floor
  kick entering at the first chorus. Banjo plays a locked syncopated roll against
  the straight grid — the bluegrass ornament riding the EDM pulse.

• Time Signature: 4/4 — the marching regularity mirrors a man keeping perfect
  outward order.

• Chord Progression (Nashville / actual in E minor):
  Intro:        i – VI (Em – C) — sparse, unresolved, waiting
  Verse:        i – VI – III – VII (Em – C – G – D) — composed, walking, controlled
  Pre-Chorus:   iv – VII – VI (Am – D – C) — rising tension, leaning forward
  Chorus:       i – III – VI – VII (Em – G – C – D) — full, anthemic, precise
  Bridge:       VI – III – iv – i (C – G – Am – Em) — stripped, the descent inward
  Final Chorus: i – III – VI – VII (Em – G – C – D) — same shape, fuller voicing,
                chamber strings doubling, the mask at maximum performance

• Modulation: None — deliberate. The final chorus grows through arrangement and
  dynamics, not a key lift. Refusing the "triumphant" major modulation keeps the
  irony intact: he never actually gets better, he just performs harder.

• Vocal: Smooth warm commanding male baritone (G2-E4), composed and mannered,
  close-mic, precise diction — but with a slight East Tennessee Appalachian lilt
  underneath. ACCENT AS THE MASK SLIPPING: formal performed lines stay crisp
  (mask intact); raw confessional lines and all whispered parentheticals let the
  twang leak through (dropped g's — burnin', runnin', comin', holdin', smilin',
  bein'; "ain't" for "haven't/isn't"). Bridge is heaviest accent — the mountain
  man shows all the way through ("a boy that this town near broke"). The dialect
  itself is a crack in the borrowed elegance. NOT exaggerated country.

• Instruments (by prominence):
  1. Electric bass (leads the groove throughout)
  2. Four-on-the-floor synth pulse / kick (EDM engine, enters chorus 1)
  3. Plucked banjo (bluegrass ornament, syncopated roll)
  4. Bowed cello + chamber strings (Victorian warmth; swell in final chorus)
  5. Rhythmic synth/percussion layers (added one per section = the build)
  6. Light parlor piano (verses, understated)

• Dynamics:
  Intro:        pp — restrained, composure intact ↗
  Verse 1:      mp — controlled, close ↗
  Pre-Chorus:   mp → mf — leaning forward ↗↗
  Chorus:       mf — full band, precise ↗↗
  Verse 2:      mp — pulled back but more layered underneath ↘↗
  Pre-Chorus:   mf — rising again ↗↗
  Chorus:       mf → f ↗↗↗
  Bridge:       p — stripped bare, the mask slips ↘↘↘
  Final Chorus: f — biggest, most precise moment, full band ↗↗↗↗
  Outro:        f → pp — instrumental fade ↘↘

• Hook Type: Title/confession hook — "I wear it well — I'm not alright."
  Placement: full chorus lands ~30s in (after a short restrained intro + one
  verse + pre-chorus). It is the first and last line of every chorus, and the
  emotional-state confession formula (elegant "I wear it well" + raw "I'm not
  alright"). Clippable moment = bridge-into-final-chorus (~15-25s standalone).

• Rhyme Scheme:
  Verse: ABCB (conversational, lets the elegant/plain contrast breathe)
  Pre-Chorus: AA couplet (tight, propulsive — pushes into the hook)
  Chorus: ABAB with the hook line bookending (well/light/line/apart/alright —
    slant rhymes preferred over forced perfect, keeps it human)
  Bridge: ABCB loosening toward free — the composure coming undone in the rhyme too
  Final Chorus: same as chorus + one added line ("The mask is the only thing
    still holding tight") = the meaning shifts after the bridge's confession.

• Emotional Arc: From performed composure ("I'm keeping fine," crisp diction) through
  the strain of the performance ("runnin' on empty for the show," accent leaking) to
  the mask fully slipping in private ("a boy that this town near broke," "I'm so tired
  of bein' fine," heaviest twang) and finally to a commanding final chorus where he
  performs harder than ever — crisp on the surface, mountain bleeding underneath —
  precisely because the mask is now the only thing holding him together.

• Accent Design: East Tennessee Appalachian lilt used as a structural device, not
  decoration. Crisp formal diction on the performed lines (the mask); dropped g's,
  "ain't," and mountain phrasing on the raw/whispered lines (the truth). The accent
  escalates through the song — barely there in V1's formal opening, leaking by the
  pre-choruses, fully present in the bridge. The contrast between borrowed elegance
  and native twang IS the tension: a working-class man dressing his collapse in
  language he wasn't raised in.
```

---

## SLIDER RECOMMENDATIONS (optional)

Only if your Suno UI exposes sliders. These are v5.5-era starting points (see the original file):
Weirdness 60% · Style Influence 90% · Audio Influence 30% (only with an inspiration track).
