# create a file in the working directory
myfile = open("employees.txt", "w")
myfile.write("Mike")
myfile.close()

#executing this again, recreates the text file and overwrites the contents
myfile = open("employees.txt", "w")
myfile.write("Mike\nJoe\nJack")
myfile.close()

# now write a new file but apply multiple writes
myfile = open("employees2.txt", "w")
myfile.write("Mike")
myfile.write("\nJoe")
myfile.close()

# now append text to "employees2.txt" file
myfile = open("employees2.txt", "a")
myfile.write("\nJack")
myfile.close()