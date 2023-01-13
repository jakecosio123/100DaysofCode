from os import system, name
import random
from art import *

computers_num = random.randint(1,100)
guess = 0
HARD_GUESSES = 5
EASY_GUESSES = 10
game_over = False
new_game = True

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def used_a_guess():
    return tries - 1

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_GUESSES
    elif difficulty == "hard":
        return HARD_GUESSES
    else:
        print("Invalid input. Looks like you need easy mode.")
        return EASY_GUESSES

while new_game:
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    tries = set_difficulty()
    while not game_over:
        guess = int(input(f"You have {tries} attempts remaining to guess the number. \nMake a guess: "))
        if guess == computers_num:
            print(f"You got it! The answer was {computers_num}.")
            print(win_art)
            game_over = True
        elif tries == 1:
            print("You've run out of guesses. Better luck next time.")
            print(lose_art)
            game_over = True
        elif guess > computers_num:
            print("Too high.")
            tries = used_a_guess()
        else:
            print("Too low.")
            tries = used_a_guess()

        if game_over:
            play_again = input("Would you like to play again? Type 'yes' or 'no' to continue: ")
            if play_again == "yes":
                new_game = True
            elif play_again == "no":
                new_game = False
            else:
                print("Invalid input. We'll take that as a no.")
                new_game = False