# Rhyme & Lyric Craft Reference (the "lyric dictionary")

> **Canonical reference** for rhyme types, consonant families, rhyme position, rhyme schemes, section
> stability, power positions, meter and flow, singability, rhetorical devices, cliché flipping, and
> rhyme/word tools. Methodology that USES this file: `core/methodology/songwriting.md` (Step 4 / Step 17)
> and `core/methodology/critique.md` (Prosody, Lyrics, Originality, flag patterns).
>
> **Deterministic readout:** `python3 tools/lyric-lint.py songs/my_song.md` reports syllables, stress,
> the rhyme type of each end-rhyme pair (using the ladder below), each section's rhyme scheme and its
> stability. Install `pip install pronouncing` (CMU Pronouncing Dictionary) for dictionary accuracy.
>
> **Evidence tiers:** [Tier 1] scholarship / phonetics fact · [Tier 2] professional craft heuristic ·
> [Tier 3] community observation. Craft rules here are tools, not laws (Tenet 1: Emotion Over Mechanics).
> Paraphrased from the sources at the end; examples are original unless credited.

---

## 1. The Rhyme Ladder (Pattison) [Tier 2]

Rhyme is a **vowel** connection first: when you sing, you stretch the vowel, so a matching stressed
vowel carries most of the effect. Pat Pattison ranks rhyme types by how much **closure** (sense of
arrival) they give, strongest first:

| Rung | Type | What matches | Examples | Feels like | Typical job |
|---|---|---|---|---|---|
| 1 | **Perfect** | Same stressed vowel + same sounds after it + **different** sound before it | time/rhyme · stone/bone · ocean/motion | Full stop, "click" | Title lines, chorus resolution, punchlines |
| 2 | **Family** | Same vowel; final consonants from the same **phonetic family** (§2) | cup/tuck · grave/praise · home/bone | Near-perfect closure, fresher | Anywhere you'd want perfect but the options are clichés |
| 3 | **Additive / Subtractive** | Same vowel; one word adds (or drops) consonant(s) after it | free/sweet (adds t) · cold/so (drops ld) · glass/last | Strong echo with a little lean | Verses, pre-choruses |
| 4 | **Assonance** | Same vowel; unrelated final consonants | fate/game · night/mine · lost/wrong | Open, floating | Verses, motion, conversational writing |
| 5 | **Consonance** | Different vowels; same final consonants | rust/lost · hand/mind · black/rock | Faint echo, unresolved | Texture, deliberately unsettled sections |

**Not rhymes (for singing):**
- **Identity:** the same word or the same onset + vowel + coda (night/knight, believe/leave). The ear
  hears repetition, not rhyme. Repetition is a tool too (refrain), just don't count it as a rhyme.
- **Eye rhyme:** spelled alike, sounds different (love/move, cough/bough). Invisible to a listener; to
  the ear, love/move is only consonance.

**Choosing a rung** [Tier 2]:
- Use the **strongest rung that doesn't bend meaning or syntax**. A forced inversion ("the love that
  fills what speaks") costs more than a looser rhyme.
- **Closure is a choice.** Perfect/family rhymes resolve; assonance/consonance keep things moving. Put
  your strongest rhymes where the song should land: the title line, the chorus's last line, the final chorus.
- **School difference:** the standards/Broadway tradition (argued strongly by Jimmy Webb in
  *Tunesmith*) prizes perfect rhyme. Pattison argues family and other near rhymes widen your choices
  and avoid cliché. Pick deliberately, and stay consistent within a song unless the change is the point.
- **Perfect-rhyme clichés:** the most available perfect rhymes are the most used (fire/desire,
  heart/apart, love/above, pain/rain). If your perfect rhyme is the first one anyone would think of,
  climb down one rung to a family rhyme.

---

## 2. Consonant Families (for Family Rhyme) [Tier 1: phonetics; usage Tier 2]

Family rhyme swaps the final consonant for one made the **same way** in the mouth. Three families matter:

