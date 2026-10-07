"""
Control preliminar: Ordo virtutum (Hildegarda de Bingen, h. 1151).

ESTATUTO: preliminar, NO réplica validada.
La secuencia de rúbricas se tomó de la traducción de L. M. Zaerr, cuyas
rúbricas siguen a las del original latino. NO se midió sobre el texto latino
de la edición crítica, y la segmentación de turnos del Ordo virtutum depende
de decisiones editoriales que varían entre ediciones.

Por esa razón este script NO calcula pruebas de significancia: un contraste
cuyo denominador depende de la edición consultada no mide lo que pretende.

Pendiente de validación: repetir sobre Dronke, Nine Medieval Latin Plays
(CUP, 1994) o el CCCM, verificando rúbrica por rúbrica.

Lo que este control sí establece, y no depende de la segmentación: el elenco
del Ordo incluye virtudes de nombre masculino (Timor Dei, Contemptus Mundi,
Amor Celestis) que abren turno con normalidad. La convención alegórica no
impide hablar a una abstracción masculina.
"""
from collections import Counter
# Secuencia de rúbricas de hablante del Ordo virtutum, en orden de aparición
# (trad. Zaerr; las rúbricas corresponden a las del original latino).
secuencia = [
 "Patriarche et Prophete","Virtutes","Patriarche et Prophete","Anime (embodied)",
 "Anima","Virtutes","Anima","Virtutes","Anima","Virtutes","Anima","Scientia Dei",
 "Anima","Virtutes","Scientia Dei","Anima","Diabolus","Virtutes","Diabolus",
 "Humilitas","Virtutes","Humilitas","Virtutes","Humilitas","Caritas","Virtutes",
 "Timor Dei","Virtutes","Diabolus","Virtutes","Obedientia","Virtutes","Fides",
 "Virtutes","Spes","Virtutes","Castitas","Virtutes","Innocentia","Virtutes",
 "Contemptus Mundi","Virtutes","Amor Celestis","Virtutes","Disciplina","Virtutes",
 "Verecundia","Virtutes","Misericordia","Virtutes","Victoria","Virtutes",
 "Discretio","Virtutes","Patientia","Virtutes","Humilitas","Virtutes","Anima",
 "Virtutes","Anima","Virtutes","Anima","Virtutes","Anima","Virtutes","Anima",
 "Humilitas","Virtutes","Humilitas","Virtutes","Diabolus","Anima","Humilitas",
 "Victoria","Virtutes","Humilitas","Virtutes","Victoria","Virtutes","Castitas",
 "Diabolus","Castitas","Virtutes",
]
# Género gramatical del nombre latino de cada figura
genero = {
 "Virtutes":"fem",            # virtus, virtutis
 "Anima":"fem",               # anima
 "Anime (embodied)":"fem",
 "Humilitas":"fem","Caritas":"fem","Obedientia":"fem","Fides":"fem","Spes":"fem",
 "Castitas":"fem","Innocentia":"fem","Disciplina":"fem","Verecundia":"fem",
 "Misericordia":"fem","Victoria":"fem","Discretio":"fem","Patientia":"fem",
 "Scientia Dei":"fem",
 "Timor Dei":"masc",          # timor, timoris
 "Contemptus Mundi":"masc",   # contemptus, -us
 "Amor Celestis":"masc",      # amor, amoris
 "Diabolus":"masc",
 "Patriarche et Prophete":"masc",
}
c = Counter(secuencia)
print(f"Turnos totales: {len(secuencia)}  |  figuras: {len(c)}\n")
for fig, n in c.most_common():
    print(f"  {fig:24s} {n:3d}  {genero[fig]}")
fem = sum(n for f,n in c.items() if genero[f]=="fem")
masc = sum(n for f,n in c.items() if genero[f]=="masc")
print(f"\nFemeninos: {fem} ({fem/len(secuencia)*100:.1f}%)   Masculinos: {masc} ({masc/len(secuencia)*100:.1f}%)")
print(f"Figuras femeninas: {sum(1 for f in c if genero[f]=='fem')} / masculinas: {sum(1 for f in c if genero[f]=='masc')}")
print("\n¿Habla Dios? ", "sí" if any("Deus" in f for f in c) else "no (Scientia Dei es una virtud, no Dios)")
