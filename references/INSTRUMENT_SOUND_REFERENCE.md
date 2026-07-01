# Instrument-to-Sound Translation Reference

> **Evidence Tier:** [Tier 3: Community/platform heuristic] -- Untested against Suno until experiments confirm per-genre. Based on 21machines' acid house experiment (June 2026).

## Design Principle

**Suno responds to SOUND DESCRIPTIONS, not equipment names.** Describe what the instrument SOUNDS like, not what it IS. Writing "TB-303" gives Suno nothing actionable. Writing "squelching acid bass, resonant filter sweeps" tells it exactly what timbre to produce.

Evidence basis: 21machines' acid house experiment (June 2026) demonstrated that timbre/scene descriptors outperform gear model names in Suno v5.5 renders.

---

## Character Budget Guidance

- ~120 usable characters in a Style Prompt (after genre and vocal tags)
- ~20 chars per instrument at **minimum** tier / ~35 at **compressed** / ~65 at **full**
- Most prompts fit 3-4 instruments at compressed tier

---

## Three-Tier Compression System

| Tier | Use When | Typical Length |
|---|---|---|
| **Full** | Single featured instrument, plenty of budget | 55-80 chars |
| **Compressed** | Normal use, 2-4 instruments sharing space | 29-48 chars |
| **Minimum** | Budget-critical, 5+ instruments | 8-22 chars |

---

## 1. Electronic / Dance

### TB-303
- **Full:** squelching resonant acid synthesizer bass with filter-sweep slides (66 chars)
- **Compressed:** squelching acid bass, resonant filter sweeps (44 chars)
- **Minimum:** acid bass (9 chars)
- **Inline tag:** `[verse | squelching acid bass, driving four-on-floor]`

### TR-909
- **Full:** punchy analog kick drum with crisp metallic hi-hats and snappy snare (68 chars)
- **Compressed:** punchy analog kick, crisp hi-hats, snappy snare (47 chars)
- **Minimum:** analog drum machine (19 chars)
- **Inline tag:** `[drop | punchy analog kick, crisp hi-hats, pounding bass]`

### TR-808
- **Full:** deep booming sub-bass kick with sharp claps and tinny cowbell (61 chars)
- **Compressed:** booming 808 kick, sharp claps (29 chars)
- **Minimum:** 808 drums (9 chars)
- **Inline tag:** `[verse | booming 808 kick, trap hi-hats, dark atmosphere]`

### Korg M1
- **Full:** glassy digital piano with lush orchestral string pads (53 chars)
- **Compressed:** glassy digital piano, lush string pads (38 chars)
- **Minimum:** digital piano pad (17 chars)
- **Inline tag:** `[chorus | glassy digital piano, lush string pads, soaring vocal]`

### Juno-106
- **Full:** warm detuned analog polysynth with shimmering chorus pads (57 chars)
- **Compressed:** warm detuned chorus synth pad (29 chars)
- **Minimum:** warm synth pad (14 chars)
- **Inline tag:** `[intro | warm detuned chorus synth pad, ambient textures]`

### DX7
- **Full:** crystalline FM electric piano with bell-like harmonic shimmer (61 chars)
- **Compressed:** crystalline FM electric piano, bell shimmer (43 chars)
- **Minimum:** FM electric piano (17 chars)
- **Inline tag:** `[verse | crystalline FM electric piano, gentle groove]`

### Minimoog
- **Full:** thick monophonic analog bass with rich harmonic saturation (58 chars)
- **Compressed:** thick analog bass, rich saturation (34 chars)
- **Minimum:** fat analog bass (15 chars)
- **Inline tag:** `[drop | thick analog bass, driving rhythm, heavy sub]`

### Prophet-5
- **Full:** lush analog polysynth with warm oscillator drift and fat unison (63 chars)
- **Compressed:** lush analog polysynth, warm drift (33 chars)
- **Minimum:** lush polysynth (14 chars)
- **Inline tag:** `[chorus | lush analog polysynth, warm drift, wide stereo]`

### Arp Synthesizer
- **Full:** bright cascading analog arpeggios with sequenced rhythmic pulses (64 chars)
- **Compressed:** bright cascading analog arpeggios (33 chars)
- **Minimum:** analog arpeggios (16 chars)
- **Inline tag:** `[build | bright cascading analog arpeggios, rising energy]`

