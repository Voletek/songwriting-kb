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
| `fractured_shadows_act1/` | Fractured Shadows — Act 1 | 8 (7 songs + T7 V6 version) | Digital dissolution → transfer |
| `fractured_shadows_act2/` | Fractured Shadows — Act 2 | 11 (10 songs + T17 V6 version) | Survival → integration |
| `fractured_shadows_act3/` | Fractured Shadows — Act 3 | 2 (T18 + its V6 version) | In progress (T18 Edge of the Rift) |
| `keeper_of_the_light/` | Keeper of the Light | 2 (T1 + its V6 version) | Folk-horror concept track |
| `standalones/` | Non-album singles | 13 (8 songs, revision variants, 2 V6 versions, 1 brief) | Duets, mental health, experimental, V6-format references (solo + duet) |
| `experimental/` | Stress tests | 4 (3 songs) | Deliberately flawed tracks for critic testing + a revision progression |

## Canonical vs Draft Versions

- `_v2` / `_v3` / `_RAW` / `_SUNO_READY` suffixes are revision history. When several versions of a song exist, the highest version (or `_SUNO_READY` over `_RAW`) is the canonical one.
- `standalones/I_Wear_It_Well_V6.md` is the V6-format reference (Style / Exclusions / V6 lyric tags / `[End]`); `I_Wear_It_Well.md` is the pre-V6 original.
- `standalones/What_If_DUET_V6.md` is the V6 duet reference (Duet Mode B: main voice + `()` response, voice roles declared in the Style Prompt, a `## RENDER SETTINGS` block with the voice left for the user to choose); `What_If_DUET.md` is the pre-V6 original.
- V6 versions of the album exemplars, same words and Style Prompt re-tagged in V6 grammar (not yet rendered on V6):
  - `fractured_shadows_act1/07_Rikan_V6.md` (from `07_Rikan_v2.md`)
  - `fractured_shadows_act2/17_Both_Names_V6.md` (from `17_Both_Names.md`)
  - `fractured_shadows_act3/18_Edge_of_the_Rift_V6.md` (from `18_Edge_of_the_Rift.md`)
  - `keeper_of_the_light/01_The_Keepers_Morning_V6.md` (from `01_The_Keepers_Morning.md`)

  Each opens with a 'What changed' table. The originals, `I_Wear_It_Well.md` and `What_If_DUET.md` included, are kept as v5.5-era archives and carry the legacy marker.
- Songs marked `<!-- song-format: legacy ... -->` are archived examples that predate (or deliberately sit outside) the current format standard: the pre-V6 songs (the early v5-era songs, `standalones/Three_In_The_Morning.md`, `experimental/The_Wound_Speaks.md`, and the v5.5-era originals of the six V6 migrations above), and `From_The_Floor_To_The_Fire.md`, whose V6 system-generated tags are kept verbatim. The validator downgrades their missing direction blocks / end tag to WARN; character limits still FAIL. Don't use the marker on new songs.
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
