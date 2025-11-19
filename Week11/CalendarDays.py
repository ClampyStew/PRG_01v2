#Prompt user to enter number of days and first day of the week
days = input('Enter number of days: ')
day_of_week = input('When is the first day of the week?: ')

#Print calendar
week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
index = week.index(day_of_week.capitalize())

print()
print('{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'.format('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'))
d = 1
while d <= int(days):
    for i in range(7):
        if d > int(days):
            break
        elif d == 1 and i < index:
            print('{:4}'.format(''),end='')
            continue

        print('{:4}'.format(d), end='')
        d+=1
    print()