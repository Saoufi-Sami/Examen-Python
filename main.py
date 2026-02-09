# Correction
# Pour cet exercice, vous allez créer un programme de conversion d'unités,
# capable de convertir des pouces (inch) en centimètres (cm), et inversement.
#
# Rappels :
# 1 pouce = 2.54 cm
# 1 cm = 0.394 pouces
#
# Exemple :
# Un écran de 17 pouces de diagonale correspond à 43,18 cm (17 * 2.54)
#
# Comportement attendu du programme :
# 1 - Demander à l'utilisateur s'il souhaite convertir :
#     - de pouces vers centimètres
#     - ou de centimètres vers pouces
# 2 - Demander à l'utilisateur de saisir la valeur à convertir
#     (en réaffichant l’unité demandée)
# 3 - Afficher la valeur convertie avec l'unité correspondante (cm ou pouces)
# - Fin du programme

#Optionnel :
#Boucler pour convertir plusieurs valeurs (en conservant toujours le même sens de conversion)
# et proposer une option pour sortir du programme.


# Cette fonction effectue la conversion de unit 1 vers unit 2
# return True : l'utilisateur ne veut plus convertir et on sort du programme
# return False l'utilisateur donne une valeur a  convertir

def demander_et_afficher_conversion(unit1, unit2, facteur):
    valeur_str = input(f"Conversion {unit1}-> {unit2}. Donnez la valeur en {unit1} ou 'q' pour quitter: ")
    if valeur_str == "q":
        return True
    valeur_float = float(valeur_str)
    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"Résultat de la conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}")
    return False



while True :
    # Menu : choix de la conversion
    print("Ce programme vous permet dreffectuer des conversions d'unités")
    print("1 - Pouces vers cm")
    print("2 - cm vers pouces")
    choix = input("vVotre choix (1 ou 2): ")
    if choix == "1" or choix == "2":
        break
    print("ERREUR : Vous devez choisir 1 ou 2")

while True:
    # Demander les valeurs à convertir a l'utilisateur
    if choix == "1":
        if demander_et_afficher_conversion("pouces", "cm", 2.54):
            break

            # On vérifie d'abord le choix (1 ou 2).
            # Ensuite seulement, dans la fonction appelée, on demande la valeur ou 'q' pour quitter.
            # Si la fonction retourne True (q), on sort de la boucle.
            # Sinon, la fonction continue son exécution et passe aux instructions suivantes
            # (conversion, affichage du résultat), puis la boucle recommence.


    # En Python, un `if fonction():` teste automatiquement si le retour vaut True
    # (comme s’il y avait un `== True` invisible).
    # Si la fonction retourne True, l’action du if s’exécute (ici : break).
    # Dans ce programme, quand l’utilisateur tape 'q', la fonction retourne True,
    # donc le if voit True et déclenche le break.
    # Si la fonction retourne False et qu’il n’y a pas de else,
    # le programme continue simplement son exécution.

    if choix == "2":
        if demander_et_afficher_conversion("cm", "pouces", 0.394):
            break


























