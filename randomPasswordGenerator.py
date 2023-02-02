import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_pass():
    pass_len = int(input("length of password:"))
    random.shuffle(characters)
    password = []

    for x in range(pass_len):
        password.append(random.choice(characters))
    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("do you want a password? y/n")

if option == "y":
    generate_pass()
elif option == "n":
    quit()
else:
    print("invalid input")
    quit()