### Oberheim
- **Full:** massive wide-stereo analog brass stabs with thick filter sweeps (63 chars)
- **Compressed:** massive analog brass stabs, thick filters (41 chars)
- **Minimum:** analog brass stabs (18 chars)
- **Inline tag:** `[chorus | massive analog brass stabs, driving beat]`

### Vocoder
- **Full:** robotic harmonized vocal synthesis with metallic formant texture (64 chars)
- **Compressed:** robotic vocoder harmonics, metallic texture (43 chars)
- **Minimum:** robotic vocoder (15 chars)
- **Inline tag:** `[bridge | robotic vocoder harmonics, ethereal pads]`

### Fairlight
- **Full:** grainy lo-fi digital orchestral samples with 8-bit character (60 chars)
- **Compressed:** grainy digital orchestral samples (33 chars)
- **Minimum:** lo-fi digital samples (21 chars)
- **Inline tag:** `[intro | grainy digital orchestral samples, cinematic atmosphere]`

---

## 2. Rock / Blues / Country

### Telecaster
- **Full:** bright twangy single-coil electric guitar with snappy pick attack (65 chars)
- **Compressed:** bright twangy electric guitar, snappy attack (44 chars)
- **Minimum:** twangy electric guitar (22 chars)
- **Inline tag:** `[verse | bright twangy electric guitar, honky-tonk groove]`

### Stratocaster
- **Full:** glassy bell-like clean electric guitar with smooth singing sustain (66 chars)
- **Compressed:** glassy clean electric guitar, singing sustain (45 chars)
- **Minimum:** clean electric guitar (21 chars)
- **Inline tag:** `[verse | glassy clean electric guitar, bluesy bends]`

### Les Paul
- **Full:** thick warm humbucker crunch with creamy sustain and fat midrange (64 chars)
- **Compressed:** thick warm crunch guitar, creamy sustain (40 chars)
- **Minimum:** warm crunch guitar (18 chars)
- **Inline tag:** `[chorus | thick warm crunch guitar, powerful riff]`

### SG
- **Full:** biting aggressive midrange electric guitar with snarling overdrive (66 chars)
- **Compressed:** biting midrange guitar, snarling overdrive (42 chars)
- **Minimum:** aggressive electric guitar (26 chars)
- **Inline tag:** `[verse | biting midrange guitar, snarling overdrive, tight rhythm]`

### Marshall Amp
- **Full:** crunchy British tube overdrive with tight midrange bark (55 chars)
- **Compressed:** crunchy British tube overdrive (30 chars)
- **Minimum:** British crunch (14 chars)
- **Inline tag:** `[chorus | crunchy British tube overdrive, heavy riff]`

### Fender Amp
- **Full:** sparkling clean American tube amp with warm breakup at volume (61 chars)
- **Compressed:** sparkling clean tube amp, warm breakup (38 chars)
- **Minimum:** clean tube amp (14 chars)
- **Inline tag:** `[verse | sparkling clean tube amp, fingerpicked arpeggios]`

### Vox AC30
- **Full:** chimey jangly British tube amp with glassy treble sparkle (57 chars)
- **Compressed:** chimey jangly tube amp, glassy sparkle (38 chars)
- **Minimum:** jangly tube amp (15 chars)
- **Inline tag:** `[verse | chimey jangly tube amp, arpeggiated chords]`

### Slide Guitar
- **Full:** smooth gliding bottleneck slide with vocal-like legato phrasing (63 chars)
- **Compressed:** smooth bottleneck slide, vocal phrasing (39 chars)
- **Minimum:** slide guitar (12 chars)
- **Inline tag:** `[solo | smooth bottleneck slide, vocal phrasing, delta blues]`

### Pedal Steel
- **Full:** weeping sustained steel guitar with lush pitch bends and volume swells (70 chars)
- **Compressed:** weeping steel guitar, lush bends and swells (43 chars)
- **Minimum:** weeping steel guitar (20 chars)
- **Inline tag:** `[chorus | weeping steel guitar, lush bends and swells]`

### Hammond B3
- **Full:** gritty overdriven rotary organ with percussive key click and drawbar growl (74 chars)
- **Compressed:** gritty rotary organ, percussive click (37 chars)
- **Minimum:** gritty organ (12 chars)
- **Inline tag:** `[verse | gritty rotary organ, percussive click, gospel groove]`

### Wurlitzer
- **Full:** warm tremolo electric piano with soft bark and reedy midrange (61 chars)
- **Compressed:** warm tremolo electric piano, reedy bark (39 chars)
- **Minimum:** warm electric piano (19 chars)
- **Inline tag:** `[verse | warm tremolo electric piano, laid-back soul groove]`

