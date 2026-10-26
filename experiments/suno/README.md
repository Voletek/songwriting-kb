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
├── README.md                                    (this file)
├── TEMPLATE.yml                                 (copy this to start)
└── 2026-07-02-performance-notation-symbols.yml  (logged experiment, v5.5-era)
```

Planned (not yet run): `era-tag-interaction` (do era tags bias production more than instrumentation?)
and `whisper-layer-reliability` (do whispered `()` layers render reliably?). Both should now be run
on V6 (`suno_version: "v6"`, with `model_variant` recorded).

## Where Findings Go

Once an experiment is concluded and meets the promotion criteria:
- Update the relevant `core/methodology/` file with the new guidance
- Add or update the entry in `references/SUNO_STYLE_GENRE_REFERENCE.md` §12 (Suno Version Status table),
  which now has V6 rows; v5.5 rows are marked "Re-validate on V6"
- For V6 lyric-tag tests, also add a row to the render-evidence table in
  `references/V6_TAG_DISCOVERY.md` → Results Log (Date | Model | Tag(s) tested | Render result/ID)
- Note the retest date (Suno updates frequently - claims expire)

**Version paradigm:** V6 (v6 / v6-wild / v6-mini) is the default since Sept 2026. Set `paradigm: "v6"`
for new tests; use `paradigm: "v5.5-legacy"` only when re-checking an old v5.5 finding.

## Evidence Impact

The first experiment reported with this framework (21machines, acid-instrument-specificity-ladder, June 2026) is the evidence basis for `references/INSTRUMENT_SOUND_REFERENCE.md` -- it reported that timbre/scene descriptors outperform gear model names in Suno v5.5. [Tier 3: external community report; its log is not in this folder and it has not been reproduced here or re-tested on V6.]
