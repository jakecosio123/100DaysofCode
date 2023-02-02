import random

#saves letters, numbers, and symbols that are acceptable for use as passwords as a list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#prints to console, asks for user input, converts user input from string to int
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#sets variable as empty string
password = ""

#loops through the user determined number of letters, numbers, and symbols to randomly choose the characters to use in the password
for number in range (0,nr_letters):
    password += random.choice(letters)

for number in range (0,nr_numbers):
    password += random.choice(numbers)

for number in range (0,nr_symbols):
        password += random.choice(symbols)

#gets the total length of the password
num_char_total = len(password)

#sets variable to be a empty list
password_characters = []

#adds each character of the password to the list separately
for number in range (0, num_char_total):
    password_characters.append(password[number])

#shuffles the list
random.shuffle(password_characters)

#joins the list together back into one string
final_password = ''.join(password_characters)

#prints the random password
print(f"Your password could be: {final_password}")