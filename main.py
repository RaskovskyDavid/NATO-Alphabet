import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Lopping through dictionaries:
for (key, value) in student_dict.items():
    pass
student_data_frame = pd.DataFrame(student_dict)

#Loop throuigh rows of a data frame

for (index, row) in student_data_frame.iterrows():
    pass
# Todo 1. Create a dictionary in this format
df = pd.read_csv("nato_phonetic_alphabet.csv")
new_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

# Todo 2. Create a list of the phonetic code words from a word that the user inputs

def generate_phonetic():
    word = input(f"What word do you want to spell: ").upper()
    # it_not_a_word = [True for letter in word if not letter.isalpha()]
    # if it_not_a_word:
    #     raise ValueError("This is not a word")
    try:
        spell = [new_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(spell)

generate_phonetic()


