path = "'[PATH]'"
file1 = open(path+"temperature.txt", 'r')
files = file1.readline()
temperatures = files.split(",")

i=0
total=0
print('The temperatures are')
while i < len(temperatures):
    temperatures[i] = float(temperatures[i])
    if temperatures[i] > 29:
        print(' {} ** higher than 29!!!'.format(temperatures[i]))
    else:
        print(' {}'.format(temperatures[i]))
    total = total + temperatures[i]
    i += 1
average = total / len(temperatures)
print('Number of readings: {}'.format(len(temperatures)))
print(f'{"Average Temperature: "}{average:.2f}')