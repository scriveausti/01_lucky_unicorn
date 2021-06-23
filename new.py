def nextline():
    next_line = False
    while next_line == False :
        next = input("go to next line?(yes or no)")
        next = next.lower().strip()
        if next == "yes":
            next_line = True
        else:
            next_line = False

nextline()
print("next line")

