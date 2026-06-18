# Suno Experiments

> Log and track Suno AI behavior experiments to build evidence-based guidance.
> Don't promote observations to universal rules without evidence from multiple songs and renders.

## Purpose

When you notice Suno behaving unexpectedly (a tag working differently, a slider producing surprising results, or a prompt technique that seems effective), log it here before updating the methodology.

## Workflow

1. Copy `TEMPLATE.yml` to a new file: `YYYY-MM-DD-experiment-name.yml`
2. Fill in your hypothesis and settings
3. Generate 3+ renders across different songs with the same variable
4. Record observations per render
5. Write your conclusion

## Promotion Rule

**Do NOT promote an observation to universal guidance until:**
- Tested across 3+ different songs (not just repeated on one)
- Produces consistent results (not random)
- Documented with specific render IDs or screenshots
- Another person can reproduce the finding

## File Structure

```
experiments/suno/
├── README.md                        (this file)
├── TEMPLATE.yml                     (copy this to start)
├── 2026-06-15-era-tag-interaction.yml   (example)
└── 2026-06-20-whisper-layer-reliability.yml
```

## Where Findings Go

Once an experiment is concluded and meets the promotion criteria:
- Update the relevant `core/methodology/` file with the new guidance
- Add or update the entry in `references/SUNO_STYLE_GENRE_REFERENCE.md` (Suno Version Status table)
- Note the retest date (Suno updates frequently - claims expire)
