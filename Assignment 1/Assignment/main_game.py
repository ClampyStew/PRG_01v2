
from random import randint
import time
import webbrowser

#Basic global variable for use
path = '[PATH]'
player = {}
game_map = []
fog = []
pick_purchase = 0

MAP_WIDTH = 0
MAP_HEIGHT = 0

TURNS_PER_DAY = 20
WIN_GP = 500

minerals = ['copper', 'silver', 'gold']
mineral_names = {'C': 'copper', 'S': 'silver', 'G': 'gold'}

prices = {'copper': (1, 3), 'silver': (5, 8), 'gold': (10, 18)}

#To ensure correct size of saved map, actual map and map with fow, used later
def sync_fog_with_map(game_map, fog):
    #Ensure fog matches the size of game_map to prevent IndexError.
    # If fog has fewer rows than game_map, add new rows filled with '?'
    while len(fog) < len(game_map):
        fog.append(['?' for _ in range(len(game_map[0]))])
    # If the fog row has fewer columns, pad with '?'
    for y in range(len(game_map)):
        while len(fog[y]) < len(game_map[y]):
            fog[y].append('?')

#6
def draw_map(game_map, fog, player, full=True):
    #Draw either the full map or just the player's viewport.
    if not game_map:
        print("Map not loaded.")
        return
    sync_fog_with_map(game_map, fog)
    if full:
        # Draw entire map with fog
        print("+" + "-" * len(game_map[0]) + "+")
        for y in range(len(game_map)):
            row = "|"
            for x in range(len(game_map[y])):
                if (x, y) == (player['x'], player['y']):
                    row += 'M'
                elif (x, y) == player['portal']:
                    row += 'P'
                else:
                    row += fog[y][x]
            row += "|"
            print(row)
        print("+" + "-" * len(game_map[0]) + "+")
    else:
        # Draw only the viewport (radius based on torch)
        # player.get('magic_torch', False) returns True if player bought the torch.
        radius = 2 if player.get('magic_torch', False) else 1
        width = radius * 2 + 1
        print("+" + "-" * width + "+")
        for y in range(player['y'] - radius, player['y'] + radius + 1):
            row = "|"
            for x in range(player['x'] - radius, player['x'] + radius + 1):
                if 0 <= y < len(game_map) and 0 <= x < len(game_map[0]):
                    if (x, y) == (player['x'], player['y']):
                        row += 'M'
                    elif (x, y) == player['portal']:
                        row += 'P'
                    else:
                        row += fog[y][x]
                else:
                    row += "#"
            row += "|"
            print(row)
        print("+" + "-" * width + "+")

#8
def save_game(game_map, fog, player):
    try:
        with open('savegame.txt', 'w') as f:
            f.write('#PLAYER\n')
            f.write(repr(player) + '\n')
            f.write('#FOG\n')
            for row in fog:
                f.write(''.join(row) + '\n')
            f.write('#MAP\n')
            for row in game_map:
                f.write(''.join(row) + '\n')
        print("Game saved successfully.")
    except Exception as e:
        print("Error saving game:", e)

def load_game(game_map, fog, player):
    try:
        with open('savegame.txt', 'r') as f:
            section = None
            fog.clear()
            game_map.clear()
            for line in f:
                line = line.strip()
                if line == '#PLAYER':
                    section = 'player'
                elif line == '#FOG':
                    section = 'fog'
                elif line == '#MAP':
                    section = 'map'
                elif section == 'player':
                    player_data = eval(line)
                    player.clear()
                    player.update(player_data)
                elif section == 'fog':
                    fog.append(list(line))
                elif section == 'map':
                    game_map.append(list(line))

        global MAP_HEIGHT, MAP_WIDTH
        MAP_HEIGHT = len(game_map)
        MAP_WIDTH = len(game_map[0]) if MAP_HEIGHT > 0 else 0

        sync_fog_with_map(game_map, fog)  #Make sure sizes match
        print("Game loaded successfully.")
    except Exception as e:
        print("Error loading game:", e)

#for loading from save file
def load_map(filename, map_struct):
    global MAP_WIDTH, MAP_HEIGHT
    with open(path+filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f if line.strip()]
    map_struct.clear()
    for line in lines:
        row = list(line)
        map_struct.append(row)
    if map_struct:
        MAP_HEIGHT = len(map_struct)
        MAP_WIDTH = len(map_struct[0])
    else:
        MAP_HEIGHT = MAP_WIDTH = 0

# Clear fog in 3x3 area around player
def clear_fog(fog, player):
    if not game_map:
        return
    sync_fog_with_map(game_map, fog)
    #again, the check will return true if the player has purchased the torch.
    radius = 2 if player.get('magic_torch', False) else 1
    for y in range(player['y'] - radius, player['y'] + radius + 1):
        #transplanting from game_map to fog, basically.
        if 0 <= y < len(game_map):
            for x in range(player['x'] - radius, player['x'] + radius + 1):
                if 0 <= x < len(game_map[y]):
                    fog[y][x] = game_map[y][x]

