# Key Value pairs
pins = {"Mike":1234, "Joe":1111, "Jack":2222}

# Print pin for "Mike"
print("1: ", pins["Mike"]) 

# Print all the Keys
print("2: ", pins.keys()) 

# Print all the Values
print("3: ", pins.values()) 

# Example dictionary
person = {"name":"Jack", "surname":"Smith", "age":"29"}

# remove pair name Jack
person.pop("name")
print("4: ", person)

# Adding new pair name Jack
person["name"] = "Jack"
print("5: ", person)

# Changing an existing value
person["age"] = 30
print("6: ", person)

# Mapping two lists to a dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]
mydict = dict(zip(keys, values))
print("7: ", mydict)