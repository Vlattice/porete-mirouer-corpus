# Le Mirouer des simples âmes — annotated corpus and dialogue network

A machine-readable corpus of Marguerite Porete's *Le Mirouer des simples âmes
anienties* (c. 1290–1300, Middle French), with a documented speaker-extraction
protocol and a reproducible analysis of the distribution of dialogue turns
among its allegorical figures.

The corpus and the extraction protocol are the reusable part of this
repository. The interpretive argument built on them is not included here.

## Why this exists

The *Mirouer* survives in Middle French only in the Chantilly manuscript
(Musée Condé). A transcription is available on Wikisource, but it is not
usable as a corpus without substantial preparation: the opening poem is on a
separate page, 833 transcription-uncertainty marks `(?)` are embedded in the
running text, and — most importantly — the manuscript marks speaker attribution
inconsistently.

Anyone counting who speaks in this text without auditing that inconsistency
will undercount, and will not notice. This repository does that work once so
it does not have to be repeated.

> Before interpreting the gender of the voices in the *Mirouer*, one has to
> establish whether that gender comes from grammar, from linguistic tradition,
> or from a textual decision. And before counting who speaks, one has to audit
> how speakers are identified.

That is the order this repository follows, and the reason the audit protocol is
published alongside the counts rather than behind them. See
[`docs/bibliography.md`](docs/bibliography.md) for the state of the art in
speaker attribution and character networks that frames the method.

## Headline figures

A **dialogue turn** here is a stretch of direct discourse opened by an explicit
speaker label in the manuscript. A new turn begins where a new label appears.
The figure of 379 is therefore the result of an annotation convention, stated in
`docs/speaker-audit.md`, not a self-evident property of the manuscript.

Over 139 chapters, 54,151 tokens and 4,587 unique lexical forms (833
uncertainty marks, 673 resolved by context dictionary, 160 left unresolved):

| | |
|---|---|
| Dialogue turns with an explicit speaker label | **379** |
| — of which by grammatically feminine figures | 375 (98.9%) |
| — of which by grammatically masculine figures (Dieu, Le Saint Esperit) | 4 (1.1%) |
| Turn transitions (directed graph edges) | 243 |

The 4 masculine turns are Le Saint Esperit (3) and Dieu (1); Dieu is counted
**within** that 4, not in addition to it. The Son opens no turn at all and so
does not appear in the figure inventory. 375 + 4 = 379.

Four further speaker labels occur mid-line; they are recorded in the turn table
flagged `midline_excluded` and left out of the 379. Including them gives 383
turns and 247 transitions without changing the centrality ranking.

Per-figure totals: [`data/tabla_consolidada.csv`](data/tabla_consolidada.csv).
Turn-by-turn data, one row per turn with its attribution rule and certainty:
[`corpus/dialogue_turns.csv`](corpus/dialogue_turns.csv). That file is the one
to challenge: every count in this repository is an aggregation of its rows.

These numbers depend on the annotation protocol described in
[`docs/speaker-audit.md`](docs/speaker-audit.md). They are not a neutral
property of the text. A different protocol yields different counts, which is
precisely why the protocol is published alongside them.

## What this repository contributes

**1. A prepared corpus.** The Wikisource transcription is not usable as-is:
the opening poem sits on a separate page and 833 transcription-uncertainty
marks are embedded in the running text. Both are handled here, with the
resolution dictionary documented and the 160 unresolved marks listed rather
than silently reconstructed.

**2. A speaker-extraction protocol, and the fact that it changes the counts.**
Published discussions of this text do not state an explicit, reproducible
criterion for what counts as a speaker label. The audit here recovers 48 turns
that naive extraction misses (331 → 379). The error is not randomly
distributed: it affects the figures that speak most and leaves the
rarely-speaking figures untouched, so ignoring it inflates exactly the
contrasts one might want to measure. See [`docs/speaker-audit.md`](docs/speaker-audit.md).

**3. A grammatical-gender map checked against the Latin etyma**
([`data/grammatical_gender_map.csv`](data/grammatical_gender_map.csv)).
This exists to constrain over-reading, not to support it. Note that it is a
*lexical* inventory, wider than the cast: it includes terms such as *charité*,
*vertu*, *deité*, *trinité*, *seigneur* and *néant*, which are named or invoked
in the text but open no counted turn. Only nine figures open turns, and of those
nine, seven are grammatically feminine and two masculine (Dieu, Le Saint
Esperit) — in every case by inheritance, not by authorial choice. *Amour* is the
one term requiring a diachronic note: Latin *amor, amoris* is masculine, but Old
French regularly feminised this class of nouns (cf. *douleur*, *peur*), and the
singular was masculinised only in the 16th–17th c. by grammarians aligning usage
with the Latin etymon. Feminine *Dame Amour* in the *Mirouer* is therefore the
period norm, not a deliberate gendering. The map also corrects a tempting error:
*néant* is masculine (*le néant*), so the configuration is not "a feminine
Nothing" but a grammatically feminine soul dissolving into a grammatically
masculine void.

