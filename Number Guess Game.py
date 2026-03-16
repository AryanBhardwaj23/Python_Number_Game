import random

to_guess=random.randint(1, 100)
while True:
    try:
        num=int(input("Guess the number (b/w 1 and 100) : "))
        if num<1 and num>100 :
            print("ENTER NUMBER WITHIN RANGE")
            continue
        if num>to_guess:
            print("GO LOWER")
        elif num<to_guess:
            print("GO HIGHER")
        else:
            print("CONGRATS, YOU FOUND THE NUMBER!!")
            break
    except ValueError:
        print("ENTER VALUE WITHIN GIVEN RANGE")