# Changelog

## 1.1

Corrections and additions found while auditing the corpus against the prose
analysis. Headline figures for the main set are unchanged: 379 turns, 375
feminine (98.9%), 4 masculine (1.1%), 243 transitions.

### Added

- **Notebook section 16**, two cells that reproduce the two figures above:
  16.1 detects `L'acteur` and reports both sets, 16.2 computes the turn
  trajectory and exports `turn_trajectory_quintiles.csv`. The notebook runs
  end to end with no errors and 5 figures; no previous cell was altered except
  the one noted below.
- **Line-ending normalisation at read time** (cell 7, one line). The raw
  Wikisource file has CRLF; without normalising, every position computed in the
  notebook is offset from the published LF corpus. This is the root cause of the
  invalid `char_offset` column and is now fixed at source: the position the
  notebook reports for `L'acteur` (3363) is the one in the published CSV.

- **`L'acteur`, a tenth explicit speaker label.** The authorial voice opens one
  turn in the Prologue and occurs nowhere else in the 139 chapters. The
  closed-list pattern did not capture it because the list catalogues the nine
  figures of the cast. Recorded as row `T384` under new rule **A08**
  (`authorial_voice`) and excluded from the main set as framing rather than
  participating. Extended set including it: 380 turns, 375 feminine (98.7%),
  5 masculine (1.3%). No conclusion depends on which set is adopted.
  See `docs/speaker-audit.md`.
- **`data/turn_trajectory_quintiles.csv`.** Distribution of turns across five
  consecutive blocks of the turn sequence. The Soul's share rises monotonically
  (5.3% → 53.9%) while Love's falls (60.0% → 25.0%); the Soul's token volume
  rises from 874 to 3,095. Relevant to Kocher's "from active women to passive
  souls" trajectory, which does not hold at the level of dialogue turns.
- Bibliography sections for Irigaray, computational work on medieval and
  mystical texts, the translations consulted for the Prologue reading, and the
  reception of the "genderless" characterisation.

### Fixed

- **`char_offset` was silently invalid.** The column had been computed against a
  copy of `mirouer_corpus_clean.txt` with mixed line endings (2,293 CRLF + 33
  LF); the published file is LF-only, so every offset was shifted by the number
  of CRLF pairs preceding it — by 5 characters at the first turn and by over
  2,000 at the end. Anyone slicing the corpus by offset got text from the wrong
  place. All 384 offsets are recomputed against the published file and verified
  to open their turn exactly. `.gitattributes` keeps git from renormalising the
  files again, and now says LF rather than mixed.

- **`crainte`** was listed as direct Latin inheritance. It is a French deverbal
  formation; feminine by Romance morphology, not by a Latin noun gender.
- **`néant`** was listed as direct Latin inheritance. It is a substantivised
  indefinite pronoun, masculine by the default French assigns to that class.
  The `*ne gentem` derivation is a hypothesis (Körting 1896, recorded by TLFi
  as "prob.", accepted by FEW), not established — and its etymon head
  *gens, gentis* is feminine, so the masculine is in no case inherited.
- **`franchise`** and **`esperance`** were likewise listed as direct
  inheritance; both are Romance formations.
- **Degree centrality** was described as measuring "connection diversity". It
  sums in- and out-edges, so one neighbour can contribute twice; it is not a
  count of distinct interlocutors.
- **`Dieu` frequency** now states the breakdown: 447 singular, 20 *dieux*,
  467 total.
- **Morton** was cited from a 1998 Garland volume. The article is *Cahiers de
  recherches médiévales et humanistes* 22 (2011), 124–137.
- **"Genderless"** was attributed to Colledge, Marler and Grant. It is Kent
  Emery, Jr.'s word, in the foreword to that edition (p. xi); Suzanne Kocher
  objected to it in her 2000 review.
- **Kirchberger (1927)** was described as an edition of M. N.'s Middle English.
  It is a modernisation of it, so the wording quoted is Kirchberger's. Doiron
  (1968) is the edition of M. N.; not consulted.

## 1.0

First release: corpus, speaker-extraction protocol, turn table, gender map,
network data and notebook.
