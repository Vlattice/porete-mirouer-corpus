# Bibliography

> Before interpreting the gender of the voices in the *Mirouer*, one has to
> establish whether that gender comes from grammar, from linguistic tradition,
> or from a textual decision. And before counting who speaks, one has to audit
> how speakers are identified.

Where an entry was not consulted directly, or where the edition used is not the
critical one, the note says so.

## Speaker attribution and character networks

Elson, David K., Nicholas Dames, and Kathleen R. McKeown. "Extracting Social
Networks from Literary Fiction." In *Proceedings of the 48th Annual Meeting of
the Association for Computational Linguistics*, 138–147. Uppsala, 2010. ACL
Anthology P10-1015. — Networks built from direct discourse exchanged between
characters; the design this repository follows at a much smaller scale.

Elson, David K., and Kathleen R. McKeown. "Automatic Attribution of Quoted
Speech in Literary Narrative." In *Proceedings of the 24th AAAI Conference on
Artificial Intelligence*, 1013–1019. 2010.

He, Hua, Denilson Barbosa, and Grzegorz Kondrak. "Identification of Speakers in
Novels." In *Proceedings of the 51st Annual Meeting of the Association for
Computational Linguistics* (Volume 1: Long Papers), 1312–1320. Sofia, 2013. ACL
Anthology P13-1129. — Speaker identification as a task in its own right, which
is what `docs/speaker-audit.md` treats as a philological problem rather than a
solved preprocessing step.

Vishnubhotla, Krishnapriya, Adam Hammond, and Graeme Hirst. "The Project
Dialogism Novel Corpus: A Dataset for Quotation Attribution in Literary Texts."
In *Proceedings of the 13th Language Resources and Evaluation Conference*,
5838–5848. Marseille, 2022. ACL Anthology 2022.lrec-1.628. — A corpus annotated
for quotation attribution; the closest methodological precedent for
`corpus/dialogue_turns.csv`.

Richard, Ange, Laura Alonzo-Canul, and François Portet. "FRACAS: A FRench
Annotated Corpus of Attribution relations in newS." Preprint, 2023.
arXiv:2309.10604. — 1,676 French newswire texts annotated for quotations and
their sources, with inter-annotator agreement reported for eight annotators.
Different genre and no gender layer; cited for its annotation-guideline design,
which is the part that transfers.

Moretti, Franco. "Network Theory, Plot Analysis." Stanford Literary Lab,
Pamphlet 2, 2011. Also in *New Left Review* 68.

Rochat, Yannick. "Character Networks and Centrality." PhD diss., École
Polytechnique Fédérale de Lausanne, 2014.

## Gender and dialogue distribution

Underwood, Ted, David Bamman, and Sabrina Lee. "The Transformation of Gender in
English-Language Fiction." *Journal of Cultural Analytics* 3, no. 2 (2018). —
Measures narrative attention by gender at corpus scale. A model for the
*distribution of attention*, not a method of speaker attribution.

Bamman, David, Ted Underwood, and Noah A. Smith. "A Bayesian Mixed Effects
Model of Literary Character." In *Proceedings of the 52nd Annual Meeting of the
Association for Computational Linguistics*, 370–379. Baltimore, 2014.

## Irigaray: enunciation as object

Irigaray, Luce. *Parler n'est jamais neutre*. Paris: Minuit, 1985. — Shifts the
object from the statement to the enunciation; records speech samples, reduces
them to minimal sentence types, tabulates them and refines the grid.
Methodological precedent for counting who speaks rather than what is said.

Irigaray, Luce. "Sorcerer Love: A Reading of Plato's *Symposium*, Diotima's
Speech." *Hypatia* 3, no. 3 (1988): 32–44. — Diotima is absent from the
banquet; Socrates reports her. The *Mirouer* inverts the figure.

Irigaray, Luce. *In the Beginning, She Was*. London: Bloomsbury, 2012. — Source
of the "relation between two" used in the network section.

## Computational work on medieval and mystical texts

Haverals, Wouter, and Mike Kestemont. "From Exemplar to Copy: The Scribal
Appropriation of a Hadewijch Manuscript Computationally Explored." *Journal of
Data Mining & Digital Humanities* (2023). doi:10.46298/jdmdh.10206. — Closest
antecedent by domain (a Flemish woman mystic, near-contemporary of Porete), not
by design: it measures manuscript transmission, not voice distribution.

Vianne, Laurine, Yoann Dupont, and Jean Barré. "Gender Bias in French
Literature." CHR 2023, CEUR-WS vol. 3558. — Adapts the Underwood–Bamman–Lee
design to 2,942 French novels. The authors call it an adaptation, not a
replication: French marks gender on adjectives and participles, so they work on
lemmas.

Prado, S. D., S. R. Dahmen, M. MacCarron, A. L. C. Bazzan, and J. Hillner.
"Gendered Networks and Communicability in Medieval Historical Narratives."
Preprint, 2020. arXiv:2002.01396. — Gendered character network on Bede.
Referential gender and social ties, not grammatical gender and speaker labels.

## Gender of medieval personifications

