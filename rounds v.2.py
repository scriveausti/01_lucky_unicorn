
no = ["no", "n"]
yes = ["yes", "y"]

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
