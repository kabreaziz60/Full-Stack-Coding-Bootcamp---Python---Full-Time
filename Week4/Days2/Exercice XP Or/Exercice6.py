# Exercice 6 : Mots Et Lettres
# Des Instructions
# Demandez à un utilisateur 7 mots, stockez-les dans une liste nommée words.
# Demandez à l'utilisateur un seul caractère, stockez-le dans une variable appelée letter.
# Bouclez dans la wordsliste et imprimez l'index de la première apparition de la lettervariable dans chaque mot de la liste.
# Si la lettre n'existe pas dans l'un des mots, imprimez un message amical avec le mot et la lettre.
from operator import index


print("--Début--")
words = []
for i in range(1,8) :
    nmb = input("Entrer un mot : ")
    words.append(nmb)
print(words)
latter = input("Entrer un choiffre : ")
print(latter)
for i in words :
    eleme = i
    for j in eleme :
        if latter == j :
            print("lindex de ",j, "dans", eleme ,"est : ",eleme.index(j))
        else :
            print("aucun mot trouver")


