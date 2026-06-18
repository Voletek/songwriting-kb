# SOP 06: Character Voice Design

> Step-by-step procedure for creating a complete vocal identity for a character,
> from accent through instrumentation through mode selection.

> **Note:** The canonical methodology for this workflow now lives in `core/methodology/character-voice.md`.
> This SOP is retained for Kiro-specific step formatting but the methodology file is the authoritative source.
> If content diverges, `core/methodology/` wins.

---

## Prerequisites

- Know WHO the character is (name, background, emotional state)
- Know WHAT they're singing about (the song's concept)
- Know the GENRE context (what instrumentation ecosystem they live in)

---

## Procedure

### Step 1 — Identify the Speaker

Answer these questions:
```
Who: [name/identity]
What are they: [human? creature? entity? concept?]
Age/era: [young? ancient? timeless?]
Emotional state: [at the START of the song — or existential state for non-human entities]
Cultural origin: [real-world basis / fantasy world / pre-cultural / cosmic / elemental]
Vocal type: [singing / speaking / non-vocal (expressed through instrumentation/production)]
```

**If "non-vocal":** This character is expressed through sound design, instrumentation, and production rather than literal voice. Steps 3, 4, and 9 will need adaptation (guided below). Steps 7, 8, and 11 apply fully.

### Step 2 — Choose Accent Base / Sonic Character

**For real-world characters:** Pick the regional accent that matches their identity.

**For fantasy characters:** Choose a BLEND of real-world phonetic models:
```
Primary accent model: [e.g., Scottish]
Secondary influence: [e.g., Nordic]
Tertiary texture: [e.g., Semitic consonant weight]
```

**For non-human entities:** Choose by FEELING, not geography:
```
What does this voice/presence FEEL like? → [e.g., stone, wind, fire, water, void, pressure]
What real-world sounds share that quality? → [e.g., whale song, tectonic rumble, throat singing, ice cracking]
```

### Step 3 — Define Vowel Character

**For vocal characters:** Answer directly about their singing voice.
**For non-vocal entities:** Answer for the PRIMARY SONIC PROXY — the choir, instrument, or texture that REPRESENTS the character. You're designing the proxy's character, not a literal voice.

| Question | Answer |
|---|---|
| Open or closed vowels? | [open = warm/vast, closed = tight/urgent] |
| Long or short? | [long = sustained/patient, short = percussive/urgent] |
| Warm or cold? | [warm = human/close, cold = distant/alien] |
| Which vowels sustain best? | [list 2-3: "ah", "oh", "ee", etc.] |
| Which to avoid sustaining? | [list 1-2] |

### Step 4 — Define Consonant Character

**For vocal characters:** Answer directly. **For non-vocal entities:** Answer for the sonic proxy, or describe the character of attacks/transients in the representing sound.

| Question | Answer |
|---|---|
| Hard or soft? | [hard = aggressive/grounded, soft = flowing/ethereal] |
| Any special features? | [rolled R? glottal stops? sibilants? — or for non-vocal: resonant attacks? smooth onsets?] |
| Consonant clusters? | [few = singable/flowing, many = rhythmic/percussive] |
| Plosives present? | [yes = punchy, no = flowing] |

### Step 5 — Define Rhythmic Tendency

Where does this voice sit relative to the beat?

| Position | Feels Like | Character Types |
|---|---|---|
| Behind the beat | Lazy, exhausted, ancient, vast | Dwarves, wounded entities, Southern characters, geological presences, ancient sleepers |
| On the beat | Grounded, deliberate, inevitable | Warriors, mentors, Nordic, keepers, duty-bound |
| Ahead of the beat | Urgent, anxious, eager | Young characters, city dwellers, desperate/panicked |
| Floating/rubato | Ethereal, timeless, untethered | Elves, spirits, cosmic entities, void presences, dream-logic beings |

### Step 6 — Fill the Character Voice Template

**For vocal characters:**
```
CHARACTER VOICE:
• Name/Identity:
• Accent base:
• Vowel character:
• Consonant character:
• Rhythmic tendency:
• Register: [bass/baritone/tenor/alto/soprano + specific range]
• Texture: [gravelly/smooth/breathy/raspy/clear/cavernous/etc.]
• Emotional subtext: [what the voice FEELS like underneath]
• Dialect words: [5-10 words to use in lyrics that reinforce the accent]
• Instruments that match:
• Production space: [where does this voice live — cave/forest/battlefield/void?]
• Mode/scale: [what harmonic language matches this culture?]
```

