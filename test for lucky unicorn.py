import random


def token_gen():
    ran_number = random.randint(1,8)
    if ran_number == 1 :
        token_gen.token = "unicorn"
    elif ran_number == 2 or ran_number == 3 :
        token_gen.token = "horse"
    elif ran_number == 4 or ran_number ==5 :
        token_gen.token = "zebra"
    else:
        token_gen.token = "donkey"
