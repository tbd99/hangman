
import random 

fruit_list = ['appple','pear','mango','peach','pineapple','peach'] #defines list of fruit, word to guess is chosen from here
random_fruit = random.choice(fruit_list) #generates random word from fruit list, the word to be guessed



def check_guess(letter_guess): #def function to check if the guessed letter is in a word, pass guessed letter as arg
    letter_guess = letter_guess.lower() #convert guess to lower case 
    if letter_guess in random_fruit: #checks if the guessed letter is in the word (defined outside the function)
       print(f"Good guess! {letter_guess} is in the word.") #prints if the letter is in the word
    else:
       print(f"Sorry, {letter_guess} is not in the word. Try again.") #prints if the letter is not in the word
    return 


def ask_for_input(): #define function to get user input
   while 1 < 2: #creates infinite while loop
    letter_guess = input("Please enter a single letter ") #user input of letter guess 
    if len(list(letter_guess)) == 1 and letter_guess.isalpha(): #breaks out the loop if the letter guess is a single alphabetical character
        break 
    else:
        print('Invalid letter. Please, enter a single alphabetical character') #otherwise prints this message and while loop continues until a valid input is given 

   check_guess(letter_guess) #calls check_guess function within this function 
   return letter_guess #returns guessed letter



ask_for_input() #calls function defined above



