# Python String capitalize() Method
# The first character is converted to upper case, and the rest are converted to lower case.
txt = "python is FUN!"

x = txt.capitalize()
print(x)

# See what happens if the first character is a number: no Change
txt = "36 is my age."

x = txt.capitalize()
print(x)

print(".................")

# casefold():	Converts string into lower case

txt = "Hello, And Welcome To My World!"

x = txt.casefold()
print(x)
print(".................")


# center()	Returns a centered string
# The center() method will center align the string, using a specified character (space is default) as the fill character.
txt = "I eat banana"

x = txt.center(20)
print(x)
print(".................")

# count():	Returns the number of times a specified value occurs in a string
# Return the number of times the value "apple" appears in the string:

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")
print(x)
print(".................")

# Search from position 10 to 24:

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)
print(x)
print(".................")

# encode()	Returns an encoded version of the string
# UTF-8 encode the string:

txt = "My name is Ståle"

x = txt.encode()
print(x)
print(".................")

# endswith()	Returns true if the string ends with the specified value
# The endswith() method returns True if the string ends with the specified value, otherwise False.
# Check if the string ends with a punctuation sign (.):

txt = "Hello, welcome to my world."

x = txt.endswith(".")
print(x)
print(".................")

# Check if the string ends with the phrase "my world.":

txt = "Hello, welcome to my world."

x = txt.endswith("my worl.")
print(x)
print(".................")

# Check if position 5 to 11 ends with the phrase "my world.":
txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)
print(x)
print(".................")

# expandtabs() Method : The expandtabs() method sets the tab size to the specified number of whitespaces.

txt = "H\te\tl\tl\to"

x = txt.expandtabs(4)
print(x)
print(".................")







