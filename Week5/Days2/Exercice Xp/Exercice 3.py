# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.



# Exercice 3 : Chiens Domestiqués
from Exercice2 import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(f"{self.bark()}")

    def play(self, *args):
        mot = self.name + ", "
        for i in range(0, len(args)):
            if i == len(args) - 1:
                mot += args[i]
            elif i == len(args) - 2:
                mot += args[i] + " et "
            else:
                mot += args[i] + ", "
        print(f"{mot}, all play together")

    def do_a_trick(self):
        import random
        if self.trained == True:
            alea = random.randint(1, 4)
            if alea == 1:
                print(f"{self.name} fait un tonneau")
            elif alea == 2:
                print(f"{self.name} se dresse sur ses pattes arrière")
            elif alea == 3:
                print(f"{self.name} te serre la main")
            else:
                print(f"{self.name} fait le mort")
        else :
            print("It can't")

print("\n")
dog1 = PetDog('sifu', 1, 30, False)
dog2 = PetDog('rufus', 5, 25, True)
dog3 = PetDog('triou', 10, 40, True)

dog1.train()
dog2.play(dog1.name,dog2.name)
dog3.do_a_trick()
dog3.do_a_trick()
dog1.do_a_trick()