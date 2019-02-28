
myfile = open("sample.txt")

# create variable to store string
content = myfile.read()
myfile.close()
print(content)

# open from a different directory (relative)
myfile = open("files/sample.txt")
content = myfile.read()
myfile.close()
print(content)

# open from a different directory (absolute)
myfile = open("/Users/eric/projects/GitHub/course-python-mega/files/sample.txt")
content = myfile.read()
myfile.close()
print(content)

# reading content from the file
myfile = open("sample.txt")

# defining a fruit and then seeing if it is the list
f = "orange"
fruits = myfile.read()
fruits = fruits.splitlines()
print(fruits)
if f in fruits:
    print(f, "is in the list")
else:
    print(f, "is not in the list")
myfile.close()
