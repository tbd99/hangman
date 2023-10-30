#task 1 - define the list of possible words 
#task 2 - choose a random word from the list

import random 

word_list = ['appple','pear','mango','peach','pineapple'] #defines list of fruits
print(word_list)

word = random.choice(word_list) #generates random word from given list
print(word)

#task 3 - ask the user for an input 
guess = input("Please enter a single letter ")
print(guess)