### Rhodes
- **Full:** smooth bell-like electric piano with gentle tremolo and rounded bass (68 chars)
- **Compressed:** smooth bell-like electric piano, gentle tremolo (47 chars)
- **Minimum:** smooth electric piano (21 chars)
- **Inline tag:** `[intro | smooth bell-like electric piano, gentle tremolo]`

### Dobro
- **Full:** bright metallic resonator guitar with nasal twang and open slide (64 chars)
- **Compressed:** bright resonator guitar, nasal twang (36 chars)
- **Minimum:** resonator guitar (16 chars)
- **Inline tag:** `[verse | bright resonator guitar, nasal twang, bluegrass feel]`

---

## 3. Orchestral / Cinematic

### Solo Violin
- **Full:** expressive solo violin with rich vibrato and soaring melodic lines (66 chars)
- **Compressed:** expressive solo violin, rich vibrato (36 chars)
- **Minimum:** solo violin (11 chars)
- **Inline tag:** `[verse | expressive solo violin, rich vibrato, intimate strings]`

### Violin Section
- **Full:** lush massed violin ensemble with wide vibrato and sweeping legato (65 chars)
- **Compressed:** lush violin ensemble, sweeping legato (37 chars)
- **Minimum:** string section (14 chars)
- **Inline tag:** `[chorus | lush violin ensemble, sweeping legato, epic crescendo]`

### Solo Cello
- **Full:** deep resonant solo cello with warm woody tone and lyrical phrasing (66 chars)
- **Compressed:** deep resonant solo cello, lyrical phrasing (42 chars)
- **Minimum:** solo cello (10 chars)
- **Inline tag:** `[bridge | deep resonant solo cello, lyrical phrasing, emotional]`

### Cello Section
- **Full:** rich warm cello ensemble with dark sustained legato bowing (58 chars)
- **Compressed:** rich cello ensemble, dark sustained bowing (42 chars)
- **Minimum:** cello section (13 chars)
- **Inline tag:** `[verse | rich cello ensemble, dark sustained bowing, tension]`

### Double Bass
- **Full:** deep rumbling orchestral double bass with woody pizzicato attack (64 chars)
- **Compressed:** deep rumbling double bass, woody pizzicato (42 chars)
- **Minimum:** orchestral bass (15 chars)
- **Inline tag:** `[verse | deep rumbling double bass, woody pizzicato, dark mood]`

### French Horn
- **Full:** noble warm brass French horn with heroic swelling crescendo (59 chars)
- **Compressed:** noble warm French horn, heroic swells (37 chars)
- **Minimum:** French horn (11 chars)
- **Inline tag:** `[chorus | noble warm French horn, heroic swells, cinematic]`

### Trumpet
- **Full:** bright piercing trumpet with clear articulation and heroic fanfare (66 chars)
- **Compressed:** bright piercing trumpet, heroic fanfare (39 chars)
- **Minimum:** bright trumpet (14 chars)
- **Inline tag:** `[intro | bright piercing trumpet, heroic fanfare, triumphant]`

### Trombone
- **Full:** rich burnished trombone with deep warm slides and legato phrasing (65 chars)
- **Compressed:** rich burnished trombone, warm slides (36 chars)
- **Minimum:** warm trombone (13 chars)
- **Inline tag:** `[verse | rich burnished trombone, warm slides, noir jazz]`

### Oboe
- **Full:** plaintive nasal oboe with pastoral reedy tone and expressive vibrato (68 chars)
- **Compressed:** plaintive nasal oboe, pastoral reedy tone (41 chars)
- **Minimum:** reedy oboe (10 chars)
- **Inline tag:** `[bridge | plaintive nasal oboe, pastoral reedy tone, melancholy]`

### Clarinet
- **Full:** warm liquid clarinet with smooth legato runs and chalumeau depth (64 chars)
- **Compressed:** warm liquid clarinet, smooth legato runs (40 chars)
- **Minimum:** warm clarinet (13 chars)
- **Inline tag:** `[verse | warm liquid clarinet, smooth legato runs, jazz club]`

### Flute
- **Full:** airy silver flute with breathy attacks and pure singing high register (69 chars)
- **Compressed:** airy silver flute, breathy singing tone (39 chars)
- **Minimum:** airy flute (10 chars)
- **Inline tag:** `[intro | airy silver flute, breathy singing tone, ethereal]`

