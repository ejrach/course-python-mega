# open file for read and write (a+)
myfile = open("employees2.txt", "a+")

# when using a+ mode (read/write), need to seek to the beginning of the file
myfile.seek(0)
print(myfile.read())

myfile.write("\nJohn")

myfile.close()
