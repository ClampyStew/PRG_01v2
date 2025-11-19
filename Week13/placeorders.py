prices = {'chicken' : 8.50,\
          'steak' : 13.80,\
          'fish' : 9.80,\
          'pasta' : 9.50,\
          'coffee' : 2.50,\
          'tea' : 1.80,\
          'water' : 0.50}

orders = {}

def showMenu():
    print()
    print("--------------------")
    print("1. Add Order")
    print("2. Summarize Orders")
    print("3. Quit")
    print("--------------------")

def showPrices():
    print("{:10s}{:6s}".format("Item", "Price"))
    print("{:10s}{:6s}".format("----", "-----"))
    for item in prices:
        print("{:10s}{:0.2f}".format(item.capitalize(), prices[item]))

choice = 0
while choice != 3:
    showMenu()
    choice = int(input("Your Choice? "))

    if choice == 1:
        showPrices()
        food = input("Your Order? ").lower()
        if food in prices:
            quantity = int(input("How many sets? "))
        if food not in orders:
            orders[food] = quantity
        else:
            orders[food] += quantity
    print('{} sets of {} ordered.'.format(quantity, food))
    else:
        print(food + " is not available.")

if choice == 2:
    print("{:10s} {:6s}".format("Item", "Quantity"))
    print("{:10s} {:6s}".format("----", "--------"))
    total = 0.0
    for item in orders:
        print("{:10s} {:<6d}".format(item.capitalize(), orders[item]))
        total += (orders[item] * prices[item])
    print("Total cost = ${:.2f}".format(total))