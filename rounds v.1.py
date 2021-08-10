
no = ["no", "n"]
yes = ["yes", "y"]

while True:
    play_again = input("do you want to play again")
    if play_again in yes:
        print("game continues")
    elif play_again in no:
        # thank the player
        print("thanks for playing")
    else:
        print("<error> please enter yes or no")
