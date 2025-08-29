## Operators ## 

# Arithmetic Operators

x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y) # modulus
print(x ** y) # Power of
print(x // y) # integer division

# Comparison Operators

print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

# Logical Operators

x = True
y = False

print(x or y)
# prints true when any one is true else if both are false it will print false.

print(x and y)
# prints true when both the values are true else prints false

print(not x)
# prints false if the value assigned is true else prints true

# Bitwise Operators

x = 2
y = 3

print ( x & y)
# converts in binary 

print (x | y)
# converts in binary 

print (x >> 2)
print (y << 3)
print (~x) 

# Assignment Operator
a = 3
print(a)

a += 3
# a = a + 3
print(a)

# similarly
a -= 3
print(a)
a *= 3
print(a)
a &= 3
print (a)

# identity operator

a = 3
b = 3
# both are stored in a same location 
print ( a is b )

a =[1,2,3]
b = [1,2,3]
# both are stored in a different location 
print(a is b)
print(a is not b)

# membership operator 

x = "Delhi"
print("D" in x)
print("D" not in x)

# can be similarly applicable for 
# list
# tuple
# sets
# dictionaries


