# 🌟 Exercice 3 : Zara
# Des Instructions
# Voici quelques informations sur une marque.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green
# 2. Créez un dictionnaire appelé brand dont la valeur correspond aux informations de la première partie (transformez les informations en clés et valeurs ).
# 3. Modifiez le nombre de magasins à 2.
# 4. Imprimez une phrase qui explique qui sont les clients de Zaras.
# 5. Ajoutez une clé appelée country_creation avec une valeur de Spain.
# 6. Vérifiez si la clé international_competitorsest dans le dictionnaire. Si c'est le cas, ajoutez le magasin Desigual .
# 7. Supprimez les informations sur la date de création.
# 8. Imprimez le dernier concurrent international.
# 9. Imprimez les principales couleurs de vêtements aux États-Unis.
# 10. Imprimez le nombre de paires clé-valeur (c'est-à-dire la longueur du dictionnaire).
# 11. Imprimez les clés du dictionnaire.
# 12. Créez un autre dictionnaire appelé more_on_zaraavec les détails suivants :
# creation_date: 1975 
# number_stores: 10 000
# 13. Utilisez une méthode pour ajouter les informations du dictionnaire more_on_zaraau dictionnaire brand.
# 14. Imprimer la valeur de la clé number_stores. Qu'est-ce qui vient juste de se passer ?



brand = {
    'name':'Zara',
    'creation_date':1975 ,
    'creator_name':'Amancio Ortega Gaona',
    "type_of_clothes":['men', 'women', 'children', 'home'],
    'international_competitors':['Gap', 'H&M', 'Benetton'],
    'number_stores': 2,
    'major_color':{
        'France':'blue', 
        "Spain": "red",
        "US": ['pink', 'green']},
},
