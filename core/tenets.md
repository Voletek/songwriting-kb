# Creative Tenets — Decision-Making Principles

> **Purpose:** When methodology rules conflict with each other or with creative intent,
> these tenets establish PRIORITY. They answer: "Which principle wins?"
>
> **Usage:** Referenced by songwriter and critic agents during conflict resolution.
> Not always-on (too heavy for every session) — loaded when a judgment call is needed.
>
> **These are not rules.** Rules live in `core/methodology/`. Tenets are PRIORITIES —
> they determine which rule wins when rules fight each other.

---

## Tenet 1: EMOTION OVER MECHANICS

> When prosody rules and emotional truth conflict, serve the emotion —
> unless the mechanical discipline itself is what makes the emotion hit harder.

**What this means in practice:**
- A 14-syllable line that devastates the listener stays. Flag it, acknowledge it, keep it.
- A reversed stress that IS the character's anxiety is an intentional choice, not a violation.
- BUT: if trimming a line from 14 to 10 syllables makes it hit HARDER (compression = power), then the discipline served the emotion and should win.
- The question is never "does this follow the rule?" — it's "does this SERVE the feeling?"

**When to invoke:**
- Prosody lint flags a line that emotionally works
- A bridge is "too long" by guidelines but the turn needs the space
- Structure rules suggest cutting something that earns its length emotionally

**Academic basis:**
- **Pattison (Berklee):** Prosody is the "appropriate RELATIONSHIP between elements" — not rigid syllable enforcement. The relationship serves meaning.
- **Juslin (BRECVEMA):** Musical emotion is induced through 8 mechanisms (contagion, expectancy, etc.) — none of which are "correct syllable count."
- **Dodge et al. (2025):** "Authenticity" ranks alongside "Technical Prowess" as a universal evaluation criterion. A daring imperfect work outscores a safe polished one on Scope of Vision.

---

## Tenet 2: SHOW OVER TELL (For Scene-Building)

> Physical, sensory imagery is preferred over abstract statement for scene-building.
> Direct statement is permitted — and often powerful — for hooks and bridge turns
> where raw confession IS the emotional mechanism.

**What this means in practice:**
- Verses: SHOW. "Kitchen floor, back against the fridge" > "I hit rock bottom"
- Pre-choruses: SHOW with building tension. Sensory details escalate.
- Hooks/Choruses: TELL permitted. "I don't know what to do" works BECAUSE it's direct confession, not imagery.
- Bridge turns: TELL permitted. "The silence isn't the end / It's where the real talk begins" — clarity of the TURN matters more than image.
- Production Direction: SHOW. "The room should SOUND like silence" > "make it quiet"

**When to invoke:**
- Critic flags a "tell" line in a chorus that's working as a raw confession hook
- A bridge turn needs to STATE the thesis clearly for the final chorus to land differently
- A verse is using abstract language where physical detail would connect more

**Academic basis:**
- **Pattison:** "Sense-bound imagery" for engagement. BUT: his own teaching distinguishes verse (specific/narrative) from chorus (universal/thematic). Choruses CAN be more abstract.
- **Nashville A&R:** The hook must be INSTANTLY understood. "I Will Always Love You," "Someone Like You," "I Can't Make You Love Me" — all direct statement. Imagery lives in verses.
- **Dodge et al.:** "Beauty" as a criterion encompasses both vivid imagery AND devastating simplicity. Both are valid artistic modes.

---

## Tenet 3: THE METHOD SERVES THE ARTIST

> The methodology is a tool, not a master. If the artist has a clear creative intent
> that conflicts with a creative guideline, the artist wins. Document the departure.
>
> **Exception:** Compliance constraints are non-negotiable regardless of artistic intent.

**Creative choices (artist can override):**
- Rhyme scheme (AABB instead of ABCB default — if intentional)
- Song length (7 minutes instead of 3:30-4:30 — if the art needs it)
- Structure (through-composed instead of verse-chorus — if intentional)
- Genre fusion ratio (50/50 instead of 70/30 — if they want the tension)
- Key choice (against the emotion table — if they hear something different)

**Compliance constraints (NON-NEGOTIABLE):**
- Character limits (Style ≤1000, Lyrics ≤5000) — Suno rejects these
- Artist name conversion — legal/ethical requirement
- Required format elements ([Title:], [Production Direction:], [Vocal Direction:]) — songs won't render without them
- Section tags on own lines — Suno parsing requirement
- [end] tag — prevents runaway generation

