# Analysez le code ci-dessous. Quelle sera la sortie ?
# Reponse : la sortie est "Hello my name is John"

# Expliquer le but des méthodes
# reponse : la methode __init__ permet d'obtenir le nom et l'age de la personne 
#la methode show_dettaills permet d'afficher un message contenant le nom de la personne

# Créer une méthode qui modifie le nom de la personne


class Person():

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print("Hello my name is " + self.name)

  def modifie(self, new_name) :
    self.name = new_name
    print("Le nouveau nom est : "+ self.name)

first_person = Person("John", 36)
first_person.show_details()

first_person.modifie("aziz")