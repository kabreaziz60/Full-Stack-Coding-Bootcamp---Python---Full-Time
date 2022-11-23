# Analysez le code ci-dessous. Quelle sera la sortie ?
#Reponse : la sortie retourne la valeur de x et de y
# Expliquer le but de la méthode `__init__()`
#Reponse : le but de la methode init est d' acceder a la valeur de x et de y

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
## create an instance of the class

p = Point(3,4)

## access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)