students = [ ['Aaron', 78, 72, 70], ['Bob', 83, 88, 50], ['Cat', 65, 90, 56] ]

for s in range( len(students) ):  #outer loop for each student
    print( '{:8} '.format(students[s][0]), end='' )
    total = 0

    for t in range(1,4):  #inner loop for each test
        total += students[s][t]
        print( '{:7} '.format(students[s][t]), end='' )

    average = total / 3
    print( '{:8.2f}'.format(average) )
