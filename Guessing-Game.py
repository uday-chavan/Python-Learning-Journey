import random

num = random.randint(1,100)
counter = 1

jackpot = random.randint(1,100)
guess = int(input("Guess the number"))

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else: 
        print("Guess lower")

    guess = int(input("Guess the number"))
    counter +=1

print("Right Answer! ")
print("You Took", counter, "Attempts")