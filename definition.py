import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))
def dictionary(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif  len(get_close_matches(word, data.keys(), cutoff=0.7)) > 0:
        alter = input("Are you looking for \"{}\" instead? , Please enter y for YES or n for NO : ".format(get_close_matches(word, data.keys())[0]))
        if alter.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif alter.lower() == "n":
            return "Please double check , Thank you..........."
        else:
            return "The word does not exist."
    else:
        return "The word does not exist."

#while True:
word = input("Please enter a word: ")
output = dictionary(word)
s = 1
if type(output) == list:
    for i in output:
         print("{}:{}".format(s, i))
         s=s+1
else:
    print(output)
    print(output)