| Family | How it's made | Voiced | Unvoiced |
|---|---|---|---|
| **Plosives (stops)** | Air stopped, then released | b · d · g | p · t · k |
| **Fricatives** (incl. affricates) | Air forced through a narrow gap (hiss/buzz) | v · th (*this*) · z · zh (*measure*) · j (*judge*) | f · th (*thin*) · s · sh · ch (*church*) |
| **Nasals** | Air through the nose | m · n · ng | (none) |

- **Partners** = the same sound voiced/unvoiced (t↔d, p↔b, k↔g, f↔v, s↔z, sh↔zh, ch↔j). Closest relatives.
- **Companions** = same family, same voicing (t↔k↔p; d↔b↔g; f↔s↔sh). Next closest.
- l, r, w, y and h belong to no family. Treat them as their own sound.
- `lyric-lint.py` classifies any same-family swap as **family** rhyme.

**How to find a family rhyme** (Pattison's method, paraphrased):
1. Find the stressed vowel of your word and the consonant after it. Example: *safe* → long-A + **f** (fricative).
2. List perfect rhymes first (chafe, waif...).
3. Swap **f** for its partner **v** (brave, grave, wave), then its companions **s / sh / th / ch**
   (place, grace, faith), then the voiced fricatives (blaze, praise, cage, rage).
4. Sing the options. The vowel carries the rhyme, so most family rhymes disappear into the melody.
   Watch **g**, **r** and **l**: they can colour the vowel before them.

Multi-syllable words work the same way: match the stressed vowel and every vowel after it, then let
the consonants differ within families (*ladder / matter*: d and t are plosive partners).

---

## 3. Rhyme Position & Compound Rhymes [Tier 2]

| Type | What it is | Example |
|---|---|---|
| **End rhyme** | Rhymes at line ends: what a rhyme scheme describes | — |
| **Internal** | A rhyme inside a single line | "the *rain* on the *pane* again" |
| **Cross / interlaced** | Mid-line of one line rhymes with the end or middle of another | "I left the *light* on in the hall / you said goodnight like it was *right*" |
| **Chain / linked** | The end of one line rhymes with the start of the next | "...across the *floor* / *More* than I can say..." |
| **Multisyllabic / feminine** | Stressed syllable + following unstressed syllable(s) rhyme | broken/spoken · tenderly/remember me |
| **Masculine** | The rhyme falls on a final stressed syllable | today/away |
| **Mosaic / compound** | Several words rhyme with one multi-syllable word, or phrase with phrase | poet/know it · hesitate/best to wait |
| **Rhyme stacking** | Same rhyme sound repeated over 3+ consecutive lines or bars | common in hip-hop verses and AAAX pre-choruses |
| **Holorime** | Two whole lines that sound (nearly) identical | rare; novelty/wordplay |

**Rhyme density** (mostly hip-hop) [Tier 1: Hirjee & Brown, 2010]: the share of syllables that take part in
a rhyme. Multis, internals and stacking raise it. Higher density reads as technical skill; pop hooks usually
keep density low so the title stands out.

---

## 4. Rhyme Schemes (notation + structural effect) [Tier 2]

**Notation:** each new rhyme sound gets the next letter; lines with the same letter rhyme; **X** marks an
unrhymed line. `lyric-lint.py` prints this per section (e.g. `XAXA`).

| Scheme | Structure | Effect | Good for |
|---|---|---|---|
| **AABB** | Couplets | Closure every two lines; propulsive. Sing-song if line lengths and content are too even | Pop/hip-hop choruses, punchy verses |
| **ABAB** | Alternating | Balanced; closure delayed by one line | Verses, ballads |
| **XAXA / ABCB** | Only even lines rhyme | Conversational ballad-stanza pattern. Least closure; lines 1 and 3 can say anything | Story verses. A common option, **not** a default |
| **ABBA** | Enclosed | Closure held until line 4; the middle couplet feels inward | Reflective verses, bridges |
| **AAAX / AAAB** | Three rhymes, then a break | Builds expectation, then the odd line is spotlit | Title on the X line; pre-choruses that tip into the chorus |
| **AABCCB** | Tail rhyme | Two couplets bound by rhyming tail lines; six-line arc | Longer verses, story songs |
| **AAAA** | Monorhyme | Hypnotic, chant-like, can feel relentless | Hooks, refrains, rap stacks |
| **Free / unrhymed** | — | Maximum openness. Rhythm and repetition carry the shape | Bridges, spoken sections, deliberate rawness |

**Matched vs unmatched sections:** repeating a verse's scheme and line lengths in Verse 2 tells the ear
"same melody". Suno also tends to reuse the verse melody, so keep V1/V2 syllable counts close
(`lyric-lint.py` flags line-by-line differences > 2 syllables).

**Phrase shape invites rhyme** (Pattison): equal-length phrases that sit next to each other invite a
couplet; an alternating long/short pattern invites ABAB. Let the melody's phrase lengths suggest the scheme.

---

## 5. Section Stability (Pattison) [Tier 2]

Every section has a job. Some should **resolve** (rest, arrival, certainty) and some should **lean
forward** (tension, motion, longing). Four structural levers control it:

| Lever | Stable / closed | Unstable / open |
|---|---|---|
| **Line count** | Even (2, 4, 6, 8) | Odd (3, 5, 7) |
| **Line length** | Matched lengths / stress counts | Unmatched: one short line, one long |
| **Rhyme** | Closed scheme; last line rhymes back | Open scheme; last line unrhymed (X) |
| **Stresses per line** | Same number of stressed syllables | Varying stress counts |

- Use **unstable** pre-choruses and bridges to push into a **stable** chorus. That's motion, then arrival.
- A chorus that ends **open** can be a deliberate effect (a song about something unresolved), but do it on purpose.
- **Common meter** (alternating 4- and 3-stress lines, usually rhymed XAXA) is the hymn and ballad
  backbone. Each short line creates a little lean that the next long line answers.
- **Prosody = structure matching emotion.** A three-line verse about longing *feels* like longing before
  the words do. Same for a lopsided line about losing balance.
- `lyric-lint.py` reports each section as **stable / mixed / unstable**, from line-count parity,
  syllable-length match (±2) and rhyme closure. The critique flag "Stability mismatch" uses the same idea.

---

## 6. Power Positions, Title Placement & Emphasis [Tier 2]

- **Power positions** are the **first and last lines of any section**. Put the title, the turn and the
  strongest images there. The last line of the chorus is the most remembered spot in most songs.
- **Title placement options:** first line of the chorus; last line; both (bookend); every line (refrain
  chorus); the X line of an AAAX section; the last line of every verse (AAA/strophic "refrain" form).
- **Front-load / back-load:** put the key word where the stress and the held note fall, usually the end
  of the line. "I'm not alright, I wear it well" and "I wear it well, I'm not alright" emphasise different things.
- **Verse development ("boxes"):** each verse is a new box (a new time, place, angle or stakes) that
  makes the unchanged chorus mean something new. V2 must add information; the bridge turns the camera.
- **Verse = detail, chorus = summary:** sense-bound specifics in verses; a broader, quotable claim in
  the chorus. Tenet 2 allows direct statement in hooks and bridge turns.

---

## 7. Meter: Poetic Feet and Musical Meter

### 7.1 Feet [Tier 1: standard prosody]

| Foot | Pattern | Example | Feel |
|---|---|---|---|
| Iamb | da-DUM | to-NIGHT, be-LIEVE | Rising, conversational: closest to English speech |
| Trochee | DUM-da | BRO-ken, HOLD-ing | Falling, insistent, chant-like: strong for hooks and anthems |
| Anapest | da-da-DUM | in the NIGHT, un-der-STAND | Rising triple, galloping, driving |
| Dactyl | DUM-da-da | MEM-o-ry, TEN-der-ly | Falling triple, rolling, waltz-like |
| Amphibrach | da-DUM-da | to-MOR-row, re-MEM-ber | Lilting triple |
| Spondee | DUM-DUM | DEAD STOP, HOLD FAST | Weight and emphasis. A *substitution*, not a sustained meter |
| Pyrrhic | da-da | (of the) | Speeds a line up. Substitution only |

Lines are counted in feet (trimeter = 3, tetrameter = 4, pentameter = 5). A **catalectic** line drops the
last unstressed syllable ("SHE'S my BITCH, my KITCH-en WITCH" = trochaic tetrameter, catalectic).

### 7.2 Musical meter and placement [Tier 2]

- **Stresses go on strong beats of the METER.** In square 4/4 that's usually beats 1 and 3. Backbeat
  and syncopated styles (R&B, funk, much pop and hip-hop) push stresses onto **anticipations** (an
  8th or 16th before the beat) or onto 2 and 4. In **3/4** and **6/8**, it's the downbeat of each group.
- **Pickups (anacrusis):** unstressed syllables before the bar line ("and I / KNOW..."). Iambic lines
  naturally start with a pickup.
- **Feminine endings** (an extra unstressed syllable after the last stress: "BRO-ken") land just after
  a beat. Good for a soft, falling cadence, but they need room in the bar.
- **Reversed stress** is a weak syllable or function word on a strong beat while the content word sits
  on a weak beat (singing to-MOR-row as TO-mor-ROW). Fix it by reordering words or shifting the phrase.
- **Syllable budget per bar** (arithmetic, 4/4): quarter-note setting = 4 syllables, 8ths = 8, 16ths = 16.
  At 90 BPM a beat is 0.67 s, so straight 16ths ≈ 6 syllables per second. That's rap territory; sung
  lines usually mix quarters and 8ths. A 7–12 syllable line therefore fits comfortably in 1–2 bars at mid tempo.
- **Flow (hip-hop):** straight 16ths, triplet flow (3 per beat), and deliberate rests are the main
  textures. Rhyme placement against the beat (on 4, across the bar line) defines style as much as the words.

---

## 8. Singability & Phonetics [Tier 2: vocal pedagogy]

| Element | Sings well | Watch out |
|---|---|---|
| **Held / high notes** | Open vowels: *ah* (father), *oh*, *aw*, *eh* | Closed *ee* and *oo* get pinched up high. Singers modify ee→ih and oo→uh/oh, and Suno often does too |
| **Diphthongs** | Sustain the FIRST vowel, close at the very end: "I" = *ah*…ee, "day" = *eh*…ee, "go" = *oh*…oo | Writing a held note on the second half sounds strained |
| **Final consonants on long notes** | Voiced continuants you can hum through: m, n, ng, l, v, z | Stops (p, t, k, b, d, g) cut the sound off. Use them for punch, not sustain |
| **Sibilance** | — | s, sh, ch, z on held or loud notes hiss. Avoid stacking them; post-render, use `plugins/de-esser/` |
| **Consonant clusters** | Simple consonant-vowel syllables at speed | "strengths", "texts", "twelfths" slow delivery and blur in fast lines |
| **Line endings** | Stressed content words, open vowels | Unstressed function words (the, of, a) on a held note. Fine when the word is sung stressed |

**Sound symbolism / phonaesthetics** [Tier 2/3, research is suggestive, not deterministic]: front/high
vowels (*ee*, *ih*) tend to read small, bright and quick; back/low vowels (*oo*, *ah*, *aw*) big, dark
and slow. Plosives read abrupt or hard, nasals and liquids soft. Use it as texture, e.g. soft nasals in a
lullaby, hard stops in an anger verse. Don't treat it as a rule.

---

## 9. Rhetorical & Sound Devices [Tier 1: standard rhetoric; examples original]

| Device | What it does | Example |
|---|---|---|
| **Anaphora** | Same opening words on successive lines (builds momentum) | "Every door I open slow / Every room I check twice" |
| **Epistrophe** | Same closing words on successive lines | "...when you're gone / ...since you've gone" |
| **Anadiplosis** | Last word of a line starts the next | "I kept the light / the light kept me" |
| **Chiasmus** | A-B-B-A reversal of words or ideas | "I wore the mask until the mask wore me" |
| **Antithesis** | Opposites side by side | "loud in the room, silent in the car" |
| **Refrain variation** | A repeated line changes one word as the story moves | "I hold too tight" → "I hold on gentle now" |
| **Metonymy** | Name a thing by something associated with it | "the bottle won" (drinking) |
| **Synecdoche** | A part for the whole | "another pair of hands on the line" |
| **Apostrophe** | Address something absent or inanimate | "Hey, three a.m., you again" |
| **Hyperbole / Understatement** | Exaggerate / play down for effect | "a thousand miles of hallway" / "it's been a bit of a year" |
| **Oxymoron / Paradox** | Contradiction that reveals truth | "a crowded kind of lonely" |
| **Extended metaphor (conceit)** | One metaphor sustained across the song | the lighthouse as a lullaby |
| **Alliteration** | Repeated initial consonants | "salt on the sill" |
| **Assonance / consonance (texture)** | Repeated vowels / consonants inside lines, not just at rhymes | "cold stone road home" |
| **Onomatopoeia** | Words that sound like their meaning | hiss, thud, crackle |

**Metaphor "collisions"** (Pattison's idea, paraphrased): fresh metaphor often comes from pairing a noun
with an unexpected verb or adjective ("the silence *billed* me", "a *rented* smile"). Do it by listing
the nouns and verbs of two worlds and crossing them.

---

## 10. Clichés and How to Flip Them [Tier 2]

A cliché is a phrase so familiar that the listener's brain finishes it for you, so it carries no
information. One familiar word is rarely the problem. The warning sign is a **cluster** of broad emotion
words, predictable rhymes and interchangeable images with no detail that proves this speaker lived it.

**Flip techniques:**
1. **Twist one word:** "cold as a razor blade" instead of "cold as ice".
2. **Literalise it:** take the idiom at face value ("I wear my heart on my sleeve, and the stain won't come out").
3. **Reverse it:** "I didn't fall apart, I fell together wrong."
4. **Specify it:** replace the stock image with a sense-bound one ("broken heart" → "your mug still in the drying rack").
5. **Give it to a character:** a cliché in the mouth of someone who'd really say it is characterisation.
6. **Rhyme around it:** if the end rhyme is the cliché (fire/desire), pick a less-used perfect rhyme
   (fire → wire, liar) or climb down the ladder to an additive rhyme (fire → tired, inspired, iron).

`tools/data/cliches.txt` holds the phrase list and worn-out rhyme pairs that `lyric-lint.py` flags. Extend it.

---

## 11. Rhyming Dictionaries, Thesauruses & Word Tools

### Online
| Tool | Strength | Notes |
|---|---|---|
| [RhymeZone](https://rhymezone.com/) | Free; perfect and near rhymes, phrases, synonyms, same-consonant-pattern words, sorted by syllables | Type `word?` for related words |
| [B-Rhymes](http://www.b-rhymes.com/) | Built for slant/near rhymes | Good for family and assonance options |
| [MasterWriter](https://masterwriter.com/) | Paid songwriting suite: rhymes, phrases, word families, syllable tracking | Subscription |
| [Datamuse API](https://www.datamuse.com/api/) | Free word-finding API (CMUdict-based sound relations, means-like, triggers, syllable/pronunciation metadata) | Its site says an API key will be required from early 2027 |
| [RhymeBrain API](https://rhymebrain.com/api.html) | Rhyme lookup API | Requires a link back when used publicly |

### Print / classic
- **Pat Pattison — *Songwriting: Essential Guide to Rhyming*** (Berklee Press): the rhyme ladder, family
  rhyme worksheets, rhyme and structure. Companion to *Writing Better Lyrics* (2nd ed., 2009).
- **Clement Wood — *The Complete Rhyming Dictionary*** (rev. ed.), a standard print rhyming dictionary.
- **Walker's Rhyming Dictionary** (John Walker, 1775) and **Andrew Loring's *The Rhymer's Lexicon*** (1905),
  both public domain and on the Internet Archive. Archaic vocabulary; useful for period/fantasy diction.
- **Sheila Davis — *The Craft of Lyric Writing*** (1985): song forms, title sources, and a large glossary of
  literary and musical terms.
- **Jimmy Webb — *Tunesmith*** (1998): the perfect-rhyme school's case, and melody-lyric craft.

### Data & libraries (for tooling)
- **[CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict):** 134k+ North American
  English pronunciations with stress marks, BSD-licensed. The basis of most rhyme tools.
- **[`pronouncing`](https://pronouncing.readthedocs.io/) (Python):** syllable counts, stress patterns and
  rhymes from CMUdict. Optional dependency of `tools/lyric-lint.py`.
- **[`prosodic`](https://pypi.org/project/prosodic/) (Python):** metrical parsing and named rhyme-scheme detection
  for poetry. Useful for deeper meter analysis.
- **Research:** Hirjee & Brown (2010), [Rhyme Analyzer](https://ismir2010.ircam.fr/proceedings/late-breaking-demo-23.pdf):
  probabilistic detection of imperfect and internal rhymes in rap lyrics, plus rhyme-density features.

### Pattison's worksheet workflow (paraphrased)
1. Write the song's key idea in one or two sentences.
2. **Object-write** around it: 10 timed minutes, all 7 senses (sight, sound, smell, taste, touch,
   organic/body, kinesthetic/motion).
3. Pull out key words. Add **thesaurus** neighbours, then **rhymes**: perfect, family, additive,
   assonance. Use the family chart in §2.
4. Draft from the worksheet. Choose rhymes for meaning first, sound second.

---

## 12. Where This Plugs In

| Workflow step | Uses |
|---|---|
| `core/methodology/songwriting.md` Step 4: Prosodic Planning | §4 schemes, §5 stability plan per section |
| Step 17: Prosody Audit | §1 ladder, §7 meter, §8 singability; run `tools/lyric-lint.py` |
| `core/methodology/critique.md` Prosody / Lyrics / Originality | §1, §5, §8, §10; flags "Rhyme forcing", "Stability mismatch", "Reversed stress" |
| `core/methodology/song-planning.md` Structure Map | "Rhyme & stability plan per section" |
| Production Notes → Rhyme Scheme | Scheme letters per section + stability intent (e.g. "Chorus AABB, closed") |

---

## Sources

- Pat Pattison, *Writing Better Lyrics* (2nd ed., 2009) and *Songwriting: Essential Guide to Rhyming* (Berklee Press).
- Pat Pattison, ["Songwriter U: Surviving Rhyme; Meeting the Family"](https://americansongwriter.com/songwriter-u-surviving-rhyme-meeting-the-family/), *American Songwriter*. Family rhyme and the consonant-family method.
- ["A Q&A on Rhyme with Pat Pattison"](https://americansongwriter.com/q-and-a-on-rhyme-with-pat-pattison/), *American Songwriter*. Phrase shapes inviting rhyme schemes.
- ["Lyrically Speaking: Putting 'Nothing' Together"](https://americansongwriter.com/lyrically-speaking-putting-nothing-together%EF%BF%BC/), *American Songwriter*. Equal vs unequal line lengths and common meter.
- Andrea Stolpe, ["How To Rhyme Like a Boss"](https://www.andreastolpe.com/articles/rhyme-types). The five rhyme types ordered by strength of closure.
- Berklee Online, ["Simple Tools for Writing from the Title"](https://online.berklee.edu/takenote/simple-tools-for-writing-from-the-title/) (power positions) and ["Prosody in Music and Songwriting"](https://online.berklee.edu/takenote/prosody-in-music-and-songwriting/) (stable vs unstable ideas).
- JMC Academy, ["Top Lyric Writing Tips With Pat Pattison"](https://www.jmcacademy.edu.au/news-and-events/news/top-lyric-writing-tips-with-pat-pattison/). Stressed-syllable counts and stability.
- Jack Righteous, ["Avoiding AI clichés in lyrics"](https://jackrighteous.com/de/blogs/music-creation-process-guide/avoiding-ai-cliches-in-lyrics-keep-your-songwriting-fresh-and-original). Clichés as clusters, not single words.
- Sheila Davis, *The Craft of Lyric Writing* (Writer's Digest, 1985). Jimmy Webb, *Tunesmith* (Hyperion, 1998).
- Hussein Hirjee & Daniel G. Brown, "Rhyme Analyzer: An Analysis Tool for Rap Lyrics" (ISMIR 2010 late-breaking demo) and "Using Automated Rhyme Detection to Characterize Rhyming Style in Rap Music" (*Empirical Musicology Review*, 2010).
- Carnegie Mellon University, The CMU Pronouncing Dictionary. Allison Parrish, `pronouncing` (Python). Datamuse API documentation.

*Content from web sources was paraphrased for licensing compliance; no passage is reproduced at length.*
