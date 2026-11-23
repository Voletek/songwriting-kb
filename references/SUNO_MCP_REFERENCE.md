# Suno MCP Reference — Rendering Songs from an Agent

> How to send a finished song file to Suno through the Suno MCP server (`audio-create`), which song-file
> section goes in which field, and what the server enforces.
> Field list taken from the `audio-create` tool schema (Nov 23, 2026). Behaviour notes are [Tier 3]:
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
| `voice_id` | string | One of your saved suno.com voices (`voices-list`). Must be ready. Always sings. |

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

## Observed behaviour [Tier 3]

| Date | Observation | Source |
|---|---|---|
| 2026-11-23 | The style text "fireside-skald menace" was rejected on both clips: *"Your tags contain artist name skald"*. Suno's artist filter matches ordinary words that are also band names (Skáld is a Nordic folk band), lowercase included. Replacing the word fixed it. | Violent Night, rev 1 |
| 2026-11-23 | The rejected generation was not charged: `credits_remaining` was unchanged after the error. | `account-usage` before and after |
| 2026-11-23 | One `audio-create` call returned 2 clip ids; both reached `streaming` within the first `audio-wait` call. | Violent Night, rev 1 and rev 2 |

`tools/validate-song.py` checks a fixed list of artist names and does not yet catch genre-adjacent band
names like "skald". When Suno rejects a word, add it here and swap it for a plain descriptor
(e.g. "storyteller", "bard").
