map =	[ [' ', 'T', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ']
      		]

num_rows = len(map)
num_columns = len(map[0])

#Print the top line
for column in range(num_columns):
    print("+---", end='')
print('+')

for row in range(num_rows):
    for column in map[row]:
        print("| {} ".format(column), end = '')
    print("|")

    for column in range(num_columns):
        print("+---", end = '')
    print('+')