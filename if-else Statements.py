# correct email - chavanuday503@gmail.com
# password - 1234

email = input("Enter Your Email: ")
if '@' in email:
    password = input("Enter Your Password: ")

    if email == "chavanuday503@gmail.com" and password == "1234":
        print("Welcome")
    elif email == "chavanuday503@gmail.com" and password != "1234":
        print("Password Incorrect")
        password = input ("Re-Enter Your Password:")
        if password == "1234":
            print("Finally Correct! ")
        else: 
            print("Still Incorrect! ")
    else:
        print("Incorrect Credentials")
else:
     print("Incorrect Email")