### Timpani
- **Full:** thundering orchestral timpani with deep resonant rolls and dramatic hits (72 chars)
- **Compressed:** thundering timpani, deep resonant rolls (39 chars)
- **Minimum:** timpani rolls (13 chars)
- **Inline tag:** `[build | thundering timpani, deep resonant rolls, epic tension]`

### Harp
- **Full:** shimmering concert harp with cascading glissando arpeggios (58 chars)
- **Compressed:** shimmering harp, cascading glissandos (37 chars)
- **Minimum:** shimmering harp (15 chars)
- **Inline tag:** `[intro | shimmering harp, cascading glissandos, fantasy atmosphere]`

### Pipe Organ
- **Full:** massive cathedral pipe organ with thundering pedal tones and full registration (78 chars)
- **Compressed:** massive cathedral organ, thundering pedals (42 chars)
- **Minimum:** cathedral organ (15 chars)
- **Inline tag:** `[chorus | massive cathedral organ, thundering pedals, sacred]`

### Harpsichord
- **Full:** bright plucked harpsichord with crisp baroque articulation and metallic ring (76 chars)
- **Compressed:** bright plucked harpsichord, crisp baroque feel (46 chars)
- **Minimum:** harpsichord (11 chars)
- **Inline tag:** `[verse | bright plucked harpsichord, crisp baroque feel, chamber]`

---

## 4. Folk / World / Celtic

### Tin Whistle
- **Full:** bright airy tin whistle with quick ornamental trills and Celtic lilt (68 chars)
- **Compressed:** bright tin whistle, quick Celtic trills (39 chars)
- **Minimum:** tin whistle (11 chars)
- **Inline tag:** `[verse | bright tin whistle, quick Celtic trills, jig rhythm]`

### Uilleann Pipes
- **Full:** mellow sweet uilleann pipes with breathy drones and ornamental grace notes (74 chars)
- **Compressed:** mellow uilleann pipes, breathy drones (37 chars)
- **Minimum:** Irish pipes (11 chars)
- **Inline tag:** `[chorus | mellow uilleann pipes, breathy drones, haunting melody]`

### Highland Bagpipes
- **Full:** powerful droning Highland pipes with piercing chanter melody and steady drones (78 chars)
- **Compressed:** powerful droning Highland pipes, piercing melody (48 chars)
- **Minimum:** bagpipes (8 chars)
- **Inline tag:** `[intro | powerful droning Highland pipes, piercing melody]`

### Bodhran
- **Full:** deep resonant bodhran frame drum with driving rhythmic pulse and tonal bends (76 chars)
- **Compressed:** deep bodhran frame drum, driving pulse (38 chars)
- **Minimum:** bodhran drum (12 chars)
- **Inline tag:** `[verse | deep bodhran frame drum, driving pulse, Celtic energy]`

### Irish Fiddle
- **Full:** bright lively Irish fiddle with rapid ornamented jig bowing (59 chars)
- **Compressed:** bright lively Irish fiddle, rapid bowing (40 chars)
- **Minimum:** Irish fiddle (12 chars)
- **Inline tag:** `[chorus | bright lively Irish fiddle, rapid bowing, dance energy]`

### Concertina
- **Full:** reedy bright concertina with punchy bellows-driven dance rhythm (63 chars)
- **Compressed:** reedy bright concertina, punchy bellows (39 chars)
- **Minimum:** concertina (10 chars)
- **Inline tag:** `[verse | reedy bright concertina, punchy bellows, folk dance]`

### Mandolin
- **Full:** bright tremolo mandolin with rapid picked arpeggios and metallic ring (69 chars)
- **Compressed:** bright tremolo mandolin, rapid picking (38 chars)
- **Minimum:** bright mandolin (15 chars)
- **Inline tag:** `[verse | bright tremolo mandolin, rapid picking, bluegrass groove]`

### Banjo
- **Full:** bright rolling banjo with rapid fingerpicked arpeggios and percussive snap (74 chars)
- **Compressed:** bright rolling banjo, rapid fingerpicking (41 chars)
- **Minimum:** rolling banjo (13 chars)
- **Inline tag:** `[chorus | bright rolling banjo, rapid fingerpicking, hoedown energy]`

### Sitar
- **Full:** resonant buzzing sitar with sympathetic string shimmer and microtonal bends (75 chars)
- **Compressed:** resonant buzzing sitar, sympathetic shimmer (43 chars)
- **Minimum:** buzzing sitar (13 chars)
- **Inline tag:** `[verse | resonant buzzing sitar, sympathetic shimmer, raga melody]`

