from art import *
from clear import *
from game_data import *
import random

score = 0
streak_going = True


def choose_insta():
    return random.choice(data)


while streak_going:
    clear()
    print(logo)
    if score == 0:
        a = choose_insta()
    else:
        print(f"You're right! Current score: {score}.")
        a=b
    print(f"Compare A: {a['name']}, {a['description']} from {a['country']}")
    print(vs)
    b = choose_insta()
    while a == b:
        b = choose_insta()
    print(f"Against B: {b['name']}, {b['description']} from {b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess == "A" and a['follower_count'] > b['follower_count']:
        score += 1
    elif guess == "B" and b['follower_count'] > a['follower_count']:
        score += 1
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        streak_going = False
