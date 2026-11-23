# Suno MCP Reference — Rendering Songs from an Agent

> How to send a finished song file to Suno through the Suno MCP server (`audio-create`), which song-file
> section goes in which field, and what the server enforces.
> Also lists the read tools (GET requests) and the values each one takes, and the modification and
> Studio-style tools (edits, extensions, covers, mashups, stems, MIDI) with their costs.
> Field lists taken from the Suno MCP tool schemas (Nov 23, 2026). Behaviour notes are [Tier 3]:
> observed in renders, version-dependent. Re-check the schema if a call is rejected.
> Formatting rules for the fields themselves: `.kiro/steering/suno-formatting.md` and
> `core/methodology/suno-optimization.md` → V6 Procedure.

---

## Two modes

| Mode | Send | Use for |
|---|---|---|
| **Custom** (our default) | `lyrics`, usually with `style`, `negative_style` and `title` | Every song written with this KB |
| **Simple** | `description` only; Suno writes lyrics and style | Quick sketches, remixes and edits of existing songs |

Mixing the modes returns `400`: `description` can't be sent with `style`, or with `lyrics` unless
`instrumental` is `true`.

---

## Song file → MCP fields

| Song-file section | MCP field | Limit | Notes |
|---|---|---|---|
| `## RENDER SETTINGS:` | `voice_id`, `model`, `controls`, `duration` | — | Written by the renderer after asking the user (SOP 10 Step 1); exported by `suno-fields.py` |
| `## STYLE PROMPT:` | `style` | 1000 chars | Same text as the UI's Style of Music box |
| `## EXCLUSIONS:` | `negative_style` | 1000 chars | Plain comma-separated text, no dash prefix. Needs your own `style` (not valid with `description`). |
| `## LYRICS:` from `[Title: …]` through `[End]` | `lyrics` | 5000 chars | Paste exactly what `validate-song.py` counts. Leave out the Production Notes. |
| `[Title: …]` | `title` | 256 chars | Send the title as its own field as well as in the lyrics |
| Song Thesis, Production Notes, revision notes | — | — | Never sent. They stay in the file as reference. |

The server enforces the same 1000 / 5000 limits as the UI, so the KB's field limits hold for V6 through the
MCP.

---

## All `audio-create` fields

### Content

| Field | Type | What it does |
|---|---|---|
| `lyrics` | string, ≤5000 | Custom lyrics |
| `style` | string, ≤1000 | Genre and style text |
| `negative_style` | string, ≤1000 | Styles to steer away from (the Exclude field). Needs the advanced-controls grant. |
| `title` | string, ≤256 | Song title |
| `description` | string, ≤3000 | Simple mode prompt |
| `instrumental` | bool, default `false` | No vocals. A `voice_id` overrides it. |

### Voice and model

| Field | Type | What it does |
|---|---|---|
| `model` | string | `v6`, `v6-wild` or `v6-mini` (whatever `account-usage` lists under `allowed_models`). Omit for the plan default; name the model you send. |
| `vocal_gender` | `male` / `female` | Forces vocal gender. Needs the advanced-controls grant. A `voice_id` takes precedence. |
| `voice_id` | string | One of your saved suno.com voices (`voices-list`). Must be ready. Always sings. **Ask the user which voice before every call** (SOP 10 Step 1); without it, Suno generates a new singer. Untested with section edits (`reference_audio_ids`); large edits re-sing the song and the voice can drift. |

### Length

| Field | Type | What it does |
|---|---|---|
| `duration` | int, 15–360 s | Target length. A target, not a guarantee. |
| `duration_strict` | bool | Hard-caps the clip at `duration`; a song that would overrun is cut off, even mid-outro. **On by default whenever `duration` is set.** |
| `duration_guidance` | bool | Sizes Suno-written lyrics to `duration`. Custom lyrics are never rewritten. |

Set `duration_strict: false` when you send a `duration` for a full song, or the outro can be truncated.
The cap is 360 s (6:00), so songs planned longer than that can't be targeted in one generation.

### Sliders (`controls` object)

Needs the advanced-controls grant on the plan (403 without it).

| Field | Range | UI equivalent | What it does |
|---|---|---|---|
| `style_influence` | 0–1 | Style Influence % ÷ 100 | How strictly `style` is followed |
| `weirdness` | 0–1 | Weirdness % ÷ 100 | How far the result may drift from expected |
| `variety` | integer 0–4 | Variety: Off / Normal / High / Extra / Max | How far the style tags are reinterpreted before generation |
| `audio_influence` | 0–1 | Audio Influence % ÷ 100 | How closely vocals match `voice_id`. Only valid with a `voice_id` (400 otherwise). |

