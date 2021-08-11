
no = ["no", "n"]
yes = ["yes", "y"]

while True:
    if token_gen.balance < 1:
        print("you ran out of money")
        print("thanks for playing")
        break
    else:
        play_again = input("do you want to play again")
        if play_again in yes:
            token_gen()
        elif play_again in no:
            print("thanks for playing")
            break
        else:
            print("<error> please enter yes or no")

