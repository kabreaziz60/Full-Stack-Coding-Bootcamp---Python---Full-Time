# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.



# Exercise 1 – Random Sentence Generator
#1..2..3
# Dict
# def get_words_from_file():
#     with open('mot.txt') as f:
#         mot = {}
#         for line in f:
#             if line[0] in mot :
#                 mot.update({line[0] : mot[line[0]]+' '+line[0:len(line)-1]})
#             else:
#                 mot.update({line[0] : line})
#     return mot

#list
def get_words_from_file():
    with open('mot.txt') as f:
        mot = []
        for line in f:
            mot.append(line[0:len(line)-1])
    return mot
#4
def get_random_sentence(length=6):
    import random
    sentence = ""
    mots = get_words_from_file()
    for x in range (0,length):
        sentence += mots[random.randint(0,len(mots))] + ' '
    return sentence


#5
# mot = get_random_sentence().lower()
# print(mot)

#6
def main():
    print("\nCe programme génère une phrase pour vour.\n"
          "C'est à vous de spécifier la taille de la phrase.\n")
    length = int(input('Entrez la taille (2 à 20) : '))
    if length >= 2 and length <= 20:
        print(get_random_sentence(length))
    else:
        print('Error')

main()

