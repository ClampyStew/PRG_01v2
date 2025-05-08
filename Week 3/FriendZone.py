Friends = ["Izzat", "Bryan", "Dalton", "Ethan", "Issac"]
NewFren = str(input("What is the name of your new friend? "))
Friends.append(NewFren)
print("My friends are:", Friends)

friendszone = str(input("Who do you want to friendszone? "))
index = Friends.index(friendszone)
print('{} was in position. He will be friendzoned.'.format(Friends[index], index))
Friends.pop(index)
print("My eligible friends are now:", Friends)