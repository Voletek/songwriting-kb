# SOP 10 — Rendering and Revising Through the Suno MCP

> Step-by-step procedure for turning a validated song file into Suno renders from an agent, checking the
> renders against the plan, fixing what didn't land without starting over, and finishing the song.
> Agent: **renderer** (`.kiro/agents/renderer.md`). Field and tool reference:
> `references/SUNO_MCP_REFERENCE.md`. Formatting rules: `.kiro/steering/suno-formatting.md`.
> Without the Suno MCP, follow the same steps by hand in the suno.com UI (paste the three fields from
> `python3 tools/suno-fields.py <file>`).

---

## Before You Start

- The song has passed SOP 03 (optimized) and SOP 07 Stage 5 (verified): `validate-song.py` has no FAIL.
- The Suno MCP server is connected: `account-me` returns the user's profile.
- **Credits are the user's money.** Each `audio-create` call makes 2 songs. Stems cost 10 or 50 credits,
  MIDI 10, and a download may spend a download credit. Say what a step costs and get a yes before the
  first paid call in a session, and before any call that repeats one.
- Never publish (`audio-settings`), change remix permission, or turn on Max Mode unless the user asks.

---

## Step 1 — Pre-flight

```bash
python3 tools/validate-song.py --strict songs/<category>/<song>.md   # no FAIL; read every WARN
python3 tools/lyric-lint.py songs/<category>/<song>.md               # prosody readout
python3 tools/estimate-runtime.py songs/<category>/<song>.md         # length and first-chorus timing
```

1. Fix every FAIL. A **Suno Rejected Words** FAIL means Suno will refuse the render: swap the word.
2. If `estimate-runtime.py` warns that the song runs past 360 s, plan an extension (Step 5b) instead
   of trimming the song to fit.
3. Run `account-usage`: note `credits_remaining` and `allowed_models`.
4. **Ask which voice to use. Every time, before every paid call** (render, cover, extension, section
   edit), even if a voice was used earlier in the session. Run `voices-list` (both `own` and `loved`) and
   offer the user's saved voices by name, or "no saved voice (Suno generates a singer)". Never default
   silently: a call without `voice_id` gets a freshly generated singer. Record the answer, and pass it
   as `voice_id` on that call and every later call for the same song. If a call type may not keep the voice
   (section edits, see Step 5), say so before sending and let the user choose.
5. Decide the other settings with the user: model (`v6` unless they choose), `vocal_gender` only when
   no voice is used, and any sliders. Sliders are optional;
   record any non-default value.

**Length:** if you send `duration`, also send `duration_strict: false`, or Suno cuts the song off at the
target, even mid-outro. Leave `duration` out to let Suno choose.

---

## Step 2 — Render

```bash
python3 tools/suno-fields.py songs/<category>/<song>.md --no-counts   # title, style, negative_style, lyrics
```

1. Call `audio-create` with those four fields plus the settings from Step 1 and a new
   `idempotency_key` (for example `<song>-<revision>-<yyyy-mm-dd>`). Change the key whenever the input changes.
2. Call `audio-wait` once with **every** id in `clip_ids`.
3. If a clip comes back `error`, read its `error` text:
   - *"Your tags contain artist name X"*: replace X in the song file, add X to
     `tools/data/suno_rejected_words.txt` with the date and song, revalidate, and resend with a new key.
     Rejected generations have not been charged so far (check `account-usage`).
   - Anything else: report it to the user with the clip id before retrying.
4. Add one row per clip to the song file's `## RENDERS` section (format below) and give the user both
   links (`song_url`).

---

## Step 3 — Verify against the plan

Ears decide, but measure first so the conversation is about facts.

