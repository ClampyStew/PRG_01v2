oddList = []
evenList = []

while True:
    number = int(input("Please enter a number: "))
    if number == 0:
        break
    if number % 2 == 1:
        oddList.append(number)
    else:
        evenList.append(number)

oddList.sort()
print("Odd numbers:", oddList)
evenList.sort()
print("Even numbers:", evenList)