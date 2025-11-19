
action = input("Enter action (A/S/Q): ")
action = action.lower()
orderno = 1
orderlist = []

while True:
    if action == 'a':
        order = str(input("Enter Customer name and order (e.g. Alice, Burger): "))
        if order.find(", ") == -1:
            print("Invalid format! Please enter as Name, Order")
            action = input("Enter action (A/S/Q): ")
        order = order.split(", ")
        orderlist.append(orderno + order)
        print(orderlist)
    
    if action == 'q':
        print("Ending program...")
        break

    if action == 's':
        orderlist.index('ice cream')
        

        
