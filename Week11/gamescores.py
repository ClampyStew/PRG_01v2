players = ['Hafu', 'Toast', 'Pokimane', 'Pewdiepie', 'Ninja', 'Markiplier']
results = [ [98, 107, 87, 121],
              [88, 111],
              [79, 130, 99],
              [86, 100, 121, 66, 98],
              [108, 79, 92],
              [77, 126, 93, 100, 73, 89],
            ]

#print table heading
print("{:12} {:5} {:4} {:5}".format('Player', 'Games', 'Wins', 'Total'))

for index in range(len(players)):
    total = 0
    num_wins = 0
    for game_score in results[index]:
        total += game_score
        if game_score >= 100:
            num_wins += 1
        
    print("{:12} {:^5} {:^4} {:^5}".format(players[index], len(results[index]), num_wins, total))