# Convert a tuple to a list
x = ("Apex","Moringa","Great")
y = list(x)
y[0] = "Motor"
x = tuple(y)
print(x)

# Add tuple to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# Remove Items from tuple is not allowed
# So to remove items from tuple first convert to tuple

tup = ("apple","banana","cherry")
y = list(tup)
y.remove("apple")
tup = tuple(y)
print(tup)

# Allowing to extract the value back into variables called Unpacking

fruits = ("chala","chaltu","garoma")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#In the above If the number of variable is less than the number of values, you can add an
# * to the variable name and the values will be assigned to the variable as a list


# NOTE_THAT
# To join two or more tuple we can use + operators

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1998
    }

x = car.values()

print(x)

car["year"] = 2020

print(x)