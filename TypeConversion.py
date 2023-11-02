import random
# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:
# Note: You cannot convert complex numbers into another number type.

# Example
# Convert from one type to another:

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)
print(a)
# convert from float to int:
b = int(y)
print(b)
# convert from int to complex:
c = complex(x)
print(c)

print(type(a))
print(type(b))
print(type(c))
print(".................")

# Random Number
# Python does not have a random() function to make a random number,
# but Python has a built-in module called "random" that can be used to make random numbers:

# Example
# Import the random module, and display a random number between 1 and 9:
# import random: Refer to 1st line
print(random.randrange(1, 10))

# Strings:
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

x = str("s1") # x will be 's1' > Complex to str
y = str(2)    # y will be '2' > int to str
z = str(3.0)  # z will be '3.0' > float to str

print(type(x))
print(type(y))
print(type(z))
print(".................")