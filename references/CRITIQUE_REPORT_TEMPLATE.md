# Song Critique Report — Template

> Standard template for all professional critique reports.
> Use this format consistently for every critique output.
> Sections marked [CONDITIONAL] are included only when applicable.

---

## Header Block

```markdown
# [Song Title] — Professional Critique

**Date:** [Month Year]
**Version analyzed:** [v1/v2/v3/final] ([brief context — e.g., "first draft," "post-revision," "Suno-ready"])
**Analyzer:** Critic agent (SOP 02 — [variant: Full 3-Layer Model / Concise Re-Critique / Quick Feedback])
**Album context:** [Album Name — Track X of Y (Phase: description)] OR [Standalone — brief genre/context descriptor]
**Previous scores:** [v1 Core X.X / Advanced X.X → v2 Core X.X / Advanced X.X] (omit for first critique)
```

---

## Layer 1: Core 12-Category Scores

```markdown
## Core 12-Category Scores

| Category | Score | Notes |
|---|---|---|
| Hook | X/10 | [One substantive sentence: timing, memorability, singability, standalone vs context-dependent impact] |
| Lyrics | X/10 | [One sentence: imagery quality, show-vs-tell ratio, specificity, any weak lines named] |
| Prosody | X/10 | [One sentence: syllable counts, stress alignment, breath points, singable vowels, any violations] |
| Arc | X/10 | [One sentence: transformation journey described, turn quality, V2 new info, final chorus earned?] |
| Structure | X/10 | [One sentence: length, pacing, negative space, contrast, anything excess or missing] |
| Originality | X/10 | [One sentence: fresh angles, unique phrasing, territory claimed, any cliches present] |
| Singability | X/10 | [One sentence: phrase rhythm, vowel placement, consonant issues, a cappella viability] |
| Commercial | X/10 | [One sentence: platform fit, hook timing, length, sync potential — scored relative to INTENDED context] |
| Genre | X/10 | [One sentence: convention adherence, fusion balance, palette coherence, Fabbri satisfaction] |
| Arrangement | X/10 | [One sentence: dynamic arc, contrast pairs, growth pattern, negative space, subtractive moments] |
| Voice/Accent | X/10 | [One sentence: persona clarity, dialect coherence, cultural instrumentation match, Moore's layers] |
| Emotional Intelligence | X/10 | [One sentence: authenticity, generosity, responsibility with darkness, transcendence achieved?] |

### COMPOSITE SCORE: X.X/10
```

**Composite calculation:** Average of all 12 scores, rounded to one decimal.

---

## Layer 2: Advanced Assessments

```markdown
## Advanced Assessments

| Assessment | Score | Notes |
|---|---|---|
| Functional Layers (Moore) | X/10 | [One sentence: all 4 layers present? Balanced? Any missing/competing? Subtraction used?] |
| Soundbox & Proxemics (Lacasse) | X/10 | [One sentence: proxemic arc described (intimate→social→public→dissolved), distance matches content?] |
| Musemic Signification (Tagg) | X/10 | [One sentence: do timbres/musemes carry correct cultural connotation? Any contradictions?] |
| Scope of Vision (Dodge) | X/10 | [One sentence: artistic ambition level, multi-layered meaning, structural innovation, daring?] |
| Skip Test (A&R) | X/10 | [One sentence: any dead zones identified? Every 15s window scanned, specific moments named] |

### ADVANCED COMPOSITE: X.X/10
```

---

## Suno Optimization Assessment

> Evaluates whether the Style Prompt, tags, and production choices are OPTIMAL for the song's
> emotional content — not just technically compliant but creatively best-suited.
> Reference: `references/SUNO_STYLE_GENRE_REFERENCE.md`

