import os

def load_map(filename):
    with open('C:\Users\Zhe Kai\PRG_01v2\Assignment 1\Assignment\level1.txt', 'r') as f:
        return [list(line.rstrip('\n')) for line in f]

def init_fog(rows, cols):
    return [['?' for _ in range(cols)] for _ in range(rows)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def reveal_area(fog, game_map, player, radius=1):
    r, c = player
    for i in range(r - radius, r + radius + 1):
        for j in range(c - radius, c + radius + 1):
            if 0 <= i < len(game_map) and 0 <= j < len(game_map[0]):
                fog[i][j] = game_map[i][j]

def draw_map(game_map, fog, player):
    pr, pc = player
    print("+" + "-" * len(game_map[0]) + "+")
    for i, row in enumerate(fog):
        line = ''
        for j, ch in enumerate(row):
            if i == pr and j == pc:
                line += 'M'
            else:
                line += ch
        print("|" + line + "|")
    print("+" + "-" * len(game_map[0]) + "+")

def draw_view(game_map, fog, player):
    pr, pc = player
    print("+---+")
    for i in range(pr - 1, pr + 2):
        line = "|"
        for j in range(pc - 1, pc + 2):
            if 0 <= i < len(game_map) and 0 <= j < len(game_map[0]):
                if i == pr and j == pc:
                    line += 'M'
                elif fog[i][j] != '?':
                    line += game_map[i][j]
                else:
                    line += '?'
            else:
                line += ' '
        print(line + "|")
    print("+---+")

def move_player(player, direction, game_map):
    dr, dc = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}.get(direction, (0, 0))
    new_r = player[0] + dr
    new_c = player[1] + dc
    if 0 <= new_r < len(game_map) and 0 <= new_c < len(game_map[0]):
        return [new_r, new_c], True  # valid move
    return player, False  # invalid move (off map)

def mine_tile(game_map, player, inventory):
    r, c = player
    tile = game_map[r][c]
    if tile in ['C', 'S', 'G']:
        inventory[tile] = inventory.get(tile, 0) + 1
        game_map[r][c] = ' '
        return True  # mined something
    return False  # nothing to mine

def sell_inventory(inventory):
    values = {'C': 1, 'S': 2, 'G': 5}
    total = 0
    for item, count in inventory.items():
        total += values.get(item, 0) * count
    inventory.clear()
    return total

def town_loop():
    print("\nYou are in the town.")
    print("Options: [m]ap  [e]nter mine  [p]ort back (sell)")
    return input("Action: ").lower()

def mine_loop(game_map, fog, player, inventory, move_count):
    while True:
        clear_screen()
        draw_view(game_map, fog, player)
        print(f"Moves: {move_count} | Inventory: {inventory}")
        cmd = input("Move [w/a/s/d], [p]ort to town: ").lower()

        if cmd == 'p':
            return player, 'town', move_count

        if cmd in 'wasd':
            move_count += 1
            new_player, moved = move_player(player, cmd, game_map)
            if moved:
                player = new_player
                mined = mine_tile(game_map, player, inventory)
            else:
                mined = False  # off-map attempt, no mining
            reveal_area(fog, game_map, player)

    return player, 'mine', move_count

def main():
    game_map = load_map("level.txt")
    fog = init_fog(len(game_map), len(game_map[0]))
    player = [1, 1]  # inside wall at top-left
    inventory = {}
    money = 0
    move_count = 0
    mode = 'town'

    while True:
        clear_screen()
        if mode == 'town':
            action = town_loop()
            if action == 'm':
                clear_screen()
                draw_map(game_map, fog, player)
                input("Press enter to return to town...")
            elif action == 'e':
                reveal_area(fog, game_map, player)
                mode = 'mine'
            elif action == 'p':
                earned = sell_inventory(inventory)
                money += earned
                player = [1, 1]
                print(f"Sold items for ${earned}. Total money: ${money}")
                input("Press enter to continue...")

        elif mode == 'mine':
            player, mode, move_count = mine_loop(game_map, fog, player, inventory, move_count)

if __name__ == "__main__":
    main()
