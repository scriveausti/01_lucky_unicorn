# imports
import random

# setting variables
no = ["no", "n"]
yes = ["yes", "y"]


# number checker
def number_check():
    while True:
        try:
            print("")
            number_check.spend = int(input("how much money do you like like to spend between $0 and $10?"))
            if 10 >= number_check.spend > 0:
                break
            else:
                print(" <error> please enter a whole number between 0 and 10")
        except:
            print(" <error> please enter a whole number between 0 and 10")

# token gen
def token_gen():
    ran_number = random.randint(1,8)
    if ran_number == 1 :
        token_gen.token = "unicorn"
        token_gen.balance += 4
    elif ran_number == 2 or ran_number == 3 :
        token_gen.token = "horse"
        token_gen.balance -= 0.5
    elif ran_number == 4 or ran_number ==5 :
        token_gen.token = "zebra"
        token_gen.balance -= 0.5
    else:
        token_gen.token = "donkey"
        token_gen.balance -= 1

token_gen.balance = 0

# instructions
def instructions():
    print("")
    print(" -=-  how to play -=-  ")
    print("")
    print(" enter the amount of money you would like to gamble, each round costs $1")
    print(" then it will generate a token that will be a zebra, horse, donkey or unicorn")
    print(" if you get a unicorn you win $5. if you get a zebra or horse you get 50c back")
    print(" if you get a donkey you don't get any money back")
    print("")

# functions variables
token_gen.balance = 0

# welcomes user
print("Welcome to lucky unicorn")
input("press enter to continue")

# asks if they have played before
answer = False
while True:
    print("")
    new = input("have you played before?").strip().lower()
    if new in yes:
        break
    elif new in no:
        instructions()
        break
    else:
        print(" <error> please enter yes or no")

# asks how much money they would like to spend
number_check()
# asks the user if they want
while True:
    sure = input("are you sure you want {} rounds".format(number_check.spend)).strip().lower()
    if sure in yes:
        break
    elif sure in no:
        number_check()
    else:
        print(" <error> please enter yes or no")

token_gen.balance = number_check.spend
token_gen()
print("")
print("you got {}".format(token_gen.token))
print("your balance is now ${}".format(token_gen.balance))
print("")

while True:
    if token_gen.balance < 1:
        print("you ran out of money")
        break
    else:
        play_again = input("do you want to continue playing")
        if play_again in yes:
            token_gen()
            print("you got {}".format(token_gen.token))
            print("your balance is now ${}".format(token_gen.balance))
        elif play_again in no:
            break
        else:
            print(" <error> please enter yes or no")

print("")
print("you made ${}".format(token_gen.balance - number_check.spend))
input("thank you for playing")
