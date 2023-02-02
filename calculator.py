def add(a,b):
    answer = a + b
    print(answer)

def substract(a,b):
    answer = a - b
    print(answer)

def multiply(a,b):
    answer = a * b
    print(answer)

def divide(a,b):
    answer = a / b
    print(answer)

while True:
    a = input("enter first number:")
    if a.isdigit():
        a = int(a)
    else:
        print("invalid input")
        continue
    b = input("enter second number:")
    if b.isdigit():
        b = int(b)
    else:
        print("invalid input")
        continue
    action = input("\n (+)Addition \n (-)Substraction \n (*)Multiplication \n (/)Division \n (q)Quit \n operation:").lower()
    if action == "+":
        add(a,b)
        quitq = input("c to continue,q to quit")
        if quitq == "c":
            continue
        elif quitq == "q":
            quit()
        else:
            print("invalid")
    elif action == "-":
        substract(a,b)
        quitq = input("c to continue,q to quit")
        if quitq == "c":
            continue
        elif quitq == "q":
            quit()
        else:
            print("invalid")
    elif action == "*":
        multiply(a,b)
        quitq = input("c to continue,q to quit")
        if quitq == "c":
            continue
        elif quitq == "q":
            quit()
        else:
            print("invalid")
    elif action == "/":
        divide(a,b)
        quitq = input("c to continue,q to quit")
        if quitq == "c":
            continue
        elif quitq == "q":
            quit()
        else:
            print("invalid")
    elif action == "q":
        quit()
    else:
        print("inavlid input")


