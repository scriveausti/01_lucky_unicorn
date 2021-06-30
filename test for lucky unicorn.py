# welcomes user
input("Welcome to lucky unicorn")


# asks if they have played before
answer = False
while answer == False:
    new = input("have you played before?")
    if new == "yes":
        answer = True
    elif new == "no":
        print("instruction")
        break
    else:
        print("pleas inter yes or no")

