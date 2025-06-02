correctpin = 12345
tries = 2
userinput = int(input("Enter pin: "))

while userinput != correctpin:
    print(f'{"Invalid pin. Please try again.\n"}{"You have {} tries left."}'.format(tries))
    tries -= 1
    userinput = int(input("Enter pin: "))
    if tries == 0:
        print("Invalid pin. You have no more tries.\nYour account is locked.")
        break
else:
    print("Correct pin entered.")
