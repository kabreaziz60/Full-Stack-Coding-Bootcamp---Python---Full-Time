# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)


#Exercice 4 : Après-Midi Au Zoo
class Zoo :
    def __init__(self,zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        list(map(lambda x : print(x),self.animals))

    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        ani = sorted(self.animals)
        animal ={}
        animal.update({1:ani[0]})
        j=2
        for i in range(1,len(ani)) :
            if ani[i][0] == ani[i-1][0] :
                animal.update({j-1: animal[j-1]+[ani[i]]})
            else :
                animal.update({j: [ani[i]]})
                j+=1
        return animal

    def get_groups(self,animal,animaux):
        print(f"{animal}/")
        for x in animaux :
            if animal[0] == animaux[x][0][0] :
                print(f"{animaux[x]}")


ramat_gan_safari = Zoo("sss")

while True :
    ani = input("Which animal should we add to the zoo ? : ")
    if ani.lower() != "exit" :
        ramat_gan_safari.add_animal(ani)
    else:
        break
    print("Entrez 'exit' pour quitter")

ramat_gan_safari.get_animals()
print("\n")

while True :
    ani = input("Which animal should we delete to the zoo ? : ")
    if ani.lower() != "exit" :
        ramat_gan_safari.sell_animal(ani)
    else :
        break
    print("Entrez 'exit' pour quitter")

ramat_gan_safari.get_animals()
print("\n")

animals = ramat_gan_safari.sort_animals()
print(animals)
print('\n')

animal = input("Entrez le nom d'un animal existant : ")
ramat_gan_safari.get_groups(animal,animals)