**When to invoke:**
- User insists on keeping something the methodology says to change
- A creative choice violates a guideline but serves a clear artistic purpose
- Distinguishing "this breaks a rule" from "this breaks a requirement"

**Academic basis:**
- **Fabbri (genre theory):** Genres are cultural processes negotiated by communities, not laws imposed by academics. The artist PARTICIPATES in genre, doesn't submit to it.
- **Moore:** "The analyst does not dictate to the music what it should mean." Music exists on its own terms.
- **Dodge et al.:** "Innovation" is a universal criterion — deliberately breaking conventions IS valued when it serves artistic intent with awareness. (Innovation without craft awareness is ignorance, not art.)

---

## Tenet 4: ONE SOURCE OF TRUTH

> Every rule lives in one canonical place (`core/methodology/`). When content is needed
> elsewhere, reference it — never create a competing authority.
>
> Context-appropriate summaries are acceptable when files may be loaded independently,
> but the canonical definition always wins on conflicts.

**What this means in practice:**
- `core/methodology/*.md` = the canonical method. If it says X, that's what X is.
- `.kiro/agents/*.md` = thin loaders. They REFERENCE the method, never restate it differently.
- `.kiro/steering/*.md` = quick-reference subsets. If a steering rule contradicts core/, core/ wins.
- The same principle (e.g., "12-syllable max") may APPEAR in multiple methodology files (songwriting AND critique) because both need it in their own context — that's acceptable as long as the DEFINITION is consistent.
- When updating a rule: update the canonical source FIRST, then sync any summaries.

**When to invoke:**
- Two files say different things about the same rule
- Someone proposes adding methodology content to a steering file (should be in core/ instead)
- An agent is duplicating instructions that should live in the methodology it loads

**Basis:**
- Software engineering: Single Source of Truth (SSOT) prevents drift
- Knowledge management: canonical sources + contextual views = maintainable systems
- Repository history: the `.kiro/` agents duplicating methodology content is what caused the `[Title:]` tag incident — the steering knew the rule but the agent didn't load it

---

## Tenet 5: RENDER-READY OR NOT DONE

> When the songwriter agent produces a FINAL song output, it must be render-ready —
> pasteable into Suno's three fields (Style / Lyrics / Exclude) with character counts
> confirmed and all required tags present.
>
> Intermediate work (brainstorms, critiques, revisions in progress) has no render requirement.

