# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# If you want to specify the data type of a variable, this can be done with casting.
# You can get the data type of a variable with the type() function.
# Variable names are case-sensitive
"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

"""
Legal variable names:

myVar = "John"
myvar = "John"
my_var = "John"

_my_var = "John"
MYVAR = "John"
myvar2 = "John"

"""


"""
Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"
"""

# String type
name1 = "Jannat Nayeem"
print(name1)
print(type(name1))

# integer type
age = 34
print(age)
print(type(age))

# Variable names are case-sensitive
# A will not overwrite a
a = 2
A = 3
print(A)
print("...............")

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x, y, z = 5, 7, 10

print(x)
print(y)
print(z)
print("...............")

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

a = b = c = "Orange"
print(a)
print(b)
print(c)
print("...............")

# Unpack a Collection of Python
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.

# Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print("...............")


# The best way to output multiple variables in the print() function is to separate them with commas,
# which even support different data types:

x1 = "Python "
x2 = "is now "
x3 = 3.12

print(x1 + x2, x3)















