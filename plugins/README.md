# Suno Studio Audio-Effect Plugins

This folder holds audio-effect plugins for **Suno Studio**, Suno's in-app effects and mixing
environment. They are applied to **rendered audio** inside Suno Studio, on the audio signal after a
track has been generated (post-render processing).

**These are NOT lyric tags and NOT part of the text-prompt / Style-Lyrics pipeline.** They do not go
in the Style field or the Lyrics field, and they are unrelated to the songwriting methodology,
agents, SOPs, and song files in the rest of this repository. That text-prompt pipeline is the rest
of this repo; these plugins are a separate, downstream concern applied to the audio Suno produces.
Do not paste plugin JSON into a prompt. Load these plugins inside Suno Studio and apply them to a
rendered track.

**Suno Studio splits a rendered song into stems** (vocals, drums, bass, guitar, keys, strings,
synth, brass, percussion, backing vocals, FX, other). Each plugin here is meant to be dropped onto a
**specific stem**, not the full mix: the vocal-oriented plugins target the vocals stem, and the
stem-targeted instrumental plugins each name their intended stem (bass, keys, guitar, strings,
synth, backing vocals, FX / other). Apply each effect to the stem it is built for.

## Status: UNVERIFIED, test in Suno Studio before relying on these

The plugin format and the DSP primitive set were reverse-engineered from a single working example.
The plugins in this folder have **not** been executed in Suno Studio or any DSP runtime, so treat
them as best-effort and needing in-Suno testing. Each plugin should be tested in Suno Studio before
production use.

## How to use in Suno Studio

These plugins are loaded and applied inside Suno Studio, not pasted into a prompt. Generically:

1. Generate or open a track in Suno so you have rendered audio to process.
2. Open the Suno Studio effects / plugin interface for that track.
3. Import the plugin's `.plugin.json` file (for example
   `plugins/intimate-proximity/intimate-proximity.plugin.json`) into that interface.
4. Apply the imported effect to the rendered track and adjust its knobs (input gain, the effect
   controls, dry/wet mix, output gain) to taste. Use the `bypass` toggle to A/B against the dry signal.

Note: confirm the exact import steps in your own Suno Studio UI. The precise import UX (menu names,
buttons, drag-and-drop vs file picker) is not documented here and may differ by Suno Studio version.

## Layout

Each plugin is a single JSON file in its own subfolder:

```
plugins/
  intimate-proximity/     intimate-proximity.plugin.json     Close-mic, in-your-ear vocal voicing
  de-esser/               de-esser.plugin.json               Tames harsh sibilance
  vintage-lofi-voicer/    vintage-lofi-voicer.plugin.json    Tilt EQ + tape saturation + band-limit
  digital-degrade/        digital-degrade.plugin.json        8-level amplitude quantizer + glitch
  telephone-radio-band/   telephone-radio-band.plugin.json   Narrow bandpass telephone/radio tone
  vocal-drive-edge/       vocal-drive-edge.plugin.json       Pre-emphasis + soft-to-hard saturation
  sub-tightener/          sub-tightener.plugin.json          Bass stem: sub-rumble highpass + envelope-tamed low band + warmth
  warm-keys-voicer/       warm-keys-voicer.plugin.json       Keys stem: attack soften + warm tilt + saturation + air
  guitar-grit-warmth/     guitar-grit-warmth.plugin.json     Guitar stem: warmth tilt + tanh grit + presence + tone lowpass
  string-air-size/        string-air-size.plugin.json        Strings stem: air lift + body + size/tilt + saturation
  synth-cold-glitch/      synth-cold-glitch.plugin.json      Synth stem: cold tilt + bandpass + reused 8-level quantizer + drive
  backing-vocal-tucker/   backing-vocal-tucker.plugin.json   Backing vocals stem: band-limit + presence cut + tilt + static tuck
  texture-filter-degrade/ texture-filter-degrade.plugin.json FX/other stem: band-limit + lo-fi tilt + reused 8-level quantizer
```

## Plugin file shape

Each `*.plugin.json` is one JSON object with these top-level keys:

- `id`, `kind` ("effect"), `displayName`, `description`
- `ports` (audioIn, audioOut, plus empty extraInputs/extraOutputs)
- `parameters` (array of knobs and toggles)
- `source` (`lang`, `metadata`, and a `code` string holding the embedded JavaScript DSP)
- `ui` (a compact grid layout)

Every plugin includes a bypass toggle, an input-gain and output-gain control, and ends with a
soft-clip safety stage. Most include a dry/wet mix; the de-esser blends by band recombination
instead, so it exposes a reduction amount rather than a mix.

For the full reverse-engineered schema, the confirmed primitive list, and authoring guidance for new
plugins, see [AUTHORING.md](AUTHORING.md).

## Plugin to KB use-case mapping

Each plugin exists to serve specific knowledge-base use-cases and song examples.

