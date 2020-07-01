class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""
    
    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
        # On appelle explicitement le constructeur de Personne :
        Personne.__init__(self, nom)
        self.matricule = matricule
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)


agent = AgentSpecial("Fisher", "18327-121")
agent.nom #retourne -> 'Fisher'
print(agent) #retourne -> Agent Fisher, matricule 18327-121
agent.prenom #retourne -> 'Martin'

issubclass(AgentSpecial, Personne) # AgentSpecial hérite de Personne
# retourne -> True
issubclass(AgentSpecial, object)
# retourne -> True
issubclass(Personne, object)
# retourne -> True
issubclass(Personne, AgentSpecial) # Personne n'hérite pas d'AgentSpecial
# retourne -> False


agent = AgentSpecial("Fisher", "18327-121")
isinstance(agent, AgentSpecial) # Agent est une instance d'AgentSpecial
# retourne -> True
isinstance(agent, Personne) # Agent est une instance héritée de Personne
# retourne -> True
