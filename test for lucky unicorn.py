import random


def token_gen():
    ran_number = random.randint(1,7)
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

token_gen.balance = 100
while True:
    token_gen()
    print(token_gen.balance)