Omit a slider to keep the model's default. `0` is a real setting, not "unset". The slider presets in
`core/methodology/suno-optimization.md` (Step 11) are v5.5-era percentages: divide by 100 to send them,
and treat them as starting points to re-validate on V6.

### Other

| Field | What it does |
|---|---|
| `max_mode` | Max Mode: more compute for consistency, charged at a multiple of the credits. Only when the user asks for it by name. |
| `reference_audio_ids` | Up to 10 of the user's finished songs to remix, sample, restyle, mash up, split stems from, or edit. Simple mode only; say what to do in `description`. |
| `midi_upload_id` | A MIDI score for the song to play. Needs `v6-wild`; simple mode only. |
| `workspace_id` | Files the new song in a workspace (`workspaces-list`) |
| `idempotency_key` | Makes retries safe: repeating a key with the same input returns the original request instead of new, charged songs. Change the key whenever the input changes. |

---

## Render workflow

1. Run `python3 tools/validate-song.py --strict <file>` and `python3 tools/lyric-lint.py <file>`. Fix every FAIL.
2. Check credits and allowed models with `account-usage`.
3. Call `audio-create` in custom mode with the fields above and a fresh `idempotency_key`.
4. Call `audio-wait` once with **every** id in `clip_ids`. Each call makes 2 songs, charged to the user's
   credits, so confirm before making several calls at once.
5. A clip is playable when `status` is `streaming` (its `song_url` works) and finished at `complete`.
   On `error`, read the clip's `error` text, fix the song file, revalidate and resend with a new key.
6. Log which tags rendered as intended in the `references/V6_TAG_DISCOVERY.md` results log.

Related tools: `audio-listen` / `audio-analysis` (hear or analyse a finished render),
`audio-extensions-create`, `audio-covers-create`, `audio-edit`, `audio-stems-create`,
`library-search` / `library-list`.

---

## Read tools (GET requests)

The MCP exposes tools, not raw HTTP requests. These are the ones that read data; the schemas map
several of them to API GET routes (`GET /v0/audio/{id}`, `GET /v0/library`, `GET /v0/account/usage`).
Taken from the tool schemas on 2026-11-23. Most need no values; only the first group requires any.

### Read tools that require a value

| Tool | Required | Optional |
|---|---|---|
| `audio-retrieve` | `id` (song ID) | — |
| `audio-stems-retrieve` | `id` (song ID), `group_id` (from `audio-stems-create`) | — |
| `playlists-list-clips` | `id` (playlist ID, from `playlists-list`) | `cursor`, `limit` (1–50, default 10) |
| `sequence-get` | `id` (Sequence ID, from `sequence-list`) | `view`: `full` (default) or `summary` |

### Read tools with only optional values

