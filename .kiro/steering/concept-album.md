---
inclusion: auto
name: concept-album
description: Concept album framework — setting up an album blueprint, album-specific conditional steering, continuity hooks, the album extension protocol, and universal album continuity rules. Use for album setup, continuity checks, track registries, and blueprint work.
---

# Concept Album — Continuity System

> Auto-included (`inclusion: auto`) when a request is about concept albums, continuity, or blueprints.
> If you have an active album, add a conditional steering file for it (see `examples/albums/`).

---

## How the Album System Works

When working on a concept album, you need three things:

1. **Album Blueprint** — The complete continuity document: track registry, hard rules, sonic palette, character voices, key relationships, motifs, callbacks. Your own blueprint lives in `references/YOUR_ALBUM_BLUEPRINT.md` (or `references/<ALBUM>_BLUEPRINT.md`). The bundled examples live in `examples/albums/fractured-shadows/BLUEPRINT.md` and `examples/albums/keeper-of-the-light/BLUEPRINT.md`.
2. **Conditional Steering File** (in `.kiro/steering/`) — A summary of hard rules that loads only when matching album files are in context. Uses `inclusion: fileMatch`.
3. **Continuity Hook** (optional, in `.kiro/hooks/`) — A Kiro v1 JSON hook that fires on agent-made saves of album song files and asks the agent to check the hard rules.

## Setting Up Your Album

Follow **SOP 04** (Setting Up a Concept Album) for the full procedure. Quick version:

1. Create your blueprint: `references/YOUR_ALBUM_BLUEPRINT.md` (template provided)
2. Create conditional steering: `.kiro/steering/your-album.md` with front matter (must be the first bytes of the file):
   ```yaml
   ---
   inclusion: fileMatch
   fileMatchPattern: "songs/your_album_dir/**"
   ---
   ```
3. (Optional) Create a continuity hook: copy `examples/albums/<album>/continuity-hook.json` to `.kiro/hooks/<album>-continuity.json` (Kiro v1 schema) and edit its matcher and prompt for your album
4. Configure the album-continuity agent with YOUR blueprint and rules

See `examples/albums/` for two complete reference implementations.

## ALBUM EXTENSION PROTOCOL

**⚠️ STOP — Before writing ANY track outside your current registry:**
1. Update your Album Blueprint with new track registry (including Persona/voice assignment)
2. Extend the sonic palette evolution map
3. Define which existing rules carry forward vs which are act-specific
4. Get the blueprint update committed BEFORE writing new songs
5. Use SOP 05 — supports sequels, prequels, and insertions

Failure to follow this protocol creates cascading continuity errors.

## Universal Album Rules

These apply to ANY concept album regardless of genre:

1. **No two adjacent tracks should share >70% instrument palette** — sonic differentiation is mandatory
2. **Recurring phrases must evolve in meaning** — same words, different weight each time
3. **Character voices must be consistent** — same production treatment for the same character across tracks
4. **The sonic pivot (if your album has one) must be clean** — no bleed between sonic worlds
5. **Reserved keys/modes should be protected** — if a key belongs to a character or moment, don't borrow it elsewhere
6. **Named parenthetical layers must be confined to their declared tracks** — no voice leakage

## Reference

When you have an active album blueprint, reference it here (replace the template path with yours):
#[[file:references/YOUR_ALBUM_BLUEPRINT.md]]
