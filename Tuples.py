# Tuples

# Create
# empty tuple
T1 = ()

# homogenious tuple
T2 = (1,2,3,4,5)

# Heterogenious tuple
T3 = ("Hello",4,5,6)

# 2D tuple

T4 = (1,2,3,(4,5))

# can also make 3d tuple same as lists

# making a tuple

T5 = ("Hello",)
Type(T5)

T6 = tuple("Goa")

T6 = tuple([1,2,3,4,5])

# Access

T2 = [1,2,3,4,5]
T2[0]

# using Slcicing
T2[:4]

# in 2d tuple
T4 = (1,2,3,(4,5))
T4[-1][0]

# Editing a tuple (different than in lists)
# because tuples are also immutable like strings
# so it cant be done

# Adding new items in tuple
# because of same reason this also cant be done

# deleting 

del T1

T2 = [1,2,3,4,5]
del T2[-1]
# but this also will not work due to same reason

# Operations

# concatination 
T2 + T3

# multiplication

T2 * 3

# loops 

for i in T2:
    print(i)

# membership operator

1 in T2

# functions

len(T2)
# min
# max
# sum
# sorted
sorted(T2,reverse=True)

# Therefore, operations and functions are same as lists

# Tuples are read-only datatype because can tbe cahnged once wrote 

# advantage = useful in the cases where the data must not be changed once wrote 
