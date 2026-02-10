import time

TEMPS_COQUE = 3
TEMPS_MOLLETS = 6
TEMPS_DURS = 9

def afficher_temps_restant(temps_choisie):
    temps_restant_sec = temps_choisie * 60
    print("Cuisson en cours " , end="",flush=True)

    for i in range(10):
        time.sleep(1)
        print(".", end="", flush=True)
        
    print()
    while temps_restant_sec >= 0:
          minutes = temps_restant_sec // 60
          secondes = temps_restant_sec - (minutes * 60)
          print(f"Durée restante : {minutes:02d}:{secondes:02d}",end="", flush=True)
          if temps_restant_sec == 0:
             break
 # on utilise ce if break pour ne pas avoir les points apres la derniere iteration 00:00
          for i in range(10):
             time.sleep(1)
             print(".", end="", flush=True)
          print()
          temps_restant_sec -= 10
    print()
    print("Cuisson terminée !")


titre = "Ma cuisson préféré"
largeur = len(titre) + 11        # Longueur du titre + 11

print("*" * largeur)            # Affiche autant d'etoile que le titre et rajoute en 11
print(titre.center(largeur))    # Affiche mon titre centré avec le même nombre de caractères que la variable largeur.
print("Oeufs a la coque : 3 minutes".center(largeur))
print("Oeufs mollets    : 6 minutes".center(largeur))
print("Oeufs durs       : 9 minutes".center(largeur))
print("*" * (len(titre) + 11))
print("")
print("")


print("Veuillez choisir votre cuisson")
print("Taper :")
print("a pour Oeufs a la coque \nb pour Oeufs mollets \nc pour Oeufs a la coque")
print("")

while True:
    choix_cuisson = input("Choix de la cuisson : ").strip().lower() # pour retirer les espaces et tout mettre en minuscules
    if choix_cuisson == "a" or choix_cuisson == "b" or choix_cuisson == "c":
        break
    print("ERREUR : Vous devez choisir a,b ou c")

temps_cuisson = {
    "a": TEMPS_COQUE,
    "b": TEMPS_MOLLETS,
    "c": TEMPS_DURS,
}

afficher_temps_restant(temps_cuisson[choix_cuisson])
















