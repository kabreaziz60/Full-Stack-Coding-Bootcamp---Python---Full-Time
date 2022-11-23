#Defi 2

# Créez un programme qui imprime une liste des articles que vous pouvez acheter dans le magasin avec l'argent que vous avez dans votre portefeuille.
# Triez la liste par ordre alphabétique.
# Renvoyez "Rien" si vous ne pouvez rien acheter du magasin.

wallet = 2000
items_purchase = {
  "Water": 1,
  "Bread": 3,
  "TV": 1000,
  "Fertilizer": 20,
"Apple": 4,
  "Honey": 3,
  "Fan": 14,
  "Bananas": 4,
  "Pan": 100,
  "Spoon": 2
}
articlePayables = [article for article in items_purchase if items_purchase[article] <= wallet]
print(articlePayables)