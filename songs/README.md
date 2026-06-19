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
├── standalone/            ← Non-album singles
└── README.md
```

## File Naming

- Album tracks: `##_Title_Words.md` (number prefix for ordering)
- Standalones: `Title_Words.md`
- Versions: append `_v2`, `_v3`, `_RAW`, `_SUNO_READY`

## What Triggers Hooks

Files in `songs/**/*.md` trigger:
- **Prosody lint** on save (flags lines >12 syllables)
- **Character count check** on save (Style ≤1000, Lyrics ≤5000)
- **Format validation** on creation (checks required sections)

If you have album continuity hooks configured, they'll fire on saves in matching subdirectories.

## Album Continuity

The album-continuity system works from whatever directory your album bible points to. Put your songs in `songs/my_album/`, set your album bible's track registry to reference that path, and it works. See `examples/albums/` for the configuration pattern.

## CLI Validation

```bash
python3 tools/validate-song.py songs/my_album/*.md
```

## Examples

For reference implementations showing the complete output format, see:
- `examples/songs/fractured_shadows_act1/` — Act 1 (7 tracks, digital dissolution)
- `examples/songs/fractured_shadows_act2/` — Act 2 (10 tracks, survival → integration)
- `examples/songs/fractured_shadows_act3/` — Act 3 (in progress)
- `examples/songs/keeper_of_the_light/` — Folk-horror concept (1 track example)
- `examples/songs/standalones/` — Non-album singles and duets
- `examples/songs/experimental/` — Stress tests and experiments
