import random 

fruit_list = ['appple','pear','mango','peach','pineapple','peach'] #defines list of fruit, word to guess is chosen from here
#random_fruit = random.choice(fruit_list) #generates random word from fruit list, the word to be guessed

class Hangman():
    def __init__(self,fruit_list,num_lives=5):
        self.word = random.choice(fruit_list) #generate random word
        self.word_guessed = ['_'] * (len(self.word)) #create list containing '_' for each letter of the random word
        self.num_letters = len(set(list(self.word.strip()))) #no. of unique letters in a word, convert word to list of letters, convert to set to remmove duplicates, get length of set to get no of unique letters
        self.num_lives = num_lives #defines no of lives
        fruit_list.self = fruit_list #defines list of fruits
        self.list_of_guesses = [] #initialise empty list
    
    def check_guess(letter_guess): #def method to check if the guessed letter is in a word, pass guessed letter as arg
        letter_guess = letter_guess.lower() #convert guess to lower case 
        if letter_guess in random_fruit: #checks if the guessed letter is in the word (defined outside the function)
           print(f"Good guess! {letter_guess} is in the word.") #prints if the letter is in the word
        else:
           print(f"Sorry, {letter_guess} is not in the word. Try again.") #prints if the letter is not in the word
        return 
 



