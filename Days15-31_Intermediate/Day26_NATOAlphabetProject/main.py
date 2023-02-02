import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


def nato_converter():
    word = input("Enter a word: ").upper()
    try:
        result = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_converter()
    else:
        print(result)


nato_converter()
