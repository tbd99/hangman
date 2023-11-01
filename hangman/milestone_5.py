import random 
fruit_list = ['pear','mango','orange','pineapple','peach'] #defines list of fruit, word to guess is chosen from here

class Hangman():
    '''
    This class represents a round of the game Hangman
    
    Attributes:
    word (str): The word to be guessed by the player
    word_guessed (list): A list containing underscores to represent the letters in the generated word
    num_letters (int): The number of unique letters in the word
    '''
    def __init__(self,fruit_list,num_lives=5):
        self.word = random.choice(fruit_list) #generate random word
        self.word_guessed = ['_'] * (len(self.word)) #create list containing '_' for each letter of the random word
        self.num_letters = len(set(list(self.word.strip()))) #no. of unique letters in a word, convert word to list of letters, convert to set to remmove duplicates, get length of set to get no of unique letters
        self.list_of_guesses = [] #initialise empty list
        self.num_lives = 5
    
    def check_guess(self,letter_guess): #def method to check if the guessed letter is in a word, pass guessed letter as arg
        '''
        This function is used to tell the player if the letter guessed is in the generated word.
        It prints a message depedning on if the letter guessed is in the word and tracks the number of lives remaining.
        '''
        letter_guess = letter_guess.lower() #convert guess to lower case 
        if letter_guess in self.word: #checks if the guessed letter is in the word 
           print(f"Good guess! {letter_guess} is in the word.") #prints if the letter is in the word
           self.num_letters = self.num_letters - 1  #reduce no of letters by 1     
           for letter in self.word: #loops over characters in word
               if letter_guess == letter: #if the guessed letter is a letter in the word
                   self.word_guessed[self.word.index(letter_guess)] = letter_guess #replace a "_" with the guessed letter at the correct position         
        else:
           self.num_lives = self.num_lives - 1 #reduces no of lives when an incorrect letter is guessed
           print(f"Sorry, {letter_guess} is not in the word. Try again.") #prints if the letter is not in the word
           print(f"You have {self.num_lives} lives left")
        return self.num_lives, self.num_letters
        
    def ask_for_input(self): #define function to get user input
        '''
        This function asks for the user to input a letter, which is a guess in the hangman game
        The function checks that the input is valid and tracks which letters have been guessed already
        '''
        while True: #creates infinite while loop
            letter_guess = input("Please enter a single letter ") #user input of letter guess 
            if len(list(letter_guess)) != 1 or (letter_guess.isalpha() == False): #if the input is not a single alphabetical character
                print('Invalid letter. Please, enter a single alphabetical character')
            elif ((letter_guess in self.list_of_guesses)== True): #if the letter has already been guessed
                print('You already tried that letter!')
            else:
                self.check_guess(letter_guess) #calls the check_guess method on the guessed letter
                self.list_of_guesses.append(letter_guess) #appends guessed letter to list of guessed letters
               
        



def play_game(word_list):
   #num_lives = 5
   game = Hangman(word_list) #,num_lives)
   num_lives = game.num_lives
   #print(num_lives)
   num_letters = game.num_letters
   #print(num_letters)

   while True:
       if num_lives == 0:
           print('You lost!')
           break
       elif num_lives > 0:
           game.ask_for_input()
           #print(num_lives)
           #break
       elif num_lives != 0 and num_letters <= 0:
           print('Congratulations, you won the game!')
           break

   return

play_game(fruit_list)





