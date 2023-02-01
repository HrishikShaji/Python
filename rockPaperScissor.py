import random

options = ["rock","paper","scissors"]
computer_wins = 0
user_wins = 0
print("\n welcome to Rock Paper Scissors \n \n")

while True:
    user_input = input("pick Rock/Paper/Scissors or Q to quit").lower()
    if user_input == "q":
        print(f"you won {user_wins} times ,computer won {computer_wins} times")
        break
    if user_input not in options:
        print("invalid input")
        continue
    if user_input in options:
        random_number = random.randint(0, 2)
        computer_pick = options[random_number]
        print(f"computer picked {computer_pick}")
        if user_input == "rock" and computer_pick == "scissors":
            print("you won")
            user_wins += 1
        elif user_input == "paper" and computer_pick == "rock":
            print("you won")
            user_wins += 1
        elif user_input == "scissors" and computer_pick == "paper":
            print("you won")
            user_wins += 1
        else:
            print("you lost")
            computer_wins += 1
    else:
        continue
