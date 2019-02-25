# Simple list and print
myList = ["a", "b", "c"]
print("1: ", myList)

# Print second item
print("2: ", myList[1])

# Print last item - a shortcut
print("3: ", myList[-1])

# Add new items to the list
myList.append("d")
myList.append("e")
print("4: ", myList)

# Adding multiple in one line
myList.extend(["f", "g", "h"])
print("5: ", myList)

# Print the first 3 items
print("6: ", myList[0:3])

# Print all the items of the list
print("7: ", myList[0:])
print("8: ", myList[:])     # same thing

# Print first 5 items
print("9: ", myList[:5])

# Print everything from the 2nd to last item to the end
print("10: ", myList[-2:])

# Remove the item 'h'
myList.remove("h")
print("11: ", myList)
