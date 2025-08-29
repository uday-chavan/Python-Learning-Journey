# Creating
a = "Hello"
b = 'Hello'
c = '''Hello'''
# used when we have to write multiline strings
d = """Hello"""
e = str("Hello")

# concept of indexing
c = "Hello"
print(c)

# Types of indexing

# Positive Indexing 
# Negative Indexing 

# We can fetch any character from string using this
print(c[1])
print(c[-3])
# We can fetch last character directly by string[-1]

# slicing
c = "Hello World"
print(c)

print(c[0:5])
# print(c[starting position:ending position])

# or

print(c[2:6:2])
# print(c[start:end:position to skip after])
# same for negetive indexing

print(c[::-1])
# Reverses the string

print(c[-1:-5:-1])