#user setup and defining player stats
def initialize_game(game_map, fog, player):
    load_map("level1.txt", game_map)
    fog.clear()
    for row in game_map:
        fog.append(['?' for _ in row])
    name = input("Greetings, miner! What is your name? ")
    if name.lower() == 'internetdown':
        webbrowser.open('https://www.youtube.com/watch?v=cQaz11b3rC8')
        time.sleep(24) 
    elif name.replace(" ",'').lower() == 'atomicamnesia':
        webbrowser.open('https://www.youtube.com/watch?v=jDS_y0SisKA')
        print("CatJAM CatJAM CatJAM CatJAM CatJAM")
    print(f"Pleased to meet you, {name}. Welcome to Sundrop Town!")
    player.update({
        'name': name,
        'x': 0,
        'y': 0,
        'GP': 0,
        'copper': 0,
        'silver': 0,
        'gold': 0,
        'day': 1,
        'steps': 0,
        'turns': TURNS_PER_DAY,
        'max_load': 10,
        'pickaxe': 1,
        'portal': (0, 0),
        'magic_torch': False
    })
    clear_fog(fog, player)

#for 'i' input, 5
def show_information(player):
    print("----- Player Information -----")
    print(f"Name: {player['name']}")
    print(f"Current position: ({player['x']}, {player['y']})")
    print(f"Pickaxe level: {player['pickaxe']}")
    print(f"Copper: {player['copper']} Silver: {player['silver']} Gold: {player['gold']}")
    print(f"Load: {player['copper'] + player['silver'] + player['gold']} / {player['max_load']}")
    print(f"GP: {player['GP']}  Steps: {player['steps']}")
    print(f"DAY {player['day']}")
    print("------------------------------")

#for ore selling
def sell_ores(player):
    total = 0
    for m in minerals:
        qty = player[m]
        if qty > 0:
            price = randint(*prices[m])
            print(f"You sell {qty} {m} ore for {qty * price} GP.")
            total += qty * price
            player[m] = 0
    player['GP'] += total
    if total > 0:
        print(f"You now have {player['GP']} GP!")

def show_town_menu():
    print("\nDAY", player['day'])
    print("----- Sundrop Town -----")
    print("(B)uy stuff")
    print("See Player (I)nformation")
    print("See Mine (M)ap")
    print("(E)nter mine")
    print("Sa(V)e game")
    print("(Q)uit to main menu")
    print("------------------------")

#3
def town_loop():
    while True:
        show_town_menu()
        choice = input("Your choice? ").lower()
        if choice == 'b':
            shop_menu()
        elif choice == 'i':
            show_information(player)
        elif choice == 'm':
            draw_map(game_map, fog, player, full=True)
        elif choice == 'e':
            result = mine_loop()
            if result == "town":
                continue  # Stay in town after mine
        elif choice == 'v':
            save_game(game_map, fog, player)
        elif choice == 'q':
            return False

#4
def shop_menu():
    global pick_purchase
    while True:
        print("\n----------------------- Shop Menu -------------------------")
        cost = player['max_load'] * 2
        p_cost = [50, 150]
        if player['pickaxe'] < 3:
            print(f"(P)ickaxe upgrade from level {player['pickaxe']} to {player['pickaxe']+1} for {p_cost[pick_purchase]} GP.")
        print(f"(B)ackpack upgrade to carry {player['max_load'] + 2} items for {cost} GP")
        if not player.get('magic_torch', False):
            print("A magical (T)orch for 30 GP.")
        print("(L)eave shop")
        print("-----------------------------------------------------------")
        print(f"GP: {player['GP']}")
        choice = str(input("Your choice? "))
        if choice.lower() == 'p':
            if pick_purchase < 2 and player['GP'] >= p_cost[pick_purchase]:
                player['GP'] -= p_cost[pick_purchase]
                player['pickaxe'] += 1
                if pick_purchase == 0:
                    print("Congratulations! You can now mine silver!")
                elif pick_purchase == 1:
                    print("Congratulations! You have reached max upgrades for your pickaxe! You can mine all three ores now!")
                pick_purchase += 1
                time.sleep(1)
            elif pick_purchase >= 2:
                print("You cannot upgrade your pickaxe anymore!")
            else:
                print("You cannot afford this upgrade!")
        if choice.lower() == 'b':
            if player['GP'] >= cost:
                player['GP'] -= cost
                player['max_load'] += 2
                print(f"Congratulations! You can now carry {player['max_load']} items!")
                time.sleep(1)
            else:
                print("Not enough GP!")
                time.sleep(1)
        if choice.lower() == 't' and not player.get('magic_torch', False):
            if player['GP'] >= 30:
                player['GP'] -= 30
                player['magic_torch'] = True
                print("You got a magical torch! Now you can see better underground...")
                time.sleep(1)
            else:
                print("Sorry Link, I can't give you the torch. Come back when you're a little mmmm...richer.")
                time.sleep(1)
        if choice.lower() == 'l':
            break

