# Songs Directory

**Your songs go here.** This directory is intentionally empty — it's YOUR workspace.

Example songs (from the developer's concept albums and standalone work) are in `examples/songs/` for reference.

---

## Suggested Structure

```
songs/
├── [your_album_name]/     ← Your album tracks (one folder per album)
│   ├── 01_Track_Title.md
│   ├── 02_Track_Title.md
│   └── ...
├── experimental/          ← Works in progress, experiments
├── standalones/           ← Non-album singles
└── README.md
```

## File Naming

- Album tracks: `##_Title_Words.md` (number prefix for ordering)
- Standalones: `Title_Words.md`
- Versions: append `_v2`, `_v3`, `_RAW`, `_SUNO_READY` (the highest version is canonical)
- Song briefs (SOP 09): `Title_Words.brief.md` next to the song

## What Triggers Hooks

Song files under `songs/` trigger two Kiro v1 hooks (`.kiro/hooks/*.json`):
- **`song-validate.json`** on create and save → `python3 tools/validate-song.py --hook <file>` (char counts Style ≤1000 / Lyrics ≤5000, required elements, V6 tag checks, exclusions format)
- **`prosody-lint.json`** on save → `python3 tools/lyric-lint.py --hook <file>` (syllables, stress, rhyme type/scheme, section stability, clichés)

`README.md` and `*.brief.md` files are skipped. File-event hooks fire only for agent-made file changes, and run in Kiro IDE 1.0+ and Kiro CLI V3. **Kiro Web sessions don't run hooks** — run the tools manually there (see below).

If you copied an album continuity hook into `.kiro/hooks/` (`<album>-continuity.json`), it fires on saves in its matching subdirectory.

## Album Continuity

The album-continuity system works from whatever directory your album blueprint points to. Put your songs in `songs/my_album/`, set your album blueprint's track registry to reference that path, and it works. See `examples/albums/` for the configuration pattern.

## CLI Validation

```bash
python3 tools/validate-song.py songs/                 # recursive; --json, --strict
python3 tools/lyric-lint.py songs/my_album/01_Track_Title.md
```

## Examples

For reference implementations showing the complete output format, see:
- `examples/songs/fractured_shadows_act1/` — Act 1 (7 tracks, digital dissolution)
- `examples/songs/fractured_shadows_act2/` — Act 2 (10 tracks, survival → integration)
- `examples/songs/fractured_shadows_act3/` — Act 3 (in progress — T18 Edge of the Rift)
- `examples/songs/keeper_of_the_light/` — Folk-horror concept (1 track example)
- `examples/songs/standalones/` — Non-album singles and duets (`I_Wear_It_Well_V6.md` = V6-format reference)
- `examples/songs/experimental/` — Stress tests and experiments
