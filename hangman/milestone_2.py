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

#task 4 - check that the input is a single character
if len(list(guess)) == 1 and guess.isalpha(): #check that the input is one character and is alphabet
    print('Good guess!')

else:
    print('Oops! That is not a valid input.') #print if conditions are not met