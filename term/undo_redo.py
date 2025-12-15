
class Pile:
	def __init__(self):
		self.valeurs = []

	def empiler(self, valeur):
		self.valeurs.append(valeur)

	def depiler(self):
		if self.valeurs:
			return self.valeurs.pop()

	def estVide(self):
		return self.valeurs == []



    