#ne fonctionne qu'avec les listes
prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
prenoms.sort() #travaille sur la meme liste
prenoms
['Albert', 'André', 'Jacques', 'Laure', 'Sophie', 'Victoire']

# Et avec la fonction 'sorted' qui fonctionne avec tout
prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
sorted(prenoms) #creer une autre liste
['Albert', 'André', 'Jacques', 'Laure', 'Sophie', 'Victoire']
prenoms
['Jacques', 'Laure', 'André', 'Victoire', 'Albert', 'Sophie']


sorted([1, 8, -2, 15, 9])
[-2, 1, 8, 9, 15] #renvoie une liste d'entier du + petit au + rand

sorted(["1", "8", "-2", "15", "9"])
['-2', '1', '15', '8', '9'] #renvoie une liste de str par ordre alphabetique


sorted([1, "8", "-2", "15", 9]) #n'arrive pas a faire le tri entre les srt et les int
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() < int()

#---------------Trier avec des clés précises---------------#

etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

sorted(etudiants) #tri par rapport au premeir element du tuple (prenom, age, moyenne)
[('Charles', 12, 15), ('Clément', 14, 16), ('Damien', 12, 15), ('Oriane', 14, 18), ('Thomas', 11, 12)]

sorted(etudiants, key=lambda patate: patate[2]) #tri par rapport à la 3e colonne
[('Thomas', 11, 12), ('Charles', 12, 15), ('Damien', 12, 15), ('Clément', 14, 16), ('Oriane', 14, 18)]


#---------------Trier avec des classes---------------#


class Etudiant:
    
    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant
    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})>".format(
                self.prenom, self.age, self.moyenne)


etudiants = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]


sorted(etudiants, key=lambda etudiant: etudiant.moyenne)
[Étudiant Thomas (âge=11, moyenne=12), Étudiant Charles (âge=12, moyenne=15),
 Étudiant Damien (âge=12, moyenne=15), Étudiant Clément (âge=14, moyenne=16),
 Étudiant Oriane (âge=14, moyenne=18)]


#---------------operator---------------#

from operator import itemgetter
sorted(etudiants, key=itemgetter(2))
#trie par rapport à la moyenne, de maniere croissante


from operator import attrgetter
sorted(etudiants, key=attrgetter("moyenne"))
#trie par rapport à l'attribut moyenne

sorted(etudiants, key=attrgetter("age", "moyenne"))
#trie par age et si age pareil, alors trie par moyenne

etudiants.sort(key=attrgetter("moyenne"), reverse=True)
sorted(etudiants, key=attrgetter("age"))
#permet de trier par age croissant puis par moyenne decroissante