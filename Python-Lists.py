# List

# What is a List - Stores multiple things together
# Difference betwn array and list - all items in array are of same datatype, in list , can be of different datatypes
# in array things are stores continuously into a memory location, not in lists
# arrays are much faster than lists
# lists are more programmer friendly


# Creating a list

# empty list
L = []

# Homogeneous List

L = [1,2,3,4,5]

# Heterogeneous List
# not allowed
L2 = ["Hello",4,5,6,True.5+6j].

# Multidimentional Lists

# 2D List
L3 = [1,2,3[4,5]]

# 3D List
L4 = [[[1,2],[3,4]],[[5,6],[7,8]]]

# Creating List using Type Conversion

L5 = list("Haldia")

# Creating Empty List using ()

L6 = list()


# Tips to access Elements

L = [1,2,3,4,5]
L[0]
# this and all others are same as in strings

# But it is different in case of multidimentional list

# 2D
L3 = [1,2,3,[4,5]]

L3[0]

x = L3[-1]

x[0]
# or
L3[-1][0]

# 3D 
L4 = [[[1,2], [3,4]],[[5,6],[7,8]]]

L4[1][1][0]

L4[0][1][1]

# Editing an element

L = [1,2,3,4,5]
L[0] = 100
# Lists in Python are mutable

# Also can be done with negative indexing
L[-1] = 500

# Also can be done with slicing
L[1:4] = [200,300,400]


# Adding new items in list

# Append

L.append[1000]
# adds anything in last (like string or number or list)

# extend

L.extend[[5000,6000,7000]]
# adds multiple items in last
# will always try to add multiple items like for "goa" it'll add 'g','o','a'

# insert

L.insert[1,'world']
# we can add items using this in any desired location

# How to delete things inside the list

# del

del L2
# deletes the entire list

del L[0]
# delets specific item from that list

del L[-3:]
# deletes complete portion of last 3 items using negative indexing

del L.remove["hello"]
# deletes item without its index position

L.pop[]
# deletes last item

L.clear[]
# empties the list without deleting it

# Operations in List

# concatination
# multiplication
# loop
# membership

L = [1,2,3,4]
L1 = [5,6,7,8]

L3 = L + L2
L4 = L * 3
for i in L:
    print(i)
4 in L3 
# return true or false

# Functitons in List

len()
min()
max()
sorted()
sorted(L,reverse=True)
# forms new list
L.sort(reverse=True)
# reverses the existing list (Permanant operation)
L.index(3)
# it gives the position of 3 in list
L.title()
# capitalizes first letter of each word.