Wouters, Dinah. "Woman Personified: A Theoretical Framework for the Female
Gender of Personifications in Medieval Literature." *Medieval Feminist Forum*
53, no. 2 (2018): 5–37. — On the debate over the femininity of medieval
personifications; directly relevant to the caveat that grammatical gender is
not authorial intent.

Morton, Jonathan. "Where Are the Bodies? Gender-Bending Voices in the *Roman de
la rose*." *Cahiers de recherches médiévales et humanistes* 22 (2011): 124–137.
doi:10.4000/crm.12520.

Paxson, James J. "Personification's Gender." *Rhetorica* 16, no. 2 (1998):
149–179. — Argues that feminine personification in medieval rhetoric can be
read as part of a misogynistic discursive tradition rather than as an assertion
of authority. The objection this repository does not resolve.

Newman, Barbara. *God and the Goddesses: Vision, Poetry, and Belief in the
Middle Ages*. Philadelphia: University of Pennsylvania Press, 2003.

## Grammatical gender in French

Littré, Émile. *Dictionnaire de la langue française*, s.v. "amour." Paris:
Hachette, 1873–1874. — The direct evidence that *amour* was feminine in Old
French, like *douleur* and *peur*.

Grevisse, Maurice, and André Goosse. *Le bon usage*. 16th ed. Louvain-la-Neuve:
De Boeck Supérieur, 2016. — On the 16th–17th c. masculinisation of the
singular.

Loporcaro, Michele. *Gender from Latin to Romance: History, Geography,
Typology*. Oxford: Oxford University Press, 2017.

## The text

Guarnieri, Romana, and Paul Verdeyen, eds. *Le Mirouer des simples ames /
Speculum simplicium animarum*. CCCM 69. Turnhout: Brepols, 1986. — The critical
edition. This corpus is **not** collated against it.

Colledge, Edmund, J. C. Marler, and Judith Grant, eds. *The Mirror of Simple
Souls*. Notre Dame Texts in Medieval Culture 6. Notre Dame: University of Notre
Dame Press, 1999. — Foreword by Kent Emery, Jr.

## Translations consulted for the Prologue reading

The sentence *"nostre seigneur n'est mie du tout enfranchi d'amour, mais amour
l'est de lui pour nous"* is grammatically ambiguous: Middle French *de* marks
both separation and agent. The reading adopted is the agentive one, following
the English tradition of the text.

Kirchberger, Clare, ed. *A Mirror of Simple Souls*. Orchard Spiritual Classics.
London: Burns Oates, 1927. — A modernisation of M. N.'s Middle English
translation, not an edition of it. Renders the passage "not that we be lords,
free of all, but that his love for us maketh us free." The wording is
Kirchberger's, not M. N.'s.

Doiron, Marilyn, ed. "Margaret Porete: *The Mirror of Simple Soules*. A Middle
English Translation." *Archivio Italiano per la Storia della Pietà* 5 (1968):
241–355. — The edition of M. N.'s Middle English. Not consulted; it is what
would allow the wording to be attributed to the medieval translator.

Van Woerkom, Hugo M., trans. *The Mirror of Simple Souls*. 2008. — Open-access
modern translation, not a critical edition. Cited only as concurrence.

The Latin *Speculum* in Guarnieri and Verdeyen (CCCM 69, 1986) would settle the
question, since the Latin translator faced the same preposition. Not consulted.

## Control corpus: Ordo virtutum

Zaerr, Linda Marie, trans. *Ordo virtutum*, by Hildegard of Bingen. Boise State
University, 2013. — Online translation, not a critical edition. The rubric
sequence used for the preliminary control was taken from it.

Dronke, Peter, ed. *Nine Medieval Latin Plays*. Cambridge: Cambridge University
Press, 1994. — The Latin text, pp. 147–184. Not consulted; it is what would
allow the measurement to be repeated on the critical Latin.

Paxson, James J. "The Allegorical Construction of Female Feeling and Forma:
Gender, Diabolism, and Personification in Hildegard of Bingen's *Ordo
virtutum*." In *The Representation of Women's Emotions in Medieval and Early
Modern Culture*, ed. Lisa Perfetti. Gainesville: University Press of Florida,
2005.

## Reception of the "genderless" reading

Kocher, Suzanne. Review of *The Mirror of Simple Souls*, ed. Colledge, Marler
and Grant. *The Medieval Review* 00.09.05 (2000). — Establishes that
"genderless" is **Kent Emery, Jr.'s** word, in the foreword (p. xi), not the
editors'. Kocher already objected to it in 2000, criticising the foreword and
introduction for not engaging the gender scholarship on Porete. This repository
adds measurement to an objection that already existed.

Kocher, Suzanne. *Allegories of Love in Marguerite Porete's "Mirror of Simple
Souls"*. Medieval Women: Texts and Contexts 17. Turnhout: Brepols, 2008. — The
nearest work by object: a reading of the *Mirouer*'s allegorical figures. Not
consulted directly.

Roccati, G. Matteo. Review of *Allegories of Love in Marguerite Porete's
"Mirror of Simple Souls"*, by Suzanne Kocher. *Studi Francesi* 166 (2012): 119.
— Open access. The source for the book's chapter architecture: II. From Active
Women to Passive Souls (gender), III. From Spiritual Servitude to Freedom
(social rank), IV. the economic register.
