# Suno Style & Genre Reference — Professional Production Guide

> Comprehensive reference for genre selection, style prompt optimization, key-emotion mapping,
> BPM-genre conventions, instrument-genre alignment, era anchoring, and Suno-specific prompt science.
> Used by the Critic agent's Suno Optimization Assessment for evaluating and improving style choices.
>
> **Sources:** Fabbri (genre theory), Eerola, Friberg & Bresin (emotional cue hierarchy), Juslin (BRECVEMA), Tagg (musemes),
> Moore (style vs genre), Schubart (1806, trans. Steblin: historical key aesthetics), community-tested Suno v4.5-v5.5
> research (legacy, re-validate on V6), and the Suno V6 working model (Sept 2026; see `references/V6_TAG_DISCOVERY.md`).
>
> **Suno version framing:** V6 (v6 / v6-wild / v6-mini) is the current default. Mechanics marked
> "v5.5-era (legacy) - re-validate on V6" were tested on v5.5 and are not assumed to carry over.
>
> **Last updated:** October 2026

---

## 1. GENRE THEORY FOUNDATIONS

### 1.1 Genre vs Style (Moore, Fabbri)

| Concept | Definition | Example |
|---|---|---|
| **Genre** | A cultural container — set of conventions, expectations, and community practices (Fabbri) | "Post-rock" |
| **Style** | Musical characteristics — timbre, articulation, harmonic language, rhythmic patterns | "Atmospheric guitars with long reverb tails" |
| **Mode** | Not musical mode — the WAY a genre is performed/received in a particular context | "Live post-rock" vs "studio post-rock" |

**Key insight for Suno:** Genre tells Suno WHAT cultural space to occupy. Style descriptors tell it HOW to sound within that space. Both are needed. Genre alone = generic. Style alone = unfocused.

### 1.2 Fabbri's 5 Types of Genre Rules

Fabbri (1982, "A Theory of Musical Genres: Two Applications") defines a genre as a set of musical events (real or possible) governed by socially accepted rules, and groups those rules into five TYPES [Tier 1]. They are not a checklist that a song must "satisfy": the weight of each type varies by genre (some genres are policed mainly by formal/technical rules, others mainly by social/ideological ones).

