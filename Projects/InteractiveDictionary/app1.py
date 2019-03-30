import json
from difflib import get_close_matches

# Load the JSON data into a python dictionary
data = json.load(open("/Users/eric/projects/GitHub/course-python-mega/Projects/InteractiveDictionary/data.json", 'r'))

# define a function to return the defintion based on a word
def translate(w):
    
    # first convert to all lower case, since the JSON data is all in lower case
    w = w.lower()

    # if the word is in data, then return the definition
    if w in data:
        return data[w]
    elif w.title() in data: #  if the user entered all lowercase "texas" this will convert first letter to upper, rest to lowercase
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    # else if there is a list of close matches > 0
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead?: " % get_close_matches(w, data.keys())[0])
        if str.upper(yn) == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif str.upper(yn) == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

# Take input from user
word = input("Enter a word: ")

# store the output in an output 'list'
output = translate(word)

# now loop through the items in the output list, if it is a list type
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

