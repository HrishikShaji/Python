name = input("what's your name:").lower()
print(f"welcome {name}")
question = input(f"Now {name},do you wanna play this game?enter y for Yes ,n for No").lower()
if question == "y":
    print("Ok ,Lets start")
    question1 = input("imagine yourself in a junction,where do you wanna go? (r)right or (l)left").lower()
    if question1 == "r":
        print("you chose right")
        question2 = input("since you chose the right path you are before a bridge do you want to cross it? (y)yes or (n)no").lower()
        if question2 == "y":
            print("now you crossed it.congratulations")
            question5 = input("as you crossed someone shot you.can you get up?(y)yes or (n)no").lower()
            if question5 == "y":
                print("you won")
            elif question5 == "n":
                print("you died")
            else:
                print("you lost")
        elif question2 == "n":
            question3 = input("you have chosen not to cross,so are you accepting failure?(y)yes or (n)no").lower()
            if question3 == "y":
                print("you lost")
            elif question3 == "n":
                print("then you should cross")
                question4 = input("are you gonna cross?(y)yes or (n)no")
                if question4 == "y":
                    print("you have won")
                elif question4 == "n":
                    print("you lost")
                else:
                    print("you lost")
            else:
                print("invalid")
    elif question1 == "l":
        print("you chose left")
        question6 = input("since you chose left a car just hit you.do you want to get up? y(yes) or (n)no").lower()
        if question6 == "y":
            print("you won")
        elif question6 == "n":
            print("you lost")
        else:
            print("invalid input")
    else:
        print("invalid input ,you lost")

elif question == "n":
    print("Ok ,fine")
else:
    print("invalid output")