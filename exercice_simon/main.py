import random
import time
import os

score = 0
sequence_memoire = ""

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')



for i in range (0,4):
    sequence_initial = (random.randint(0,9))
    sequence_memoire= str(sequence_memoire) + str(sequence_initial)

while True :
    print("Retenez la séquence")
    time.sleep(1)
    clear_screen()

    print(sequence_memoire, end="")
    time.sleep(3)
    clear_screen()

    votre_reponse = input("Votre reponse : ")
    print()

    if votre_reponse == sequence_memoire:
        score += 1
        sequence_memoire = sequence_memoire + str(random.randint(0, 9))
        print("Bonne reponse votre score est : " + str(score))
        time.sleep(1)
        clear_screen()
    else:
        print("Mauvaise réponse, la séquence était : " + str(sequence_memoire) )
        print("Votre score final est : " +str(score))
        break




