**What this means in practice:**
- The songwriter agent's FINAL output = ready to paste into Suno. No further formatting needed.
- A critique output = NOT required to be render-ready (it's analysis, not a song)
- A brainstorm/idea = NOT required to be render-ready (it's exploration)
- A revision-in-progress = NOT required to be render-ready (it's still being worked)
- The distinction: did the agent produce a SONG FILE, or did it produce WORK TOWARD a song?

**When to invoke:**
- Someone says "is this done?" — the answer includes render-readiness as a criterion
- An output is missing Style Prompt, tags, or Production Notes — it's not done yet
- Distinguishing a draft (acceptable without formatting) from a deliverable (must be complete)

**Academic basis:**
- **Record production theory (Moylan, Moore):** In popular music, the recording IS the primary text. The song doesn't fully exist until it's rendered. Production decisions are creative decisions — they're not optional polish.
- **Nashville method:** A song isn't pitched until the demo is competitive. The demo format IS part of the writing process, not something added after.
- **Platform reality:** Suno won't accept unformatted text. An unrendered song is hypothetical.

---

## Tenet 6: UNIVERSAL RESONANCE

> Specificity creates universality. Physical emotional experience over plot information.
> Individual tracks should resonate without requiring external context,
> while album sequences reward deeper listening.

**What this means in practice:**
- "Kitchen floor, back against the fridge" > "I hit rock bottom" (specific physical > generic abstract)
- A concept album track should EMOTIONALLY connect even if the listener doesn't know the plot
- Plot-specific exposition ("He told me of the Syndicate") should be converted to emotional experience ("He told me things that rearranged the dark")
- Character-specific dialect/accent is FINE — it's still emotional truth through a specific lens
- Album callbacks and motifs REWARD deep listeners without REQUIRING them for basic emotional connection

**When to invoke:**
- A lyric explains plot instead of expressing feeling
- A concept album track requires reading the blueprint to make emotional sense
- Deciding between a specific image and a generic phrase (always choose specific)
- Balancing accessibility (new listener) with depth (dedicated fan)

**Academic basis:**
- **Pattison:** "Specificity creates universality" — his core teaching. "Everyone lost someone, but only YOU lost them at that specific diner at 2am on a Tuesday."
- **Juslin (Episodic Memory):** One of the 8 BRECVEMA mechanisms — music triggers personal memories. This requires touching UNIVERSAL experiences. Plot doesn't trigger episodic memory; emotion does.
- **Dodge et al. (Generosity of Spirit):** Does the song GIVE something to the listener? Can they find themselves in it without a prerequisite? Generosity = emotional accessibility without condescension.
- **Concept album precedent:** Pink Floyd, Radiohead, Kendrick Lamar — all create albums that work as individual emotional experiences AND sequential narratives. Individual accessibility + sequential reward = the proven standard.

---

## Tenet 7: PLATFORM-NEUTRAL CRAFT

> The craft methodology (how to write, how to critique, how to design voice) must work
> without any specific tool. Platform-specific optimization (Suno formatting, Kiro automation)
> is a LAYER on top of the craft, not embedded within it.

**What this means in practice:**
- `core/methodology/songwriting.md` should be followable by someone using ChatGPT, Claude, pen and paper, or no AI at all
- Suno-specific tags, char limits, and slider recommendations are in a SEPARATE layer (references/SUNO_*, suno-optimization methodology)
- Kiro-specific wiring (.kiro/agents, hooks, steering) is automation that CONSUMES the methodology — it IS NOT the methodology
- If Suno disappears tomorrow, the craft method still works. Only the optimization layer needs replacing.
- If Kiro changes its format, only the .kiro/ adapter needs updating. core/ survives untouched.

**When to invoke:**
- Someone proposes embedding Suno-specific rules into the core craft methodology
- A methodology file references `.kiro/` paths (should reference core/ or references/ instead)
- Distinguishing permanent craft knowledge from volatile platform behavior
- Suno updates break something — the fix should be in the platform layer, not core craft

**Academic basis:**
- **All sources (Moore, Tagg, Pattison, Fabbri, Juslin, Moylan):** None reference a specific platform. Music theory, prosody, semiotics, genre theory, emotion psychology — all predate digital tools. The knowledge is inherently platform-neutral.
- **Record production theory:** Production techniques evolve (analog → digital → AI) but PRINCIPLES (space, timbre, dynamics, proximity) remain constant across all technologies.
- **Software architecture (separation of concerns):** Business logic should be independent of implementation layer. The method = business logic. The platform = implementation.
- **Suno community evidence:** Tag behavior is version-dependent. What worked in v4.5 may not work in v5.5. This IS a volatile layer that must be separable from permanent knowledge.

---

## How Tenets Are Used

### By the Songwriter Agent

Check tenets when:
- A methodology rule would produce a worse emotional result than breaking it
- The user's creative intent conflicts with a guideline (but not a compliance constraint)
- Choosing between two valid approaches that the methodology doesn't disambiguate
- Auto-pilot mode: tenets inform the "best choice" when no user preference is stated

### By the Critic Agent

Check tenets when:
- Scoring a line that breaks a rule but works emotionally (Tenet 1 → don't flag as issue)
- A song is technically strong but emotionally flat — or emotionally powerful but technically rough (Tenet 1 → which matters more for the score?)
- A "tell" line in a chorus that functions as raw confession (Tenet 2 → don't flag it)
- The Suno Optimization Assessment suggests changes that would harm the lyrics (Tenet 3 → artist intent wins on creative choices)
- An album track requires plot knowledge to connect (Tenet 6 → flag for universalization)

### By the Builder Agent

Check tenets when:
- Setting up an album blueprint: remind user that individual tracks should be emotionally accessible (Tenet 6)
- Configuring preferences: respect user's creative intent even if unconventional (Tenet 3)
- Organizing project structure: maintain one source of truth (Tenet 4)

---

## Tenet Priority Order

When tenets THEMSELVES conflict (rare but possible):

```
1. EMOTION OVER MECHANICS        ← highest priority (the whole point is feeling)
2. THE METHOD SERVES THE ARTIST  ← artist intent is sovereign for creative choices
3. UNIVERSAL RESONANCE           ← accessibility matters
4. SHOW OVER TELL                ← craft principle
5. RENDER-READY OR NOT DONE      ← completion standard
6. ONE SOURCE OF TRUTH           ← architecture principle
7. PLATFORM-NEUTRAL CRAFT        ← lowest priority (implementation concern)
```

**Example conflict:** Tenet 5 (render-ready) says add all tags. But Tenet 1 (emotion) says the tags are cluttering the creative flow during drafting. Resolution: Tenet 1 wins during DRAFTING (don't interrupt flow), Tenet 5 wins for FINAL OUTPUT (must be render-ready before delivery).
