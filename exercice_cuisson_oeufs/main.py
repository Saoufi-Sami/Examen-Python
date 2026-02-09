titre = "Ma cuisson préféré"

largeur = len(titre) + 11        # Longueur du titre + 11

print("*" * (len(titre) + 11))   # Affiche autant d'etoile que le titre et rajoute en 11
print(titre.center(largeur))    # Affiche mon titre centré avec le même nombre de caractères que la variable largeur.
print("Oeufs a la coque : 3 minutes".center(largeur))
print("Oeufs mollets    : 6 minutes".center(largeur))
print("Oeufs a la coque : 3 minutes".center(largeur))
print("*" * (len(titre) + 11))
