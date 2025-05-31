usernumber = int(input("Please enter a number: "))
multiplyby = 1

while multiplyby <= 10:
    mutiplied = (usernumber*multiplyby)
    print("{} x {} = {}".format(usernumber, multiplyby, mutiplied))
    multiplyby = multiplyby + 1