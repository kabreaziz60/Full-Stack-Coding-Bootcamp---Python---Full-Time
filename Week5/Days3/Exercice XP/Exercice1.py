# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.



# Exercice 1 : Fonctions Intégrées
#2
class Info:
    def __init__(self):
        #1
        print(abs(4.5))
        print(int("7"))
        print(input('Appuyer sur Entrer'))

    def __doc__(self):
        return "Ce programme imprime des résultats"

info = Info()
print(info.__doc__())

