# setting variables
no = ["no", "n"]
yes = ["yes", "y"]

# welcomes user
print("Welcome to lucky unicorn")
input("press enter to continue")

# instructions
def instructions():
    print("how to play ")
    print("")
    print(" enter the amount of money you would like to gamble ")
    print("")
    print("")
    print("")
    print("")

# asks if they have played before
answer = False
while True:
    new = input("have you played before?").strip().lower()
    if new in yes:
        print("plays game")
        break
    elif new in no:
        instructions()
        break
    else:
        print(" <error> please enter yes or no")

# asks how much money they would like to spend
while True:
    spend = int(input("how much money do you like like to spend between $0 and $10?"))
    if 10 >= spend > 0:
        break
    else:
        print(" <error> please enter a number between 0 and 10")
