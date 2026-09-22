# Authoring Suno Studio Plugins

This document describes the reverse-engineered **Suno Studio** plugin format and how to author new
plugins for it. Suno Studio plugins are audio-effect processors applied to **rendered audio** inside
Suno's in-app effects and mixing environment. They are NOT lyric tags and NOT part of the
text-prompt / Style-Lyrics pipeline. See [README.md](README.md) for the use-case framing and the
list of built plugins.

## Important: this schema is reverse-engineered and incomplete

The schema and the primitive list below were derived from **one** working example. They are
best-effort and may be incomplete or slightly wrong. Nothing here has been executed in Suno Studio
from this repository. Treat every plugin as UNVERIFIED and test it in Suno Studio before relying on
it.

## Top-level JSON schema

Each plugin is a single JSON object (`<name>.plugin.json`) with these top-level fields:

| Field | Type | Notes |
| --- | --- | --- |
| `id` | string | Stable identifier, e.g. `intimate-proximity`. Matches the folder / file name. |
| `kind` | string | `"effect"`. |
| `displayName` | string | Human-readable name shown in the UI. |
| `description` | string | Short description of what the effect does. |
| `ports` | object | Audio routing (see below). |
| `parameters` | array | The knobs and toggles (see below). |
| `source` | object | `lang`, `metadata`, and the embedded DSP `code` (see below). |
| `ui` | object | A `compact` grid layout (see below). |

### `ports`

```json
"ports": {
  "audioIn":  { "kind": "audio" },
  "audioOut": { "kind": "audio" },
  "extraInputs":  [],
  "extraOutputs": []
}
```

`audioIn` / `audioOut` are the stereo audio in and out. `extraInputs` / `extraOutputs` are empty
arrays for these effects.

### `parameters[]`

Each entry has a `name` (used to read the value in `source.code`) and a `label`, plus EITHER a
continuous form or a toggle / enum form.

Continuous (knob):

```json
{
  "name": "air",
  "label": "Air",
  "range": { "min": 0, "max": 12, "step": 0.1 },
  "scale": "linear",
  "default": 3,
  "unit": "db"
}
```

- `range` is `{ min, max, step }`.
- `scale` is `"linear"` or `"log"`.
- `default` is a number.
- `unit` is one of `db`, `ms`, `percent`, `hz`.

Toggle / enum:

```json
{
  "name": "bypass",
  "label": "Bypass",
  "enumOptions": [
    { "value": "off", "label": "Off" },
    { "value": "on",  "label": "On"  }
  ],
  "default": "off"
}
```

Every plugin must include a `bypass` toggle (default `off`), an input-gain and an output-gain
parameter (`unit: "db"`), and a dry/wet mix (`unit: "percent"`) where mixing is meaningful.

### `source`

```json
"source": {
  "lang": "js",
  "metadata": { ... },
  "code": "function build(g, config) { ... }"
}
```

- `lang` is `"js"`.
- `metadata` mirrors `displayName`, `kind`, and `description`, and adds:
  - a `controls` map keyed by parameter name. Each entry has a `widget`
    (`{ "type": "knob" }` or `{ "type": "toggle" }`, with optional `"pan": true`), a `description`
    string, and mirrors `range` / `scale` / `unit` / `label` / `default` for knobs, or
    `enumOptions` / `label` / `default` for toggles.
  - a `ui` object whose `compact` layout matches the top-level `ui.compact`.
- `code` is the embedded DSP as a JavaScript function string (see the build contract below).

### `source.code` build contract

The DSP is a single function string:

```js
function build(g, config) {
  // Header comment: describe the full signal chain in order.
  var inL = g.input('audioInL');
  var inR = g.input('audioInR');
  var air = g.input('air');       // read a parameter by its name
  // ... processing using g.* primitives ...
  g.output('audioOutL', outL);
  g.output('audioOutR', outR);
}
```

- Read audio via `g.input('audioInL')` and `g.input('audioInR')`.
- Read parameters via `g.input('<param name>')`.
- Write outputs via `g.output('audioOutL', <node>)` and `g.output('audioOutR', <node>)`.
- Use `config.sampleRate` where a filter or envelope needs the sample rate.
- START the code string with a header comment (`//` lines) explaining the full signal chain in order.
- Implement `bypass` by selecting between the dry input and the processed signal with `g.lerp`
  (or `g.compareLt`) on the bypass control.
- Convert dB gains with `g.dbToLin`.
- END every plugin with a `g.tanh` output-safety stage (soft-clip) before `g.output`.

### `ui.compact`

A grid layout. `unit` is `"gr"` (grid units). It holds `boxes` that position widgets with `x` / `y`
/ `w` / `h` coordinates, each referencing its `paramName` (a knob for a continuous param, a toggle
for `bypass`, optional label boxes). Keep the grid tidy, for example a 2 to 3 row layout. Mirror the
same compact layout inside `source.metadata.ui.compact`.

## Confirmed `g.*` primitives

Use ONLY these primitives in `source.code`:

```
g.input
g.output
g.zero
g.constant
g.mul
g.add
g.sub
g.div
g.abs
g.max
g.min
g.clamp
g.lerp(mask, a, b)
g.compareLt(a, b)
g.dbToLin
g.tanh
g.biquad({ input, cutoff, resonance, mode })   // mode: 'highpass' | 'lowpass' | 'peaking' | 'lowshelf' | 'highshelf'
g.asymmetricOnePole({ target, attackCoef, releaseCoef })
```

### This list is incomplete: derived from ONE example

This confirmed list was derived from a **single** example plugin, so it is almost certainly
incomplete. The following primitives are **unconfirmed**: we do not know they exist in Suno Studio,
and they MUST NOT be used until verified there:

- Delay lines
- Reverb
- Noise generators
- LFO / oscillators
- FFT

If a plugin idea needs any of these, do NOT invent a `g.*` call for it. Either approximate the effect
with the confirmed set (and document the approximation), or list the idea under Tier 2 in
[README.md](README.md) until the primitive is confirmed.

## Authoring guidance for new plugins

- Keep the JSON valid and structurally parallel to the six existing plugins (same top-level keys,
  same `source` / `ui` shapes).
- Always include a `bypass` toggle, an input-gain and an output-gain control, and a `g.tanh`
  output-safety stage. Include a dry/wet mix where mixing is sensible.
- Start `source.code` with a signal-chain header comment describing the chain in order.
- Use only the confirmed `g.*` primitives. If an effect would need a primitive outside that set,
  approximate it with the confirmed primitives and document the approximation in the code header
  comment (as `digital-degrade` does for its amplitude-staircase bitcrush).
- If an idea genuinely needs an unconfirmed primitive and cannot be reasonably approximated, list it
  under Tier 2 in [README.md](README.md) instead of building it.
- Validate JSON before committing:

  ```
  python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('plugins/**/*.plugin.json', recursive=True)]"
  ```

- Treat every new plugin as UNVERIFIED until it has been tested in Suno Studio.
