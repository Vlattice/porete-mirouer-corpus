# Bibliography

> Before interpreting the gender of the voices in the *Mirouer*, one has to
> establish whether that gender comes from grammar, from linguistic tradition,
> or from a textual decision. And before counting who speaks, one has to audit
> how speakers are identified.

Entries marked ✓ were verified against the publisher or the ACL Anthology.
Entries marked ◇ were supplied with a source link but not independently
verified; confirm before citing in print.

## Speaker attribution and character networks

✓ Elson, David K., Nicholas Dames, and Kathleen R. McKeown. "Extracting Social
Networks from Literary Fiction." In *Proceedings of the 48th Annual Meeting of
the Association for Computational Linguistics*, 138–147. Uppsala, 2010.
ACL Anthology P10-1015. — Networks built from direct discourse exchanged
between characters; the design this repository follows at a much smaller scale.

✓ Elson, David K., and Kathleen R. McKeown. "Automatic Attribution of Quoted
Speech in Literary Narrative." In *Proceedings of the 24th AAAI Conference on
Artificial Intelligence*, 1013–1019. 2010.

◇ He, Hua, Denilson Barbosa, and Grzegorz Kondrak. "Identification of Speakers
in Novels." In *Proceedings of the 51st Annual Meeting of the ACL*, 2013.
ACL Anthology P13-1129. — Speaker identification as a task in its own right,
which is precisely what `docs/speaker-audit.md` treats as a philological
problem rather than a solved preprocessing step.

◇ Vishnubhotla, Krishnapriya, et al. *Project Dialogism Novel Corpus*. — A
corpus annotated for quotation attribution; the closest methodological
precedent for `corpus/dialogue_turns.csv`.

◇ FRACAS: a French corpus annotated for quotation attribution and speaker
gender. arXiv:2309.10604. — The nearest analogue in French, though for modern
prose; useful as a comparison point for annotation schema design.

✓ Moretti, Franco. "Network Theory, Plot Analysis." Stanford Literary Lab,
Pamphlet 2, 2011.

✓ Rochat, Yannick. "Character Networks and Centrality." PhD diss., École
Polytechnique Fédérale de Lausanne, 2014.

## Gender and dialogue distribution

✓ Underwood, Ted, David Bamman, and Sabrina Lee. "The Transformation of Gender
in English-Language Fiction." *Journal of Cultural Analytics* 3, no. 2 (2018).
— Measures narrative attention by gender at corpus scale. Note that it is a
model for *distribution of attention*, not a method of speaker attribution.

✓ Bamman, David, Ted Underwood, and Noah A. Smith. "A Bayesian Mixed Effects
Model of Literary Character." In *Proceedings of the 52nd Annual Meeting of the
ACL*, 2014.

## Irigaray: enunciation as object

✓ Irigaray, Luce. *Parler n'est jamais neutre*. Paris: Minuit, 1985. — Shifts
the object from the statement to the enunciation; records speech samples,
reduces them to minimal sentence types, tabulates them and refines the grid.
Methodological precedent for counting who speaks rather than what is said.

✓ Irigaray, Luce. "Sorcerer Love: A Reading of Plato's Symposium, Diotima's
Speech." *Hypatia* 3, no. 3 (1988): 32–44. — Diotima is absent from the
banquet; Socrates reports her. The *Mirouer* inverts the figure.

✓ Irigaray, Luce. *In the Beginning, She Was*. London: Bloomsbury, 2012. —
Source of the "relation between two" used in the network section.

## Computational work on medieval and mystical texts

✓ Haverals, Wouter, and Mike Kestemont. "From Exemplar to Copy: The Scribal
Appropriation of a Hadewijch Manuscript Computationally Explored." *Journal of
Data Mining & Digital Humanities* (2023). doi:10.46298/jdmdh.10206. — Closest
antecedent by domain (a Flemish woman mystic, near-contemporary of Porete), not
by design: it measures manuscript transmission, not voice distribution.

✓ Vianne, Laurine, Yoann Dupont, and Jean Barré. "Gender Bias in French
Literature." CHR 2023, CEUR-WS vol. 3558. — Adapts the Underwood–Bamman–Lee
design to 2,942 French novels. The authors call it an adaptation, not a
replication: French marks gender on adjectives and participles, so they work on
lemmas.

