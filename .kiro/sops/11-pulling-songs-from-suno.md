# SOP 11 — Pulling Songs from Suno (Library, Workspaces, Share Links)

> Step-by-step procedure for finding songs in the user's suno.com account through the Suno MCP, turning a
> chosen take into a song file the other SOPs can work on, and deciding which workspace new renders go to.
> Agent: **renderer** (`.kiro/agents/renderer.md`). Field reference: `references/SUNO_MCP_REFERENCE.md` →
> Workspaces and Read tools. Everything in this SOP is free: it only reads, except Step 6 (filing songs),
> which changes the user's library and needs a yes first.

---

## Before You Start

- The Suno MCP is connected: `account-me` returns the user's profile.
- Know what the user wants to pull: a share link (`suno.com/s/…`), a song link (`suno.com/song/<id>`), a
  workspace link (`suno.com/create?wid=<id>`), a title, or "the songs in workspace X".
- Personal songs belong on the user's personal branch, not on `main` (`songs/README.md` → Branches).

---

## Step 1 — Ask which workspace

Run `workspaces-list` (no arguments; `query` to search by name) and show the user their workspaces by
**name and song count**. Ask:

1. **Which workspace to pull from**, or "the whole library".
2. **Which workspace new renders should go into** (Step 6 and SOP 10), or "none" (unfiled).

Never assume a workspace from an earlier song or session. Record both answers in the song file's
`## RENDER SETTINGS` as `source_workspace:` and `workspace:` / `workspace_id:` (SOP 10, Step 1).

A link with `?wid=<id>` names the workspace already: confirm it by name from `workspaces-list` instead of
asking again.

---

## Step 2 — Find the song

| What the user gave | Call |
|---|---|
| Workspace (`wid=` or a name from Step 1) | `library-list` with `workspace_id`, `limit` 50; page with `cursor` |
| A title or style words | `library-search` with `query` (add `workspace_id` to search one workspace) |
| A song link `suno.com/song/<id>` | `audio-retrieve` with that `id` |
| A share link `suno.com/s/<code>` | It doesn't contain the song id. Resolve it: the link redirects to `/song/<id>?sh=<code>` (an HTTP HEAD request shows the `location`), or search the library by the title shown on the share page. Never guess between takes: confirm the id |
| "Liked songs" | `library-liked` (songs by anyone) or `library-list` with `liked: true` (own songs) |

Show the results as a table: **title, length, created date, id (first 8 characters)**. Most titles have two
takes with the same name: tell them apart by length, date and `metadata.style`, and ask which one.

List results leave out lyrics. Collaborators' songs in a shared workspace aren't listed by `library-list`.

---

## Step 3 — Retrieve the chosen take

`audio-retrieve` with the `id`. Note from `metadata`:

| Field | Goes to |
|---|---|
| `lyrics` | `## LYRICS:` (as sung; see Step 4) |
| `style` | `## STYLE PROMPT:` (it may be Suno's rewrite, not what was typed) |
| `negative_style` | `## EXCLUSIONS:` |
| `description` | Keep under a **Source Fields** section (simple-mode or add-vocals prompts often hold exclusions and a timed plan) |
| `model`, `controls`, `voice_id`, `duration` | `## RENDER SETTINGS:` |
| `cover_audio_id` | `cover_of:` in `## RENDER SETTINGS` (the song is a cover of that clip) |
| `type`, `created_at`, `song_url` | The file header and the `## RENDERS` row |

A take with `lyrics: "[Instrumental]"` or no lyrics is an instrumental: it can be a bed for SOP 10 Step 5d.

---

## Step 4 — Make the song file

1. Save the fields **exactly as sent** under a `## SOURCE FIELDS` section, so nothing is lost.
2. Build the working sections from them: `## STYLE PROMPT:`, `## EXCLUSIONS:`, `## RENDER SETTINGS:`,
   `## LYRICS:`. If the lyrics were pasted without headings or tags, keep every word and format them with
   SOP 03 (V6 tags, no end-of-line punctuation).
3. Add a `## RENDERS` table and log the pulled take as its first row (date, model, clip id, settings).
4. If the user's original lyrics aren't in the repo yet, save them as `<Title>_RAW.md` with
   `<!-- validate: skip -->`.
5. Run `python3 tools/validate-song.py --strict <file>` and `python3 tools/lyric-lint.py <file>`.

Name it `songs/<category>/<Title>_<Source>.md` when it is one of several versions (for example
`Song_Waltzbed.md` for a version sung over a specific instrumental).

---

## Step 5 — Measure it (free)

Same as SOP 10, Step 3: `audio-analysis` (BPM, meter, key, sections), `audio-lyrics-alignment` (when each
line is sung, and whether any were skipped), and narrow `audio-listen` questions. Fill in the `## RENDERS`
row and the Production Notes' key and tempo with the measured values. Confirm anything reported "missing"
with the word alignment before acting on it.

Then hand the file to the SOP the user wants: SOP 02 (critique), SOP 03 (format), SOP 10 (re-render,
cover, edit, stems).

---

## Step 6 — Filing songs into workspaces (changes the library: ask first)

| Task | Call |
|---|---|
| File new renders when making them | Pass `workspace_id` to `audio-create`, `audio-covers-create`, `audio-extensions-create` or `audio-mashups-create` (from `## RENDER SETTINGS` → `workspace_id`) |
| Move existing songs | `workspaces-update-clips` with the workspace `id` and `add` / `remove` (up to 50 ids each) |
| New workspace | `workspaces-create` with `name` (≤100 chars) and optional `description` |

A song is in **at most one workspace**: adding it to one moves it out of the other. Check `skipped` in the
answer: songs the user may not file are left where they were. Tell the user what moved.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Song from a shared workspace missing | `library-list` only lists your own songs there | Ask the user for the song link and use `audio-retrieve` |
| No lyrics in the list | List results omit `metadata.lyrics` | `audio-retrieve` the chosen take |
| Two takes, same title | Every generation makes 2 | Compare length, date, style; ask the user |
| Share link gives no id | `/s/` codes aren't ids | Resolve the redirect, or search by title (Step 2) |
| Style looks different from what the user typed | Suno rewrote it (e.g. when a voice was applied) | Keep both: stored style in the file, original in Source Fields if known |
