# Song Length Reference — Targets by Use

> Typical song lengths for radio, streaming, genres, short-form video and sync, with sources, and how
> to check a song against them with `tools/estimate-runtime.py --target <preset>`.
> **These are defaults, not rules.** Song length is the artist's call (`core/tenets.md`, Tenet 3): choose a
> target, override any number, or ignore the check, and note the choice in the song file. The only hard
> limit is technical: one Suno MCP generation is capped at 360 s (longer songs need an extension).
> Researched Nov 23, 2026. Figures are [Tier 2] professional practice or [Tier 3] chart and platform
> observations; they change over time, so re-check yearly.

---

## What the numbers say

| Context | Typical length | Tier | Source |
|---|---|---|---|
| Billboard Year-End Hot 100, 2025 | about 3:24 average, 3:13 median (4:37 around 1990, 3:16 in 2020) | Tier 3 | [Major Mixing, citing a 6,618-song Hot 100 analysis](https://majormixing.com/how-long-should-my-song-be-and-why-it-matters-more-than-you-think/) |
| Billboard #1 hits | median 2:31 (1958–64), 4:11 (1985–95), 3:19 (2019–24); nearly 3 in 10 recent #1s under 3:00 | Tier 3 | [Northeastern University, Billboard #1 database](https://www.khoury.northeastern.edu/home/rachlin/somai/stories/skip-to-the-chorus/index.html) |
| Spotify charting songs, 2024 | about 3:00, roughly 30 s shorter than in 2019 | Tier 3 | [Chartmetric](https://hmc.chartmetric.com/shorter-songs-trend-streaming-history/) |
| Radio play | generally 3–5 min; radio edits shorten long songs, from a few seconds to nearly half | Tier 2 | [Wikipedia: Radio edit](https://en.wikipedia.org/wiki/Radio_edit) |
| Radio edit | usually 3–4 min, reaching the hook faster and ending cleanly | Tier 2 | [Plugg Supply](https://plugg-supply.net/articles/how-to-make-dj-friendly-extended-mix) |
| Pop, hip-hop, R&B | 2:30–3:30 | Tier 2 | [Major Mixing](https://majormixing.com/how-long-should-my-song-be-and-why-it-matters-more-than-you-think/) |
| Rock, indie, alternative | 3:30–4:30 | Tier 2 | same |
| Ballads, jazz, acoustic | 4:00–5:00 | Tier 2 | same |
| EDM / house club mix | 4:00–6:00, with a shorter edit for streaming | Tier 2 | same |
| Spotify stream count | a play counts only after 30 s, so a long intro costs streams | Tier 3 (platform rule) | [Spotify Community](https://community.spotify.com/t5/Other-Podcasts-Partners-etc/30-second-songs/td-p/4841226) |
| Intros | often under 15 s outside cinematic or ambient genres | Tier 2 | [Major Mixing](https://majormixing.com/how-long-should-my-song-be-and-why-it-matters-more-than-you-think/) |
| TikTok / Reels / Shorts | promotion runs on 15–60 s clips built around one section; TikTok's music library allows up to 60 s | Tier 3 | [VideoCreek](https://www.videocreek.com/blog/how-to-promote-a-new-song-with-short-form-video-a-plan-for-independent-artists/), [Soundstripe](https://www.soundstripe.com/blogs/how-long-can-a-song-be-before-copyright-tiktok) |
| Sync (ads, TV, trailers) | 15-, 30- and 60-second cuts, plus instrumentals and clean intros/outros | Tier 2 | [That Pitch](https://thatpitch.com/blog/15-30-and-60-second-cuts), [Foxi Music](https://www.foximusic.com/blog/short-promo-music-video-guide-licensing/) |

Sources were paraphrased; the figures above are the sources' own.

---

## Presets used by the tool

Defined in `tools/data/length_targets.json`. "Hook" is time from the start of the track to the first
chorus. All values are starting points.

| Preset | Use | Length | Intro ≤ | First chorus ≤ |
|---|---|---|---|---|
| `streaming` | Streaming single, playlists | 2:30–3:30 | 15 s | 0:45 |
| `pop` | Pop / hip-hop / R&B | 2:30–3:30 | 15 s | 0:45 |
| `radio` | Radio edit | 3:00–3:45 | 15 s | 0:50 |
| `rock` | Rock / indie / alternative | 3:30–4:30 | 20 s | 1:00 |
| `ballad` | Ballad / acoustic | 4:00–5:00 | 20 s | 1:10 |
| `album` | Album track / story song | 3:00–6:00 | 40 s | 1:30 |
| `cinematic` | Cinematic / folk epic / concept | 4:00–7:00 | 45 s | 1:40 |
| `club` | Club / extended mix | 4:00–6:00 | 60 s | 1:30 |
| `short` | TikTok / Reels / Shorts clip | 0:15–1:00 | 3 s | 0:05 |
| `sync30` | 30-second sync cut | 0:28–0:32 | 3 s | 0:10 |
| `sync60` | 60-second sync cut | 0:57–1:03 | 5 s | 0:20 |

The `streaming`, `pop`, `radio`, `rock`, `ballad` and `club` lengths follow the sources above. The `album`
and `cinematic` presets are this repo's own allowance for story songs and concept tracks (Tier 2), and
the `short` / `sync` hook limits express "the hook is the clip".

---

## Choosing and overriding a target

**Pick per song.** Put a `Length Target:` line anywhere in the song file (for example under the title or
in the Production Notes). The tool reads it automatically:

```
Length Target: radio
Length Target: cinematic, intro <= 40s
Length Target: 5:30-6:30, intro <= 45s, hook <= 1:20     (custom, no preset)
Length Target: none                                       (turn the check off for this song)
```

**Pick per run.** `--target radio`, and override single numbers with `--min 3:00 --max 4:00
--max-intro 20 --max-hook 1:00`. Command-line values beat the song file, which beats the preset.

**Change the defaults for your repo.** Edit `tools/data/length_targets.json`, or create
`tools/data/length_targets.local.json` with the same shape: its presets are merged on top (add new
names or redefine existing ones) and it is git-ignored, so personal targets stay out of the community
defaults.

**When you go outside a target,** the tool reports it as INFO, never as a failure. Note the decision
in the song file (Tenet 3: document the departure), for example: *"Length: 5:59 on purpose (cinematic
story song); radio edit planned."*

---

## Versions for different uses

One song often needs several cuts. Plan them in the song file's release notes (SOP 10, Step 7):

| Version | Target | How |
|---|---|---|
| Album / full | `album` or `cinematic` | The main render |
| Radio edit | `radio` | Shorten the intro, cut instrumental breaks and repeats, keep the hook early. Cut the keeper's own audio in Studio or a DAW so the voice and performance stay the same (SOP 10, Step 5) |
| Short-form clip | `short` | The hook or most striking 15–60 s, starting on it |
| Sync cuts | `sync30`, `sync60` | Edited from stems; also deliver an instrumental |
