#setting variables
no = ["no", "n"]
yes = ["yes", "y"]

# welcomes user
input("Welcome to lucky unicorn")

# asks if they have played before
answer = False
while True:
    new = input("have you played before?").strip().lower()
    if new in yes:
        print("plays game")
        break
    elif new in no:
        print("instruction")
        break
    else:
        print(" <error> please enter yes or no")

# asks how much money they would like to spend
while True:
    try:
        spend = int(input("how much money do you like like to spend between $0 and $10?"))
        if spend <= 10 or spend > 0 :
            break
    except:
        print(" <error> please enter a number between 0 and 10")