| Tool | Optional values |
|---|---|
| `library-list` | `limit` (1–50, default 10), `cursor`, `liked`, `downloaded`, `visibility` (`public` / `private`), `origin` (`upload` / `cover` / `extension` / `remaster`), `workspace_id` |
| `library-search` | Same as `library-list`, plus `query` (1–200 chars, matched against title or style) |
| `library-liked` | `limit` (1–50, default 10), `cursor` |
| `playlists-list` | `limit` (1–50, default 25), `cursor`, `query` |
| `workspaces-list` | `cursor`, `query` |
| `voices-list` | `collection` (`own`, default, or `loved`), `limit` (1–100, default 20), `cursor`, `query` (name, or a voice ID) |
| `sequence-list` | `limit` (1–20, default 20), `cursor`, `query` |
| `visuals-library` | `limit` (1–50, default 20), `cursor`, `liked`, `media_type` (`image` / `video`), `sequence_id`, `song_id` (can't be combined with `media_type`, `liked` or `sequence_id`) |
| `characters-list` | `presets` |
| `visuals-show` | `ids` (up to 10, comma-separated), `at` (up to 4 frame times for one video) |

### Read tools that take no values

`account-me`, `account-usage`, `visuals-models`.

### Checking a finished render

| Tool | Required | Optional | Notes |
|---|---|---|---|
| `audio-wait` | `id` or `ids` (up to 12) | `until`: `playable` (default) or `complete` | Waits about 50 s per call; call again if still pending |
| `audio-analysis` | `id` | — | Beats, BPM, meter, key, sections and a description of the audio. Free. Poll until `status` leaves `processing`. |
| `audio-listen` | `id`, `question` (≤2000 chars) | — | Suno's music agent answers a question about the song. Free, but it starts a job: read the answer with `audio-listen-wait`. Limits: 5 open questions, 200 a day. |
| `audio-download` | `id` | `format` (`mp3` default, or `wav`), `confirm` | Can spend a download credit. Call without `confirm`; if it answers `requires_credit`, ask the user before calling again with `confirm: true`. |

Use `audio-analysis` and `audio-listen` to check whether a render followed the tags (tempo, meter, key
change, section order) before logging results in `references/V6_TAG_DISCOVERY.md`.

### Common rules

- **Paging:** list tools return `next_cursor`; pass it back as `cursor`. With a `query`, send the same
  `query` on each page. Filtered pages can be short or empty and still have a cursor.
- **Lyrics:** library, liked and playlist results leave out `metadata.lyrics`. Only `audio-retrieve`
  returns lyrics, and only for the user's own songs.
- **Access:** library tools need a suno.com sign-in with library permissions; an API key gets 403.
  Visuals and Sequence tools return 404 without visuals access.
- **IDs:** song IDs come from a creation's `clip_ids` or a library listing. Playlist, workspace and
  Sequence IDs come from `playlists-list`, `workspaces-list` and `sequence-list`.
- `audio-settings` is a write tool (publish, unpublish, remix permission), not a read. Only use it when
  the user asks.

---

## Modification and Studio-style tools

Taken from the tool schemas on 2026-11-23. The MCP can change a song's audio and do several Studio
jobs (stems, MIDI, word timings), but it has **no access to Studio itself**: no editor, timeline,
mixing, EQ, effects, mastering or pitch shifting, and it can't run the Studio audio-effect plugins in
`plugins/`. Do those steps in Suno Studio or a DAW.

### Changing a song's audio

| Tool | What it does | Required | Cost |
|---|---|---|---|
| `audio-create` with `reference_audio_ids` | Edits a finished song: change a few words, redo a time range, add or cut a section, add or drop an instrument. Describe the change in `description`, naming the song by title (never an ID or link). The closest thing to Studio's Replace Section. | `description`, `reference_audio_ids` (the one song) | A normal generation (2 songs) |
| `audio-extensions-create` | Continues a song from `continue_at` seconds. The new clip holds only the continuation. Takes the same `style`, `lyrics`, `negative_style`, `controls` and length fields as `audio-create`. | `id`, `continue_at` (≥0.4 s) | A normal generation |
| `audio-full-song` | Joins an extension chain into one track (up to 20 segments: the source plus 19 extensions). Name only the last extension. | `id` | Free; retries return the same join |
| `audio-covers-create` | Re-renders a song in a new style or voice. The source's lyrics are **not** carried over: pass them again in `lyrics` to keep the vocals, or the cover comes out instrumental. | `id` | A normal generation |
| `audio-mashups-create` | Blends exactly two songs | `id`, `additional_audio_id` | A normal generation |

All sources must be `complete`. A source can also be any suno.com song the user may remix (404 if they
can't see it, 403 if they can't remix it, 503 while it is still finishing).

**Edit rules (`reference_audio_ids`):** pass only the song being edited, and send no `duration`,
`instrumental` or `vocal_gender`, which regenerate the whole song. A small edit keeps the rest of the
original audio. Changing words in more than 5 places re-sings the whole song as a cover.

**Slider meaning changes per tool:** in extensions, covers and mashups, `controls.audio_influence` sets
how closely the result stays to the source audio (in `audio-create` it only applies to a `voice_id`).

### Studio-style tools

| Tool | What it does | Required | Cost |
|---|---|---|---|
| `audio-stems-create` | Splits a song into stems, two takes each, as suno.com's Get Stems does. `two`: vocals + instrumental (4 stems). `twelve`: vocals, backing vocals, drums, bass, guitar, keyboard, percussion, strings, synth, FX, brass, woodwinds (24 stems). Read the result with `audio-stems-retrieve`. | `id`, `mode` (`two` / `twelve`) | 10 credits for `two`, 50 for `twelve` |
| `audio-midi` | Transcribes a song or stem to a multi-track `.mid` file, as Studio does. Needs a Premier plan. Call again with the same `id` until `status` is `ok`. | `id` | 10 credits; free if already transcribed, or for a Get Stems stem. Tell the user the cost first. |
| `audio-lyrics-alignment` | The timing of each sung word, for karaoke or captions | `id` | Free |

Stems are ordinary songs in the library, so every read tool works on a stem's `audio_id`. A stem can't
be split again, and the source can be at most 16 minutes.

### Metadata only

`audio-edit` changes a song's `title`, `lyrics` text or `caption` (≤500 chars) on suno.com. It does
**not** change the audio: editing lyrics there won't re-sing anything, it only re-aligns the word timings.

### Adding vocals to an existing instrumental

suno.com's "add vocals/lyrics to this song" (sing a lyric sheet over an uploaded or existing instrumental,
keeping the bed unchanged) has **no MCP equivalent**. `reference_audio_ids` is simple mode and takes no lyric
sheet; `audio-covers-create` regenerates the instrumental. Do these runs on suno.com and log the clip.
Because the bed is fixed, its meter and arrangement survive: this is the reliable way to keep a non-4/4
meter that text-only renders lose. Lyric tags that ask the instrumental to change do nothing there.

