# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.




class Family:

    def __init__(self,last_name):
        self.last_name = last_name
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]

    def born(self, **kwargs):
        info = {
        }
        for x in kwargs:
            info.update({x : kwargs[x]})
        self.members.append(info)

    def is_18(self,name):
        for membre in self.members:
            if name == membre['name']:
                if membre['age'] > 18:
                    return True
                else:
                    return False
        return False

    def family_presentation(self):
        print(self.last_name)
        i = 1
        for membre in self.members:
            print(i,":",membre['name'])
            i+=1

fama = Family("SAWADOGO")
fama.born(name = 'Sss', age = 15, gender = 'Male', is_child=True)
fama.born(name = 'Sah', age = 2, gender = 'Female', is_child=True)
print(fama.is_18('Sarah'))
print(fama.is_18('Sah'))
fama.family_presentation()

