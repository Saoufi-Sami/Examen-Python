
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
