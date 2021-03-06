# variables
yes = ["yes", "y"]
no = ["no", "n"]
rock = ["rock", "r"]
paper = ["paper", "p"]
scissors = ["scissors", "s"]

# functions
def instructions():
    print("")
    print("are you sure about that")
    print("")

def game():
    # asks the user
    while True:
        RPS = input("please choose rock, paper or scissors").strip().lower()
        if RPS in rock or RPS in paper or RPS in scissors:
            break
        else:
            print("<error> Please enter rock, paper or scissors")

    if RPS in rock :
        RPS = "rock"
    elif RPS in scissors:
        RPS = "scissors"
    elif RPS in paper:
        RPS = "paper"

# generates the bot
    import random
    number_RPS = random.randint(1,4)
    if number_RPS == 1:
        bot_RPS = "rock"
    elif number_RPS == 2:
        bot_RPS = "paper"
    else:
        bot_RPS = "scissors"

# compears the players and the bots
    if RPS == bot_RPS:
        print("you draw")
        print("the bot chose {}".format(bot_RPS))

    elif RPS in rock and bot_RPS == "paper":
        print("you lose")
        print("the bot chose {}".format(bot_RPS))
        game.score -=1

    elif RPS in paper and bot_RPS == "scissors":
        print("you lose")
        print("the bot chose {}".format(bot_RPS))
        game.score -= 1

    elif RPS in scissors and bot_RPS == "rock":
        print("you lose")
        print("the bot chose {}".format(bot_RPS))
        game.score -= 1

    else:
        print("☺ YOU WIN ☺")
        print("the bot chose {}".format(bot_RPS))
        game.score += 1

    print("your score is {}".format(game.score))

game.score = 0
# welcomes new users
print("   welcome to")
print("-=-   rock   -=-")
print("-=-   paper  -=-")
print("-=- scissors -=-")
print("")

# asks the user if they know how to play
while True:
    played_before = input("Do you know how to play?").strip().lower()
    if played_before in yes:
        break
    elif played_before in no:
        instructions()
        break
    else:
        print("<error> Please enter yes or no")

game()
while True:
    play_agin = input("do you want to play agin")
    if play_agin in yes:
        game()
    elif play_agin in no:
        # thank the player
        print("thanks for playing")
        break
    else:
        print("<error> please enter yes or no")