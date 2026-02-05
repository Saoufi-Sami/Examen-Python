
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







option_un = "pouce vers centimetre"
option_deux = "centimetre vers pouce"

unpouce = 2.54
uncm = 0.394



reponse_str = input("Vous souhaitez convertir de " + option_un + " ou de " + option_deux + " ? ")


if reponse_str == option_un:
    choix_un = input("Rentrer la valeur à convertir en  " + option_un + " : " )
    choix_un_float = float(choix_un)
    choix_un_resultat = round(choix_un_float * unpouce,2)
    print("Resultat : " + choix_un + " pouces = " + str(choix_un_resultat) + " cm ")



elif reponse_str == option_deux:
    choix_deux = input("Rentrer la valeur à convertir en " + option_deux + " : ")
    choix_deux_float = float(choix_deux)
    choix_deux_resultat = round(choix_deux_float * uncm,2)
    print("Resultat : " + choix_deux + " cm = " + str(choix_deux_resultat) + " pouces")

else:
    print("Veuillez choisir " + option_un + " ou " + option_deux )
