numbers = [2, 7, 11, 6, 7, 3, 17, 7, 12, 41, 8, 11, 13, 10, 15]

result = []

for value in numbers:
    #check for even
    if value % 2 == 0:
        continue
    #skip duplicate value
    if value in result:
        continue
    result.append(value)
    #end if 5 numbers found
    if len(result) == 5:
        break
print(result)