from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar (input_text, input_shift, input_direction):
    for item in range(len(input_text)):
        if alphabet.count(input_text[item]) > 0:
            letter = input_text[item]
            letter_index = alphabet.index(letter)
            if input_direction == "decode" and input_shift>0:
                input_shift *= -1
            text_as_list[item] = alphabet[letter_index + input_shift]
    updated_text = ''.join(text_as_list)
    print(f"The {input_direction}d text is {updated_text}")

print(logo)
user_wants_to_run = True
while user_wants_to_run:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    text_as_list = list(text)

    ceasar(input_text = text_as_list, input_shift = shift, input_direction = direction)

    user_keep_running_input = input("Would you like to continue? Type 'yes' to keep going, or 'no' to exit.\n").lower()

    if user_keep_running_input == "no":
        user_wants_to_run = False
        print("Goodbye!")