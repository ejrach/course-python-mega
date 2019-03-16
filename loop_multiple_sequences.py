a = ['a', 'b', 'c']
b = [1, 2, 3]

# zip is a built-in function that merges two lists. But will only do the smallest
# quantity of items in the lists.
for  i, j in zip(a, b):
    print("%s is %s" % (i,j))

