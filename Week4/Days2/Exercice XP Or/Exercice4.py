# Exercice 4 : Le Plus Grand Nombre
# Des Instructions
# Demandez à l'utilisateur 3 chiffres et imprimez le plus grand nombre.
#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87
#     The greatest number is: 87

print("---Début---")

nb1 = int(input("Entrer le Premier nombre : "))
max = nb1
nb2 = int(input("Entrer le Deuxieme nombre : "))
if nb2 > max :
    max = nb2
nb3 = int(input("Entrer lr Troixieme nombre : ")) 
if nb3 > max :
    max = nb3
print("Le plus grand des trois nombre : ",max)
