import random
def token_gen():
    ran_number = random.randint(0,101)
    if 75 <= ran_number <= 100:
        token_gen.token = "unicorn"
    elif 50 <= ran_number < 75:
        token_gen.token = "horse"
    elif 25 <= ran_number <50:
        token_gen.token = "zebra"
    else:
        token_gen.token = "donkey"
