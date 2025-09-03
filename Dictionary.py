# Dictionary

# Dictionary is a special datatype where key value pairs are stored

# Rules -

# no indexing
# mutable datatype
# keys -> immutable ; values -> they can be mutable or immutable
# Keys should be unique

# Mutable datatypes -> list, sets, Dictionaries
# Immutable datatypes -> Strings, int, float, boolean, complex

# Creating an empty dictionary
D = {}

# Creating a normal dictionary
D = {"Name":"Nitish", "Gender":"Male"}

D1 = {[1,2,3]:"Nitish"}
# error cauz list

D1 = {(1,2,3), "Nitish"}
# creates a dictionaries
# keys always immutable
# values can either be mutable or immutable

D2 = {"Name":"Rahul","Name":"Rohit"}
# updates and prints only last one pair

# Creating a 2D dictionary
D3 = {"Name":"Rohit","College":"HIT","Marks":{"M1":56,"DS":54,"Eng":67}}

# Accessing items from a Dictionary
D[0]
# shows error

D["Name"]
# Therefore, Can only accessed using keys lik this
# hence, no indexing

# How to access items in 2D dictionary
D3["Marks"]["DS"]

# How to Edit a Dictionary

D["Name"] = "Rahul"
# or
D3["Marks"]["DS"]=64

D.get('Name')
# only can be used in 1D not in 2D or 3D

# How to add new key value pairs

D["Age"] = 23
# Adds new key called Age with value 

D3["Marks"]["M2"] = 50

# How to Delete 

D5 = {}
del D5

del D["Gender"]

D.clear()
# empties the dictionary

# Operations

D1 + D2
D1 * 3
# no concatination and multiplication, but loops can be done
 
for i in D3:
    print(i)
# returns only keys not values

# returns complete dictionariy using this 
for i in D3:
    print(i,D3(i))

# membership operator
"Rohit" in D3
# returns false cauz it checks key
"Name" in D3
# Returns true

# Functions
# All Functions present

len()
min()
max()
sorted()
sorted(D3,reverse = True)
D3.keys()
# returns list of all keys
D3.values()
# returns list of all values