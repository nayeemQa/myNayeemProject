# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
# Ex-1:
print("Jannat" + "Nayeem")

# Ex-2:
print("Jannat" + " " + "Nayeem")

# Ex-3:
a = "Jannat "
b = "Nayeem"
c = a + b
print(c)

# Ex-4:
# You can use Comma (,) to String concatenation:
print("This is ", "Jannat ", "Nayeem")

# Ex-5:
age = '34'
txt = "My name is John, I am "
print(txt + age)

# Ex-6: String and int concatenation:
age = 34
print(type(age))
txt = "My name is John, I am"
print(txt, age)

# Ex-7: format() method
# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# Use the format() method to insert numbers into strings:
age = 35
text = "My name is John, and I am {}"
print(text.format(age))

# Ex-8:
# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemNo = 456
price = 10.5
myOrder = "I like to Order {} pcs, my itemNo is {} with the price of ${}"

print(myOrder.format(quantity, itemNo, price))


# Ex-9
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders: 0 ,1, 2
quantity = 3
itemNo = 567
price = 49.95
myOrder = "I want to pay {2} dollars for {0} pieces of item {1}."

print(myOrder.format(quantity, itemNo, price))





