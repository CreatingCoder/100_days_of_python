import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

#import csv into pandas
nato = pandas.read_csv('nato_a.csv')

#translate into dict
nato_dict = {row.letter: row.code for (index,row) in nato.iterrows()}


userinput = input('Input a single word: ').upper()

output = [nato_dict[letter] for letter in userinput]

print(output)





