# Suno Studio Audio-Effect Plugins

This folder holds audio-effect plugins for **Suno Studio**, Suno's in-app effects and mixing
environment. They are applied to **rendered audio** inside Suno Studio, on the audio signal after a
track has been generated.

**These are NOT lyric tags and NOT part of the text-prompt pipeline.** They do not go in the Style
field or the Lyrics field, and they are unrelated to the songwriting methodology, agents, SOPs, and
song files in the rest of this repository. Do not paste plugin JSON into a prompt. Load these plugins
inside Suno Studio and apply them to a rendered track.

## Status: UNVERIFIED

The plugin format and the DSP primitive set were reverse-engineered from a single known example.
The plugins in this folder have **not** been executed in Suno Studio or any DSP runtime, so treat
them as best-effort and needing in-Suno testing before you rely on them.

## Layout

Each plugin is a single JSON file in its own subfolder:

```
plugins/
  intimate-proximity/     intimate-proximity.plugin.json     Close-mic, in-your-ear vocal voicing
  de-esser/               de-esser.plugin.json               Tames harsh sibilance
  vintage-lofi-voicer/    vintage-lofi-voicer.plugin.json    Tilt EQ + tape saturation + band-limit
  digital-degrade/        digital-degrade.plugin.json        Bitcrush-style corruption and glitch
  telephone-radio-band/   telephone-radio-band.plugin.json   Narrow bandpass telephone/radio tone
  vocal-drive-edge/       vocal-drive-edge.plugin.json       Pre-emphasis + soft-to-hard saturation
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

## DSP primitives

The embedded DSP uses only a confirmed set of `g.*` primitives (input, output, zero, constant, mul,
add, sub, div, abs, max, min, clamp, lerp, compareLt, dbToLin, tanh, biquad, asymmetricOnePole).
Effects that would need a primitive outside that set are approximated and the approximation is
documented in the header comment of that plugin's `source.code`. For example, `digital-degrade` uses
an amplitude-staircase approximation because a true bit-reduction rounding primitive is not confirmed.
