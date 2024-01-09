# Operations on strings
# Addition sign concatenation

Greetings = "Hello"
Name = " Mojid"

# * Operator
print(Name*3)
print(Greetings + Name*3)
print(Name[1] + Greetings[1])

# Slicing strings
print(Name[0:4])
print(Greetings[0:3])
print(Name[:2])
print(Name[2:])

# Lowercase and Uppercase
print(Name.lower())
print(Name.upper())

# Count how many time a letter appears in a string

print(Greetings.count('l'))

# Replace specific characters with other characters

print(Name.replace('o', 'a'))
Name = "Aroje"
New_Name = Name.replace("A", "E")
print(New_Name)

# Finding the length of a string
print(len(Name))

# Format String
# your_name = input("Your Name: ")
# hello = "Hello {}".format(your_name)
# print(hello)

# Each letter in python is assigned to a specific number
print("orange" < "strawberry")
print(ord("o"))
print(chr(38)) # Are not restricted to just numbers
# We can perform maths on strings

# in and not operators
fruit = "banana"
print("a" in fruit)
print("s" in fruit)

x = "HELLO"
y = ""
for character in x:
    y = character.lower() + y
print(y)