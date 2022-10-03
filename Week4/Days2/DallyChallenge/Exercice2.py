# Défi 2
# Écrivez un programme qui demande une chaîne à l'utilisateur et affichez une nouvelle chaîne avec toutes les lettres consécutives en double supprimées.
# Exemples
# user's word : "ppoeemm" ➞ "poem"
# user's word : "wiiiinnnnd" ➞ "wind"
# user's word : "ttiiitllleeee" ➞ "title"
# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Remarques
# Les chaînes finales n'incluront pas les mots avec des lettres doubles (par exemple « passant », « loterie »).

from os import remove


chaine = input("Entrer une chaine de caractere : ")
liste= []
for i in chaine :
    liste.append(i)
    nliste = set(liste)
liste = list(set(liste))
mot ="".join(liste)
print(mot)

