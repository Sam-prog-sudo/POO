#-*- coding: utf8 -*-

class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom ;
    - son prénom ;
    - son âge ;
    - son lieu de résidence"""

    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris" # Notez le souligné _ devant le nom

    def _get_lieu_residence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut 'lieu_residence' """
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence

    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
                self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence

    # On va dire à Python que notre attribut lieu_residence pointe vers une propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)


jean = Personne("Micado", "Jean")
jean.nom            #retourne 'Micado'
jean.prenom         #retourne 'Jean'
jean.age            #retourne 33
jean.lieu_residence
#                   retourne On accède à l'attribut lieu_residence !
#                            'Paris'
jean.lieu_residence = "Berlin"
#                   retourne Attention, il semble que Jean déménage à Berlin.
jean.lieu_residence
#                   retourne On accède à l'attribut lieu_residence !
#                            'Berlin'
