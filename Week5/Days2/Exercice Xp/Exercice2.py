# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.


# Exercice 2 : Chiens
#1...2
class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight/(self.age*10)

    def fight(self,other_dog):
        if self.run_speed() > other_dog.run_speed():
            print(f'{self.name} is a winner')
        else :
            print(f'{other_dog.name} is a winner')

#3
dog1 = Dog('sifu',1,30)
dog2 = Dog('rufus',5,25)
dog3 = Dog('triou',10,40)

print(f'{dog1.run_speed()} m/s.')
dog2.fight(dog3)