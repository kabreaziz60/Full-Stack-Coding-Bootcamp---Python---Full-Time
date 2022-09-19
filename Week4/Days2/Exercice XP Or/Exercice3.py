# Exercice 3 : Vérifier L'index
# Des Instructions
# Utilisation de cette variable
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Demander son nom à un utilisateur, si son nom est dans la liste des noms imprimer l'index de la première occurrence du nom.
# Example: if input is 'Cortana' we should be printing the index 

print("--Debut--")
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
nomN = input("Entrer votre nom : ")
for i in names :
    if nomN == i :
        print(names.index(i))