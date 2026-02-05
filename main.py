
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




option_un = "1"
option_deux = "2"

unpouce = 2.54
uncm = 0.394
taillemini_cm = 43
taillemini_pouce = 17


reponse_str = input(
    "Vous souhaitez convertir de pouce vers centimetre ? Tapez "
    + option_un
    + ". ou de centimetre vers pouce ? Tapez "
    + option_deux
    + " : "
)


if reponse_str == option_un:
    while True:
        choix_un = input("Rentrer la valeur à convertir en pouce vers centimetre : ")

        try:
            choix_un_float = float(choix_un)
        except ValueError:
            print("Veuillez entrer un nombre valide")
        else:
            choix_un_resultat = round(choix_un_float * unpouce, 2)

            if choix_un_resultat < taillemini_cm:
                print(
                    "Resultat : " + choix_un + " pouces = "
                    + str(choix_un_resultat)
                    + " cm vous devez atteindre au moins "
                    + str(taillemini_cm) + " cm "
                )
            else:
                print(
                    "Resultat : " + choix_un + " pouces = "
                    + str(choix_un_resultat)
                    + " cm vous avez atteint le minimum demandé "
                )
                break


elif reponse_str == option_deux:
    while True:
        choix_deux = input("Rentrer la valeur à convertir en centimetre vers pouce : ")

        try:
            choix_deux_float = float(choix_deux)
        except ValueError:
            print("Veuillez entrer un nombre valide")
        else:
            choix_deux_resultat = round(choix_deux_float * uncm, 2)

            if choix_deux_resultat < taillemini_pouce:
                print(
                    "Resultat : " + choix_deux + " cm = "
                    + str(choix_deux_resultat)
                    + " pouces vous devez atteindre au moins "
                    + str(taillemini_pouce) + " pouces "
                )
            else:
                print(
                    "Resultat : " + choix_deux + " cm = "
                    + str(choix_deux_resultat)
                    + " pouces vous avez atteint le minimum demandé "
                )
                break


else:
    print("Veuillez choisir " + option_un + " ou " + option_deux)