---
inclusion: auto
description: Framework for managing concept album continuity — how to set up album bibles, conditional steering, continuity hooks, and universal album rules.
---

# Concept Album — Continuity System

> Auto-loaded. Provides the framework for managing concept album continuity.
> If you have an active album, add a conditional steering file for it (see examples/albums/).

---

## How the Album System Works

When working on a concept album, you need three things:

1. **Album Bible** (in `references/`) — The complete continuity document: track registry, hard rules, sonic palette, character voices, key relationships, motifs, callbacks.
2. **Conditional Steering File** (in `.kiro/steering/`) — A summary of hard rules that auto-loads when you open album files. Uses `inclusion: fileMatch` so it only appears when relevant.
3. **Continuity Hook** (in `.kiro/hooks/`) — Automated check that fires on file save and verifies rules aren't violated.

## Setting Up Your Album

Follow **SOP 04** (Setting Up a Concept Album) for the full procedure. Quick version:

1. Create your bible: `references/YOUR_ALBUM_BIBLE.md`
2. Create conditional steering: `.kiro/steering/your-album.md` with front-matter:
   ```yaml
   ---
   inclusion: fileMatch
   fileMatchPattern: "songs/your_album_dir/**"
   ---
   ```
3. Create continuity hook: `.kiro/hooks/your-album-continuity.json`
4. Configure the album-continuity agent with YOUR rules

See `examples/albums/` for two complete reference implementations.

## ALBUM EXTENSION PROTOCOL

**⚠️ STOP — Before writing ANY track outside your current registry:**
1. Update your Album Bible with new track registry (including Persona assignment)
2. Extend the sonic palette evolution map
3. Define which existing rules carry forward vs which are act-specific
4. Get the bible update committed BEFORE writing new songs
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

When you have an active album bible, reference it here:
#[[file:references/YOUR_ALBUM_BIBLE.md]]
