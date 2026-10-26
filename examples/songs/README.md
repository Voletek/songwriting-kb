# Example Songs

These songs were created during development of the songwriting methodology. They demonstrate:
- Complete Suno-ready output format (Style Prompt + Exclusions + Direction blocks + Lyrics + Production Notes)
- The critique/revision pipeline in action (v1 → v2 → v3 progression)
- Concept album continuity across tracks
- Various formatting modes (solo, duet, character voice, cinematic)

---

## Contents

| Directory | Album/Context | Files | Notes |
|---|---|---|---|
| `fractured_shadows_act1/` | Fractured Shadows — Act 1 | 7 | Digital dissolution → transfer |
| `fractured_shadows_act2/` | Fractured Shadows — Act 2 | 10 | Survival → integration |
| `fractured_shadows_act3/` | Fractured Shadows — Act 3 | 1 | In progress (T18 Edge of the Rift) |
| `keeper_of_the_light/` | Keeper of the Light | 1 | Folk-horror concept track |
| `standalones/` | Non-album singles | 12 (8 songs, revision variants, 1 brief) | Duets, mental health, experimental, V6-format reference |
| `experimental/` | Stress tests | 4 (3 songs) | Deliberately flawed tracks for critic testing + a revision progression |

## Canonical vs Draft Versions

- `_v2` / `_v3` / `_RAW` / `_SUNO_READY` suffixes are revision history. When several versions of a song exist, the highest version (or `_SUNO_READY` over `_RAW`) is the canonical one.
- `standalones/I_Wear_It_Well_V6.md` is the V6-format reference (Style / Exclusions / V6 lyric tags / `[End]`); `I_Wear_It_Well.md` is the pre-V6 original.
- Songs marked `<!-- song-format: legacy ... -->` are archived examples that predate (or deliberately sit outside) the current format standard: the early v5-era songs, and `From_The_Floor_To_The_Fire.md`, whose V6 system-generated tags are kept verbatim. The validator downgrades their missing direction blocks / end tag to WARN; character limits still FAIL. Don't use the marker on new songs.
- `experimental/Broken_Wings_Of_Time.md` carries `<!-- validate: skip ... -->`: it is a deliberately flawed draft for stress-testing the critic, so the validator skips it (lyric-lint still flags its clichés, on purpose).
- `standalones/Shapes_Behind_My_Eyes_DUET_v2.md` and `fractured_shadows_act1/07_Rikan_v2.md` were over the 5000-character Lyrics limit. Their direction blocks are now condensed, and the full original direction is kept in an `ADVANCED BOX (overflow direction)` section.
- `*.brief.md` files are Song Briefs (SOP 09), not songs — the validator and hooks skip them.

## Using These as Templates

Feel free to copy any song file as a starting template for your own work (start from the V6-format reference for new songs). The format includes:
- Style Prompt — ready to paste into Suno's Style field
- `## EXCLUSIONS:` — ready to paste into Suno's Exclude field (plain comma-separated)
- Lyrics — ready to paste into Suno's Lyrics field (includes all direction blocks)
- Production Notes — reference document for arrangement decisions

Check any song with `python3 tools/validate-song.py examples/songs/` and `python3 tools/lyric-lint.py <file>`.

## Album Blueprints

The concept album examples have corresponding blueprints in `examples/albums/`:
- `examples/albums/fractured-shadows/BLUEPRINT.md`
- `examples/albums/keeper-of-the-light/BLUEPRINT.md`

Each album folder also holds its example conditional steering (`steering.md`) and continuity hook (`continuity-hook.json`).
