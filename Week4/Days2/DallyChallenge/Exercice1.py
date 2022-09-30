# Défi 1
# Demandez à l'utilisateur un number et un length.
# Créez un programme qui imprime une liste de multiples de number jusqu'à ce que la longueur de la liste atteigne length.
# Exemples
# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

from tkinter import N


number = int(input("Entrer un entier : "))
long = int(input("Entrer une longeur : "))
liste = [number]
for i in range(2,long+1):
    ajout = number * i
    liste.append(ajout)
print(liste)