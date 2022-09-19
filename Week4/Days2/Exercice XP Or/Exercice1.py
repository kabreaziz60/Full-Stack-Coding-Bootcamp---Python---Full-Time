# Exercice 1 : Concaténer Des Listes
# Des Instructions
# Écrivez du code qui concatène deux listes sans utiliser le +signe.

from operator import concat


print("--Début--")

list1 = ["Aziz","Abdoul","KABRE"]
list2 =["30","01","99"]
grandlist = concat(list1,list2)
print(grandlist)
