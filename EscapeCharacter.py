# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

"""

    \'	Single Quote	
    \"  Double Quote
    \\	Backslash	
    \n	New Line	
    \t	Tab	
    \b	Backspace	
    \r	Carriage Return	
    \f	Form Feed	
    \ooo Octal value	
    \ xhh Hex value
    
    
"""
print("This is a \'Single Quote\' example ")

print("This is a \" Double Quote \" example ")

print("This is a \\ Backslash \\ example ")

print("This is a \n new line example ")

print("This is a \t Tab- 4 space example ")

print("This is a b\b backspace or deletion example ")

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)


