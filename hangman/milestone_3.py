#code to iteratively check if the input is a valid guess 
import random 

fruit_list = ['appple','pear','mango','peach','pineapple'] #defines list of fruits
random_fruit = random.choice(fruit_list) #generates random word from given list
print(random_fruit) #sensecheck

#define function to check if the guessed letter is in a word 
def check_guess(letter_guess): #pass guessed letter and random word as arguments
    letter_guess = letter_guess.lower() #convert guess to lower case 
    if letter_guess in random_fruit: #checks if the guessed letter is in the word, defined outside the function
       print(f"Good guess! {letter_guess} is in the word.") #prints if the letter is in the word
    else:
       print(f"Sorry, {letter_guess} is not in the word. Try again.") #prints if the letter is not in the word
    return 

#define function to get user input
def ask_for_input():
   while 1 < 2: #creates infinite while loop
    letter_guess = input("Please enter a single letter ") #user input of letter guess 
    if len(list(letter_guess)) == 1 and letter_guess.isalpha(): #breaks out the loop if the letter guess is a single alphabetical character
        break 
    else:
        print('Invalid letter. Please, enter a single alphabetical character') #otherwise prints this message and while loop continues until a valid input is given 

   check_guess(letter_guess)
   return letter_guess


ask_for_input() #call function