### Tabla
- **Full:** crisp articulate tabla with complex rhythmic patterns and tonal bass strokes (76 chars)
- **Compressed:** crisp tabla, complex rhythmic patterns (38 chars)
- **Minimum:** tabla rhythms (13 chars)
- **Inline tag:** `[verse | crisp tabla, complex rhythmic patterns, meditative groove]`

### Djembe
- **Full:** resonant hand-struck djembe with sharp slaps and deep bass tones (64 chars)
- **Compressed:** resonant djembe, sharp slaps and bass (37 chars)
- **Minimum:** djembe drums (12 chars)
- **Inline tag:** `[chorus | resonant djembe, sharp slaps and bass, tribal energy]`

### Taiko
- **Full:** thundering massive taiko drums with powerful ensemble strikes and deep resonance (80 chars)
- **Compressed:** thundering taiko drums, powerful strikes (40 chars)
- **Minimum:** taiko drums (11 chars)
- **Inline tag:** `[build | thundering taiko drums, powerful strikes, epic tension]`

### Koto
- **Full:** bright plucked koto with delicate glissando sweeps and pentatonic melody (72 chars)
- **Compressed:** bright plucked koto, delicate glissandos (40 chars)
- **Minimum:** plucked koto (12 chars)
- **Inline tag:** `[intro | bright plucked koto, delicate glissandos, zen atmosphere]`

### Didgeridoo
- **Full:** deep droning didgeridoo with rhythmic circular breathing and overtone pulses (76 chars)
- **Compressed:** deep droning didgeridoo, rhythmic overtones (43 chars)
- **Minimum:** droning didgeridoo (18 chars)
- **Inline tag:** `[verse | deep droning didgeridoo, rhythmic overtones, primal groove]`

---

## 5. Synthesizer Specific Sounds

### Supersaw
- **Full:** massive detuned unison sawtooth wave with wide stereo spread and bright shimmer (79 chars)
- **Compressed:** massive detuned supersaw, wide stereo spread (44 chars)
- **Minimum:** supersaw lead (13 chars)
- **Inline tag:** `[drop | massive detuned supersaw, wide stereo spread, euphoric]`

### Moog Bass
- **Full:** deep growling Moog-style bass with ladder filter resonance and sub weight (73 chars)
- **Compressed:** deep growling synth bass, filter resonance (42 chars)
- **Minimum:** growling synth bass (19 chars)
- **Inline tag:** `[verse | deep growling synth bass, filter resonance, dark groove]`

### Juno Pad
- **Full:** warm evolving analog pad with gentle chorus movement and soft attack (68 chars)
- **Compressed:** warm evolving analog pad, gentle chorus (39 chars)
- **Minimum:** warm analog pad (15 chars)
- **Inline tag:** `[intro | warm evolving analog pad, gentle chorus, ambient wash]`

### DX7 Bass
- **Full:** punchy percussive FM bass with metallic transient and quick decay (65 chars)
- **Compressed:** punchy FM bass, metallic transient (34 chars)
- **Minimum:** punchy FM bass (14 chars)
- **Inline tag:** `[verse | punchy FM bass, metallic transient, synth-pop groove]`

### Reese Bass
- **Full:** dark phasing detuned bass with undulating beating frequencies and sub depth (75 chars)
- **Compressed:** dark phasing detuned bass, undulating sub (41 chars)
- **Minimum:** phasing sub bass (16 chars)
- **Inline tag:** `[drop | dark phasing detuned bass, undulating sub, heavy DnB]`

### Amen Break
- **Full:** chopped frenetic breakbeat with rapid snare rolls and stuttering edits (70 chars)
- **Compressed:** chopped frenetic breakbeat, rapid snare rolls (45 chars)
- **Minimum:** chopped breakbeat (17 chars)
- **Inline tag:** `[drop | chopped frenetic breakbeat, rapid snare rolls, jungle]`

---

## 6. Piano Variations

### Concert Grand
- **Full:** rich resonant concert grand piano with full dynamic range and long sustain (74 chars)
- **Compressed:** rich concert grand piano, full dynamics (39 chars)
- **Minimum:** grand piano (11 chars)
- **Inline tag:** `[verse | rich concert grand piano, full dynamics, classical feel]`

### Upright Piano
- **Full:** intimate slightly muted upright piano with woody character and soft hammer tone (79 chars)
- **Compressed:** intimate muted upright piano, woody tone (40 chars)
- **Minimum:** upright piano (13 chars)
- **Inline tag:** `[verse | intimate muted upright piano, woody tone, indie folk]`

