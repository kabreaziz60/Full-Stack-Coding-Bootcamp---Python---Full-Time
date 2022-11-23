# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:

# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]


# 2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# 3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.


# 4. Call the incredible_presentation method.
# 5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# 6. Call the incredible_presentation method again.








# Exercice 2 : La Famille Des Indestructibles
from Exercice1 import Family
class TheIncredibles(Family):
    def __init__(self,lastname):
        super().__init__(lastname)
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly',
             'incredible_name': 'MikeFly'},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
             'incredible_name': 'SuperWoman'}
        ]
    def use_power(self, name):
        for membre in self.members:
            if name == membre['name']:
                if membre['age'] > 18:
                    print(f"{membre['power']}")
                else :
                    raise Exception(f"{name} n'a pas plus de 18 ans")
            else:
                print(f"{name} n'est pas membre de cette famille")

    def incredible_presentation(self):
        super().family_presentation()
        print('\nChaque membre à comme pouvoir : ')
        i = 1
        for membre in self.members:
            print(i,':',membre['power'])
            i += 1

fama = TheIncredibles("NARE")
fama.born(name = 'Jack', age = 5, gender = 'Male', is_child=True, power = 'Unknown Power', incredible_name= 'Baby')
fama.born(name = 'Marie', age = 15, gender = 'Female', is_child=True, power = 'Speak to animals', incredible_name= 'SuperWoman')
fama.incredible_presentation()
