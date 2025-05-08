#For Qn B: Movie Budgeting
import math
Snack = 2.50
Drink = 1.80
Ticket = 12.00

IntTickets = float(input("Enter the number of movie tickets:"))
IntSnack = float(input("Enter the number of snacks:"))
IntDrinks = float(input("Enter the number of drinks:"))

#Calculating price without GST first then using the value as a way to obtain just the GST Price
NetTotal = float((IntSnack*Snack) + (IntDrinks*Drink) + (IntTickets*Ticket))
GrandTotal = float(NetTotal + (NetTotal*0.10))
GrandTotal = round(GrandTotal, 2)

print("Total cost of purchase is ", "$",GrandTotal, sep='')