**For non-vocal entities (mark inapplicable fields N/A):**
```
CHARACTER SONIC PRESENCE:
• Name/Identity:
• Sonic character: [what it FEELS like — replaces "accent base"]
• Vowel character: [of the sonic proxy, if applicable — e.g., choir glossolalia]
• Consonant character: [of the sonic proxy / attack transients]
• Rhythmic tendency:
• Frequency range: [replaces "register" — e.g., sub-bass <40Hz + choir mid-range]
• Timbral texture: [expanded beyond vocal — e.g., sub-bass rumble, glass resonance, reversed whale song]
• Emotional/existential subtext: [what the presence FEELS like]
• Dialect words: N/A — entity does not use language
• Instruments that manifest it:
• Production space: [where does this entity exist — ocean trench? cathedral? void?]
• Mode/scale:
• Exclusions: [what this entity NEVER does — e.g., speaks, uses words, produces melody]
```

### Step 7 — Select Matching Instrumentation

Based on the accent/culture, choose instruments that BELONG:

**Use the reference tables** in `references/CHARACTER_VOICE_REFERENCE.md`

If the character's cultural ecosystem doesn't have obvious instruments, build from the FEELING:
```
Voice feels like: [stone? wind? fire? water? machine?]
→ Instruments that evoke that: [deep drums? flutes? distortion? ambient pads?]
```

### Step 8 — Choose Mode/Scale

The harmonic language should match the cultural DNA:
- Celtic/Irish → Dorian, Mixolydian
- Nordic/Viking → Aeolian, Phrygian
- Elvish/ethereal → Lydian, Ionian
- Dwarvish/heavy → Aeolian, natural minor
- Middle Eastern → Phrygian dominant
- Southern US → Mixolydian, major pentatonic
- Cosmic/unknowable/alien → Chromatic, atonal clusters, whole-tone, Locrian
- Deep/ancient/gravitational → Low Aeolian, natural minor, Phrygian
- Horror/dread → Phrygian, Locrian, diminished, tritone-heavy
- Oceanic/elemental → Aeolian with suspended harmonies, open 5ths
- Industrial/machine → Chromatic, repetitive minor ostinato

### Step 9 — Write Dialect into Lyrics

**If the character does not use language (non-vocal entities, ambient presences): SKIP this step.** Their sonic identity is expressed through instrumentation and production (Steps 7-8), not lyric content.

**For vocal characters:**

Choose 5-10 words from the dialect/accent that will appear IN the lyrics to reinforce the vocal:
```
Dialect words chosen: [list them]
Usage plan: [1-2 per verse, more in intimate moments]
```

**Important:** Dialect in the lyrics FORCES the vocal model to commit to the accent. Without dialect words, the style prompt alone may produce inconsistent results.

### Step 10 — Craft the Suno Style Prompt Descriptor

**For vocal characters — write the vocal portion of the Style Prompt:**
```
[accent descriptor], [voice quality], [register], [delivery style]
```

**Examples:**
- "Scottish burr accent, rolled R's, deep gravelly baritone, intimate storytelling"
- "ethereal flowing vocal, musical liquid consonants, ancient soprano, reverb-heavy"
- "cold clinical delivery, precise articulation, subtle digital artifacts, female contralto"

**For non-vocal entities — write the sonic presence descriptor:**
```
[primary sound/instrument], [texture quality], [frequency range/spatial character], [temporal behavior], [exclusions]
```

**Examples:**
- "Sub-bass drone below 40Hz, 40-voice choir glossolalia at half-tempo, reversed whale song textures, cathedral-trench reverb, no words, no human language"
- "Crackling static field, machine-breathing rhythm, mid-frequency oscillation, sterile clinical space, no melody, no vocal"

### Step 11 — Document Voice Evolution (If Album)

If this character appears in multiple tracks:
```
Track X: [voice at this point — texture, state, delivery]
Track Y: [how it's changed — what happened, what's different]
Track Z: [final evolution]
```

**Rule 8:** The voice must be DIFFERENT in every track. Document what changes.

**Note:** If the album bible already documents voice evolution in its Character Voice Registry, reference it rather than duplicating. This step ensures the design is PLANNED; the bible is where it's DOCUMENTED in full.

---

## Verification Checklist

Before using the voice design:
- [ ] All applicable template fields filled (mark N/A for non-vocal entities where fields don't apply)?
- [ ] Vowel choices are SINGABLE in the chosen key (vocal characters only)?
- [ ] Instruments match the cultural ecosystem / sonic feeling?
- [ ] Mode/scale matches the culture or emotional territory?
- [ ] Dialect words chosen and placed in lyrics (vocal characters only — skip for non-vocal)?
- [ ] Suno style prompt descriptor written?
- [ ] If album: voice evolution documented?
- [ ] Production space chosen (reverb/room type)?

---

## Time Estimate: 15-25 minutes per character
