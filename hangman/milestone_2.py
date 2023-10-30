#task 1 - define the list of possible words 
#task 2 - choose a random word from the list

import random 

fruit_list = ['appple','pear','mango','peach','pineapple'] #defines list of fruits
print(fruit_list)

random_fruit = random.choice(fruit_list) #generates random word from given list
print(random_fruit)

#task 3 - ask the user for an input 
letter_guess = input("Please enter a single letter ")
print(letter_guess)

#task 4 - check that the input is a single character
if len(list(letter_guess)) == 1 and letter_guess.isalpha(): #check that the input is one character and is alphabet
    print('Good guess!')

else:
    print('Oops! That is not a valid input.') #print if conditions are not met