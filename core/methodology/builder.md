# The Builder Method

> **CANONICAL METHODOLOGY** -- This file is the single source of truth for project setup and configuration.
> A non-Kiro user can read ONLY this file and interactively set up a new album, configure agents,
> create character voice templates, log experiments, and manage project structure.

---

## Overview

The Builder is the interactive setup specialist. It creates the structures that other agents consume --
album blueprints, steering files, continuity hooks, character voice templates, experiment logs,
and project directories.

**Core principle:** NEVER assume. Always ask the user what they need, gather requirements
conversationally, then generate the correct files in the correct locations.

Every workflow follows the same pattern:
1. Ask questions to gather requirements
2. Confirm the plan with the user
3. Create files in the correct locations
4. Explain what was created and how to use it

---

## 1. Setting Up a New Album

### Gather First

- Album name (kebab-case for dirs, title-case for display)
- Album thesis (one sentence -- the transformation the album tracks)
- Approximate track count (8-17 sweet spot)
- Protagonist/speaker(s)
- Genre/sonic territory
- Rough emotional arc (if they have one)

### Create

1. **Album Blueprint** -- `references/[ALBUM_NAME]_BLUEPRINT.md`
   - Use template from `references/YOUR_ALBUM_BLUEPRINT.md`
   - Fill in what the user provided, mark unknowns as `[TBD]`

2. **Steering File** -- `.kiro/steering/[album-name-kebab].md`
   - Condensed blueprint for quick session reference
   - Include: title, track count, hard rules, palette table, character voices

3. **Continuity Hook** -- `.kiro/hooks/[album-name]-continuity-check.md`
   - Checkbox-format verification rules from the hard rules

4. **Track Registry** -- included in the blueprint
   - Table: #, Working Title, Key, BPM, Core Emotion, Sonic Palette

### Post-Creation

- Tell user to configure album-continuity agent to point at their blueprint
- Remind: commit documentation BEFORE writing songs
- Point to `core/methodology/album-continuity.md` for extension protocol

---

## 2. Creating Character Voice Templates

### Gather First

- Character name and role (protagonist, antagonist, ambient presence, narrator)
- Which tracks they appear in
- Vocal characteristics: register, texture, delivery style
- Production treatment: reverb, effects, spatial positioning
- Voice evolution across the album
- Any voice-specific constraints

### Create

A character entry in the blueprint's Character Voice Registry:

```
CHARACTER: [Name]
- Register: [range]
- Texture: [description]
- Delivery: [how they sound]
- Appears in: [which tracks]
- Production treatment: [reverb, effects, spatial details]
- Evolution: [how their voice changes across tracks]
- Rule: [any voice-specific constraints]
```

For non-vocal presences, adapt to describe sonic manifestation rather than vocal performance.
Update steering file's character voices section after creation.
Reference `core/methodology/character-voice.md` for full voice design theory.

---

## 3. Configuring the Album-Continuity Agent

### Gather First

- Which album blueprint file to point at (confirm it exists in `references/`)

### Do

1. Open `.kiro/agents/album-continuity.md`
2. Replace `#[[file:references/YOUR_ALBUM_BLUEPRINT.md]]` with user's actual blueprint path
3. Confirm methodology load is still present
4. Remind user the agent is read-only -- it verifies, does not create

---

## 4. Setting Up Project Directory Structure

### Gather First

- Album name (kebab-case)
- Whether they need analysis and experiments directories
- Whether they have existing songs to migrate

### Create

```
songs/[album_name]/          -- Song files for this album
analysis/                    -- Critique and continuity reports (shared)
experiments/suno/            -- Suno experiment logs (shared)
```

Rules:
- Song directories use snake_case: `songs/album_name/`
- Each album gets its own song subdirectory
- Analysis and experiments are shared, not per-album
- Create `.gitkeep` in empty directories to preserve in git

---

## 5. Logging Suno Experiments

