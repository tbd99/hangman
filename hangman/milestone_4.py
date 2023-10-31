import random 

fruit_list = ['appple','pear','mango','peach','pineapple','peach'] #defines list of fruit, word to guess is chosen from here
#random_fruit = random.choice(fruit_list) #generates random word from fruit list, the word to be guessed

class Hangman():
    def __init__(self,fruit_list,num_lives=5):
        self.word = random.choice(fruit_list) #generate random word
        self.word_guessed = ['_'] * (len(self.word)) #create list containing '_' for each letter of the random word
        self.num_letters = len(set(list(self.word.strip()))) #no. of unique letters in a word, convert word to list of letters, convert to set to remmove duplicates, get length of set to get no of unique letters
        self.num_lives = num_lives #defines no of lives
        self.fruit_list = fruit_list #defines list of fruits
        self.list_of_guesses = [] #initialise empty list
    
    def check_guess(self,letter_guess): #def method to check if the guessed letter is in a word, pass guessed letter as arg
        letter_guess = letter_guess.lower() #convert guess to lower case 
        if letter_guess in self.word: #checks if the guessed letter is in the word 
           print(f"Good guess! {letter_guess} is in the word.") #prints if the letter is in the word
        else:
           print(f"Sorry, {letter_guess} is not in the word. Try again.") #prints if the letter is not in the word
        #return letter_guess
    def ask_for_input(self): #define function to get user input
        while 1 < 2: #creates infinite while loop
            letter_guess = input("Please enter a single letter ") #user input of letter guess 
            if len(list(letter_guess)) != 1 or (letter_guess.isalpha() == False): 
                print('Invalid letter. Please, enter a single alphabetical character')
            elif ((letter_guess in self.list_of_guesses) == True):
                print('You already tried that letter!')
            else:
                self.check_guess(letter_guess)
                self.list_of_guesses.append(letter_guess)
                #print(self.list_of_guesses)
               

        
        #return #letter_guess #returns guessed letter
    

my_hangman = Hangman(fruit_list)
my_hangman.ask_for_input()



