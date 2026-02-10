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

print("Retenez la séquence" )

for i in range (0,4):
    sequence_initial = (random.randint(0,9))
    print(sequence_initial,end="" )
    sequence_memoire= str(sequence_memoire) + str(sequence_initial)
print()
time.sleep(3)
clear_screen()

votre_reponse = input("Votre reponse : ")