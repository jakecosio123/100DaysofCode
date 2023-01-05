import random
# sets ascii art variables for display in the console
rock = '''
You chose rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
You chose paper!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
You chose scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
c_rock = '''
Computer chose rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

c_paper = '''
Computer chose paper!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

c_scissors = '''
Computer chose scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#defines user choice options as a list and asks the user for their choice
user_choice_options = [rock, paper, scissors]
user_choice = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n")

#defines computer choice options as a list and randomly generates the computer's choice
computer_choice_options = [c_rock, c_paper, c_scissors]
computer_int= random.randint(0,2)

#filters out invalid inputs
if user_choice == "0" or user_choice == "1" or user_choice == "2":
    #converts user choice from string to integer so we can use it to index
    user_int = int(user_choice)

    #prints both the user and computer choices
    print(user_choice_options[user_int])
    print(computer_choice_options[computer_int])

    #decides the outcome of the game
    if user_int == 0 and computer_int == 2:
        print("You win! Congratulations!")
    elif user_int == 2 and computer_int == 0:
        print("You lose! Try again.")
    elif user_int == computer_int:
        print("You tie! Try again.")
    elif user_int < computer_int:
        print("You lose! Try again.")
    elif user_int > computer_int:
        print("You win! Congratulations!")
    else:
        print("Something has gone terribly wrong. Contact your friendly neighborhood Spiderman.")

#prints message in the event of invalid inputs
else:
    print("Your input was invalid. You lose.")