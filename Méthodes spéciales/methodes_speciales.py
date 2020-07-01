#-------------------Représentation de l'objet--------------------#


class Personne:
    """Classe représentant une personne"""
    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        
    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Personne: nom({}), prénom({}), âge({})".format(
                self.nom, self.prenom, self.age)
        
p1 = Personne("Micado", "Jean")
p1      #retourne --> Personne: nom(Micado), prénom(Jean), âge(33)


class Personne:
    """Classe représentant une personne"""
    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        
    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        return "{} {}, âgé de {} ans".format(
                self.prenom, self.nom, self.age)

p1 = Personne("Micado", "Jean")
print(p1)   #retourne --> Jean Micado, âgé de 33 ans
chaine = str(p1)
chaine      #retourne --> 'Jean Micado, âgé de 33 ans'

#---------------Accès aux attributs de notre objet---------------#

class Protege:
    """Classe possédant une méthode particulière d'accès à ses attributs :
    Si l'attribut n'est pas trouvé, on affiche une alerte et renvoie None"""

    
    def __init__(self):
        """On crée quelques attributs par défaut"""
        self.a = 1
        self.b = 2
        self.c = 3
    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
        cette méthode. On affiche une alerte"""

        
        print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))

pro = Protege()
pro.a   #retourne --> 1
pro.c   #retourne --> 3
pro.e   #retourne --> Alerte ! Il n'y a pas d'attribut e ici !


#-------------------------------------------------------------------------#

def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistrer l'objet"""
        
        
        object.__setattr__(self, nom_attr, val_attr)
        self.enregistrer()


#-------------------------------------------------------------------------#


def __delattr__(self, nom_attr):
        """On ne peut supprimer d'attribut, on lève l'exception
        AttributeError"""
        
        object.__delattr__(self, nom_attr)
        raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")


#-------------------------------------------------------------------------#


mon_objet = MaClasse() # On crée une instance de notre classe
getattr(mon_objet, "nom") # Semblable à mon_objet.nom
setattr(mon_objet, "nom", val) # = mon_objet.nom = val ou mon_objet.__setattr__("nom", val)
delattr(mon_objet, "nom") # = del mon_objet.nom ou mon_objet.__delattr__("nom")
hasattr(mon_objet, "nom") # Renvoie True si l'attribut "nom" existe, False sinon