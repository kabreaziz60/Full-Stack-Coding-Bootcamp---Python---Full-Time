# Exercice 5 : L'alphabet
# Des Instructions
# Créer une chaîne de toutes les lettres de l'alphabet
# Faites une boucle sur chaque lettre et imprimez un message qui contient la lettre et si c'est une voyelle ou une consonne.

from sys import setswitchinterval


print("---Début---")

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabet))
for i in alphabet :
    if i=="a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y" :
        print(i,"est une voyelle")
    else :
        print(i,"est une consone")

