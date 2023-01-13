import random
from hangman_art import *
from hangman_words import *
from clear import *

#set variables
end_of_game = False
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
guessed_letters = []
guessed_yet = False

#add number of blanks to the display list equal to the number of letters in the chosen_word
for letter in chosen_word:
    display.append("_")

#continues the game until the player wins or loses
while not end_of_game:
    
    #if this is the first guess, it prints various items and gets the first guess. This allows for the screen to be cleared between guesses so no scrolling is needed.
    if not guessed_yet:
        print(logo)
        print("The word is:")
        print(f"{' '.join(display)}")
        print(stages[lives])
        guess = input("Choose a letter.\n").lower()
        guessed_yet = True

    else:
        #clears screen and prints various things to console
        clear()
        print(logo)
        print("The word is:")

        #warns user if they have already guessed a letter
        if guess in guessed_letters:
            print(f"You've already guessed {guess}.")
        else:
            #adds a correctly guessed letter to the display
            for num in range(0,word_length):
                if guess == chosen_word[num]:
                    display[num] = guess
            
            #decreases life variable with incorrect guesses
            if guess not in chosen_word:
                lives -= 1
        
        #prints more things
        print(f"{' '.join(display)}")
        print(stages[lives])


        #tells user thier guess was wrong
        if guess not in chosen_word:
            print (f"The word does not contain {guess}.")
        #adds the guess to the list of letters the user has guessed
        guessed_letters +=guess
        
        #tells the player if they win, lose, or need to keep guessing
        if "_" not in display:
            end_of_game = True
            print(f"You win! {win_art}")
        elif lives == 0:
            end_of_game = True
            print(f"You lose. {lose_art}")
        else:
            guess = input("Choose a letter.\n").lower()

