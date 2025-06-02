num = input('Enter number of days: ')

for i in range(1, int(num)+1):
    if i % 7 == 1:
        print('{:3} | {}'.format('Day', 'Task(s)'))

print('{:3} | {}'.format(i, ''))
