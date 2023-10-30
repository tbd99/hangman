#code to iteratively check if the input is a valid guess 

while 1 < 2: #creates infinite while loop
    letter_guess = input("Please enter a single letter ") #user input of letter guess 
    if len(list(letter_guess)) == 1 and letter_guess.isalpha(): #breaks out the loop if the letter guess is a single alphabetical character
        break 
    else:
        print('Invalid letter. Please, enter a single alphabetical character') #otherwise prints this message and while loop continues until a valid input is given 
import random 

fruit_list = ['appple','pear','mango','peach','pineapple'] #defines list of fruits
print(fruit_list)

random_fruit = random.choice(fruit_list) #generates random word from given list