```markdown
## Suno Optimization Assessment

**Current Style approach:** [One sentence summarizing the genre/key/BPM/vocal specified]
**Compliance:** PASS / ISSUES — [list any missing required elements]
**Optimization verdict:** OPTIMAL / COULD IMPROVE / MISMATCHED

### 7-Point Dimensional Check

| # | Dimension | Current Choice | Assessment | Notes |
|---|---|---|---|---|
| 1 | Genre | [what's specified] | CORRECT / SUBOPTIMAL / WRONG | [Does this genre serve the emotional content? Fabbri's 5 rules satisfied?] |
| 2 | Key | [key specified] | CORRECT / SUBOPTIMAL / WRONG | [Does the key carry the correct emotional weight? Mode = #1 emotional cue] |
| 3 | BPM | [tempo specified] | CORRECT / SUBOPTIMAL / WRONG | [Is tempo in the right range for genre AND emotion?] |
| 4 | Instruments | [main instruments] | CORRECT / SUBOPTIMAL / WRONG | [Do instruments signify correctly? (Tagg) Cultural connotation aligned?] |
| 5 | Vocal Style | [vocal specified] | CORRECT / SUBOPTIMAL / WRONG | [Does delivery match genre expectations AND lyric content?] |
| 6 | Era/Production | [era if specified] | CORRECT / SUBOPTIMAL / N/A | [Is the production aesthetic serving or fighting the content?] |
| 7 | Space/Mood | [mood descriptors] | CORRECT / SUBOPTIMAL / WRONG | [Are atmospheric descriptors aligned and non-contradictory?] |

### Section-Level Tag Assessment

| Section | Current Tags | Signification Check | Recommendation |
|---|---|---|---|
| [Intro] | [current tags] | ALIGNED / MISMATCHED | [Any changes needed?] |
| [Verse] | [current tags] | ALIGNED / MISMATCHED | [Any changes needed?] |
| [Chorus] | [current tags] | ALIGNED / MISMATCHED | [Any changes needed?] |
| [Bridge] | [current tags] | ALIGNED / MISMATCHED | [Any changes needed?] |
| ... | ... | ... | ... |

### Style Alternatives (if verdict is not OPTIMAL)

**Option A:**
```
[Complete rewritten Style Prompt — full text ready to paste into Suno]
```
Reasoning: [Why this genre/key/BPM combination serves the emotional content better]
Expected improvement: [What changes in the Suno render — be specific]
Slider recommendation: Weirdness X% / Style Influence X% / Audio Influence X%

**Option B:**
```
[Complete rewritten Style Prompt — different angle]
```
Reasoning: [What this prioritizes differently]
Expected improvement: [What this optimizes for]
Slider recommendation: Weirdness X% / Style Influence X% / Audio Influence X%

### Compliance Checklist

| Check | Status | Notes |
|---|---|---|
| `[Title:]` present above intro | ✅/❌ | |
| `[Production Direction:]` present | ✅/❌ | |
| `[Vocal Direction:]` present | ✅/❌ | |
| Style Prompt ≤1000 chars | ✅/❌ | [actual count if close/over] |
| Lyrics ≤5000 chars (with tags) | ✅/❌ | [actual count if close/over] |
| `[end]` at bottom | ✅/❌ | |
| Section tags on own lines | ✅/❌ | |
| Named `()` layers declared in Style | ✅/❌ | [list any undeclared] |
| Exclusions in Exclude field (not lyrics) | ✅/❌ | |
| Genre is FIRST in Style Prompt | ✅/❌ | |
| Tag count 5-8 (not >10) | ✅/❌ | [actual count] |
| No contradictory tags | ✅/❌ | [flag any conflicts] |
| BPM/tempo specified | ✅/❌ | |
| Per-section tags ≤3 per section | ✅/❌ | [flag any over-tagged sections] |
```

**Optimization verdict meanings:**
- **OPTIMAL** — Genre, key, BPM, instruments, vocal, and tags all serve the emotional content perfectly. No changes recommended.
- **COULD IMPROVE** — Fundamentally sound but specific dimensions could be stronger. Alternatives provided.
- **MISMATCHED** — The Style Prompt is fighting the lyric content. Genre/key/BPM don't serve the emotion. Revision strongly recommended.

**When to include Style Alternatives:**
- Always include if verdict is COULD IMPROVE or MISMATCHED
- Omit if verdict is OPTIMAL (just confirm why it works)

---

## Layer 3: Album-Context Assessment [CONDITIONAL]

> Include ONLY for concept album tracks. Omit entirely for standalone songs.

```markdown
## Album-Context Assessment

| Check | Result | Notes |
|---|---|---|
| Position Awareness | PASS / CONCERN / FAIL | [One sentence: does track serve its position in the album arc?] |
| Intention vs Delivery | MATCH / PARTIAL / MISS | [One sentence: bible's stated emotion vs what the song actually delivers] |
| Transition Consciousness | STRONG / ADEQUATE / WEAK | [One sentence: does the ending create gravity toward next track?] |
| Dramatic Irony | PRESENT & EFFECTIVE / PRESENT BUT HEAVY-HANDED / ABSENT | [One sentence: audience knowledge vs character knowledge managed?] |
| Motif & Callback Accuracy | CORRECT / MINOR ISSUE / VIOLATION | [One sentence: motifs in right tracks, correct meaning, forbidden absent?] |
| Sonic Differentiation | PASS / BORDERLINE / FAIL | [One sentence: <70% palette overlap with adjacent tracks?] |
```

---

## Calibration & Technical Audit

```markdown
## Calibration & Technical Audit

- **Self-Score Delta:** [Self X.X → Critic Y.Y — delta Z.Z — calibration assessment sentence] (omit if no self-score provided)
- **Layer Audit:** [Declarations verified / density appropriate / issues found — one sentence]
- **Production-Lyric Alignment:** [Aligned / Intentional contrast at X / Mismatch at X — one sentence per finding]
- **Discovery Depth:** HIGH / MEDIUM / LOW — [One sentence: what rewards re-listening? How many meaning-layers?]
```

---

## Strongest Line

```markdown
## Strongest Line

> "quoted line" — [2-4 sentences explaining WHY: imagery quality? Rhythmic perfection? Multi-level meaning? Prosodic beauty? Album-wide significance? How many layers does it operate on? What does it teach about the song's best instincts?]
```

---

## Flagged Issues

