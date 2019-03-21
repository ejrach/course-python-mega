import json

# Load the JSON data into a python dictionary
data = json.load(open("/Users/eric/projects/GitHub/course-python-mega/Projects/InteractiveDictionary/data.json", 'r'))

# define a function to return the defintion ased on a word
def translate(w):
    return data[w]

# Take input from user
word = input("Enter a word: ")

print(translate(word))

