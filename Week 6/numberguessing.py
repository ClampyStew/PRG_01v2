import random
correctnumber = random.randint(1,100)
attempt = 1


#If you want to cheat
print(correctnumber)

userguess = int(input("Welcome to Number Guessing Game\nTry {}: Enter a number between 1 and 100 (or -1 to end): ".format(attempt)))
while userguess != (-1) and attempt<5:
    if userguess > correctnumber:
        print("{} is too high".format(userguess))
        attempt += 1
        userguess = int(input("Try {}: Enter a number between 1 and 100 (or -1 to end): ".format(attempt)))
    if userguess < correctnumber:
        print("{} is too low".format(userguess))
        attempt += 1
        userguess = int(input("Try {}: Enter a number between 1 and 100 (or -1 to end): ".format(attempt)))
    if userguess == correctnumber:
        print("Bingo, you've got it right!\nBye-Bye!")
        break
    if attempt == 5:
        print("You didn't guess the number correctly. The number was {}.".format(correctnumber))
else:
    print("Bye-Bye!")

