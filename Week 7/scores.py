with open('scores.txt') as f:
    heading = f.readline().strip(',')
    print('{:10} {:10} {:6} {:6} {:7}'.format(heading[0],heading[1],heading[2],heading[3],'Average'))
    highest = 0
    for line in f:
        data = line.strip().split(',')
        average = (int(data[-2]) + int(data[-1]))/2
        if average > highest:
            highest = average
            highestName = data[1]
            print('{:10} {:10} {:^6} {:^6} {:7.2f}'.format(data[0],data[1],data[2],data[3],'Average'))
print('{} has the highest average score of {}'.format(highestName, highest))