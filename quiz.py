print("welcome to the Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! lets begin")
score = 0

answer = input("what does cpu stand for? ").lower()
if answer == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does gpu stand for? ").lower()
if answer == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does ROM stand for? ").lower()
if answer == "read only memory":
    print("correct")
    score += 1
else:
    print("incorrect")

print("you got " + str(score) + " questions correct")
print("you got " + str((score / 4) * 100) + "%.")

