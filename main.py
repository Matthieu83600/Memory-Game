import random
import time
import os

# Nettoyer écran
def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# Sequence => boucle gère 4 premiers chiffres
sequence = ""
for i in range (0, 4):
    chiffre = random.randint(0, 9)
    sequence += str(chiffre)

# Score du joueur
score = 0

print("Bienvenue dans le jeu du Simon")
print()
while True:
    print("Retenez la séquence")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()

    seq_utilisateur = input("Votre réponse : ")
    if seq_utilisateur == sequence:
        score += 1
    else:
        break
    ajout_chiffre = random.randint(0, 9)
    sequence += str(ajout_chiffre)
    clear_screen()

print("Mauvaise réponse")
print(f"La séquence était {sequence}")
print(f"Votre score final est : {score}")