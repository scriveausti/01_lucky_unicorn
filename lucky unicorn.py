# setting variables
no = ["no", "n"]
yes = ["yes", "y"]

# welcomes user
print("Welcome to lucky unicorn")
input("press enter to continue")

# instructions
def instructions():
    print("")
    print(" -=-  how to play -=-  ")
    print("")
    print(" enter the amount of money you would like to gamble ")
    print(" then it will generate a token that will be a zebra, horse, donkey or unicorn")
    print(" if you get a unicorn you win $5. if you get a zebra or horse you get 50c back")
    print(" if you get a donkey you don't get any money back")
    print("")

# asks if they have played before
answer = False
while True:
    new = input("have you played before?").strip().lower()
    if new in yes:
        break
    elif new in no:
        instructions()
        break
    else:
        print(" <error> please enter yes or no")

# asks how much money they would like to spend
while True:
    try:
        spend = int(input("how much money do you like like to spend between $0 and $10?"))
        if 10 >= spend > 0:
            break
        else:
            print(" <error> please enter a whole number between 0 and 10")
    except:
        print(" <error> please enter a whole number between 0 and 10")

while True:
    import random
    ran_number = random.randint(1,8)
    if ran_number == 1 :
        token = "unicorn"

    elif ran_number == 2 or ran_number == 3 :
        token = "horse"

    elif ran_number == 4 or ran_number ==5 :
        token = "zebra"

    else:
        token = "donkey"