**Through the MCP, the closest route is a cover of the instrumental** (`audio-covers-create` on the bed,
with `lyrics`, `style`, `voice_id` and `controls.audio_influence` ~0.8). It regenerates the bed, so the key
can move, but it kept a 3/4 meter on 4 of 4 takes in testing. See SOP 10, Step 5d.

### Not Studio

The `sequence-*`, `image-create`, `video-create` and `visuals-*` tools make music videos and images,
not audio edits.

### When to use which

| Goal | Tool |
|---|---|
| One section didn't render as tagged (e.g. a missed key change) | `audio-create` edit on that song, describing the section and time range. Cheaper than a full re-render. |
| A song ends too early, or needs to run past the 6:00 cap | `audio-extensions-create`, then `audio-full-song` |
| Same song, different arrangement or genre | `audio-covers-create`, passing the lyrics again and the `voice_id` |
| Sing lyrics over an existing instrumental (keep its meter) | suno.com "add vocals", or `audio-covers-create` on the instrumental with lyrics and `voice_id` (SOP 10, Step 5d) |
| Radio edit of a voiced take | Cut the take's audio in Studio or a DAW (keeps the voice), or a cover with shortened lyrics and `voice_id` |
| Mixing, mastering, effects, or a pitch-shifted final section | Stems from `audio-stems-create`, then Suno Studio or a DAW |
| Chart the arrangement or rebuild parts by hand | `audio-midi` |

---

## Observed behaviour [Tier 3]

| Date | Observation | Source |
|---|---|---|
| 2026-11-23 | The style text "fireside-skald menace" was rejected on both clips: *"Your tags contain artist name skald"*. Suno's artist filter matches ordinary words that are also band names (Skáld is a Nordic folk band), lowercase included. Replacing the word fixed it. | Render test |
| 2026-11-23 | The rejected generation was not charged: `credits_remaining` was unchanged after the error. | `account-usage` before and after |
| 2026-11-23 | A broad `audio-listen` question reported a stripped bridge and a final spoken line as missing; `audio-lyrics-alignment` and narrow follow-up questions showed both present. Confirm misses before paying for fixes (SOP 10 Step 3). | Render test |
| 2026-11-23 | A song made with suno.com "add vocals" over a 3/4 instrumental kept 3/4; text-only renders of the same lyrics came out 4/4 on 3 of 4 takes. | Render test |
| 2026-11-23 | Covers of a 3/4 instrumental with lyrics (Audio Influence 0.8, Variety 1) kept 3/4 on 4 of 4 takes; the key moved (the bed is regenerated). | Render test |
| 2026-11-23 | Applying a `voice_id` to a cover, Suno replaced the sent Style with its own rewrite (`metadata.style`). | Render test |
| 2026-11-23 | A section edit (`reference_audio_ids`) asking for several timed cuts (a radio edit) re-sang the song: the singer changed, one extra section was cut, and the second take lost the meter. | Render test |
| 2026-11-23 | One `audio-create` call returned 2 clip ids; both reached `streaming` within the first `audio-wait` call. | Render test |

`tools/validate-song.py` checks a fixed list of artist names and does not yet catch genre-adjacent band
names like "skald". When Suno rejects a word, add it here and swap it for a plain descriptor
(e.g. "storyteller", "bard").