| Plugin | What it does | KB use-case / song examples it serves |
| --- | --- | --- |
| Intimate Proximity | Close-mic, in-your-ear vocal voicing: air lift, low-mid warmth, presence bump | Intimate close-mic across the vulnerable lane and Three in the Morning |
| De-Esser | Tames harsh sibilance by ducking the sibilant band | Breathy close-mic vocals prone to sibilance (same vulnerable / intimate lane) |
| Vintage / Lo-Fi Voicer | Tilt EQ, tape-style saturation, and band-limiting for analog warmth | Lo-fi / vintage: Three in the Morning + lo-fi indie lane (analog warmth / 70s / 90s-Bristol) |
| Digital Degrade / Glitch | Fixed-depth 8-level amplitude quantizer, drive, and filtered degradation | Fractured Shadows Act 1 (digital degradation / corrupted signal / progressive glitch, MODE C) |
| Telephone / Radio Band | Narrow bandpass plus drive for a telephone / radio broadcast tone | Shadow Weaver / AI-voice / robotic layers (telephone-filtered, cold-clinical broadcast) |
| Vocal Drive / Edge | Pre-emphasis into soft-to-hard saturation for rasp and grit | Rikan personas / Maren Storm (rasp, vocal-fry, strained-breaking character) |
| Sub Tightener | Sub-rumble highpass, envelope-tamed low-band boom, low-shelf warmth, tanh drive | Apply to the bass stem in Suno Studio: deep sub-bass pulse / distorted bass |
| Warm Keys Voicer | Attack soften, warm tilt EQ, saturation, air lift | Apply to the keys stem in Suno Studio: felt piano / distant Rhodes / intimate ballads |
| Guitar Grit / Warmth | Warmth tilt, tanh grit, presence bump, tone lowpass | Apply to the guitar stem in Suno Studio: acoustic warmth through distorted / overdriven guitar |
| String Air / Size | Air lift, body control, size/tilt shelving, gentle saturation | Apply to the strings stem in Suno Studio: cinematic / chamber / distant strings |
| Synth Cold / Glitch | Cold tilt, bandpass voicing, reused 8-level quantizer, tanh drive | Apply to the synth stem in Suno Studio: Fractured Shadows cold synths / MODE C |
| Backing Vocal Tucker | Band-limit, presence cut, tilt, static tuck attenuation | Apply to the backing vocals stem in Suno Studio: the () backup-vocal technique |
| Texture Filter / Degrade | Band-limit highpass/lowpass, lo-fi tilt, reused 8-level quantizer | Apply to the FX stem in Suno Studio: room tone / FX-texture beds (FX / other) |

## Tier 1 (built) vs Tier 2 (pending API confirmation)

**Tier 1 (built).** The 13 plugins in this folder, each using only confirmed `g.*` primitives. The
first six target the vocals stem; the last seven are stem-targeted for the instrumental / non-lead
stems:

1. Intimate Proximity (`intimate-proximity`)
2. De-Esser (`de-esser`)
3. Vintage / Lo-Fi Voicer (`vintage-lofi-voicer`)
4. Digital Degrade / Glitch (`digital-degrade`)
5. Telephone / Radio Band (`telephone-radio-band`)
6. Vocal Drive / Edge (`vocal-drive-edge`)
7. Sub Tightener (`sub-tightener`), bass stem
8. Warm Keys Voicer (`warm-keys-voicer`), keys stem
9. Guitar Grit / Warmth (`guitar-grit-warmth`), guitar stem
10. String Air / Size (`string-air-size`), strings stem
11. Synth Cold / Glitch (`synth-cold-glitch`), synth stem
12. Backing Vocal Tucker (`backing-vocal-tucker`), backing vocals stem
13. Texture Filter / Degrade (`texture-filter-degrade`), FX / other stem

**Tier 2 (pending API confirmation).** Ideas that need primitives we have not confirmed exist in
Suno Studio, so they are NOT built yet:

- Reverb / delay / space effects (need delay-line or reverb primitives).
- Analog noise / vinyl-crackle / tape-hiss beds (need a noise generator).
- SFX synthesis (needs oscillators and related generators).
- Anything else that depends on an LFO / oscillator or FFT.

These are deferred until the corresponding `g.*` primitives are confirmed to exist in Suno Studio.
If a new plugin idea needs an unconfirmed primitive, list it here under Tier 2 rather than building
it with an unverified call. See [AUTHORING.md](AUTHORING.md) for the confirmed primitive list.

## DSP primitives

The embedded DSP uses only a confirmed set of `g.*` primitives (input, output, zero, constant, mul,
add, sub, div, abs, max, min, clamp, lerp, compareLt, dbToLin, tanh, biquad, asymmetricOnePole).
Effects that would need a primitive outside that set are approximated and the approximation is
documented in the header comment of that plugin's `source.code`. For example, `digital-degrade` uses
a fixed 8-level amplitude quantizer (a sum of `g.compareLt` step comparators) because a variable
bit-depth crush would need a runtime rounding primitive that is not confirmed.
The full list, with the unconfirmed / forbidden primitives, is documented in [AUTHORING.md](AUTHORING.md).
