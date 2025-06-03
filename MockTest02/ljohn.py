#Set the price of the items
price_coffee = 4.5
price_tea = 4
price_pastry = 6.3

#Prompt the user to enter the quantity and price of each item 
qty_coffee = int(input("Enter the quantity of coffee ordered: "))
qty_tea = int(input("Enter the quantity of tea ordered: "))
qty_pastry = int(input("Enter the quantity of pastry: "))

#Calculate the total bill
gst = (9/100)
nogst = (qty_coffee*price_coffee)+(qty_tea*price_tea)+(qty_pastry*price_pastry)
total_bill = (gst*nogst)+nogst

#Display the total bill including GST
print(f"{"Your total cost is $"}{total_bill:.2f}")

#Display voucher message if entitled to the voucher
if total_bill > 20:
    print("You've spent more than $20!\nYou get a 20 percent discount voucher for your next visit.")