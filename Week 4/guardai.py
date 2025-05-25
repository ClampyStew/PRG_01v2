sees_player = str(input("Does the guard see the player (y/n)? "))

if sees_player == "n":
    response = "The guard waits."
elif sees_player == "y":
    playerdist = int(input("How far away is the player? "))
    if playerdist <= 1:
        response = "The guard attacks!"
    elif (playerdist >= 2) and (playerdist <= 4):
        response = "The guard advances."
    elif playerdist >= 5:
        response = "The guard wait."

print (response) 