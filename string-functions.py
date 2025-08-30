# Common functions

# len
# max
# min
# sorted

c = "Kolkata"
len(c)

max(c)

min(c)

sorted(c)

sorted(c,reverse=True)
# just true the reverse parameter for decending oorder

# Capitalize/Title/Upper/Lower/Swapcase

c

c.capitalize()
# will output capital K but original string will remain same

c.title()

print("it is raining today".capitalize())
print("it is raining today".title())

c.upper()

c.lower()
# all characters in string to upper/lower

c.swapcase()
"KolkAtA".swapcase()
# lower to upper, upper to lower

c.count()
print("it is raining".count("i"))
# counts any character or name in string according to no. of times it has occured / finding frrequency of any substring

# Find/Index
c.find()
"it is raining".find("i")
# position of the character

c.index()
"it is raining".index("x")
# same, just throws error if not found

# endswith/startswith
c.endswith()
"It is raining".endswith("ing")
# returns true or false

c.startswith()
"It is raining".startswith("It")
#returns true or false

# format
c.format()
print("Hello my name is {} and I am {}".format("Uday",30))
print("Hello my name is {1} and I am {0}".format("Uday",30))
print("Hello my name is {name} and I am {age}".format(name = "Uday",age = 30))
print("Hello my name is {name} and I am {weight}".format(name = "Uday",age = 30, weight = 80))
print("Hello my name is {weight} and I am {weight}".format(name = "Uday",age = 30, weight = 80))

# isalnum/ isalpha/ isdecimal/ isdigit/ isidentifier

c.isalnum()
"FLAT20".isalnum()
# returns true if alphabetical or numerical else false

c.isalpha()
"FLAT".isalpha()
# returns true if in alphabetical order else false

c.isdigit()
"20".isdigit()
# returns true if digits else false

c.isidentifier()
"Hello World".isidentifier()
# returns true if valid identifier else false. for like - empty space

# all other many 'is' based functions are available,, we can use them as needed

# Split 
c.split()
"Who is the prime minister of India".split()
"Who is the prime minister of India".split("minister")
"Who is the prime minister of India".split("i")

# Join
c.join()
" ".join(['Who', 'is', 'the', 'prime', 'minister', 'of', 'India'])
"-".join(['Who', 'is', 'the', 'prime', 'minister', 'of', 'India'])

# Replace
c.replace()
"Hi my name is Nitish". replace("Nitish","Amit")

# Strip
c.strip()
name = "          nitish"
name.strip()
# removes all the spaces

# almost 80% functions are covered, remaining can be accessed using -
# "string".