### Honky-Tonk Piano
- **Full:** bright detuned honky-tonk piano with jangling out-of-tune character (67 chars)
- **Compressed:** bright detuned honky-tonk piano, jangling (41 chars)
- **Minimum:** honky-tonk piano (16 chars)
- **Inline tag:** `[verse | bright detuned honky-tonk piano, jangling, saloon vibe]`

### Prepared Piano
- **Full:** metallic percussive prepared piano with muted strings and unusual timbres (73 chars)
- **Compressed:** metallic percussive prepared piano, muted strings (49 chars)
- **Minimum:** prepared piano (14 chars)
- **Inline tag:** `[bridge | metallic percussive prepared piano, experimental texture]`

### Toy Piano
- **Full:** tiny bright toy piano with thin metallic tines and childlike simplicity (71 chars)
- **Compressed:** tiny bright toy piano, metallic tines (37 chars)
- **Minimum:** toy piano (9 chars)
- **Inline tag:** `[intro | tiny bright toy piano, metallic tines, music box feel]`

### Celesta
- **Full:** sparkling crystalline celesta with delicate bell-like high register shimmer (75 chars)
- **Compressed:** sparkling celesta, delicate bell shimmer (40 chars)
- **Minimum:** celesta bells (13 chars)
- **Inline tag:** `[bridge | sparkling celesta, delicate bell shimmer, magical]`

---

## 7. Drums / Percussion (Acoustic)

### Jazz Kit (Brushes)
- **Full:** soft swishing jazz brushes on snare with gentle ride cymbal ping and kick thud (78 chars)
- **Compressed:** soft jazz brushes, gentle ride ping (35 chars)
- **Minimum:** jazz brushes (12 chars)
- **Inline tag:** `[verse | soft jazz brushes, gentle ride ping, late-night club]`

### Rock Kit (Studio)
- **Full:** tight punchy studio rock drums with controlled room and crisp snare crack (73 chars)
- **Compressed:** tight studio rock drums, crisp snare crack (42 chars)
- **Minimum:** studio rock drums (17 chars)
- **Inline tag:** `[chorus | tight studio rock drums, crisp snare crack, driving]`

### Rock Kit (Live Room)
- **Full:** roaring live-room rock drums with big ambient reverb and explosive fills (72 chars)
- **Compressed:** roaring live-room rock drums, big reverb (40 chars)
- **Minimum:** live room drums (15 chars)
- **Inline tag:** `[chorus | roaring live-room rock drums, big reverb, anthemic]`

### Motown Kit
- **Full:** warm compressed vintage drums with thick snare thwack and muted kick (68 chars)
- **Compressed:** warm vintage drums, thick snare thwack (38 chars)
- **Minimum:** vintage Motown drums (20 chars)
- **Inline tag:** `[verse | warm vintage drums, thick snare thwack, soul groove]`

### Bonham-Style Kit
- **Full:** massive thundering drums with huge ambient room sound and powerful triplet fills (80 chars)
- **Compressed:** massive thundering drums, huge room sound (41 chars)
- **Minimum:** thundering room drums (21 chars)
- **Inline tag:** `[chorus | massive thundering drums, huge room sound, epic rock]`

### Cajon
- **Full:** warm woody cajon with snappy buzz tone and deep bass slap (57 chars)
- **Compressed:** warm woody cajon, snappy buzz and bass (38 chars)
- **Minimum:** cajon percussion (16 chars)
- **Inline tag:** `[verse | warm woody cajon, snappy buzz and bass, acoustic vibe]`


---

## Cross-References

- **Genre/style tags:** See [SUNO_STYLE_GENRE_REFERENCE.md](SUNO_STYLE_GENRE_REFERENCE.md) for genre selection and mood-key mapping
- **Experiment framework:** See [experiments/suno/](../experiments/suno/) for validation testing methodology
- **Tag formatting:** See [SUNO_TAGS_REFERENCE.md](SUNO_TAGS_REFERENCE.md) for tag syntax and section-level cues

## Promotion Criteria

This reference requires per-genre validation experiments before promotion to [Tier 2]. Each genre family needs at least 3 controlled A/B tests comparing gear-name prompts vs sound-descriptor prompts. See `experiments/suno/TEMPLATE.yml` for the testing framework. Current status: [Tier 3] - validated only for acid house (21machines, June 2026).