Sources for these claims: Littré, *Dictionnaire de la langue française*, s.v.
*amour*; Grevisse & Goosse, *Le bon usage*; Loporcaro, *Gender from Latin to
Romance* (OUP, 2017).

**4. Concordance counts for metalinguistic vocabulary**
([`data/metalinguistic_terms.csv`](data/metalinguistic_terms.csv)), with the
counting rules stated: singular and plural counted separately, nested formulas
reported as subsets rather than summed, manuscript abbreviations included.
That last point matters: the manuscript writes *prsonne* and *psonne* 13 times,
so a pattern matching only *personne* undercounts the family by roughly a third.

**5. A turn-level table rather than a headline number.**
[`corpus/dialogue_turns.csv`](corpus/dialogue_turns.csv) gives 383 rows — the
379 counted plus the 4 excluded mid-line labels — each with the rule that
produced it and its certainty. Three subsets are reproducible from the same
file: `strict` (331 regular labels only), `audited_main` (379, the reported
result) and `sensitivity_extended` (383). No turn in the corpus is an editorial
restoration: all rest on a label present in the transcription.

## Contents

```
source/
  raw/                       Untouched Wikisource download; never overwritten
  checksums/SHA256SUMS.txt   Checksums for source and derived files
metadata/
  corpus_metadata.yaml       Machine-readable record of every global decision
corpus/
  dialogue_turns.csv         One row per turn: chapter, speaker, surface label,
                             status, certainty, rule applied, offset, token
                             count, inclusion flag, text
  mirouer_corpus_clean.txt   Full text: opening poem + 139 chapters,
                             uncertainty marks resolved
  opening_poem.txt           4 stanzas, 28 lines, absent from the standard
                             Wikisource export
  chapter_titles.txt         139 chapter titles, in sequence, transcribed from
                             the TABLE OF CHAPTERS that opens the manuscript —
                             not from the in-text rubrics. The two differ
                             orthographically (table: "Le cplogue", "amor",
                             "pais"; rubric: "Le prologue", "amour", "paix"),
                             so they will not match on a string comparison.
                             Chapters are identified in the analysis by the
                             numeric markers in the corpus, never by title.
notebook/
  mirouer_analisis.ipynb     Full pipeline, executed, with outputs
data/
  tabla_consolidada.csv      Per-figure: lexical frequency, turns, questions,
                             answers, in/out degree, degree centrality,
                             grammatical gender
  grammatical_gender_map.csv Each key term with its Latin etymon, gender and
                             route of inheritance
  metalinguistic_terms.csv   Concordance counts with explicit counting rules
  frecuencias_totales.csv    Full word-frequency list
  vocabulario_clave_por_capitulo.csv   Key vocabulary per chapter
code/
  ordo_virtutum_control.py   Control measurement: turn counts for Hildegard's
                             Ordo virtutum under the same protocol
docs/
  bibliography.md            State of the art and verification status of sources
  speaker-audit.md           Annotation protocol and audit results
  unresolved_uncertainty_marks.txt   The 160 `(?)` marks left unresolved
```

## Source and licensing

Documentation, protocol, derived data and code: CC BY 4.0 (see `LICENSE`).


Base text: Wikisource transcription of the Chantilly manuscript (Musée Condé),
15th c. The underlying work is in the public domain. Check the Wikisource
page for the licensing terms of the transcription itself before redistributing.

