import random 


fruit_list = ['pear','apple','mango','orange','pineapple','peach'] #defines list of fruit, word to guess is chosen from here


class Hangman():
    '''
    This class represents a round of the game Hangman
    
    Attributes:
    word (str): The word to be guessed by the player
    word_guessed (list): A list containing underscores to represent the letters in the generated word
    num_letters (int): The number of unique letters in the word
    list_of_guesses (list): empty list to be filled with letter guesses
    num_lives (int): number of lives the player has
    '''
    def __init__(self,fruit_list,num_lives=5):
        self.word = random.choice(fruit_list) 
        self.word_guessed = ['_'] * (len(self.word)) 
        self.num_letters = len(set(list(self.word.strip())))
        self.list_of_guesses = [] 
        self.num_lives = 5 
    
    def _check_guess(self,letter_guess): 
        '''
        This function is used to tell the player if the letter guessed is in the generated word.
        It takes the guessed letter as an argument and prints a message depedning on if the letter guessed is in the word and tracks the number of lives remaining.
        '''
        letter_guess = letter_guess.lower() #convert guess to lower case 
        if letter_guess in self.word: #checks if the guessed letter is in the word 
           print(f"Good guess! {letter_guess} is in the word.") 
           self.num_letters = self.num_letters - 1  #reduce no of letters by 1     
           for letter in self.word: #loops over characters in word
               if letter_guess == letter: 
                   self.word_guessed[self.word.index(letter_guess)] = letter_guess #replace a "_" with the guessed letter at the correct position         
        else:
           self.num_lives = self.num_lives - 1 #reduces no of lives when an incorrect letter is guessed
           print(f"Sorry, {letter_guess} is not in the word. Try again.") 
           print(f"You have {self.num_lives} lives left")
        return self.num_lives, self.num_letters 
        
    def ask_for_input(self): 
        '''
        This function asks for the user to input a letter, which is a guess in the hangman game
        The function checks that the input is valid and appends to list_of_guesses to track which letters have been guessed already
        '''
        while True: #creates infinite while loop
            letter_guess = input("Please enter a single letter ") 
            if len(list(letter_guess)) != 1 or (letter_guess.isalpha() == False): #if the input is not a single alphabetical character
                print('Invalid letter. Please, enter a single alphabetical character')
            elif ((letter_guess in self.list_of_guesses)== True): #if the letter has already been guessed
                print('You already tried that letter!')
            else:
                self._check_guess(letter_guess) #calls the check_guess method on the guessed letter
                self.list_of_guesses.append(letter_guess) #appends guessed letter to list of guessed letters
                break 

               
        
def play_game(word_list):
   '''
   This functions defines a round of the game hangman, taking a list of words as an argument
   The function creates an instance of the hangman class and works out the outcome of the game based on user input
   It will print whether the user has guessed the word or lost the game.
   '''
   game = Hangman(word_list) #initialise an instance of the hangman class 
  
   while True: #creates infinite while loop
       if game.num_lives == 0: #if all lives have been used
           print('You lost!') 
           break
       elif game.num_lives != 0 and game.num_letters <= 0: #if the user has lives remaining and has guessed all the letters in the word
           print(f'Congratulations, you won the game!, the word was {game.word}!') 
           break
       elif game.num_lives > 0: #if win/loss hasnt been determined yet, continue to ask for user input to guess the letters
           game.ask_for_input()
          
   return


play_game(fruit_list) #initialise an instance of the play_game class to start the game 






