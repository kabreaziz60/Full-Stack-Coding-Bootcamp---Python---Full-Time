# 🌟 Exercise 2: Currencies
# Instructions
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     #Your code starts HERE


# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>








# Exercice 2 : Devises
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount > 1 :
            return f"{self.amount} {self.currency}s"
        else :
            return f"{self.amount} {self.currency}"

    def __repr__(self):
        if self.amount > 1 :
            return f"{self.amount} {self.currency}s"
        else :
            return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        a=True
        try :
            if self.currency == other.currency :
                print(self.amount + other.amount)
                return Currency(self.currency,self.amount + other.amount)
            else :
                a=False
        except :
            if a :
                print(self.amount + other)
                return Currency(self.currency,self.amount + other)
        if not a :
            raise TypeError("Cannot add between Currency type <dollar> and <shekel>")




c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))

print(int(c1))

print(repr(c1))

c1 + 5

c1 + c2

print(c1)

c1 += 5

print(c1)

c1 += c2

print(c1)