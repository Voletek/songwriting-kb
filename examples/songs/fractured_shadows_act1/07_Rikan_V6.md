# Rikan — Album Track 7 / Act 1 Finale — V6 Format

> **V6 migration of `07_Rikan_v2.md`** (the v5.5-era polished version). Same words, same Style Prompt,
> same condensed direction blocks, ADVANCED BOX and Production Notes, re-tagged in the canonical V6
> grammar from `references/V6_TAG_REFERENCE.md`. The polish notes and the change list from v1 stay in
> the original. Status: not yet rendered on V6. Log results in `## RENDERS` below and in the
> `references/V6_TAG_DISCOVERY.md` results log.

## What changed from the v5.5-era version

| v5.5-era original | V6 version | Why |
|---|---|---|
| Free-text cue rows `[Wet cavern ambience] [Stone drips] [Low hum] [Distant broken piano]` | `[Instrument: Cave Ambience In]` + `[Instrument: Drone In]` + `[Instrument: Piano In]` | V6 honours entrances and exits on cue; the low hum maps to the listed Drone |
| Section cues for strings, choir, thunder, heartbeat, horn, drums, war horns | `[Instrument: X In]` / `[Instrument: X Out]` at the same sections (strings pre-chorus, choir chorus 1, thunder in and out in V2, heartbeat and distant horn pre-chorus 2, drums chorus 2, drums and horn out in the bridge, war horns final chorus) | Same entry points, namespaced |
| `[Cinematic lift]`, `[Strings stronger]`, `[Low strings swelling]`, `[Instruments drop low]` | `[Dynamic: Swell]`, `[Dynamic: Crescendo]`, `[Dynamic: p]` | Namespaced dynamics |
| `[Voice almost spoken]`, `[Fractured whispers]`, `[Choir and baritone together]` | `[Vocal: Half-Spoken]`, `[Male lead, fractured whispers]`, `[Male lead, with choir]` | V6 vocal and role forms |
| `[Heavy silence]` (breakdown); `[War horns sustain — choir holds — one beat of silence]` | `[Dynamic: Silence]` + `[Instrument: Piano Out]`; `[Transition: Sustain, Stop-Time]` | V6 dictionary dynamics and compound transition |
| `[Broken piano returns]` (outro) + `[end]` | `[Instrument: Piano In]` (after the breakdown's Piano Out) + `[Instrument: War Horns Out]` + `[End]` | V6 terminator |
| Section subtitles (`[Intro - After the Transfer]`, `[Verse 1 - Wrong Body]` ...) | Plain `[Intro]`, `[Verse 1]`, `[Verse 2]`, `[Bridge]` | Frees characters for the V6 tags: the Lyrics field must stay under 5000 |
| `[Exclusions: ...]` inside the Style section | `## EXCLUSIONS:` section, plain comma-separated | Exclude field format |

Kept on purpose: the condensed `[Production Direction:]` / `[Vocal Direction:]` blocks and the full
ADVANCED BOX (with the Whisper Rule), the `()` whispered layer (declared in the Style Prompt), F minor
reaching toward Ab major, choir subtle until the final chorus, and the Production Notes block. Dropped
for length: the separate `[Stone drips]` / `[Cave drip]` cues (covered by Cave Ambience), `[Cave reverb]`
and `[Soft distorted piano]`'s "distorted" (the Style Prompt carries "broken piano"). `[Haunted choir]` in
chorus 2 has no tag of its own: the choir is already in from chorus 1, and chorus 2 gets `[Dynamic: f]`.

---

## STYLE PROMPT:
Epic dark cinematic cyber-fantasy ballad, haunted identity awakening, male baritone A2-E4, key F minor shifting toward Ab major, 4/4, 84 BPM, wet cavern ambience, broken piano, low electrical hum fading into cave resonance, distant thunder memories, soft glitch textures, rising fantasy strings, buried war horns, emotional final choir, lyrics in parentheses are close breathy whispered intrusive thoughts panned with delay

---

## EXCLUSIONS:

upbeat pop feel, trap drums, rap delivery, EDM festival drop, cheerful melody, playful vocals, comedic tone, bright synth lead, chipmunk vocals, excessive autotune, vocal chops, beatboxing, humming, scat vocals, random ad-libs, spoken narrator except where directed

---

## LYRICS:

[Title: Rikan]

[Production Direction: Right after Fracture Protocol. Wet, cold, terrified; body horror to haunted recognition. Choir subtle until a powerful, not victorious, final chorus: he has his name, not his peace. Cave and storm ambience as sound design.]

[Vocal Direction: Close-mic male baritone, breathless and confused, building through fear and identity fracture to a stronger, still-haunted end. Whispered thoughts may glitch.]

[Intro]
[Instrument: Cave Ambience In]
[Instrument: Drone In]
[Instrument: Piano In]

Where am I...

The dark answers first

Cold stone beneath me
Rain in the air
But there is no sky

My hands are wrong
(My hands are wrong...)

I try to breathe
But the breath comes sharp

I try to move
But something moves with me

A tail against the floor
Claws against the stone

And somewhere under my heartbeat
A name begins to wake

[Verse 1]
[Instrument: Low Pulse In]
[Dynamic: Soft]

I woke beneath a ceiling
That the world had carved from black
With dirt against my fingers
And no way to turn back

The air was wet and ancient
The shadows watched me crawl
I reached for human balance
But I was much too small

There was fur against the cold
There were claws where hands had been
There was fear behind my breathing
There was fire under skin

I tried to say my old name
But it broke between my teeth
Like a signal losing contact
Like a memory underneath

[Pre-Chorus]
[Instrument: Strings In]
[Dynamic: Crescendo]
[Instrument: Mark of Balance Glow In]

I was pulled across the veil
I was scattered in the fall
I built the world inside the vault
Now I'm lost inside its walls

And I don't know what still is mine
I don't know what I became
But something burning in my chest
Won't stop reaching for a name

[Chorus]
[Dynamic: Swell]
[Instrument: Choir In]

Rikan
Rikan

A name inside the dark

Rikan
Rikan

A fire beneath the mark

I was pulled across the veil
I built the world inside the vault
Now I'm scattered
Searching for the pieces of me

Rikan
Rikan

Why does it sound like me

[Verse 2]
[Instrument: Thunder In]

I remember rain on windows
I remember wires and light
I remember being Draeven
Before the world turned white

I remember something striking
I remember no goodbye
I remember reaching outward
As the room fell from my eyes

[Instrument: Thunder Out]

Now something ancient breathes beside me
And the dark responds to where I turn
Every stone I touch remembers fingers
Every shadow knows my name will burn

That the man I was is fading
But he has not disappeared
He is scattered through the silence
He is broken — but he's here

[Pre-Chorus 2]
[Instrument: Heartbeat In]
[Instrument: Distant Horn In]
[Dynamic: Crescendo]

Something burns beneath my chest
Like a star caught under skin
Something old and full of purpose
Says this is not the end

I don't know if I was chosen
I don't know if I was saved
But the mark is glowing brighter
Like a path beneath the cave

[Chorus]
[Instrument: Drums In]
[Dynamic: f]

Rikan
Rikan

A name inside the dark

Rikan
Rikan

A fire beneath the mark

I was pulled across the veil
I built the world inside the vault
Now I'm scattered
Searching for the pieces of me

Rikan
Rikan

Why does it sound like me

[Bridge]
[Instrument: Drums Out]
[Instrument: Distant Horn Out]
[Dynamic: p]
[Vocal: Half-Spoken]

Was I taken
Was I chosen
Was I broken by the storm

Was I buried
Was I copied
Was I forced into this form

(Draeven...)

I hear the name behind me

(Rikan...)

I hear the name ahead

One belongs to what I lost
One belongs to what is left

I am not erased
I am not whole

I am not only flesh
I am not only soul

If Draeven was the doorway
And the storm became the key

Then Rikan is the answer
Waiting somewhere inside me

[Breakdown]
[Dynamic: Silence]
[Instrument: Piano Out]
[Male lead, fractured whispers]
[Dynamic: Swell]

I was a body
I was a name
I was a voice inside a room

Now I am breathing
Inside the dark
Inside the stone
Inside the wound

(find the pieces)

I was pulled across the veil
I built the world inside the vault
Now I'm scattered
Searching for the pieces of me

[Final Chorus]
[Dynamic: Full]
[Instrument: War Horns In]
[Male lead, with choir]

Rikan
Rikan

Not a ghost
Not a dream

Rikan
Rikan

Not as lost
As I seem

I was pulled across the veil
I built the world inside the vault
Now I'm scattered
Searching for the pieces of me

Rikan
Rikan

The dark remembers me

Rikan
Rikan

The broken parts still breathe

[Transition: Sustain, Stop-Time]

I was Draeven in the thunder
I was human in the rain
Now the mark is burning through me
And nothing stays the same

Rikan
Rikan

I hear the name and turn

And somewhere in me
Something answers

[Outro]
[Instrument: War Horns Out]
[Instrument: Piano In]
[Dynamic: Soft]

Cold stone beneath me
Rain in the air
But there is no sky

The old world fades behind me
But I am still alive

I don't know where I'm going
I don't know what waits for me

But the name inside the darkness
Is the first real thing I feel

Rikan...

[End]

---

## ADVANCED BOX (overflow direction)

> The Lyrics field must stay under 5000 characters, so the direction blocks above are condensed.
> The full original direction is kept here. Paste it into Suno's More Options / Advanced box if your UI has one,
> or use it as the reference when re-rendering.

```
[Production Direction:
This begins immediately after Fracture Protocol. The transfer is complete. Draeven has crossed the veil and wakes in Eryndor. Start quiet, wet, cold, and terrified. Build from fear and body horror into haunted recognition. The final chorus should feel powerful but not fully victorious — he's found his name but not his peace.]

[Vocal Direction:
Close-mic male baritone, confused and breathless at first. Build through fear, memory loss, and identity fracture. Final vocal becomes stronger and more resolved, but still haunted.]

[Whisper Rule:
Lyrics in parentheses are whispered intrusive thoughts, close and breathy, panning left-to-right with delay.]

[Exceptions:
Whispered thoughts may be glitched and intimate. Choir stays subtle until the final chorus. Storm, cave, and Mark of Balance ambience may appear as sound design.]
```

---

## PRODUCTION NOTES:

• Key: F minor → shifting toward Ab major (relative major) — starts dark/terrified, resolves toward cautious hope. The key NEVER fully arrives at Ab — it reaches toward it. Mirrors his identity: not yet resolved, but moving.
• Tempo: 84 BPM (matches Fracture Protocol — continuity of pulse, as if the same heartbeat carried over)
• Time Signature: 4/4
• Chord Progression:
  Verse: i – VI – III – iv (Fm – Db – Ab – Bbm) [dark, searching, cave-like resonance]
  Pre-Chorus: iv – VII – VI – III (Bbm – Eb – Db – Ab) [rising, reaching, trying to resolve]
  Chorus: VI – III – i – VII (Db – Ab – Fm – Eb) [open, anthemic-minor, the name calling]
  Bridge: i – VII – VI – VII (Fm – Eb – Db – Eb) [questioning, unresolved, back-and-forth]
  Final Chorus: VI – VII – I – i (Db – Eb – Ab – Fm) [touches major (Ab) then pulls back to minor — hope but not resolution]
• Vocal: Male baritone (A2–E4), confused whisper → fearful → building recognition → powerful but haunted. Never triumphant — resolved but scarred.
• Instruments: Wet cavern ambience (throughout), broken piano, low electrical hum → cave resonance, soft glitch textures (fading from previous track), rising fantasy strings, distant thunder (memory of transfer), buried war horns (final chorus), choir (builds from whisper to full — final chorus only), heartbeat percussion
• Dynamics: Terrified whisper in cave (intro) → fragile confession (V1) → rising strings (PC) → open cinematic (C1) → broken memories (V2) → stronger build (PC2) → haunted choir (C2) → stripped questioning (bridge) → heavy silence into swelling force (breakdown) → full cinematic power (FC) → gentle warm resolution (outro)
• Hook Type: Name as hook — "Rikan" repeated on separate lines, chant-like, building meaning with each repetition. Secondary: "I was pulled across the veil / I built the world inside the vault / Now I'm scattered / Searching for the pieces of me" (recurring refrain across 3 songs)
• Rhyme Scheme: V=ABCB (folk-ballad feel — storytelling), PC=ABAB (more structured, building), C=Free (the name dominates), Bridge=AABB (couplets — questions paired), FC=AABB (resolution in paired statements)
• Emotional Arc: Terrified awakening → body horror → reaching for identity → memory fragments surfacing → the name calling → questioning origin → accepting duality → claiming the name — not victory, but the first step. He's not home. But he knows his name.

---

## RENDERS

| Date | Model | Clip ID | Settings | Measured | Verdict |
|---|---|---|---|---|---|
