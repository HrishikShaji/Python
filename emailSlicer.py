print("welcome to email slicer!")
def main(user_email):

    (username, domain) = user_email.split("@")
    (domain, extension) = domain.split(".")
    print(f"\n username is {username}.\n domain is {domain}.\n extension is {extension}.")

while True:

    user_email = input("enter email:")
    if "@" not in user_email or "." not in user_email:
        print("wrong email address")
        continue
    else:
        main(user_email)
        quitq = input("enter q to quit,c to continue").lower()
        if quitq == "q":
            quit()
        elif quitq == "c":
            continue
        else:
            print("invalid input")