#7
def mine_loop():
    print("--------------------------------------------------------")
    print(f"                       DAY {player['day']}                             ")
    print("--------------------------------------------------------")
    player['turns'] = TURNS_PER_DAY
    player['x'], player['y'] = player['portal']

    while player['turns'] > 0:
        print("\nDAY", player['day'])
        clear_fog(fog, player)
        draw_map(game_map, fog, player, full=False)  # player view
        print(f"Turns left: {player['turns']}  Load: {player['copper'] + player['silver'] + player['gold']} / {player['max_load']}  Steps: {player['steps']}")
        move = input("(WASD) to move, (M)ap, (I)nfo, (P)ortal, (Q)uit to town: ").lower()

        if move in 'wasd':
            dx = {'a': -1, 'd': 1}.get(move, 0)
            dy = {'w': -1, 's': 1}.get(move, 0)
            nx, ny = player['x'] + dx, player['y'] + dy

            if 0 <= nx < MAP_WIDTH and 0 <= ny < MAP_HEIGHT:
                tile = game_map[ny][nx]

                # If it's ore, check conditions before stepping on it
                if tile in mineral_names:
                    ore_name = mineral_names[tile]
                    ore_level_required = {'copper': 1, 'silver': 2, 'gold': 3}[ore_name]

                    # Too weak pickaxe → skip turn
                    if player['pickaxe'] < ore_level_required:
                        print(f"Your pickaxe isn't strong enough to mine {ore_name} ore.")
                        continue

                    # Backpack full → skip turn
                    total_load = player['copper'] + player['silver'] + player['gold']
                    if total_load >= player['max_load']:
                        print("Your backpack is full. You can't carry any more.")
                        continue

                    # Mine ore
                    ore_ranges = {'copper': (1, 5), 'silver': (1, 3), 'gold': (1, 2)}
                    qty = randint(*ore_ranges[ore_name])
                    available = player['max_load'] - total_load
                    mined = min(qty, available)
                    player[ore_name] += mined
                    print(f"You mined {qty} piece(s) of {ore_name}. But you can only carry {mined}.")
                    game_map[ny][nx] = ' '  # remove ore

                # Move player
                player['x'], player['y'] = nx, ny
                player['steps'] += 1
                player['turns'] -= 1
                clear_fog(fog, player)

                # Town tile
                if tile == 'T':
                    print("You returned to town.")
                    player['day'] += 1
                    return "town"

            else:
                print("You can't move there!")
                player['turns'] -= 1

        elif move == 'm':
            draw_map(game_map, fog, player, full=True)  # full map with fog
        elif move == 'i':
            show_information(player)
        elif move == 'p':
            player['portal'] = (player['x'], player['y'])
            print("------------------------------------------------------")
            print("You place your portal stone here and zap back to town.")
            player['day'] += 1
            sell_ores(player)
            return "town"
        elif move == 'q':
            print("Returning to town...")
            player['day'] += 1
            return "town"

    # Exhaustion
    print("You are exhausted. You place your portal stone and zap back to town.")
    player['portal'] = (player['x'], player['y'])
    player['day'] += 1
    sell_ores(player)
    return "town"

#2
def show_main_menu():
    print("\n--- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
    print("(Q)uit")
    print("------------------")

#1
def main_game_loop():
    print("---------------- Welcome to Sundrop Caves! ----------------")
    print("You spent all your money to get the deed to a mine, a small")
    print("  backpack, a simple pickaxe and a magical portal stone.\n")
    print("How quickly can you get the 500 GP you need to retire")
    print("  and live happily ever after?")
    print("-----------------------------------------------------------")

    while True:
        show_main_menu()
        cmd = input("Your choice? ").lower()

        if cmd == 'n':
            initialize_game(game_map, fog, player)
            while True:
                if not town_loop():  # returns False if player chooses (Q) in town
                    break
                if player['GP'] >= WIN_GP:
                    print("\n-------------------------------------------------------------")
                    print(f"Woo-hoo! Well done, {player['name']}, you have {player['GP']} GP!")
                    print(f"You now have enough to retire and play video games every day.")
                    print(f"And it only took you {player['day']} days and {player['steps']} steps! You win!")
                    print("-------------------------------------------------------------")
                    break

        elif cmd == 'l':
            load_game(game_map, fog, player)
            while True:
                if not town_loop():
                    break
                if player['GP'] >= WIN_GP:
                    print("\n-------------------------------------------------------------")
                    print(f"Woo-hoo! Well done, {player['name']}, you have {player['GP']} GP!")
                    print(f"You now have enough to retire and play video games every day.")
                    print(f"And it only took you {player['day']} days and {player['steps']} steps! You win!")
                    print("-------------------------------------------------------------")
                    break

        elif cmd == 'q':
            print("Goodbye!")
            return  # Exit the game completely

main_game_loop()