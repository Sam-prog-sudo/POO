#-*- coding: utf8 -*-

class Personne:
    """une personne est defiie par:
    -nom
    -prenom
    -age
    -lieu de naissance"""
    def __init__(self):
        """Le constructeur permet de definir les attribut de cette classe:"""
        self.nom = "Dupond"
        self.prenom = "Jean"
        self.age = 33
        self.lieu_residence = "Paris"

        
jean = Personne()               #créer l'objet 'bernard' appartenant à la classe personne
jean.nom                        #retourne 'Dupond'
jean.age                        #retourne 33
jean.lieu_residence = "Berlin"  #change le lieu de residence


#-------------------------------------------------------------------#


class Personne:
    """une personne est definie par:
    -nom
    -prenom
    -age
    -lieu de naissance"""
    def __init__(self, nom, prenom):
        """Le constructeur permet de definir les attribut de cette classe:"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self.lieu_residence = "Paris"


bernard = Personne("Micado", "Beranrd")
bernard.nom         #retourne 'Micado'
bernard.prenom      #retourne 'Bernard'
bernard.age         #retourn 33


#-------------------------------------------------------------------#


class Compteur:
    """Cette classe possède un attribut de classe qui s'incremente
    à chaque fois que l'on crée un objet de ce type de class."""
    objets_crees = 0
    
    def __init__(self):
        self.objets_crees += 1
        
    def combien(cls):
        """Méthode de classe affichant combien d'objets ont été créé dans la classe"""
        print("Jusqu'à présent, {} objets ont été créés." .format(cls.objets_crees))
    combien = classmethod(combien)


Compteur.objets_crees   #retourne '0'
a = Compteur()          # On crée un premier objet
Compteur.objets_crees   #retourne '1'

Compteur.combien() #retourne 'Jusqu'à présent, 1 objets ont été créés.'
b = Compteur()
Compteur.combien() #retourne 'Jusqu'à présent, 2 objets ont été créés.'


#-------------------------------------------------------------------#


class TableauNoir:
    """Cette classe définit une surface sur laquelle on peut ecrire"""
   
    def __init__(self):
        """par défaut, la surface est vide"""
        self.surface = ""
    
    def ecrire (self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, fait un saut de ligne,
        avant de rajouter le message à écrir."""
        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire
    
    def lire (self):
        """cette méthodeaffiche la surface du tableau"""
        print (self.surface)

    def effacer (self):
        """cette méthode efface la surface du tableau"""
        self.surface = ""


tab = TableauNoir()
tab.surface #retourne ""

tab.ecrire("ceci est une chaine")
tab.surface #retourne "ceci est une chaine"

tab.ecrire("joyeux noel !")
tab.surface #retourne "ceci est une chaine\njoyeux noel !"

x=tab.surface
print(x)
#retourne   ceci est une chaine
#           joyeux noel !

"""tab.ecrire(…) revient à taper TableauNoir.ecrire(tab, …)"""

tab.lire()
#retourne   ceci est une chaine
#           joyeux noel !

tab.effacer()
tab.lire()  #retourne rien


#-------------------------------------------------------------------#
#methode statique

class Test1:
    """Une classe de test tout simplement"""
    def afficher():
        """Fonction chargée d'afficher quelque chose"""
        print("On affiche la même chose.")
        print("peu importe les données de l'objet ou de la classe.")
    afficher = staticmethod(afficher)


#-------------------------------------------------------------------#


class Test:
    """Une classe de test tout simplement"""
    def __init__(self):
        """On définit dans le constructeur un unique attribut"""
        self.mon_attribut = "ok"
    
    def afficher_attribut(self):
        """Méthode affichant l'attribut 'mon_attribut'"""
        print("Mon attribut est {0}.".format(self.mon_attribut))


un_test = Test()
un_test.afficher_attribut()  # retourne Mon attribut est ok.
dir(un_test)
#   retourne ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__g
#   e__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__',
#   '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '_
#   _setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'affich
#   er_attribut', 'mon_attribut']

un_test.__dict__    #retourne {'mon_attribut': 'ok'}
"""__dict__ est un attribut spéciale qui contient:
        - en clef, le nom des attributs de la classe
        - en valeur, les valeurs des attributs de la classe"""