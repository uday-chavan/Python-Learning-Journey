sample = "how are you? today has been great for me"

print(sample.split())

L = []

for i in sample.split():
    print(i.capitalize())
    L.append(i.capitalize())

print(L)
print(" ".join(L))



