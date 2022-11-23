# Des Instructions
# En cryptographie, un chiffrement de César est l'une des techniques de chiffrement les plus simples et les plus connues.
# C'est un type de chiffrement par substitution dans lequel chaque lettre du texte en clair est remplacée par une lettre à un nombre fixe de positions dans l'alphabet.

# Par exemple, avec un décalage à gauche de 3 –> D serait remplacé par A ,
# –> E deviendrait B, et ainsi de suite.

# La méthode porte le nom de Jules César, qui l'a utilisée dans sa correspondance privée.

# Créez un programme python qui crypte et décrypte les messages avec le chiffrement césar.
# L'utilisateur entre dans le programme, puis le programme lui demande s'il veut chiffrer ou déchiffrer, puis exécuter le chiffrement/déchiffrement sur un message donné et un décalage donné.
from tkinter.messagebox import QUESTION
from xml.sax.xmlreader import InputSource


print (" DEbut de decriptage")

messages = input("Entrer un message")
question =input("Voulez")
cypher_text=""
text_decrip=""
for letter in messages:
    cypher_text += chr(ord(letter) + 3)
    text_decrip += chr(ord(letter)-3)
print(cypher_text)

