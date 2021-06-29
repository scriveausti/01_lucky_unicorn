answer = False
while answer == False:
    new = input("have you played befor?")
    if new == "yes":
        answer = True
        break
    elif new == "no":
        print("instruction")
        break
    else:
        print("pleas inter yes or no")
