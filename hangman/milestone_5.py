import random

from milestone_3 import word_list   #word list was defined in previous milestone

#print(word_list)

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word) #TODO not sure if word or self.word needed here
#TODO the previous line does not account for when some letters guessed already
        self.num_letters = len(set(self.word)) 
        self.list_of_guesses = [] #a list of guesses that have already been tried. initially set to an empty list

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            print(self.word_guessed)
            self.num_letters -=1 # we reduce the set of unique unguessed letters by 1, to track when all letters have been guessed (and game has been won)
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
       

    def ask_for_input(self):
        #while True:     #TODO I MADE THIS # AND GAME NOW WORKS!!! BECAUSE WE HAD TWO WHILE TRUE LOOPS
            guess = input("Please enter a single letter: ")

            #check if input is 1 character long and that the character is alphabetical
            #if it isn't 1 letter long or isn't alphabetical print an error message
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetical character.") 

            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess) #call for check_guess method
                self.list_of_guesses.append(guess) #add last guess to list with already guessed letters

def play_game(word_list):
    num_lives = 5
    print("In this game of Hangman, you will try to guess a fruit. You have 5 lives left. Good luck!")
    game = Hangman(word_list, num_lives)
    print(game.word_guessed)

    while True:
        if game.num_lives == 0:
           print("You lost!")
           break
        else:
            if game.num_letters == 0:
                print("Congratulations. You won the game!")
                break
            else:
                game.ask_for_input()
           
play_game(word_list)
        
      
       