### Gather First

- Experiment name, claim under test, hypothesis
- Suno settings (style prompt, exclude, weirdness, etc.)
- Variable being changed (for A/B testing)

### Create

Copy `experiments/suno/TEMPLATE.yml` to:
```
experiments/suno/YYYY-MM-DD-[experiment-name].yml
```

Fill in gathered info. Leave `renders:` section with empty placeholders for the user.
Remind: if experiment supports a methodology change, update `promoted_to` field.

---

## 6. Output Preferences Configuration

### Gather First

- Production Notes preference (default: yes)
- Direction block preferences (Production Direction, Vocal Direction)
- Duet format conventions, parenthetical layer usage
- Character limit strategy for Suno
- Hit formula preferences, any custom conventions

### Do

1. Open `.kiro/steering/output-preferences.md`
2. Walk through each section with the user
3. Customize to their preferences (add custom sections at bottom if needed)
4. Remind: this file auto-loads (inclusion: auto) -- all agents respect it

---

## 7. Adding Tracks to an Existing Album

### Gather First

- Which album is being extended?
- How many new tracks?
- Where do they fit? (sequel, prequel, inserted, parallel)
- Does new material continue same character arc and thesis?
- Any new characters or motifs?

### Pre-Extension Gate

Confirm with user:
- Same character arc? Same thesis? Palette evolution makes sense? Narrative reason to stay together?
- **If NO to 2+:** Recommend starting a new album (Section 1).

### Do (Interactive Extension Protocol)

1. Define scope -- extension act, track range, position, numbering convention
2. Update track registry -- add new rows, verify key/BPM/emotion variation
3. Extend sonic palette -- add new range to evolution map
4. Review existing rules -- check each still applies, add new if needed
5. Update character voices -- evolve returning, add new
6. Plan motifs -- existing motif fate + new motifs
7. Verify key relationships -- new keys against existing harmonic architecture
8. Update blueprint -- all sections
9. Update steering file -- condensed reference

### Numbering Convention

| Position | Convention |
|---|---|
| Sequel | Continue sequential (T9, T10...) |
| Prequel | Prefix numbering (P01, P02...) |
| Inserted | Decimal (T3a, T3b) or act headers |
| Parallel | Prefix (S01 or character-initial) |

**Never renumber existing tracks** -- existing rules and cross-references use track numbers.

### Post-Extension

- Commit documentation BEFORE writing new songs
- Remind user to run continuity verification on new tracks

---

## Universal Builder Rules

1. **Ask before creating** -- never generate files without confirming requirements
2. **Confirm before writing** -- show the plan, get approval
3. **Correct locations** -- every file has a canonical home
4. **Explain after creating** -- tell user what exists and how to use it
5. **Reference the methodology** -- point users to canonical docs for deep dives
6. **Commit documentation first** -- structure before content, always

---

## File Location Reference

| File Type | Location |
|---|---|
| Album Blueprint | `references/[ALBUM_NAME]_BLUEPRINT.md` |
| Steering File | `.kiro/steering/[album-name-kebab].md` |
| Continuity Hook | `.kiro/hooks/[album-name]-continuity-check.md` |
| Song Files | `songs/[album_name]/` |
| Experiment Logs | `experiments/suno/YYYY-MM-DD-[name].yml` |
| Output Preferences | `.kiro/steering/output-preferences.md` |
| Character Voice Ref | `references/CHARACTER_VOICE_REFERENCE.md` |
| Continuity Agent | `.kiro/agents/album-continuity.md` |

---

## References

- `core/methodology/album-continuity.md` -- Full album setup and extension methodology
- `core/methodology/character-voice.md` -- Character voice design procedure
- `references/YOUR_ALBUM_BLUEPRINT.md` -- Blueprint template
- `experiments/suno/TEMPLATE.yml` -- Experiment log template
- `.kiro/steering/output-preferences.md` -- Output format configuration
