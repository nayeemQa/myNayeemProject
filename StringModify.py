# Python has a set of built-in methods that you can use on strings.
# Upper Case
#The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
print("..............")

# Lower Case
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
print("..............")

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The strip() method removes any whitespace from only from the beginning or from the end: (not able to inside 2 words)
a = " Hello , Wor ld! "
print(a.strip())
print("..............")

# Replace String
# Example
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
print(a.replace("Hello", "Hola"))
print("..............")

# Split String
# The split() method returns a list, where the text between the specified separator becomes the list items.
# The split() method splits the string into substrings if it finds instances of the separator:

# depends on (,)
a = "Hello, World!"
print(a.split(","))

# depends on (space)
b = "Hello Wor ld!"
print(b.split(" "))

print("...............")

# capitalize() only the 1st word of the sentences:
c = "hello world.this is python"
print(c.capitalize())

# startswith() : Return True/False
d = "Mango"
print(d.startswith("M"))
print(".................")

# endswith(): Return True/False
d = "Mango"
print(d.endswith("o"))
print(".................")

# Convert uppercase characters to lowercase and lowercase characters to uppercase.
e = "MANgO"
print(e.swapcase())
print(".................")