```markdown
## Flagged Issues

1. **[Problem name — concise label]**
   Current: "[the exact line or moment quoted]"
   Why: [2-3 sentences: what's wrong, which framework identifies it (Tagg/Moore/Pattison/Fabbri/etc.), why it matters for the listener experience]
   Fix:
   a) [Option 1 — with reasoning]
   b) [Option 2 — with reasoning]
   c) [Option 3 — with reasoning] (optional third option)

2. **[Problem name]**
   Current: "[quoted]"
   Why: [explanation]
   Fix:
   a) ...
   b) ...

3. ...
```

**Issue ordering:** Highest impact first. Limit to 3-6 issues maximum. If more exist, group minor ones under a "Minor Notes" sub-section.

---

## Priority Recommendations

```markdown
## Priority Recommendations

1. [Highest impact fix — one sentence describing the change + expected score impact]
2. [Second priority — one sentence]
3. [Third priority — one sentence]
```

**Rules:**
- Maximum 3-5 recommendations
- Each must be actionable (not vague)
- Order by: (1) score impact, (2) ease of implementation, (3) cascade effect on other categories

---

## Decision Gate

```markdown
## Decision Gate

**Core composite X.X/10 — [CLEARS the 8.5 threshold / Falls in 7.0-8.4 revision band / Falls below 7.0]**

→ **[Action: Skip revision, proceed to Optimize (Stage 4) / Proceed to Revise (Stage 3) — specify which issues / Return to concept with new approach (Stage 1) — specify brief]**

[1-2 sentences: any override conditions? Album-context failures overriding craft score? Advanced vs Core gap analysis?]
```

---

## Revision Delta Table [CONDITIONAL]

> Include ONLY on re-critiques (v2+). Shows progression across versions.

```markdown
## Revision Delta Table (v1 → v2)

| Category | v1 | v2 | Δ | Notes |
|---|---|---|---|---|
| Hook | X | X | +X | [brief] |
| Lyrics | X | X | +X | [brief] |
| Prosody | X | X | +X | [brief] |
| Arc | X | X | +X | [brief] |
| Structure | X | X | +X | [brief] |
| Originality | X | X | +X | [brief] |
| Singability | X | X | +X | [brief] |
| Commercial | X | X | +X | [brief] |
| Genre | X | X | +X | [brief] |
| Arrangement | X | X | +X | [brief] |
| Voice/Accent | X | X | +X | [brief] |
| Emotional Intelligence | X | X | +X | [brief] |
| | | | | |
| **CORE COMPOSITE** | **X.X** | **X.X** | **+X.X** | **[gate status]** |
| | | | | |
| Functional Layers | X | X | +X | [brief] |
| Soundbox & Proxemics | X | X | +X | [brief] |
| Musemic Signification | X | X | +X | [brief] |
| Scope of Vision | X | X | +X | [brief] |
| Skip Test | X | X | +X | [brief] |
| | | | | |
| **ADVANCED COMPOSITE** | **X.X** | **X.X** | **+X.X** | **[depth assessment]** |
```

For 3+ versions, extend columns: `| v1 | v2 | v3 | Δ(v1→v3) |`

---

## Summary [CONDITIONAL]

> Include ONLY on final-version critiques or multi-revision reports. Provides the narrative arc of the song's development.

```markdown
## Summary

[2-4 sentences: What was the song's journey? What were the biggest transformations? What does the final state tell us about the craft? Is it render-ready?]
```

---

## Format Rules

1. **Be specific, never vague.** Every score note must name WHAT earns or costs the score — quote lines, name sections, cite timestamps.
2. **One voice, consistent tone.** Professional but direct. No hedging ("maybe," "sort of," "a little bit"). State assessments with confidence.
3. **Cite frameworks by name.** When a score is informed by a theoretical framework, name it parenthetically: (Tagg), (Moore), (Pattison), (Fabbri), (Lacasse), (Dodge).
4. **Fixes must be concrete.** Never "make it better" — always "change X to Y because Z." Provide actual replacement text where applicable.
5. **Respect context.** A concept album track is scored against concept album standards. A fun novelty song is scored against novelty standards. State the context in the header and score within it.
6. **Strongest Line must explain WHY.** Not just "this is good" — identify the specific craft mechanisms that make it work (prosody, multi-level meaning, imagery, surprise, etc.).
7. **Decision Gate is mandatory.** Every critique must end with a clear next-action directive.
8. **No padding.** If a section isn't applicable, omit it entirely rather than writing "N/A" placeholders.

---

## Quick Reference: When to Include Each Section

| Section | First Critique | Re-Critique | Final/Render-Ready |
|---|---|---|---|
| Header | Always | Always | Always |
| Core 12 Scores | Always | Always | Always |
| Advanced 5 Scores | Always | Always | Always |
| Suno Optimization | Always | Always | Always |
| Album-Context | If album track | If album track | If album track |
| Calibration | Always | Always | Always |
| Strongest Line | Always | Always | Always |
| Flagged Issues | Always | If issues remain | Omit or "Minor Notes" only |
| Priority Recommendations | Always | If revisions needed | Omit if gate cleared |
| Decision Gate | Always | Always | Always |
| Revision Delta Table | Never (no prior) | Always | Always |
| Summary | Optional | Optional | Always |
