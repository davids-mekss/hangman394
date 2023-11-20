import random

word_list = ["mango", "blueberry", "banana", "apple", "persimmon"]
print(word_list)

word = random.choice(word_list)
print(word)

def validate_guess():
    while True:     # will run forever until a valid entry is provided in input
        guess = input("Please enter a single letter: ")

        if len(guess) == 1 and guess.isalpha(): #check if input is 1 character long and that the character is alphabetical
            print("Good guess!")
            return guess
        else:
            print("Oops! That is not a valid input.")

validate_guess()

