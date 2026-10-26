# SOP 08: Contributing (Community Guide)

> How to use this system for your own projects, add your own album,
> customize preferences, and contribute back.

---

## For New Users: Getting Started

### Step 1 — Clone the Repo

```bash
git clone https://github.com/Voletek/songwriting-kb.git
```

The `.kiro/` directory configures Kiro with all agents, skills, hooks, and steering. (On Kiro Web, hooks don't run and project agents are available for sub-agent delegation only — run the `tools/` scripts manually there.)

### Step 2 — What You Get Immediately (Universal)

These work for ANY songwriter with zero customization:
- 6 agents (song-planner, songwriter, critic, suno-optimizer, album-continuity, builder)
- 5 skills (song-critique, suno-meta-tags, music-theory, character-voice, concept-album-blueprint)
- 2 hooks — Kiro v1 JSON in `.kiro/hooks/`: `song-validate.json` (runs `tools/validate-song.py` on create/save of song files under `songs/`) and `prosody-lint.json` (runs `tools/lyric-lint.py` on save)
- 2 manual steering commands: `/quick-score` and `/full-pipeline` (`.kiro/steering/quick-score.md`, `.kiro/steering/full-pipeline.md`)
- Example album continuity hooks in `examples/albums/*/continuity-hook.json` (copy into `.kiro/hooks/` to enable)
- 9 SOPs (writing, critiquing, optimizing, album setup, extending, character voice, full pipeline, contributing, planning)
- Full songwriting knowledge base (13 sections)
- Full music production theory (13 disciplines + 23-point framework + 18 advanced concepts)
- Suno references: V6 tag dictionary + discovery/results log (`references/V6_TAG_REFERENCE.md`, `references/V6_TAG_DISCOVERY.md`) and the v5.x tag reference with 100+ tags (legacy, `references/SUNO_TAGS_REFERENCE.md`)
- Rhyme & lyric craft reference (`references/RHYME_AND_LYRIC_CRAFT.md`)
- Deterministic tools: `tools/validate-song.py`, `tools/lyric-lint.py`, `tools/check-repo.py`
- Character voice design system

### Step 3 — What You Should Customize

These files contain templates — personalize them:

| File | What to Do |
|---|---|
| `.kiro/steering/output-preferences.md` | Edit with YOUR output format preferences |
| `.kiro/steering/concept-album.md` | Generic framework — leave as is; add your album's own conditional steering file (see `examples/albums/`) |
| `.kiro/agents/album-continuity.md` | Point its `resources:` blueprint entry at YOUR blueprint and configure YOUR rules |
| `references/YOUR_ALBUM_BLUEPRINT.md` | Replace with YOUR album blueprint (or delete if no album) |
| `songs/` | Put YOUR songs here (ships empty apart from its README) |

**Example albums** live only in `examples/albums/` (`fractured-shadows/` and `keeper-of-the-light/`, each with `BLUEPRINT.md`, `steering.md`, and `continuity-hook.json`) — study them for format reference, then copy patterns to your active files. There are no example blueprints in `references/`.

---

## Setting Up Your Own Preferences

### Step 4 — Create Your Preferences File

Edit `.kiro/steering/output-preferences.md` directly — it ships as a generic template.

See `examples/preferences/voletek-preferences.md` for a filled-in reference implementation showing all options.

Customize:
- What should Production Notes include? (minimum: Key, Tempo, Chords, Vocal, Instruments)
- What's your preferred rhyme scheme?
- What are YOUR hit formulas (your audience, your genre)?
- How do you format duets?
- Any personal conventions?

---

## Setting Up Your Own Concept Album

### Step 5 — Follow SOP 04

Use SOP 04 (Setting Up a Concept Album) to create:
1. Your Album Blueprint in `references/YOUR_ALBUM_BLUEPRINT.md` or `references/[YOUR_ALBUM]_BLUEPRINT.md`
2. Your steering file in `.kiro/steering/[your-album].md` (`inclusion: fileMatch`)
3. (Optional) Your continuity hook: copy `examples/albums/<album>/continuity-hook.json` to `.kiro/hooks/[your-album]-continuity.json` (Kiro v1 JSON) and edit its matcher and prompt

### Step 6 — Update the Concept Album Blueprint Skill

Edit `.kiro/skills/concept-album-blueprint/SKILL.md`:
- Change the blueprint path in its "read …" instruction to YOUR blueprint (e.g. `references/YOUR_ALBUM_BLUEPRINT.md`)
- Update the rule list to YOUR rules

**How files get loaded (by file type):**
- **Steering files** (`.kiro/steering/*.md`) can embed another file with the include syntax `#[[file:path]]` — e.g. `#[[file:references/YOUR_ALBUM_BLUEPRINT.md]]`. That syntax is documented for steering only.
- **Agents** (`.kiro/agents/*.md`) load files through `resources:` front matter, e.g. `resources: ["file://references/YOUR_ALBUM_BLUEPRINT.md"]`.
- **Skills** reference files by plain path with an explicit "read X" instruction.

### Step 7 — Update the Album Continuity Agent

Edit `.kiro/agents/album-continuity.md`:
- Point the blueprint entry in its `resources:` front matter at YOUR blueprint
- Replace specific rule checks with YOUR rules
- Replace the key map with YOUR key map
- Replace the emotional arc with YOUR arc

---

## Contributing Back to the Community

### What We Accept

| Type | Examples | Requirements | Target File |
|---|---|---|---|
| **Knowledge base additions** | New genre conventions, new Suno tag findings, new theory | Must be sourced, verified, and universal | `SONGWRITING_KNOWLEDGE_BASE.md` or `MUSIC_PRODUCTION_THEORY.md` |
| **Suno tag findings** | New confirmed tags, updated tag behavior | Must be tested and verified (log the experiment in `experiments/suno/`) | V6: `references/V6_TAG_DISCOVERY.md` results log; v5.x: `references/SUNO_TAGS_REFERENCE.md` |
| **New skills** | Genre-specific skills (metal songwriting, hip-hop production) | Must follow SKILL.md format with reference doc | `.kiro/skills/[new-skill]/` |
| **New hooks** | Additional quality checks | Kiro v1 JSON (`.kiro/hooks/*.json`); must be useful to >1 person | `.kiro/hooks/` |
| **Bug fixes** | Incorrect tag syntax, outdated Suno info | Must include evidence of the fix | Relevant file |
| **SOPs** | New procedures for workflows not covered | Must follow SOP format | `.kiro/sops/` |
| **Example albums** | YOUR completed album blueprint as a reference | Helps others see how a filled system looks | `examples/albums/<album>/` (`BLUEPRINT.md`, `steering.md`, `continuity-hook.json`) |

### What We Don't Accept

- Personal preferences as universal rules
- Unverified Suno tag claims (test first)
- Genre opinions disguised as facts
- Style prescriptions ("you SHOULD write in minor keys")

### How to Submit

1. Fork the repo
2. Create a branch: `contribution/[your-addition]`
3. Add your content following existing format (see also the root `CONTRIBUTING.md`)
4. Verify: no personal references in universal files (search for your album name, character names, or personal details — these should only appear in personal files)
5. Run the checks: `python3 tools/check-repo.py` (include/resource paths, hook schema, steering front matter, JSON) and `python3 tools/validate-song.py songs/` if you touched songs
6. Submit PR with description of what you're adding and why

---

## File Organization Rules

### Universal Files (Don't Put Personal Content Here)
```
SONGWRITING_KNOWLEDGE_BASE.md
MUSIC_PRODUCTION_THEORY.md
references/*.md (except YOUR_ALBUM_BLUEPRINT.md / your own blueprints)
core/methodology/*.md
core/tenets.md
.kiro/steering/songwriting.md
.kiro/steering/suno-formatting.md
.kiro/steering/output-preferences.md
.kiro/steering/concept-album.md
.kiro/agents/songwriter.md
.kiro/agents/critic.md
.kiro/agents/suno-optimizer.md
.kiro/agents/song-planner.md
.kiro/agents/builder.md
.kiro/steering/quick-score.md
.kiro/steering/full-pipeline.md
.kiro/skills/*/SKILL.md
.kiro/hooks/song-validate.json
.kiro/hooks/prosody-lint.json
.kiro/sops/*.md
tools/*.py
```

### Personal Files (Customize These)
```
.kiro/agents/album-continuity.md (configure YOUR rules)
.kiro/steering/[your-album].md (create for YOUR album)
.kiro/hooks/[your-album]-continuity.json (optional — copy from examples/albums/<album>/continuity-hook.json)
references/YOUR_ALBUM_BLUEPRINT.md (replace with YOUR blueprint)
references/[YOUR_ALBUM]_BLUEPRINT.md
songs/**/*
```

### Example/Reference Files (Study, don't edit)
```
examples/albums/*/          (BLUEPRINT.md, steering.md, continuity-hook.json per album)
examples/songs/
examples/analysis/
examples/preferences/
```

---

## Example: Starting From Scratch

```bash
# Clone
git clone https://github.com/Voletek/songwriting-kb.git
cd songwriting-kb

# Edit preferences (already a generic template — just fill in your conventions)
# See examples/preferences/voletek-preferences.md for a filled-in reference
nano .kiro/steering/output-preferences.md

# Optional: remove (or replace) the example albums and songs — they are all under examples/
# (songs/ already ships empty, so there is nothing personal to delete there)
rm -rf examples/albums/fractured-shadows examples/albums/keeper-of-the-light
rm -rf examples/songs examples/analysis

# Create your own album (follow SOP 04)
# Put your blueprint at references/YOUR_ALBUM_BLUEPRINT.md (or references/<ALBUM>_BLUEPRINT.md),
# add .kiro/steering/<your-album>.md, and optionally .kiro/hooks/<your-album>-continuity.json

# Check the repo still wires up correctly (flags any active .kiro/ file that still points at removed examples)
python3 tools/check-repo.py

# Start writing songs (follow SOP 01)
# Use the full pipeline (SOP 07) for best results
```

---

## FAQ

**Q: Do I need a concept album to use this system?**
A: No. The songwriter agent, critic, suno-optimizer, and all knowledge base files work for standalone songs. The album continuity system is optional.

**Q: Can I use this without Kiro IDE?**
A: Yes. The knowledge base files, SOPs, and reference docs work with any AI assistant. The agents/skills/hooks/powers are Kiro-specific features but the CONTENT they contain is universal. SOPs (in `.kiro/sops/`) are tool-agnostic procedures — follow them with any AI assistant or manually. Run `python3 tools/validate-song.py` and `python3 tools/lyric-lint.py` yourself for the deterministic checks the hooks would otherwise run.

**Q: Do I need to use Suno?**
A: No. The songwriting methodology (9-step, 12-category rubric, Nashville method) works for any songwriting — human performance, other AI tools, or traditional recording. The Suno-specific sections (V6 tags, formatting, legacy v5.5 sliders/features) are only relevant if using Suno.

**Q: Can I use this for genres not covered in the knowledge base?**
A: Yes. The framework is genre-agnostic. The theory, prosody, and arrangement principles apply to any style. If you write metal, hip-hop, jazz, or country — the 9-step analysis still works. You'd just apply different genre conventions in Step 6.
