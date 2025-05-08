#Removing every instance in the string
'''OrginalStr = str(input("Enter original string:"))
SubStr = str(input("Substring to delete:"))

ModStr = OrginalStr.replace(SubStr, '')

print("The modified string is:", ModStr)'''

#Removing only the first occurence in the string
OrginalStr = str(input("Enter original string:"))
SubStr = str(input("Substring to delete:"))

index = OrginalStr.find(SubStr) #Finding index of string to be deleted
leftstr = OrginalStr[0:index] # Extracting left substring until just before index
rightstr = OrginalStr[index + len(SubStr):] #Extracting right substring

newstr = leftstr + rightstr
print("The modified string is: {}".format(newstr))