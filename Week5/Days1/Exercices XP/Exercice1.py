# 🌟 Exercice 1 : Chats
# Des Instructions
# Utilisation de cette classe

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instanciez trois Catobjets à l'aide du code fourni ci-dessus.
# En dehors de la classe, créez une fonction qui trouve le chat le plus ancien et renvoie le chat.
# Imprimez la chaîne suivante : "Le chat le plus âgé est <cat_name>, et a <cat_age>ans.". Utilisez la fonction précédemment créée.
liste =[]
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


def older():
    chat_1 = Cat("bibi",5)
    chat_2 = Cat("milou",7)
    chat_3 = Cat("miyo",9)
    age_chat=[chat_1.age,chat_2.age,chat_3.age]
    max_age = age_chat[0]
    for i in range(0,len(age_chat)):
        if age_chat[i] >max_age:
            max_age = age_chat[i]   
    print("le plus agé a",max_age,"ans")


print(older())