import random

user_range = input("enter range:")
if user_range.isdigit():
    user_range = int(user_range)
else:
    print("enter valid number")
    quit()


def guesser(user_range):
    random_number = random.randint(1, user_range)
    guess = 0
    while random_number != guess:
        guess = input("guess number")
        if guess.isdigit():
            guess = int(guess)
            if guess > random_number:
                print("too high.try again")
            elif guess < random_number:
                print("too low,try again")
        else:
            print("enter valid number")
            continue

    print("you won")


guesser(user_range)
