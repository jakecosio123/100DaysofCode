from clear import *
from art import logo

print(logo)
bidders = {}
current_bid = 0

def secret_auction():
    more_bidders_exist = True
    while more_bidders_exist:
        name = input("What is your name? ")
        bid = int(input ("What is your bid? $"))
        more_bidders = input("Are there more bidders? Type 'yes' or 'no'.\n").lower()

        bidders[name] = bid
        if more_bidders == "no":
            more_bidders_exist = False
        clear()

secret_auction()
for key in bidders:
    if bidders[key] > current_bid:
        current_bid = bidders[key]
        bidders_name = key

print(logo)
print(f"The winner of the auction is {bidders_name} with a bid of ${current_bid}.")
print(f"Congratulations {bidders_name}!")

