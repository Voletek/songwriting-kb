# Examples

> Reference implementations showing how to configure the songwriting system for your own projects.
> These files are NOT active — they're here for you to study and copy from.

---

## What's Here

### `albums/` — Complete Album Configurations

Two fully-realized concept album setups showing how every piece connects:

| Album | Genre | Tracks | Shows You |
|---|---|---|---|
| **Fractured Shadows** | Industrial → Cinematic Rock | 18 (17 in Acts 1–2 + Act 3 in progress) | Large multi-act album, vocal evolution, sonic pivot, named layers, character voices, an in-progress extension (T18) |
| **Keeper of the Light** | Folk-Horror / Sea-Shanty | 8 | Smaller focused album, non-vocal entity design, single Persona with delivery variants |

Each album folder contains:
- `BLUEPRINT.md` — The full album blueprint (the canonical copy; use it as a format reference or copy it to `references/` as your own starting point)
- `steering.md` — The conditional steering file (copy to `.kiro/steering/<album>.md` and configure `fileMatchPattern`)
- `continuity-hook.json` — The continuity check hook, Kiro v1 schema with an `agent` action (copy to `.kiro/hooks/<album>-continuity.json` and edit its matcher and prompt)

### `preferences/` — Format Preference Examples

- `voletek-preferences.md` — One user's complete preference configuration showing all available options filled in with real values

---

## How to Use These

### Setting Up Your Own Album

1. Read through one of the example albums to understand the structure
2. Follow **SOP 04** (Setting Up a Concept Album) to create your own
3. Copy the relevant files to their active locations:
   ```
   examples/albums/<album>/steering.md            → .kiro/steering/<your-album>.md
   examples/albums/<album>/BLUEPRINT.md           → references/YOUR_ALBUM_BLUEPRINT.md
   examples/albums/<album>/continuity-hook.json   → .kiro/hooks/<your-album>-continuity.json
   ```
4. Update file paths and patterns in your copies (the steering `fileMatchPattern`, the hook `matcher`, and the blueprint include at the end of the steering file)

The continuity hook fires only for agent-made saves, in Kiro IDE 1.0+ / Kiro CLI V3 (Kiro Web doesn't run hooks).

### Customizing Preferences

1. Read `examples/preferences/voletek-preferences.md` to see a filled-in example
2. Edit `.kiro/steering/output-preferences.md` with YOUR conventions
3. The active preferences file has comments explaining each section

---

## Don't Edit These Directly

These are reference copies. Edit the ACTIVE files in `.kiro/steering/`, `.kiro/hooks/`, and `references/` instead.

Other example folders: `songs/` (example song files — see `songs/README.md`) and `analysis/` (example critique reports — see `analysis/README.md`).