✓ Prado, S. D., S. R. Dahmen, M. MacCarron, A. L. C. Bazzan, and J. Hillner.
"Gendered Networks and Communicability in Medieval Historical Narratives."
Preprint, 2020. arXiv:2002.01396. — Gendered character network on Bede.
Referential gender and social ties, not grammatical gender and speaker labels.

## Gender of medieval personifications

◇ Wouters, "Woman Personified." *Medieval Feminist Forum* 53, no. 2. — On the
debate over the femininity of medieval personifications; directly relevant to
the caveat that grammatical gender is not authorial intent.

✓ Morton, Jonathan. "Where Are the Bodies? Gender-Bending Voices in the *Roman
de la rose*." *Cahiers de recherches médiévales et humanistes* 22 (2011):
124–137. doi:10.4000/crm.12520.

✓ Paxson, James J. "Personification's Gender." *Rhetorica* 16, no. 2 (1998):
149–179. — Argues that feminine personification in medieval rhetoric can be
read as part of a misogynistic discursive tradition rather than as an
assertion of authority. The objection this repository does not resolve.

✓ Newman, Barbara. *God and the Goddesses: Vision, Poetry, and Belief in the
Middle Ages*. Philadelphia: University of Pennsylvania Press, 2003.

## Grammatical gender in French

✓ Littré, Émile. *Dictionnaire de la langue française*, s.v. "amour."
Hachette, 1873–1874. — The direct evidence that *amour* was feminine in Old
French, like *douleur* and *peur*.

✓ Grevisse, Maurice, and André Goosse. *Le bon usage*. De Boeck Supérieur. —
On the 16th–17th c. masculinisation of the singular.

✓ Loporcaro, Michele. *Gender from Latin to Romance: History, Geography,
Typology*. Oxford University Press, 2017.

## The text

✓ Guarnieri, Romana, and Paul Verdeyen, eds. *Le Mirouer des simples ames /
Speculum simplicium animarum*. CCCM 69. Turnhout: Brepols, 1986. — The
critical edition. This corpus is **not** collated against it.

✓ Colledge, Edmund, J. C. Marler, and Judith Grant, eds. *Margaret Porette:
The Mirror of Simple Souls*. Notre Dame: University of Notre Dame Press, 1999.

## Translations consulted for the Prologue reading

The sentence *"nostre seigneur n'est mie du tout enfranchi d'amour, mais amour
l'est de lui pour nous"* is grammatically ambiguous: Middle French *de* marks
both separation and agent. The reading adopted is the agentive one, following
the English tradition of the text.

✓ Kirchberger, Clare, ed. *A Mirror of Simple Souls*. London: Burns Oates, 1927.
Orchard Spiritual Classics. — A **modernisation** of M. N.'s Middle English
translation, not an edition of it. Renders the passage "not that we be lords,
free of all, but that his love for us maketh us free." The wording is
Kirchberger's, not M. N.'s.

◇ Doiron, Marilyn, ed. "Margaret Porete: The Mirror of Simple Soules. A Middle
English Translation." *Archivio Italiano per la Storia della Pietà* 5 (1968):
241–355. — The edition of M. N.'s Middle English. **Not consulted**; needed to
attribute wording to the medieval translator.

◇ Van Woerkom, Hugo M., trans. *The Mirror of Simple Souls*. 2008. — Open-access
modern translation, **not a critical edition**. Cited only as concurrence.

◇ The Latin *Speculum* in Verdeyen and Guarnieri (CCCM 69, 1986) would settle
the question: the Latin translator faced the same preposition. **Not consulted.**

## Reception of the "genderless" reading

✓ Kocher, Suzanne. Review of *Margaret Porette: The Mirror of Simple Souls*, ed.
Colledge, Marler and Grant. *The Medieval Review* 00.09.05 (2000). — Establishes
that "genderless" is **Kent Emery, Jr.'s** word, in the foreword (p. xi), not
the editors'. Kocher already objected to it in 2000, criticising the foreword
and introduction for not engaging the gender scholarship on Porete. This
repository adds measurement to an objection that already existed.
