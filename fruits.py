# write some code that reads the content of the 
# fruits.txt file and generates the following output in the command line:

# pear
# apple
# orange
# mandarin
# watermelon
# pomegranate

fruitfile = open("fruits.txt", "r")
fruits = fruitfile.read()
fruitfile.close()
print(fruits)