1. **`audio-analysis`** on each clip (free; poll until `status` is `complete`). Compare with the
   Production Notes:

   | Production Notes | Analysis field |
   |---|---|
   | Tempo | `bpm` (within about ±5 is a match) |
   | Time Signature | `time_signature` (3 = 3/4, 4 = 4/4) and the largest `bar_position` |
   | Key | `key` (whole-track; it won't show a short modulation) |
   | Structure | `sections` (repeated labels are repeated material, usually the chorus) |
   | Instruments / Vocal | `terms`, `labels` |

2. **`audio-listen`** (free; up to 5 open questions, 200 a day) for what the analysis can't measure.
   Ask about the specific tags you used, and ask for a JSON block so the answer can be logged. A
   reusable question:

   > Check this render against its arrangement plan: meter (3/4 or 4/4?), key and any key change
   > (where, to what?), length of the instrumental intro, whether the bridge strips back as planned,
   > whether the final chorus is the biggest, whether [named vocal or instrument cues] are audible,
   > and how it ends. End with a JSON block with fields: meter, key_changes, intro_s,
   > bridge_stripped, final_chorus_biggest, instruments, ending.

   Read the answer with `audio-listen-wait`.
3. Mark each planned element as landed, partial or missed in the `## RENDERS` row.
4. Log tag results in `references/V6_TAG_DISCOVERY.md` → Results Log: one row per render, with the tag
   tested and what happened. A finding needs 3+ different songs before it is promoted (see
   `experiments/suno/README.md`).
5. Ask the user which take they prefer. Their ears overrule the measurements.

---

## Step 4 — Decide

| Situation | Next step |
|---|---|
| One take is right | Step 6 (finish) |
| Most of a take is right, one section missed (a key change, a bridge strip, a bad line) | Step 5a (section edit) |
| The song needs to run longer than 6:00, or ends too early | Step 5b (extend) |
| The arrangement or genre is wrong everywhere, but the lyrics are right | Step 5c (cover), or change the Style Prompt and render 2 more takes |
| Several elements missed on every take | Change the tags or Style in the song file, save it as a new version (`_v2`, `_v3`), revalidate, and render 2 more takes. Tags shape probability: render at least 3-4 takes before concluding a tag doesn't work. |
| The lyrics need rework | SOP 07 Stage 3 (revise), then re-critique |

---

## Step 5 — Fix without a full re-render

> **Voice check before any Step 5 call.** Covers and extensions take `voice_id`: pass the song's voice.
> Whether a section edit (`reference_audio_ids`) honours `voice_id` is **untested** (the schema doesn't
> say). A large edit re-sings the song, so the voice can drift away from the saved one (observed: a multi-cut radio edit came back with a
> different, alternating singer). For a radio edit or any multi-section cut of a take with a saved voice,
> prefer cutting the take's own audio in Suno Studio or a DAW, or a cover with the shortened lyrics and
> the `voice_id`. Tell the user which route keeps their voice before spending credits.
> **Proofread every `description`** before sending: Suno acts on all of it, including half-finished thoughts.

### 5a. Section edit
`audio-create` with `reference_audio_ids: [<the take>]` and a plain-language `description` naming
the song by title and the time range or section, e.g. *"In Lantern Road, redo 4:55–5:15 as a quiet
warm passage in F major, then return to D minor for the outro."*
- Send only that song, and no `style`, `lyrics`, `duration`, `instrumental` or `vocal_gender`
  (those regenerate the whole song).
- Changing words in more than 5 places re-sings the whole song as a cover.
- Costs a normal generation (2 songs).

### 5b. Extend
`audio-extensions-create` with the take's `id` and `continue_at` (seconds), plus `lyrics` for the
continuation (and `style` if it should change). The new clip holds only the continuation: join the chain
with `audio-full-song` on the last extension (free, up to 20 segments).

### 5c. Cover
`audio-covers-create` with the take's `id` and a new `style`. Pass the lyrics again in `lyrics`, or the
cover comes out instrumental. `controls.audio_influence` sets how close it stays to the source.

Log every fix as its own `## RENDERS` row, with the parent clip id.

---

## Step 6 — Finish

1. Record the keeper in `## RENDERS` (verdict: **keeper**).
2. **Stems** (optional, 10 credits for `two`, 50 for `twelve`): `audio-stems-create`, then
   `audio-stems-retrieve` until `complete`. Apply the stem-matched plugins from `plugins/` in Suno Studio
   (each plugin names the stem it is built for; see `plugins/README.md`), or mix in a DAW. Pitch-shifting
   a single section is a DAW job.
3. **MIDI** (optional, 10 credits): `audio-midi` for charts or rebuilding parts by hand.
4. **Download** (optional): `audio-download` (mp3 or wav). If it answers `requires_credit`, ask before
   calling again with `confirm: true`.

---

## Step 7 — Release checklist (optional)

Only when the user is releasing the song. Ask before each public step.

- [ ] Keeper chosen and noted in `## RENDERS`
- [ ] Title final (consider a subtitle if the title collides with a film or famous song)
- [ ] Caption written (`audio-edit` `caption`, ≤500 characters); lyrics on suno.com match the file
      (`audio-edit` `lyrics` changes the text only, never the audio)
- [ ] Word timings for a lyric video or captions (`audio-lyrics-alignment`, free)
- [ ] Platform cut: a shorter edit if the full song runs long (extend or edit from the keeper)
- [ ] Versions: solo and duet versions if the song suits both (cover with a `voice_id`, or a duet rewrite via SOP 01)
- [ ] Publish (`audio-settings` `visibility: public`) **only on the user's request**

---

## The `## RENDERS` section

Every song file ends with a render log after the Production Notes (the validator ignores everything
after `[End]`). One row per clip, newest at the bottom:

```markdown
## RENDERS

| Date | Model | Clip ID | Settings | Measured | Verdict |
|---|---|---|---|---|---|
| 2026-11-23 | v6 | [`<clip id>`](https://suno.com/song/<clip id>) | male vocals, duration 359 (soft), default sliders | 133 BPM, D minor, 4/4; intro ~22 s | Take B. Bridge strip landed; F major lift missed. |
```

- **Settings:** everything you sent besides the three fields (model, voice, sliders, duration, edit
  description and parent clip for fixes).
- **Measured:** the `audio-analysis` values and anything `audio-listen` timed.
- **Verdict:** what landed, what missed, and **keeper** for the chosen take.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Clip `error`: "artist name X" | Suno's artist filter matched a word | Step 2.3 |
| 400 on `description` + `style` | Mixed simple and custom mode | Custom mode: `lyrics` + `style`; section edits: `description` + `reference_audio_ids` only |
| 403 on `controls`, `negative_style` or `vocal_gender` | Plan lacks advanced controls | Drop the field; put exclusions in the Style as a last resort |
| Outro cut off | `duration` sent with `duration_strict` left on | Resend with `duration_strict: false`, or extend the take |
| Lyrics ignored in a cover | Covers don't carry lyrics over | Pass `lyrics` again |
| Meter or key change ignored | Tags shape probability; Suno defaults to 4/4 | Render more takes; strengthen the Style (meter word early, e.g. "6/8 lilting folk waltz"); then a section edit |
