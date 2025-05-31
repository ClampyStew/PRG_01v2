target = int(input('Enter target number of pushups: '))
day = 1
specday = int(input('Day {}: How many pushups did you do today? '.format(day)))
total = 0
totalsofar = total + specday

while totalsofar < target:
    day += 1
    specday = int(input('Day {}: How many pushups did you do today? '.format(day)))
    totalsofar += specday
    
if totalsofar >= target:
    print("You did a total of {} pushups.\nYou hit the target in {} days!".format(totalsofar, day))

