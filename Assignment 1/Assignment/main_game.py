from random import randint
import time

path = 'C:\\Users\\Zhe Kai\\PRG_01v2\\Assignment 1\\Assignment\\'
player = {}
game_map = []
fog = []

MAP_WIDTH = 0
MAP_HEIGHT = 0

TURNS_PER_DAY = 20
WIN_GP = 500

minerals = ['copper', 'silver', 'gold']
mineral_names = {'C': 'copper', 'S': 'silver', 'G': 'gold'}
pickaxe_price = [50, 150]

prices = {'copper': (1, 3), 'silver': (5, 8), 'gold': (10, 18)}

# Load the map from file
def load_map(filename, map_struct):
    global MAP_WIDTH, MAP_HEIGHT
    with open(path+filename, 'r') as f:
        lines = f.readlines()
    map_struct.clear()
    for line in lines:
        map_struct.append(list(line.strip()))
    MAP_HEIGHT = len(map_struct)
    MAP_WIDTH = len(map_struct[0])

# Clear fog in 3x3 area around player
def clear_fog(fog, player):
    for y in range(player['y'] - 1, player['y'] + 2):
        for x in range(player['x'] - 1, player['x'] + 2):
            if 0 <= y < MAP_HEIGHT and 0 <= x < MAP_WIDTH:
                fog[y][x] = game_map[y][x]

def initialize_game(game_map, fog, player):
    load_map("level1.txt", game_map)
    fog.clear()
    for row in game_map:
        fog.append(['?' for _ in row])
    name = input("Greetings, miner! What is your name? ")
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
        'portal': (0, 0)
    })
    clear_fog(fog, player)

def draw_map(game_map, fog, player):
    print("+" + "-" * MAP_WIDTH + "+")
    for y in range(MAP_HEIGHT):
        row = "|"
        for x in range(MAP_WIDTH):
            if (x, y) == (player['x'], player['y']):
                row += 'M'
            elif (x, y) == player['portal']:
                row += 'P'
            else:
                row += fog[y][x]
        row += "|"
        print(row)
    print("+" + "-" * MAP_WIDTH + "+")

def draw_view(game_map, fog, player):
    print("+---+")
    for y in range(player['y'] - 1, player['y'] + 2):
        row = "|"
        for x in range(player['x'] - 1, player['x'] + 2):
            if 0 <= y < MAP_HEIGHT and 0 <= x < MAP_WIDTH:
                if (x, y) == (player['x'], player['y']):
                    row += 'M'
                else:
                    row += game_map[y][x]
            else:
                row += '#'
        row += "|"
        print(row)
    print("+---+")

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

def town_loop():
    sell_ores(player)
    while True:
        show_town_menu()
        choice = input("Your choice? ").lower()
        if choice == 'b':
            shop_menu()
        elif choice == 'i':
            show_information(player)
        elif choice == 'm':
            draw_map(game_map, fog, player)
        elif choice == 'e':
            mine_loop()
            break
        elif choice == 'v':
            print("Game saved. (not implemented)")
        elif choice == 'q':
            break


def shop_menu():
    while True:
        print("\n----------------------- Shop Menu -------------------------")
        cost = player['max_load'] * 2
        print(f"(B)ackpack upgrade to carry {player['max_load'] + 2} items for {cost} GP")
        print("(L)eave shop")
        print("-----------------------------------------------------------")
        print(f"GP: {player['GP']}")
        choice = str(input("Your choice? "))
        if choice.lower() == 'b':
            if player['GP'] >= cost:
                player['GP'] -= cost
                player['max_load'] += 2
                print(f"Congratulations! You can now carry {player['max_load']} items!")
                time.sleep(1)
            else:
                print("Not enough GP!")
                time.sleep(1)
        elif choice == 'l':
            break


def mine_loop():
    print("\n--- Entering the Mine ---")
    player['turns'] = TURNS_PER_DAY
    player['x'], player['y'] = player['portal']
    while player['turns'] > 0:
        print("\nDAY", player['day'])
        draw_view(game_map, fog, player)
        print(f"Turns left: {player['turns']}  Load: {player['copper'] + player['silver'] + player['gold']} / {player['max_load']}  Steps: {player['steps']}")
        move = input("(WASD) to move, (M)ap, (I)nfo, (P)ortal, (Q)uit to town: ").lower()
        if move in 'wasd':
            dx = {'a': -1, 'd': 1}.get(move, 0)
            dy = {'w': -1, 's': 1}.get(move, 0)
            nx, ny = player['x'] + dx, player['y'] + dy
            if 0 <= nx < MAP_WIDTH and 0 <= ny < MAP_HEIGHT:
                if game_map[ny][nx] in mineral_names:
                    if player['copper'] + player['silver'] + player['gold'] >= player['max_load']:
                        print("You can't carry any more, so you can't go that way.")
                    else:
                        qty = randint(*{'C': (1,5), 'S': (1,3), 'G': (1,2)}[game_map[ny][nx]])
                        ore = mineral_names[game_map[ny][nx]]
                        available = player['max_load'] - sum(player[m] for m in minerals)
                        taken = min(qty, available)
                        player[ore] += taken
                        print(f"You mined {qty} piece(s) of {ore}. But you can only carry {taken}.")
                        player['x'], player['y'] = nx, ny
                        clear_fog(fog, player)
                        player['steps'] += 1
                        player['turns'] -= 1
                else:
                    player['x'], player['y'] = nx, ny
                    clear_fog(fog, player)
                    player['steps'] += 1
                    player['turns'] -= 1
                    if game_map[ny][nx] == 'T':
                        print("You returned to town.")
                        player['day'] += 1
                        return
            else:
                print("You can't move there!")
                player['turns'] -= 1
        elif move == 'm':
            draw_map(game_map, fog, player)
        elif move == 'i':
            show_information(player)
        elif move == 'p':
            player['portal'] = (player['x'], player['y'])
            print("You place your portal stone here and zap back to town.")
            player['day'] += 1
            return
        elif move == 'q':
            print("Returning to town...")
            player['day'] += 1
            return

    print("You are exhausted. You place your portal stone and zap back to town.")
    player['portal'] = (player['x'], player['y'])
    player['day'] += 1

def show_main_menu():
    print("\n--- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
    print("(Q)uit")
    print("------------------")

# Main Game Loop
print("---------------- Welcome to Sundrop Caves! ----------------")
print("You spent all your money to get the deed to a mine, a small")
print("  backpack, a simple pickaxe and a magical portal stone.\n")
print("How quickly can you get the 500 GP you need to retire")
print("  and live happily ever after?")
print("-----------------------------------------------------------")

game_running = True
while game_running:
    show_main_menu()
    cmd = input("Your choice? ").lower()
    if cmd == 'n':
        initialize_game(game_map, fog, player)
        town_loop()
        if player['GP'] >= WIN_GP:
            print("\n-------------------------------------------------------------")
            print(f"Woo-hoo! Well done, {player['name']}, you have {player['GP']} GP!")
            print(f"You now have enough to retire and play video games every day.")
            print(f"And it only took you {player['day']} days and {player['steps']} steps! You win!")
            print("-------------------------------------------------------------")
    elif cmd == 'l':
        print("Load game not implemented yet.")
    elif cmd == 'q':
        print("Goodbye!")
        game_running = False
