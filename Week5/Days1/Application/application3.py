# Analysez le code ci-dessous. Quelle sera la sortie ?
#Reponse :
# Apple
# I am a computer, my name is Mark
# <__main__.Computer object at 0x000002151E27BEE0>
# I am a computer, my name is Mark
# <__main__.Computer object at 0x000002151E27BEE0>



class Computer():

    def description(self, name):
        
        #This is a totally useless function
        
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")