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
word = input(f"What word do you want to spell: ").upper()
spell = [new_dictionary[letter] for letter in word]
print(spell)


