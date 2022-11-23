# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.





# 1. Create a class called Dog.
class Dog :
    def __init__(self, name, height) :
        self.name = name
        self.height = height
# 2. In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.

    def bark(self) :
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jump {self.height*2} cm high!")

davids_dog = Dog("Rex",50)
print(f"Chien de David: {davids_dog.name} and have {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()
print("\n")

sarahs_dog = Dog("Teacup", 20)
print(f"Chien de Sarah: {sarahs_dog.name} and have {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

print("\n")
if sarahs_dog.height > davids_dog.height:
    print(f"Chien de Sarah: {sarahs_dog.name}")
else:
    print(f"Chien de David: {davids_dog.name}")