Original spelling is preserved throughout. The text is **not** normalised to
modern French, and quotations in the documentation are given unmodernised
(*dame amour*, *l'ame anientie*, *le loingprès*).

## Running the notebook

Requires Python 3 with `matplotlib` and `networkx`. The raw source ships with
the repository, under a different filename from the one the notebook expects:

```bash
cp source/raw/Margarita_wikisource_raw.txt notebook/Margarita.txt
cd notebook && jupyter notebook mirouer_analisis.ipynb   # run all cells
```

Alternatively, point `RUTA_ARCHIVO_CRUDO` at `../source/raw/Margarita_wikisource_raw.txt`.

**Do not re-encode the corpus.** The `char_offset` column in
`corpus/dialogue_turns.csv` indexes `corpus/mirouer_corpus_clean.txt` exactly as
shipped. That file has mixed line endings — 2,293 CRLF inherited from the source
transcription and 33 LF from the prepended opening poem — and the offsets assume
them. `.gitattributes` disables Git's newline normalisation for `.txt` and
`.csv`; normalising the file shifts every offset and they stop resolving. A
checksum for the file is in `source/checksums/SHA256SUMS.txt`. The notebook rebuilds the clean
corpus from the raw file: `corpus/mirouer_corpus_clean.txt` is provided for
convenience and as a checksum against your own run.

The notebook is written in Spanish (comments and variable names). Key terms:

| Spanish | English |
|---|---|
| `turnos` | dialogue turns |
| `transiciones` | turn transitions (graph edges) |
| `conteo_agrupado` | turns per figure |
| `capitulos` | chapters |
| `frecuencia_total` | word frequency |
| `centralidad_ordenada` | degree centrality, ranked |
| `CASOS_AUDITADOS` | manually audited turns (see `docs/speaker-audit.md`) |
| `GENERO_GRAMATICAL` | grammatical gender of each term |

## Method

Turn transitions follow the character-network approach of Franco Moretti,
*Network Theory, Plot Analysis* (Stanford Literary Lab, Pamphlet 2, 2011) and
Yannick Rochat, *Character Networks and Centrality* (PhD diss., EPFL, 2014).
The distribution of narrative attention by gender follows the design of Ted
Underwood, David Bamman and Sabrina Lee, "The Transformation of Gender in
English-Language Fiction", *Journal of Cultural Analytics* 3.2 (2018).

Degree centrality is computed with `networkx.degree_centrality()` on a
directed graph. Values above 1 are expected: for a DiGraph, `G.degree()`
returns in-degree plus out-degree, which can reach 2(n−1), while the function
normalises by n−1.

## Caveats

- **The figures are not neutral.** They are the output of an annotation
  convention: before counting who speaks, one has to decide how speakers are
  identified, and that decision is itself philological. Every count here is an
  aggregation of `corpus/dialogue_turns.csv`, where each row carries the rule
  that produced it.
- **Grammatical gender is not authorial intent.** The feminine gender of the
  speaking figures is accounted for in every case by direct Latin inheritance
  (*ratio*, *veritas*, *fides*, *anima*...) or, for *amour*, by a regular Old
  French development. None of them supports an argument from authorial choice
  on its own. The weight of the analysis rests on the distribution of speech,
  not on the gender of the nouns.
- **"Silence" here means absence of an explicit speaker label**, not absence
  from the text. *Dieu* occurs 467 times as a word and opens one turn. These
  are different measurements.
- **Degree centrality measures connection diversity**, not authority,
  prominence or theological weight.
- The audit covers one known class of error (irregular speaker punctuation).
  It is not a full philological reading of all 139 chapters.
- 4 further speaker labels occur mid-line and are excluded from the 379. Their
  effect is reported as a sensitivity check in the notebook (§14.5): the
  centrality ranking is unchanged.

- **This is not a substitute for the critical edition.** The corpus is built
  from the Wikisource transcription for reasons of open access and
  reproducibility. Speaker attributions, chapter divisions and unresolved
  readings should be validated against Guarnieri & Verdeyen, *Le Mirouer des
  simples ames / Speculum simplicium animarum*, CCCM 69 (Brepols, 1986).

## Control corpus

Hildegard of Bingen's *Ordo virtutum* (c. 1151) is the only control text to
which this protocol applies unmodified, since it rubricates its speakers. A
preliminary count gives 84 turns across 22 figures: 74 (88.1%) to figures with
grammatically feminine names, 10 (11.9%) to masculine ones.

**This is a preliminary control, not a statistically validated replication.**
It was measured on a translation whose rubrics follow the Latin original, not
on the critical Latin edition, and turn segmentation in the *Ordo* depends on
editorial decisions that vary between editions. No significance test is
reported here for that reason. Validation agenda: repeat the measurement
against Dronke, *Nine Medieval Latin Plays* (CUP, 1994) or the CCCM.

What the control does establish — and this does not depend on segmentation —
is that the *Ordo* cast includes virtues with masculine Latin names (*Timor
Dei*, *Contemptus Mundi*, *Amor Celestis*) that take turns normally. Allegorical
convention does not prevent a masculine abstraction from speaking. In the
*Mirouer*, the only masculine figures with a voice are divine Persons, and they
open 4 turns out of 379.

The *Roman de la Rose* and Christine de Pizan's *Cité des dames* cannot be
measured with this protocol: neither rubricates its speakers.

## What this corpus makes visible

> The *Mirouer* is not a text without gender; but its gender is not
> self-evident either. This corpus makes the difference between grammatical
> inheritance, allegorical convention and interpretive claim visible, countable
> and open to dispute.

---

## Citation

If you use the corpus or the protocol, please cite this repository.
A DOI can be minted via Zenodo.
