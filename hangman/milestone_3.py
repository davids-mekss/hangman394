import random

#Define a list of words from which computer will chose a random one
word_list = ["mango", "blueberry", "banana", "apple", "persimmon"]
print(word_list)


word = random.choice(word_list) #Picks a random word from the list
print(word)
#TODO IN FINAL IMPLEMENTATION WE SHOULD NOT SHOW THE WORD TO BE GUESSED TO USER
# THIS IS FOR TESTING PURPOSES ONLY

#define a function that asks for user to input their letter guess
def ask_for_input():
    
    while True:     # will run forever until a valid entry is provided in input
        guess = input("Please enter a single letter: ")

        if len(guess) == 1 and guess.isalpha(): #check if input is 1 character long and that the character is alphabetical
            print("Good guess!") #TODO PROBABLY CAN BE REMOVED
            break   #stops asking for input when correct input provided
        else:
            print("Invalid letter. Please enter a single alphabetical character.")
    check_guess(guess) #call for check_guess function which changes input to lowercase and checks if guessed letter is in the word picked from word list

def check_guess(guess):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()