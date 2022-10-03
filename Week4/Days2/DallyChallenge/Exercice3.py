# Des Instructions
# Demandez à l'utilisateur sa date de naissance (précisez le format, par exemple : DD/MM/YYYY).
# Présentez un petit gâteau comme ci-dessous :
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# Le nombre de bougies sur le gâteau doit être le dernier numéro de l'âge des utilisateurs, s'ils ont 53 ans, puis ajoutez 3 bougies.

# Bonus : S'ils sont nés une année bissextile, affichez deux gâteaux !

from timeit import repeat


Date = input("Entrer votre date de naissance (Ex : 30/01/2003) : ")
print(Date)
nbb = Date[1]
nbb = int(nbb)
ann = Date[6:11]
ann = int(ann)
print(ann)
bougi = ""
i=1
while i <= nbb :
    bougi = bougi +"i"
    i = i+1
print("___{nb}___".format(nb=bougi))
print("|:H:a:p:p:y:|")
print("__|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")

if ann % 4 ==0 and ann % 100 != 0 or ann % 400 == 0 :
    print("___{nb}___".format(nb=bougi))
    print("|:H:a:p:p:y:|")
    print("__|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")


