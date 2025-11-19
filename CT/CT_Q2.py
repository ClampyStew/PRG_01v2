
import random
bustimeleft = random.randint(2, 15)
passengers = 0

while True:
    print("A new bus will arrive in {} minutes.\nPassengers waiting: {}".format(bustimeleft, passengers))
    user = input("Press Enter to move the time forward by 1 minute, or type 'exit' to quit: ")
    if user == 'exit':
        break
    passengers += random.randint(0, 1)
    bustimeleft -= 1
    print("Passenger Arrived!\n")
    if bustimeleft == 0:
        print("The bus has arrived! {} passengers boarded.\n".format(passengers))
        bustimeleft = random.randint(2, 15)
        passengers = 0
