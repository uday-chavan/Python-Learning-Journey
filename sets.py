# sets

# sets do not allow duplicates
# sets have no indexing (no slicing)
# sets dont allow mutable datatypes
# set itself is a mutable data type

# Creating a set

# empty set

S1 = {}

type(S1)
# returns dectionary (no set formed)

# how to create an empty set

S1 = set()
# this is an empty set

# it can be homogenious (one datatypes)
# it can be heterogenious (different datatypes)

S3 = {1,1,2,2,3,3}
# returns - {1,2,3} as duplicates are not allowed

S4 = {[1,2,3],"Hello"}
# returns error as it is immutable

S4 = {(1,2,3),"Hello"}
# returns output as both are immutable

# sets have no hashing
# hashing concept later

# 2d sets are not possible
S5 = {(1),(2)}

# How to access items in sets

S1 = {1,2,3,4,5}
S1[0]

# not possible to access items or slicing

# We also cant edit items in sets

# Adding items in sets
# possible

S1.add(6)
id(S1)
S1.add(7)
id(S1)
# adds without changing memory location

# Deleting the items in sets

# del
del S2
# can be applied to complete set not individual item

S1 = {1,2,3,4,100}
S1.remove(100)
# can remove any item in it (mutable operation)

S1.pop()
# pops the last item ( but shows in opposite order )

# Set operations

S1 = {1,2,3,4,5}
S2 = {3,4,5,6,7}

S1 + S2
# cannot concatinate
# cant be multiplied

# but loops work

for i in S1:
    print(i)

1 in S1
# membership operator is available 

# Functions

len(S1)
min(S1)
max(S1)
sum(S1)
sorted(S1)
sorted(S1,reverse=True)
S1.union(S2)
# all unique no. combined from both the sets

S1.intersection(S2)
# common

S1.difference(S2)
# items in s1 not in s2

S2.difference(S1)
# items in s2 not s1

S1.symmetric_difference(S2)

S1.isdisjoint(S2)

S1.issubset(S2)

S1.issuperset(S2)

S1.clear()

# remaining functions can be accessed using S1.

