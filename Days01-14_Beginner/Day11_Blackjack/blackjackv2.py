from os import system, name
from art import *
import random

wants_to_play = True

def calculate_score(input_cards):
    return sum(input_cards)

def aces_check(input_cards, input_score):
    """If ace would cause hand to bust, change its value to 1"""
    if input_score > 21 and 11 in input_cards:
        return 1
    else:
        return 11

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    computer_cards = []
    player_score = 0
    computer_score = 0
    another_card = "no"
    
    for num in range(2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)
    
    clear()
    print(logo)
    print(f"Your cards: {player_cards}, current score =  {player_score}")
    print(f"Dealer's first card: {computer_cards[0]}")
    
    if player_score <21:
        another_card = input("Type 'yes' to get another card, type 'no' to pass: ").lower()
    
    while another_card == "yes":
        player_cards.append(random.choice(cards))
        player_score = calculate_score(player_cards)
        if 11 in player_cards:
            player_cards[player_cards.index(11)] = aces_check(player_cards, player_score)
            computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score =  {player_score}")
        if player_score < 21:
            another_card = input("Type 'yes' to get another card, type 'no' to pass: ").lower()
        if player_score >=21:
            another_card = "no"

    while computer_score <17:
        computer_cards.append(random.choice(cards))
        computer_score = calculate_score(computer_cards)
        if 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = aces_check(computer_cards, computer_score)
            computer_score = calculate_score(computer_cards)
    clear()
    print(logo)
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {computer_cards}, final score {computer_score}")
    
    
    if computer_score == 21 and len(computer_cards) == 2:
        print("Dealer has a Blackjack. You lose. Better luck next time")
        print(lose_art)
    elif player_score == 21 and len(player_cards) == 2:
        print("Blackjack! You win, congratulations!")
        print(win_art)
    elif player_score > 21:
        print("You bust and, therefore, lose. Better luck next time.")
        print(lose_art)
    elif computer_score > 21:
        print("Dealer busts. You win, congratulations!")
        print(win_art)
    elif player_score > computer_score:
        print("You win, congratulations!")
        print(win_art)
    elif player_score == computer_score:
        print("It's a draw. Try again!")
        print(draw_art)
    else:
        print("You lose. Better luck next time")
        print(lose_art)

    keep_playing = input("Would you like to play again? Type 'yes or 'no' to continue. ").lower()
    
    if keep_playing == "yes":
        return True
    elif keep_playing == "no":
        print("See you next time!")
        return False
    else:
        print("Invalid input. We'll take that as a 'no.' Catch you next time!")
        return False

while wants_to_play:
    wants_to_play = blackjack()