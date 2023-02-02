# open the file with the names in it and save the names as a list
with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

# open the letter that needs to be formatted and save the message as a list
with open("Input/Letters/starting_letter.txt") as letter:
    #save contents of the letter to a list
    message = letter.readlines()

    #iterate through the names
    for name in name_list:
        # save message in list form for temporary usage
        formatted_message = message[:]
        # strip name of unneeded characters
        formatted_name = name.strip("\n")
        # change name
        greeting = formatted_message[0].replace("[name]", formatted_name)
        # remove first item from list to prevent repetition
        formatted_message.remove(formatted_message[0])

        # open (or create if not already created) letter for each name in the list and write the message
        with open(f"Output/ReadyToSend/letter_for_{formatted_name}", mode="w") as new_letter:
            # write the greeting with the changed name
            new_letter.write(greeting)
            # iterate through the message writing it line by line
            for line in formatted_message:
                new_letter.write(line)
