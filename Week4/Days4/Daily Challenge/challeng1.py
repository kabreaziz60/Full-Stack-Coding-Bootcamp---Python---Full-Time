#Defi 1


#Demander un mot à un utilisateur
# Écrivez un programme qui crée un dictionnaire. Ce dictionnaire stocke les index de chaque lettre dans une liste.

# Assurez-vous que les lettres sont les clés.
# Assurez-vous que les lettres sont des chaînes.
# Assurez-vous que les index sont stockés dans une liste et que ces listes sont des valeurs.

sortie = {}
mot = input("Veillez saisir un mot : ")
for i in range(len(mot)):
  if mot[i] in sortie :
    sortie[mot[i]].append(i)
  else :
    sortie[mot[i]] = [i]
print(sortie)





