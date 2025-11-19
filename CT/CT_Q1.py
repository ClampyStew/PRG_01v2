
ticket_price = 12.00

seat_type = str(input("Choose seat type [Regular / Premium]: "))
snack = str(input("Would you like to add a popcorn combo? [Yes / No]: "))
senior = str(input('Are you a "senior" citizen? [Yes / No]: '))

if seat_type.lower() == 'premium':
    ticket_price += 5.00

if snack.lower() == 'yes':
    ticket_price += 4.50

if senior.lower() == 'yes':
    total = ticket_price * (75/100)
else:
    total = ticket_price

print("Your total bill is: ${:.2f}".format(total))