| Rule type | What It Governs | Suno Prompt Implication (repo's practical adaptation) [Tier 2] |
|---|---|---|
| **Formal and technical** | Structure, length, instrumentation, techniques | Structure notes, instrument list, section lengths |
| **Semiotic** | What the genre SIGNIFIES and how it communicates | Mood descriptors, cultural reference points |
| **Behavioural** | Performance conventions (how it's played/sung, how audiences act) | Vocal delivery tags, performance cues |
| **Social and ideological** | Community values, identity, context | Audience targeting, thematic alignment |
| **Economical and juridical** | How the music is produced, owned, distributed, and sold | Repo adaptation: length, hook timing, sync readiness |

**Application:** If a song's lyrics deal with intimate male vulnerability but the Style Prompt says "epic orchestral metal", the semiotic and social expectations of that genre pull against what the lyrics express -- unless the clash is deliberate. Ironic lyric/genre juxtaposition is itself a recognised convention, so treat a mismatch as a choice to make consciously, not an automatic failure.

### 1.3 The Specificity Principle

The more prompt dimensions you specify, the less Suno fills gaps with statistical averages:

```
Dimension 1: Genre           → anchors the cultural space
Dimension 2: Tempo/BPM       → anchors the energy
Dimension 3: Mood            → anchors the emotional tone
Dimension 4: Instruments     → anchors the texture
Dimension 5: Vocal style     → anchors the delivery
Dimension 6: Era/Production  → anchors the sonic period
Dimension 7: Space/Reverb    → anchors the environment
```

**The 7-dimension prompt** produces precise, controlled output. Missing any dimension = Suno guesses.

**But:** Over-specifying with CONTRADICTORY tags causes Suno to average between them → mush [Tier 3]. Keep every descriptor pointing the same direction. (The "5-8 tags" count is a v5.5-era (legacy) finding - re-validate on V6.)

---

## 2. KEY-EMOTION MAPPING

### 2.1 The Emotional Cue Hierarchy (Eerola, Friberg & Bresin, 2013, *Frontiers in Psychology* 4:487)

Eerola, Friberg & Bresin ("Emotional expression in music: contribution, linearity, and additivity of primary musical cues") systematically manipulated six cues and measured PERCEIVED (expressed) emotion -- what listeners judge the music to convey, not what they feel. Ranked by overall contribution:

```
1. MODE (major/minor)     ← contributed most overall; strongly shapes valence
2. TEMPO (BPM)            ← next; the strongest cue for arousal/energy
3. REGISTER (high/low)    ← weight/lightness
4. DYNAMICS (loud/soft)   ← intensity
5. ARTICULATION (legato/staccato) ← character
6. TIMBRE (instrument choice)     ← color/signification
```

> **Tier split:** The cue ranking for perceived emotion = [Tier 1: Eerola, Friberg & Bresin 2013]. Note the study manipulated MODE (major vs minor), not specific keys. Specific key characters (e.g. "D minor = devotional") = [Tier 2 historical tradition at most (Schubart 1806), not psychology]; the repo's own key feel-words = [Tier 3 working associations]. Useful as creative prompts, not empirical claims. See §2.2.

**Critical implication:** If mode and tempo are wrong for the emotional content, no amount of instrument tags will fix it. Mode + tempo are the foundation; instruments are paint on the wall. The specific key matters mainly through vocal tessitura and instrument resonance (§2.2).

### 2.2 Key Characteristics — Major Keys

> **How to read these tables.** The Schubart column paraphrases C. F. D. Schubart's *Ideen zu einer
> Ästhetik der Tonkunst* (written 1784-85, published 1806; English in Rita Steblin, *A History of Key
> Characteristics*, 1983/2002). It is historical aesthetics written for unequal temperaments, where
> keys really did differ in tuning colour [Tier 2: historical tradition, not psychology]. Under modern
> equal temperament, and for listeners without absolute pitch, a key cannot be identified by ear.
> Real "key effects" come from **mode** (major/minor), **vocal tessitura** (where the melody sits in
> the singer's range), and **instrument resonance** (open strings on guitar/violin, brass-friendly flat
> keys). The working-association column is the repo's prompt vocabulary [Tier 3]; where it differs
> from Schubart it is NOT Schubart's view.

| Key | Schubart (1806, trans. Steblin) — paraphrased | Working association for Suno prompts [Tier 3] | Best For | Suno Context |
|---|---|---|---|---|
| **C major** | Pure, innocent, simple, naive | Pure, simple, clear | Anthems, declarations, simplicity, childlike wonder | Universal starting point; the piano's "white-key" key (shapes voicings, not mood) |
| **D major** | Triumph, hallelujahs, war cries, victory | Triumphant, bright, victorious | Victory, arrival, celebration, marches | Strong for final chorus key lifts, heroic moments; open D resonates on strings and guitar |
| **E major** | Noisy shouts of joy, laughing pleasure | Bright, powerful, joyful | Love songs, confidence, sunshine | Guitar-friendly key — open strings ring |
| **F major** | Complaisance and calm | Pastoral, calm, gentle | Nature, peace, resolution, folk | Warm resolution after minor sections ("pastoral" echoes Beethoven's Pastoral Symphony in F) |
| **G major** | Rustic, idyllic, lyrical; calm, satisfied passion | Happy, rustic, open, honest | Folk, country, acoustic singer-songwriter | The "campfire key" — guitar-friendly, open, warm |
| **A major** | Innocent love, contentment, youthful cheerfulness, hope of reunion | Warm, full, confident | Pop, rock, declarations of love | Balanced warmth; guitar-friendly |
| **Bb major** | Cheerful love, clear conscience, hope for a better world | Grand, noble, expansive | Orchestral, brass-driven, proclamation | Horn/brass-friendly key (many brass instruments are pitched in Bb) |
| **Eb major** | Love, devotion, intimate conversation with God | Heroic, warm, majestic | Grand emotional statements, triumph over adversity | The "heroic" association comes from Beethoven's *Eroica* Symphony (No. 3, Eb), not from Schubart; brass-friendly |
| **Ab major** | Key of the grave: death, putrefaction, judgment, eternity | Romantic, dreamy, lush | Romance, longing fulfilled, beauty | Rich warmth on piano; note the working association is the opposite of Schubart's |

### 2.3 Key Characteristics — Minor Keys

| Key | Schubart (1806, trans. Steblin) — paraphrased | Working association for Suno prompts [Tier 3] | Best For | Suno Context |
|---|---|---|---|---|
| **A minor** | Pious womanliness, tenderness | Melancholic, tender, introspective | Gentle sadness, reflection, vulnerability | The "default sad" — piano/guitar natural minor |
| **B minor** | Patience, calm awaiting of one's fate, submission | Aggressive, dark, physical | Combat, primal energy, visceral intensity | Guitar power chords, drop-tuning territory (a playing-technique effect, not a key property) |
| **C minor** | Declaration of love and lament of unhappy love; longing, sighing | Dark, dramatic, heavy | Tragedy, fate, gravitas | The "fate/storm" association comes from Beethoven's C-minor works (5th Symphony, *Pathétique*) |
| **D minor** | Melancholy womanliness; brooding spleen | Devotional, melancholic, solemn | Grief, spiritual pain, medieval, processional | "The saddest of all keys" is a *This Is Spinal Tap* joke (Nigel Tufnel), not a finding |
| **E minor** | Naive, womanly, innocent declaration of love; lament without grumbling | Searching, introspective, vast | Journey, identity crisis, existential questioning | The most guitar-friendly minor — open strings enable atmosphere |
| **F minor** | Deep depression, funereal lament, longing for the grave | Anguish, obsession, dark passion | Desperation, obsessive love, fury contained | Romantic-piano associations (Chopin's F-minor works) |
| **F# minor** | Gloomy; resentment and discontent ("tugs at passion like a dog biting a dress") | Gloomy, mysterious, shadowy | Secrets, hidden truths, supernatural | Not actually rare in pop/rock; any "otherworldly" feel comes from arrangement and harmony |
| **G minor** | Discontent, uneasiness, worry, resentment | Restless, yearning, romantic darkness | Unfulfilled desire, tension, noir | Associated with Mozart's G-minor works (Symphonies 25 and 40) |
| **Bb minor** | Quaint, surly, "dressed in night"; mocking God and the world, discontented | Desolation, extreme darkness | Horror, void, absolute despair | Not especially rare in modern production; the darkness comes from mode, register and arrangement |
| **Eb minor** | Anxiety of the soul's deepest distress, brooding despair, blackest depression | Cold, alien, disorienting | Psychological thriller, paranoia, unreality | A "something is wrong" feel comes from harmony and arrangement, not the key |
| **C# minor** | Penitential lament, intimate conversation with God | Piercing, painful, beautiful | Heartbreak, beautiful sadness | "Moonlight Sonata" association (Beethoven, C# minor); any "shimmer" comes from voicing and register |

### 2.4 Key Selection Decision Framework

```
Step 1: What is the DOMINANT emotion? → determines Major or Minor
Step 2: What is the INTENSITY and VOCAL RANGE? → pick the key that puts the melody's peak where the
        singer sounds right (strained/belted high vs warm/low) — tessitura is the real "key effect"
        ("sharp keys brighter, flat keys darker" is a historical/folk association [Tier 3]; under
        equal temperament any difference comes from instrument resonance, not the key itself)
Step 3: What INSTRUMENTS dominate? → determines playability (guitar = E/A/B/G friendly, piano = any, brass = Bb/Eb/F)
Step 4: Is there a KEY CHANGE? → plan the relationship (relative major/minor, chromatic lift, parallel major)
Step 5: Does the album context demand a specific key? → continuity rules may override emotional preference
```

### 2.5 Key Modulation Patterns

| Pattern | Emotional Effect | When to Use |
|---|---|---|
| Minor → Relative Major (Am→C) | Gentle resolution, warmth arriving | Bridge→Final Chorus acceptance |
| Minor → Parallel Major (Am→A) | Dramatic transformation, "everything changes" | Key change final chorus, revelation |
| Up a half step (C→Db) | Pop lift, energy boost, "bigger" | Final chorus repeat with extra power |
| Up a whole step (C→D) | Natural rise, earned growth | Final chorus after bridge |
| Major → Relative Minor (C→Am) | Darkening, complications arriving | Verse→Pre-chorus tension |
| Down a minor third (Am→F#m) | Unsettling shift, ground removed | Surprise bridge, plot twist |

---

## 3. BPM-GENRE-EMOTION MAPPING

### 3.1 BPM Ranges by Genre

> **Canonical BPM table.** Other files (e.g. `MUSIC_PRODUCTION_THEORY.md` §7 Tempo & Bodily Feel)
> point here. Genre ranges are typical conventions [Tier 2]; the "Suno Behavior" column is [Tier 3].
> Half-time and double-time feels shift the perceived tempo (a half-time groove at 140 feels like 70).

| BPM Range | Genres | Emotional Territory | Suno Behavior |
|---|---|---|---|
| 40-60 | Ambient, drone, funeral doom | Suspended time, meditation, grief | Very slow — Suno may struggle. Use "glacial pace" descriptor |
| 60-70 | Ballad, ambient folk, hymnal, cinematic ballad | Contemplation, prayer, intimacy, dirge/ritual | Works well with "slow ballad" + BPM |
| 70-85 | R&B, soul, lo-fi, trip-hop, intimate rock, dark indie, slow alt-rock | Vulnerability, sensuality, confession | Sweet spot for male vulnerability songs |
| 85-100 | Hip-hop, alternative, indie folk, dark pop, cinematic folk-rock | Walking pace, storytelling, moderate energy | Conversational delivery territory |
| 100-115 | Indie pop, synth-pop, folk-rock, classic rock, gothic rock, pop-rock | Confident, anthemic, driving but not aggressive | Good for anthems that don't need to shout |
| 115-125 | Pop, dance-pop, house, funk | Energy, movement, danceability | Mainstream radio territory |
| 125-135 | Rock, punk-pop, pop-punk, EDM, disco | High energy, driving, physical, urgent | Aggressive guitar/drums territory |
| 135-150 | Punk, hardcore, drum & bass, metal | Urgency, aggression, chaos | Extreme energy — Suno renders well |
| 150-170 | Speed metal, jungle, breakcore | Overwhelming, mechanical, inhuman | Push Suno's limits — may lose control |
| 170+ | Speedcore, gabber | Novelty/extreme only | Unreliable in Suno |

### 3.2 BPM-Emotion Interaction

> [Tier 2/3: craft pairings. Tempo is the strongest cue for arousal (Eerola et al. 2013), but these
> specific ranges and the body-based explanations are heuristics.]

| Emotion | Optimal BPM | Why |
|---|---|---|
| Grief/mourning | 60-72 | Folk heuristic [Tier 3]: "matches a resting heartbeat — feels like breathing" (resting heart rates vary widely; treat as imagery, not physiology) |
| Vulnerability/confession | 72-85 | Conversational pace — intimate without dragging |
| Determination/journey | 85-96 | Walking pace — forward motion without rushing |
| Anxiety/tension | 96-110 | Elevated heartbeat — the body responds |
| Confidence/swagger | 110-125 | Head-nodding pace — control expressed as groove |
| Joy/celebration | 120-135 | Dancing pace — the body wants to move |
| Aggression/combat | 130-150 | Fight-or-flight — primal urgency |
| Transcendence | 60-75 OR 135+ | Either suspended time OR overwhelming speed creates altered state |

### 3.3 BPM Alignment Checklist

When evaluating a song's BPM:
1. Does the BPM match the GENRE conventions? (±10 BPM acceptable)
2. Does the BPM match the EMOTIONAL content of the lyrics?
3. Does the BPM allow the PROSODY to breathe? (faster = fewer syllables per line needed)
4. Does the BPM serve the HOOK timing? (faster BPM = hook arrives sooner in seconds)
5. Is the BPM consistent with ADJACENT TRACKS in the album? (variety needed)

### 3.4 Groove / Time-Feel Descriptors

> [Tier 3: Community heuristic]
> Credit: Omnisona (Suno AI God Mode Manual v3.0, March 2026)

Beyond BPM, groove descriptors add an 8th dimension of specificity to the Style Prompt -- telling Suno HOW the rhythm feels, not just how fast it is.

| Descriptor | Feel | Best For |
|---|---|---|
| Medium swing | Relaxed jazz bounce, triplet-based | Jazz, blues, swing revival, soul |
| Laid-back shuffle | Behind-the-beat groove, relaxed drag | Blues, southern rock, chill R&B |
| Straight eighth notes | Even, mechanical, precise | Pop-rock, punk, EDM, industrial |
| Half-time feel | Halved pulse, heavy and spacious | Ballad choruses, trap, cinematic builds |
| Double-time feel | Doubled pulse, urgent and driving | Punk breakdowns, drum fills, transitions |
| Triplet feel | Three-note groupings, rolling | Gospel, 6/8 ballads, waltz-adjacent |
| Four-on-the-floor | Steady kick on every beat | Disco, house, dance-pop, EDM |
| Syncopated | Off-beat accents, unpredictable | Funk, Latin, progressive, neo-soul |

**Usage in Style Prompt:** Add the groove descriptor after BPM: `"Dark indie rock, 92 BPM, syncopated, melancholic..."`

**Note:** This functions as an optional 8th dimension beyond the standard 7-dimension formula. Not required for every song, but adds rhythmic specificity when the groove character matters.

---

## 4. INSTRUMENT-GENRE CONVENTIONS (Tagg Applied)

> For detailed sound-descriptor vocabulary with character-budget-aware compression levels, see `references/INSTRUMENT_SOUND_REFERENCE.md`. When building Style Prompts, use SOUND descriptors ('squelching acid bass') rather than gear names ('Roland TB-303').

### 4.1 Instrument Signification — What Sounds MEAN

Every instrument carries cultural connotation independent of melody. Choosing the wrong instrument for the emotional content creates subconscious dissonance:

| Instrument | Signifies (Cultural Connotation) | Best For |
|---|---|---|
| **Acoustic guitar (fingerpicked)** | Honesty, vulnerability, folk-truth, handmade | Confession, storytelling, intimacy |
| **Acoustic guitar (strummed)** | Community, warmth, campfire, accessibility | Anthems, group singing, folk |
| **Electric guitar (clean)** | Clarity, jangle, indie, daylight | Upbeat indie, 80s nostalgia, brightness |
| **Electric guitar (distorted)** | Rebellion, aggression, electricity, youth | Rock, metal, anger, power |
| **Electric guitar (reverb/delay)** | Space, atmosphere, post-rock, vastness | Emotional swells, cinematic, introspection |
| **Piano (sparse)** | Solitude, confession, intimacy, truth | Ballads, vulnerability, grief |
| **Piano (full/orchestral)** | Grandeur, drama, classical weight | Epic moments, revelation, ceremony |
| **Strings (sustained)** | Emotion, drama, film score, beauty | Climactic moments, beauty, sadness |
| **Strings (staccato)** | Tension, urgency, thriller, precision | Action, fear, investigation |
| **Strings (pizzicato)** | Playfulness, quirk, curiosity, ticking | Comedy, whimsy, light tension |
| **Cello (solo)** | Deep emotion, gravitas, masculine grief | Grief, weight, introspection |
| **Violin (solo)** | Beauty, fragility, light, yearning | Longing, nostalgia, beauty |
| **Brass (full)** | Power, triumph, ceremony, authority | Victory, declarations, marches |
| **Brass (muted/jazz)** | Noir, sophistication, night, smoke | Jazz, noir, late-night storytelling |
| **Synth pads** | Space, digital, otherworldly, atmosphere | Ambient, electronic, sci-fi, dreamstate |
| **Synth lead** | Retro, future, neon, energy | 80s, synthwave, dance, sci-fi |
| **Sub bass** | Threat, depth, heartbeat, underground | Dark music, horror, primal |
| **Drums (tribal/hand)** | Primal, ancient, ritual, earth | Ceremonial, combat awakening, folk-tribal |
| **Drums (electronic)** | Machine, precision, modernity, cold | Electronic, industrial, clinical |
| **Drums (brushed)** | Gentle, jazz, intimate, warm | Jazz, soul, intimate ballads |
| **Drums (full kit, loud)** | Energy, rock, power, driving | Rock, punk, anthems |
| **Choir** | Spiritual, vast, collective, transcendence | Resolution, acceptance, spiritual moments |
| **Choir (whispered)** | Dread, haunting, supernatural, secrets | Horror, psychological tension, mystery |
| **Concertina/accordion** | Coastal folk, warmth, tradition, handmade | Celtic, folk, warmth, nostalgia |
| **Flute** | Nature, pastoral, lightness, ancient | Folk, celtic, spiritual, pastoral |
| **Organ** | Church, sacred, vast, authority | Spiritual, gothic, ceremonial |
| **Heartbeat percussion** | Mortality, vulnerability, primal fear, life | Tension, intimate dark moments |
| **Wind/breath textures** | Nature, isolation, open space, cold | Journey, solitude, landscape |
| **Water sounds** | Cleansing, flow, peace, transition | Bridge sections, oasis moments, transitions |
| **Glass/crystal textures** | Otherworldly, ethereal, fragile, liminal | Supernatural, transformation, threshold |

### 4.2 Genre-Instrument Matrix

| Genre | Required Instruments | Optional Color | Avoid |
|---|---|---|---|
| **Dark cinematic rock** | Distorted guitar, heavy drums, bass, strings | Piano, choir, brass | Acoustic guitar, ukulele, happy synths |
| **Post-rock** | Reverb guitar, bass, drums (dynamic), pads | Strings, piano, field recordings | Brass, EDM synths, rap vocals |
| **Atmospheric indie** | Guitar (clean/reverb), pads, subtle drums | Piano, strings, ambient textures | Heavy distortion, brass, tribal drums |
| **Folk/acoustic** | Acoustic guitar, minimal percussion | Violin, cello, flute, harmonica | Synths, heavy drums, distortion |
| **Dark indie pop** | Guitar, synths, drums, bass | Strings, piano, electronic textures | Orchestra, metal guitars, tribal |
| **Cinematic orchestral** | Strings, brass, piano, percussion | Choir, harp, woodwinds | Electric guitar, synths, drum machine |
| **Lo-fi indie** | Guitar, soft drums, bass, tape texture | Piano, ambient noise, vinyl crackle | Pristine production, orchestra, choir |
| **Tribal/primal** | Hand drums, percussion, sub bass | Didgeridoo, chanting, earth textures | Synths, clean electric, piano |
| **Neo-soul/jazz** | Rhodes/keys, bass (walking), drums (brushed) | Guitar (clean), horns (muted), strings | Distortion, metal drums, tribal |
| **Industrial** | Synths, drum machines, distorted bass | Samples, noise, glitch | Acoustic instruments, warmth, strings |
| **Nordic/Celtic folk** | Acoustic strings, violin/fiddle, flute | Bodhran, harp, voice as instrument | Synths, heavy drums, brass |
| **Ambient** | Pads, textures, field recordings, minimal piano | Guitar (long reverb), voice-as-texture | Drums, bass, anything rhythmically driving |

### 4.3 Instrument Density Guidelines

| Song Moment | Instrument Count | Reasoning |
|---|---|---|
| Intro (sparse) | 1-2 | Draws listener in, creates space to fill |
| Verse (intimate) | 2-4 | Supports voice without competing |
| Pre-Chorus (building) | 3-5 | Layering creates anticipation |
| Chorus (full) | 4-7 | Maximum texture for maximum impact |
| Bridge (stripped) | 1-3 | Subtraction = contrast = emotional power |
| Final Chorus (maximum) | 5-8 | Earned density — everything deployed |
| Outro (dissolving) | 1-3 | Resolution requires space |

---

## 5. SUNO PROMPT SCIENCE

### 5.1 The Prompt Formula (Community-Tested, 2025-2026) [Tier 3]

```
Genre, BPM, Mood, Instruments, Vocal Style, Era/Production, Direction
```

**Rules:**
- Genre MUST be first — it anchors everything else
- Comma-separated descriptors — not sentences
- 5-8 tags maximum — past 10, signals conflict (v5.5-era (legacy) - re-validate on V6)
- Each tag must point in the same direction — no contradictions
- Negative tags (exclusions) go in Suno's Exclude field as plain comma-separated text with no dash prefix (e.g. `trap drums, beatboxing, vocal hums, bright synths`), not in the Style Prompt

### 5.2 Era Anchoring (More Powerful Than Genre Labels)

Era references give Suno a specific sonic period to build from. In community testing the model responds to time and scene references more precisely than to genre names alone [Tier 3]. Era and scene words are fine; artist, album and band names are not -- convert them to descriptors (§11). The examples below follow that rule:

| Instead of... | Use... | Why |
|---|---|---|
| "Indie rock" | "Early 2000s garage rock revival with raw production" | Specific sonic period = specific sound |
| "Pop" | "Late-2010s minimal dark pop, whispered close-mic vocal, heavy sub bass" | Era + signature production traits anchor the sound |
| "Jazz" | "Late-1950s modal jazz, spacious improvisation, muted trumpet, brushed drums, warm room mic" | A specific sonic moment described in production terms |
| "Folk" | "Late 1960s Laurel Canyon folk, warm tape saturation" | Place + time + production = precise |
| "Electronic" | "Early-1980s German electronic, cold precise drum machines, minimal sequenced synths, vocoder" | Cultural movement > genre label |

**Critical rule:** Era tags bias PRODUCTION STYLE (recording technique, mix character, sonic texture), not just instrumentation. Saying "1970s" adds tape warmth, analog compression, room mic character. To get vintage instruments with modern production, separate explicitly: "modern production, vintage 1970s guitar tone."

### 5.3 Genre Combination Rules

| Pattern | Result | Example |
|---|---|---|
| Single genre (specific) | Focused, conventional | "Dark cinematic rock" |
| Genre + modifier | Genre with a flavor | "Post-rock with industrial undertones" |
| Genre + Genre (70/30) | Dominant + flavor | "Dark indie pop + ambient post-rock swells" |
| Genre + Genre + Genre | DANGER — averaged mush | "Jazz + rock + electronic + folk" = nothing |
| Genre + Era | Precise sonic period | "Mid-90s Bristol trip-hop, dusty breakbeats, noir strings" |

**The 70/30 Rule** [Tier 2/3: craft heuristic]: One dominant genre (70% of the sound) + one flavor genre (30% color/texture). This produces fusion that still has an identity. 50/50 splits tend to confuse Suno.

### 5.4 What Suno Responds To (Tested Tags by Category)

#### Drum Identity (Name the style, not "good beat"):
```
boom-bap, one-drop, four-on-the-floor, brushed swing, half-time trap,
tribal percussion, breakbeat, blast beat, marching, shuffled, syncopated,
hi-hat driven, tom-heavy, rim clicks, jazz brushes, military snare,
hand percussion, cajon, bodhran, frame drum, taiko
```

#### Production Space:
```
intimate room, cathedral reverb, bedroom production, stadium mix,
lo-fi tape, pristine digital, warm analog, cold clinical,
vinyl crackle, tape saturation, close-mic, distant-mic,
room tone, dead room, live room, ambient field recording
```

#### Vocal Delivery:
```
breathy, raspy, smooth, powerful, whispered, gritty, warm, soulful,
spoken word, falsetto, chest voice, head voice, belting, crooning,
conversational, intimate, projected, strained, cracking, fragile,
close-mic, distant, reverbed, dry, doubled, harmonized
```

#### Mood/Atmosphere:
```
haunting, ethereal, cinematic, intimate, vast, claustrophobic,
warm, cold, aggressive, gentle, melancholic, triumphant,
unsettling, comforting, eerie, peaceful, tense, released,
brooding, uplifting, bittersweet, nostalgic, futuristic, ancient
```

### 5.5 Common Suno Prompt Failures

> [Tier 3: community observations, mostly from v5.x renders]

| Failure Pattern | What Happens | Fix |
|---|---|---|
| **Genre overload** | "Jazz rock electronic folk ambient" → averaged generic | Pick ONE dominant genre + ONE flavor maximum |
| **Mood pile-up** | "Dark mysterious noir smoky cinematic tense" → mush | Pick 2-3 mood words maximum that ALIGN |
| **Contradictory tags** | "Aggressive + gentle" / "Intimate + stadium" | Remove the contradiction — pick a direction |
| **Missing genre** | Only mood + instruments, no genre anchor | Genre MUST be first — it's the foundation |
| **Missing BPM** | No tempo reference → Suno guesses average | Always specify BPM or tempo descriptor |
| **Over-specific instruments** | 12+ instruments listed → Suno can't render all | Pick 4-6 key instruments maximum |
| **Era conflict** | "1980s synth + modern trap drums" → confused | Separate era from production explicitly |
| **Vocal mismatch** | Vocal tag doesn't match genre expectations | Vocal style must align with genre conventions |
| **Tags past 10** | Signal conflict → defaults to generic center | Reduce to 5-8 focused, aligned tags (v5.5-era count - re-validate on V6) |
| **Sentences instead of tags** | "I want a song that sounds like..." → parsed poorly | Comma-separated descriptors in the Style field (V6's section-edit feature does take plain-language instructions; that is a separate input) |

### 5.6 Suno v5.x Behavioral Notes — v5.5-era (legacy) - re-validate on V6

> Observed on v5.0-v5.5 [Tier 3]. For V6 lyric-tag behaviour see `references/V6_TAG_DISCOVERY.md`
> (V6 format: no pipe notation, no `[Tag Vocabulary]` block, 2-4 tags per section).

| Behavior | Implication |
|---|---|
| Genre combinations work reliably | Use `+` to combine: "dark cinematic rock + nordic folk" |
| Natural language tempo descriptors parse | "Slow funeral march pace" works alongside BPM |
| Extended prompt parsing improved | Production Direction blocks are now read as tag-adjacent |
| Unrecognized `[tags]` become section labels | Our mood-labeled sections work: `[Verse 1 – Cold / Vast]` |
| Era tags bias production aggressively | Specify era for MIX character, not just instruments |
| "No" negation works in Style Prompt | "No drums" in Style field is effective (but Exclude field is cleaner) |
| Pipe notation is parsed efficiently (v5.5) | `[chorus | powerful, wide, choir swell]` = one-line control. Legacy: do not use in V6 songs |
| 48kHz output available | `[Hyper-Realistic]` tag was reported to raise quality (v5) |

### 5.7 Anti-Pairs (Genre Combinations That Do NOT Work)

> [Tier 3: Community heuristic]
> Credit: Omnisona (Suno AI God Mode Manual v3.0, March 2026)

Certain genre combinations have near-zero compatibility in Suno. The tags pull vocal delivery, rhythmic framework, or production aesthetic in directly opposing directions, producing averaged mush rather than meaningful fusion:

| Genre A | Genre B | Why |
|---|---|---|
| Gregorian Chant | Trap | Monophonic sacred vocal tradition vs. 808 sub-bass and hi-hat rolls -- incompatible vocal register, rhythmic framework, and production aesthetic |
| Classical Baroque | Lo-fi Bedroom Pop | Ornate counterpoint and formal harpsichord structure vs. deliberately degraded production and simple chord loops -- contradictory production intent |
| Opera | Mumble Rap | Bel canto projection and vibrato vs. understated, relaxed delivery with heavy processing -- directly contradictory vocal instructions |

**Note:** Genre pairs that share vocabulary (e.g., "dark" + "cinematic") are modifiers of each other, not anti-pairs. "Dark cinematic rock" is a valid compound genre. Anti-pairs are combinations where the core production or performance demands genuinely conflict.

**Fix:** Replace one genre with a compatible alternative, or restructure as a 70/30 split where one genre clearly dominates.

---

## 6. STYLE PROMPT EVALUATION FRAMEWORK

### 6.1 The 7-Point Assessment

When evaluating a Style Prompt, check each dimension:

| # | Dimension | Question | Score If Wrong |
|---|---|---|---|
| 1 | **Genre** | Is this the right cultural container for the emotional content? (Fabbri) | Fatal — whole sound mismatches |
| 2 | **Key/Mode** | Is the MODE right for the emotion (cue hierarchy), and does the key put the melody in the right part of the singer's range? | High — mode is the #1 perceived-emotion cue |
| 3 | **BPM** | Is the tempo in the right range for both genre AND emotion? | High — tempo is the #2 emotional cue |
| 4 | **Instruments** | Do the chosen instruments signify correctly? (Tagg) | Medium — wrong instruments = wrong connotation |
| 5 | **Vocal style** | Does the vocal delivery match genre expectations AND lyric content? | Medium — voice is the melodic layer focus |
| 6 | **Era/Production** | Is the production aesthetic serving or fighting the content? | Medium — wrong era = wrong sonic period |
| 7 | **Space/Mood** | Are the atmospheric descriptors aligned and non-contradictory? | Low — vague is worse than wrong |

### 6.2 Genre-Emotion Alignment Matrix

Use this to check if the specified genre serves the song's emotional content:

| Emotional Territory | Optimal Genres | Suboptimal (Will Fight) |
|---|---|---|
| Male vulnerability/confession | Dark indie, lo-fi indie rock, atmospheric folk, neo-soul | Metal, EDM, pop-punk, happy pop |
| Epic journey/determination | Cinematic rock, post-rock, orchestral folk | Jazz, ambient, lo-fi, minimal |
| Grief/loss | Dark folk, ambient, piano ballad, post-rock, chamber | Funk, EDM, punk, ska, pop |
| Combat/aggression | Dark cinematic rock, industrial, metal, tribal | Acoustic folk, jazz, ambient, bossa nova |
| Love/warmth | Indie pop, folk, neo-soul, dream pop | Industrial, metal, dark ambient, noise |
| Horror/dread | Dark ambient, industrial, cinematic thriller, noise | Happy pop, folk, funk, reggae |
| Transcendence/acceptance | Ambient, post-rock, choir-driven, ethereal folk | Punk, metal, industrial, trap |
| Anxiety/tension | Dark indie pop, trip-hop, industrial-lite, post-punk | Acoustic folk, happy pop, reggae |
| Found family/warmth | Folk, acoustic, indie pop, warm rock | Metal, industrial, dark ambient |
| Self-discovery/identity | Atmospheric rock, indie, post-rock, art pop | Genre conventions too rigid (metal, country, EDM) |

### 6.3 Alternative Style Prompt Generation

When the current Style Prompt is suboptimal, generate alternatives by:

1. **Identify the core emotional territory** of the lyrics (not the plot)
2. **Find the optimal genre(s)** from the Genre-Emotion Matrix
3. **Select the key** using the Key Selection Decision Framework
4. **Set the BPM** from the BPM-Emotion Interaction table
5. **Choose instruments** that signify correctly for both genre and emotion (Tagg)
6. **Add era anchoring** if a specific sonic period would serve the song
7. **Build the prompt** using the 7-dimension formula: Genre, BPM, Mood, Instruments, Vocal, Era/Production, Direction

**Output format for alternatives:**
```
Option A: [Complete rewritten Style Prompt]
Reasoning: [Why this genre/key/BPM serves the emotional content better]
Expected improvement: [What changes in the Suno render]

Option B: [Complete rewritten Style Prompt]  
Reasoning: [Different angle — what this prioritizes instead]
Expected improvement: [What this optimizes for]
```

---

## 7. SECTION-LEVEL TAG OPTIMIZATION

### 7.1 Per-Section Tag Selection (Tagg Applied to Suno Tags)

Each section's production cue tags should:
1. **Signify the correct emotion** for that section's lyric content
2. **Contrast with adjacent sections** (variety prevents monotony)
3. **Support the proxemic arc** (intimate sections = sparse tags, public sections = full tags)
4. **Stay at 2-4 tags per section** (V6 canonical grammar; tag the section top, not every line). The older "max 3 per section" sweet spot is v5.5-era (legacy).

### 7.2 Section-Emotion-Tag Mapping

> The examples below are v5.5-era free-form descriptor tags. In V6 songs, express the same intent with
> canonical tags (`[Instrument: Piano In]`, `[Dynamic: Crescendo]`, `[Vocal: Whisper]`) -- see
> `references/V6_TAG_REFERENCE.md`.

| Section Emotion | Effective Tags | Ineffective Tags |
|---|---|---|
| Intimate/vulnerable | `[Sparse piano, close-mic vocal]` | `[Full orchestra, stadium reverb]` |
| Building tension | `[Strings enter, bass deepens, drums build]` | `[Everything at once, massive]` |
| Explosive release | `[Full drums, distorted guitar, wide stereo]` | `[Quiet, minimal, sparse]` |
| Aftermath/silence | `[Single note, breath, room tone]` | `[Driving, energetic, full band]` |
| Acceptance/warmth | `[Gentle strings, choir pad, warmth]` | `[Cold, clinical, sparse]` |
| Dread/horror | `[Dissonant strings, sub bass, no melody]` | `[Bright, warm, major chords]` |
| Transcendence | `[Vast reverb, choir swell, dissolving]` | `[Close-mic, dry, tight]` |

### 7.3 Dynamic Contrast Rules

- **Never** use the same tag density for adjacent sections
- **Always** strip at least ONE layer for bridges (subtraction = power)
- **Build** gradually: +1 element per section maximum (don't add 5 instruments at once)
- **Peak** density should occur at the Final Chorus (save your biggest texture for last)
- **Resolve** by removing layers in the outro (mirror the intro's sparseness)

---

## 8. CREATIVE SLIDER RECOMMENDATIONS — v5.5-era (legacy) - re-validate on V6

> OPTIONAL. Use only if your Suno UI exposes these sliders; the values are v5.5-era starting points
> [Tier 3], not V6-validated settings.

### 8.1 Slider-Genre Mapping

| Genre/Context | Weirdness | Style Influence | Audio Influence (if Inspo) |
|---|---|---|---|
| Radio pop/commercial | 35-45% | 60-70% | 55-65% |
| Indie/alternative | 50-55% | 50-60% | 45-55% |
| Concept album (this repo's albums) | 50-55% | 50-60% | 45% |
| Experimental/art | 60-75% | 40-50% | 30-40% |
| Genre-strict (jazz, metal) | 40-50% | 65-80% | 50-60% |
| Character voice songs | 45-55% | 60-70% | 45-55% |
| Atmospheric/ambient | 55-65% | 45-55% | 40-50% |

### 8.2 When to Adjust Sliders

- **Increase Weirdness** when: the song needs surprise, the genre is being subverted, you want Suno to contribute ideas
- **Decrease Weirdness** when: strict genre adherence matters, the song is commercial, predictability serves the hook
- **Increase Style Influence** when: the Style Prompt is highly specific and you want strict adherence
- **Decrease Style Influence** when: the prompt is looser and you want Suno to interpret freely

---

## 9. COMPLIANCE CHECKLIST (Technical Readiness)

### 9.1 Required Elements

| Check | Present? | Notes |
|---|---|---|
| `[Title: Song Title]` | ☐ | Must be above intro, in lyrics field |
| `[Production Direction: ...]` | ☐ | Consistency anchor — survives regenerations |
| `[Vocal Direction: ...]` | ☐ | Voice specs + delivery arc |
| Style Prompt ≤1000 chars | ☐ | Count positives; negatives to Exclude field |
| Lyrics ≤5000 chars (with tags) | ☐ | Total including all direction blocks |
| `[End]` at bottom | ☐ | Song termination signal (V6 format) |
| Section tags on own lines | ☐ | Never same line as lyrics |
| Lines ~7-12 syllables | ☐ | Target [Tier 2]; 13-15 = review stress density/singability; 16+ = Compression Test |
| Named `()` layers declared | ☐ | Any `(X layer: text)` needs Style Prompt declaration |
| Exclusions in Exclude field | ☐ | Plain comma-separated, no dash prefix; in song files an `## EXCLUSIONS:` section; never inside the lyrics body |
| Per-section production tags | ☐ | Present, 2-4 per section (V6) |
| BPM specified | ☐ | In Style Prompt or as descriptor |
| Genre specified FIRST | ☐ | First element of Style Prompt |

### 9.2 Style Prompt Structure Validation

```
✓ Genre is the FIRST element
✓ BPM or tempo descriptor is present
✓ Mood/atmosphere words ≤3 (non-contradictory)
✓ Instrument list is ≤6 items
✓ Vocal style is specified
✓ Total tag count is 5-8, not exceeding 10 (v5.5-era (legacy) - re-validate on V6)
✓ No contradictory tags present
✓ Era anchoring used (if applicable)
✓ Negative exclusions are in Exclude field (not Style), plain comma-separated, no dash prefix
```

---

## 10. QUICK REFERENCE TABLES

### 10.1 Genre → Key → BPM Quick Lookup

> Starting points [Tier 3 working associations]. The key column matters mainly for mode and for where
> the melody sits in the singer's range (§2.2 note); BPM ranges follow §3.1.

| Your Song Is About... | Try This Genre | In This Key | At This BPM |
|---|---|---|---|
| Male vulnerability | Dark indie atmospheric | Em or Am | 72-85 |
| Epic fantasy journey | Cinematic rock / post-rock | Dm or Em | 85-96 |
| Combat/violence discovered | Dark aggressive cinematic rock | Bm or C#m | 96-110 |
| Grief for a mentor | Dark folk / chamber | Am or Dm | 65-76 |
| Found family/warmth | Acoustic folk / warm indie | G or D | 88-100 |
| Psychological thriller | Cinematic thriller / noir | Eb minor or F#m | 75-82 |
| Self-integration/acceptance | Atmospheric indie / art rock | Am→C (modulation) | 88-96 |
| Love/romance | Indie pop / dream pop | Ab or E | 95-110 |
| Transcendence/spiritual | Ambient / ethereal / post-rock | Em or open tuning | 65-75 |
| Anger/betrayal | Post-punk / dark rock | Bm or Gm | 110-130 |
| Anxiety/spiral | Dark indie pop / trip-hop | F#m or Ebm | 96-108 |
| Nostalgia/memory | Lo-fi indie / dream pop | Am or G | 80-95 |

### 10.2 Hit Formula Alignment

| Formula | Genre Space | Key | BPM | Vocal | Production |
|---|---|---|---|---|---|
| **F1 (Vulnerability)** | Dark indie / lo-fi rock | Minor (Em, Am) | 70-85 | Breathy, close-mic, imperfect, cracking | Minimal, intimate, room tone |
| **F2 (Anthem)** | Indie rock / atmospheric pop | Minor→Major lift | 90-110 | Builds from restrained to open, chant-friendly | Maximum production, earned layers |

---

## THEORETICAL SOURCES

| Source | Contribution |
|---|---|
| **Franco Fabbri** (1982, "A Theory of Musical Genres: Two Applications") | Genre as musical events (real or possible) governed by socially accepted rules of five TYPES -- formal and technical, semiotic, behavioural, social and ideological, economical and juridical; their weight varies by genre |
| **Allan F. Moore** (2001, 2012) | Style vs genre distinction, categorical conventions in music discourse |
| **Philip Tagg** (2013) | Musemes — smallest meaningful musical units, cultural connotation of timbres |
| **Patrik Juslin** (2013, "From everyday emotions to aesthetic emotions: towards a unified theory of musical emotions", *Physics of Life Reviews* 10(3)) | BRECVEMA -- 8 mechanisms by which music INDUCES (felt) emotion |
| **Eerola, Friberg & Bresin** (2013, "Emotional expression in music: contribution, linearity, and additivity of primary musical cues", *Frontiers in Psychology* 4:487) | PERCEIVED-emotion cue hierarchy from systematically manipulated cues (mode > tempo > register > dynamics > articulation > timbre); tempo most important for arousal. Studied mode, not specific keys |
| **Gabrielsson & Lindström** (2010) | Emotional expression in music -- contribution of primary musical cues |
| **C. F. D. Schubart** (*Ideen zu einer Ästhetik der Tonkunst*, written 1784-85, publ. 1806; English in Rita Steblin, *A History of Key Characteristics*, 1983/2002) | Historical key characteristics under unequal temperaments [Tier 2 historical tradition, not psychology] |
| **Suno community research** (2025-2026) | Prompt formula, era anchoring, genre combination rules, tag limits, slider behavior (mostly v5.x; re-validate on V6) |
| **beehiiv/roo research** (2026) | 301 styles tested, prompt ordering matters, genre-first principle, 5-8 tag sweet spot |
| **HowToPromptSuno** (2025-2026) | Structural prompt methodology, drum identity naming, production space descriptors |

---

*Reference document for the Suno Optimization Assessment module of the Critic agent.*

---

## 11. ARTIST REFERENCE CONVERSION

### Purpose

When an artist name appears in creative direction (e.g., "in the style of X", "like Billie Eilish"), it must be converted to descriptive production language before final output. Artist names are not recognized as Suno prompt parameters -- Suno does not understand "make it sound like [Artist]." Descriptive language gives Suno actionable production instructions that produce dramatically better renders.

### Conversion Methodology

Step-by-step process to convert any artist reference:

1. **Identify the artist's genre ecosystem** -- What cultural container do they occupy?
2. **Pin the era** -- What sonic period defines their signature sound?
3. **List signature instruments/textures** -- What do you HEAR in their productions?
4. **Describe production characteristics** -- Recording technique, mix style, spatial design
5. **Define vocal style** -- Delivery, register, techniques, emotional character
6. **Note structural habits** -- Song forms, dynamics patterns, arrangement choices
7. **Combine into comma-separated descriptors** -- Following the 7-Dimension formula

### Conversion Examples

| Artist Reference | Converted To |
|---|---|
| "In the style of Radiohead" | "Atmospheric post-rock, electronic textures, unconventional structures, falsetto vocals, quiet-loud dynamics, 2000s experimental production" |
| "Like Billie Eilish" | "Dark minimal pop, whispered close-mic vocals, heavy sub bass, sparse production, intimate bedroom aesthetic, 2019 lo-fi pop" |
| "Wardruna vibes" | "Nordic folk, ancient instrumentation, throat singing textures, ritualistic percussion, vast reverb, pre-Christian atmosphere" |
| "Sigur Ros feel" | "Ethereal post-rock, bowed guitar, falsetto vocals as texture, glacial builds, Icelandic atmosphere, vast reverb spaces" |
| "Like Hozier" | "Dark folk-rock, rich baritone, gospel-influenced builds, literary lyrics, organic production, Celtic-soul fusion" |

### Why This Matters for Suno

- **Artist names are not prompt parameters.** Suno's model does not map "Radiohead" to a specific set of production instructions. It may produce vaguely related output or ignore the reference entirely.
- **Descriptive language IS actionable.** "Atmospheric post-rock, electronic textures, falsetto vocals, 2000s experimental production" maps directly to genre, instruments, vocal delivery, and era -- all dimensions Suno understands and responds to.
- **Consistency across renders.** Artist names produce inconsistent results because Suno interprets them differently each generation. Descriptive language produces consistent, reproducible output.
- **Specificity outperforms shortcuts.** The 7-dimension formula (genre, BPM, mood, instruments, vocal, era, space) always outperforms shorthand references.

---

## 12. SUNO VERSION STATUS

> Track which Suno-specific claims have been verified and when they need retesting.
> Suno updates frequently. V6 (v6 / v6-wild / v6-mini) has been the default since ~Sept 8, 2026;
> every v5.5-era finding below needs re-validation on V6 before it is relied on.
> See `experiments/suno/` for detailed test logs and `references/V6_TAG_DISCOVERY.md` → Results Log
> for V6 render evidence.

| Claim | Verified On | Suno Version | Confidence | Retest By |
|---|---|---|---|---|
| V6 model family (v6 / v6-wild / v6-mini) is the default; v5.5 and earlier are being retired | Sept 2026 | v6 | High | Ongoing |
| `[Instrument: X In]` / `[Instrument: X Out]` entrances/exits are honored | Sept 2026 | v6 | Working model (user-confirmed) | Log render IDs in V6 results log; Dec 2026 |
| `[Tag Vocabulary]` block is not needed in final output | Sept 2026 | v6 | Working model (user-confirmed) | Dec 2026 |
| Style field = WHAT (identity), inline tags = HOW (arrangement) | Sept 2026 | v6 | Working model (user-confirmed) | Dec 2026 |
| V6 lyric format: section tags, 2-4 tags per section, `[End]`, no pipe notation | Sept 2026 | v6 | Working model | Dec 2026 |
| 1000-char Style / 5000-char Lyrics limits still apply on V6 | — | v6 | Unverified (open question) | Re-validate on V6 |
| Style Prompt limit is 1000 chars | June 2026 | v5.5 | High | Re-validate on V6 |
| Lyrics field limit is 5000 chars | June 2026 | v5.5 | High | Re-validate on V6 |
| `[control: no-repeat]` prevents line looping | June 2026 | v5.5 | Medium | Re-validate on V6 (legacy global tag) |
| Pipe notation `[section | params]` parsed correctly | June 2026 | v5.5 | High | Re-validate on V6 (not used in V6 format) |
| Era tags bias production style (not just instruments) | June 2026 | v5.5 | High | Re-validate on V6 |
| Genre must be first element in Style Prompt | June 2026 | v5.5 | High | Re-validate on V6 |
| 5-8 tags optimal (>10 causes signal conflict) | June 2026 | v5.5 | Medium | Re-validate on V6 |
| Named `()` layers require Style Prompt declaration | June 2026 | v5.5 | High | Re-validate on V6 |
| Personas maintain vocal identity across generations | June 2026 | v5.5 | Medium | Re-validate on V6 |

---

## 13. TEMPORAL SPECIFICITY IN SUNO RENDERING

Numbers and time references in lyrics interact with Suno's generation in specific ways:

- **Numbers are rendered literally** -- Suno vocalizes "3am" and "25 or 6 to 4" as written; ensure the syllable count works melodically
- **Days of the week may carry implicit mood** -- "Friday night" likely biases toward upbeat/celebratory generation; "Sunday morning" toward reflective/sparse (based on community testing, not confirmed)
- **Precise times in lyrics may anchor production** -- referencing time in Production Direction (e.g., "3am insomnia atmosphere") may help Suno select appropriate timbral palette
- **Cultural-code times may carry genre/mood signals** -- "Summer of '69" likely triggers classic rock warmth; "Friday night" likely triggers party-energy; "3am" likely triggers intimate/dark production (hypothesized from the theoretical framework; untested systematically)
- **Odd numbers read as authentic** -- Suno does not weight this, but listeners will perceive irregularity (6:14) as more real than round numbers (6:00)

> **Confidence note:** The claims above about Suno's mood/genre responses to temporal language are untested hypotheses extrapolated from the theoretical framework and anecdotal community observations. Systematic A/B testing has not been performed.

> Full temporal specificity guidelines: `core/methodology/songwriting.md` → "Temporal Specificity in Lyrics"
