# Speaker extraction: annotation protocol and audit

## The problem

The Chantilly manuscript marks who is speaking with a label at the start of a
paragraph — `Amour. Je suis dieu dit amour...`, `Raison. Et quoy donc...`.
A naive regular expression keyed on `Name.` at line start assumes the
manuscript is consistent about that period. It is not. The text variously:

- uses a colon instead of a period (`Amour: Ce livre a bien dit verité...`)
- uses no punctuation at all (`Amour Elle peut dit amour estre nommée...`)
- runs a chapter heading into the first turn of that chapter without a
  separator, so the turn is absorbed into the heading
- places a speaker label mid-line rather than at the start of a paragraph

Because of this, the first extraction pass captured 331 turns. The audited
count is 379.

## Protocol

**Step 1 — closed-list matching.** Replace the generic pattern with a regular
expression built from an explicit inventory of known speaker labels and their
orthographic variants (`GRUPOS` in the notebook). Variants are normalised to a
single figure name: `Amour`, `Amor` and `Ici parle amor` all resolve to *Amor*.
This eliminates the false positives that the generic pattern produced.

**Step 2 — candidate retrieval.** For every figure name in the inventory,
retrieve every occurrence *not* followed by an immediate period. This produced
62 candidates: 13 for Amor, 13 for Raison, 30 for L'Ame, 4 for Saincte Eglise,
2 for Verité, and none for Le Saint Esperit, Dieu, Crainte or Foy.

**Step 3 — manual classification.** Each candidate was read in context and
assigned to one of six categories:

| Category | Definition | Counted? |
|---|---|---|
| Genuine turn | A real dialogue turn with irregular punctuation | Yes |
| Already counted | The variant carries its own period later in the phrase (e.g. `L'ame franche.`) | No — would double-count |
| Heading/turn fusion | Chapter heading run into the first turn; the turn is separated manually | Yes |
| Other speaker's turn | The fusion conceals a turn belonging to a different figure | Yes, attributed correctly |
| Not a turn | A line of the opening poem or of the song in ch. 122 | No |
| Poetic voice | The figure is the grammatical subject of a verb inside sung verse, without opening a dialogue turn | No |

**Step 4 — incorporation.** 48 genuine turns were added to the closed-list
count. They are listed verbatim in the notebook (`CASOS_AUDITADOS`) and matched
back to the corpus by exact string, so each one is traceable.


## Numbered decision rules

Every row in `corpus/dialogue_turns.csv` records the rule applied and the
resulting certainty, so each of the 383 rows can be challenged individually.

| Rule | Condition | Status assigned | Certainty | Rows |
|---|---|---|---|---|
| A01 | Standalone explicit speaker label, regular punctuation | `explicit` | high | 331 |
| A02 | Explicit label with irregular punctuation (colon, no mark) or fused with a chapter heading | `irregular_explicit` | high | 48 |
| A07 | Label embedded mid-line rather than opening a paragraph | `midline_excluded` | high | 4 (excluded) |

Two rules were defined but **not used**, and are recorded here so their absence
is explicit rather than implied:

| Rule | Condition | Status | Used |
|---|---|---|---|
| A05 | Speaker inferred from syntax or context, no label present | `editorial_restoration` | No — 0 rows |
| A06 | Attribution not demonstrable | `unassigned` | No — 0 rows |

This matters: **no turn in this corpus is an editorial restoration.** Every one
of the 379 rests on a label present in the transcription, regular or irregular.
Had restorations been included, they would have been reported as a separate
category and excluded from the headline figure.

## Three reproducible subsets

`included_main_analysis` and `speaker_label_status` let any reader rebuild
three different totals from the same file:

| Subset | Filter | Turns |
|---|---|---|
| `strict` | `speaker_label_status == "explicit"` | 331 |
| `audited_main` | `included_main_analysis == TRUE` | **379** (reported result) |
| `sensitivity_extended` | all rows | 383 |

The extended subset yields 247 transitions instead of 243; the centrality
ranking is unchanged and the turn counts for Dieu and Le Saint Esperit are
unchanged.

## Results

| Figure | Before audit | After audit |
|---|---|---|
| Amor | 145 | 154 |
| L'Ame | 92 | 117 |
| Raison | 69 | 79 |
| Verité | 12 | 13 |
| Saincte Eglise | 6 | 9 |
| Le Saint Esperit | 3 | 3 |
| Crainte | 2 | 2 |
| Dieu | 1 | 1 |
| Foy | 1 | 1 |
| **Total** | **331** | **379** |

The audit changed volumes, not structure: the ranking of figures by degree
centrality is identical before and after. Amor remains at 1.375 exactly, Dieu
and Foy at 0.125 exactly.

Note that the error is not randomly distributed. It affects the figures that
speak most and leaves the rarely-speaking figures untouched — which is what
makes it dangerous to ignore.

## Two cases worth recording

**Capitalisation disambiguates figure from noun.** Three Raison candidates read
`Raison dit amor...` and were initially set aside as ambiguous: was the speaker
Raison or Amor? They are resolved by case. Lowercase *amor* / *amour* is the
common noun "love", the topic Raison is speaking about; the figure is
capitalised wherever it is the speaker. All three are Raison turns. Any regex
using case-insensitive matching erases this distinction.

**Poetic voice is a third state.** In the song of chapter 122, Verité is the
grammatical subject of a verb (*Verité denonce a mon cueur...*) without opening
a dialogue turn. This is neither a passive mention nor an interlocution. It is
recorded as a distinct category and excluded from the turn count.

## Known limits

- The audit addresses one identifiable class of error. It is not equivalent to
  a full philological reading of all 139 chapters, and further uncaptured turns
  cannot be ruled out.
- 4 speaker labels occurring mid-line (2 L'Ame, 1 Amour, 1 Raison) are not
  included in the 379. Including them yields 383 turns and 247 transitions; the
  centrality ranking is unchanged and the turn counts for Dieu and Le Saint
  Esperit are unchanged. Reported as a sensitivity check in notebook §14.5.
- Turn boundaries are set at the first paragraph break. Extending them to the
  next detected turn absorbs chapter headings and unlabelled text — in one
  trial this attributed a question by Raison to Dieu.

## Uncertainty marks

Separately from speaker attribution, the Wikisource transcription contains 833
`(?)` marks, each flagging a letter the transcriber could not confirm. 673
(81%) were resolved with a context dictionary documented in the notebook,
based on attested Middle French forms. The remaining 160 had the mark stripped
without reconstructing the letter, and are listed in
`unresolved_uncertainty_marks.txt`. No speculative reconstruction was made.
