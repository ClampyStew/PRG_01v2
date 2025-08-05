import pygame
from random import randint
import os

player = {}
game_map = []
fog = []
file_path = 'saves/gamesave'
day = 1
tm_menu = ''
gp = 0

MAP_WIDTH = 0
MAP_HEIGHT = 0

TURNS_PER_DAY = 20
WIN_GP = 500

minerals = ['copper', 'silver', 'gold']
mineral_names = {'C': 'copper', 'S': 'silver', 'G': 'gold'}
pickaxe_price = [50, 150]

prices = {}
prices['copper'] = (1, 3)
prices['silver'] = (5, 8)
prices['gold'] = (10, 18)

# This function loads a map structure (a nested list) from a file
# It also updates MAP_WIDTH and MAP_HEIGHT
def load_map(filename, map_struct):
    map_file = open(filename, 'r')
    global MAP_WIDTH
    global MAP_HEIGHT
    
    map_struct.clear()
    
    with open(filename, 'r') as f:
        return [list(line.rstrip('\n')) for line in f]
    
    MAP_WIDTH = len(map_struct[0])
    MAP_HEIGHT = len(map_struct)

    map_file.close()

# This function clears the fog of war at the 3x3 square around the player
def clear_fog(fog, player):
    return

def initialize_game(game_map, fog, player):
    # initialize map
    load_map("level1.txt", game_map)

    # TODO: initialize fog
    
    # TODO: initialize player
    #   You will probably add other entries into the player dictionary
    player['x'] = 0
    player['y'] = 0
    player['copper'] = 0
    player['silver'] = 0
    player['gold'] = 0
    player['GP'] = 0
    player['day'] = 0
    player['steps'] = 0
    player['turns'] = TURNS_PER_DAY

    clear_fog(fog, player)
    
# This function draws the entire map, covered by the fof
def draw_map(game_map, fog, player):
    return

# This function draws the 3x3 viewport
def draw_view(game_map, fog, player):
    return

# This function shows the information for the player
def show_information(player):
    print("----- Player Information -----")
    print("Name: {}".format(player))
    print("Portal position: (7, 1)")
    print("Pickaxe level: {} ({})".format(pickaxe_price,pickaxe_price))
    print("------------------------------")
    print("Load: {} / {}")
    print("------------------------------")
    print("GP: {}".format(WIN_GP))
    print("Steps taken: {}".format(WIN_GP))
    print("------------------------------")
    return

# This function saves the game
def save_game(game_map, fog, player):
    # save map
    # save fog
    # save player
    return
        
# This function loads the game
def load_game(game_map, fog, player):
    # load map
    # load fog
    # load player
    return

def show_main_menu():
    print()
    print("--- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
#    print("(H)igh scores")
    print("(Q)uit")
    print("------------------")

def show_town_menu():
    print()
    print("DAY {}".format(day))
    print("----- Sundrop Town -----")
    print("(B)uy stuff")
    print("See Player (I)nformation")
    print("See Mine (M)ap")
    print("(E)nter mine")
    print("Sa(V)e game")
    print("(Q)uit to main menu")
    print("------------------------")
    return

            
def game_end():
    print()
    print("-------------------------------------------------------------")
    print("Woo-hoo! Well done, {}, you have {} GP!".format(player,player['GP']))
    print("You now have enough to retire and play video games every day.")
    print("And it only took you {} days and {} steps! You win!".format(player['day'], player['steps']))
    print("-------------------------------------------------------------")
#--------------------------- MAIN GAME ---------------------------
game_state = 'main'
print("---------------- Welcome to Sundrop Caves! ----------------")
print("You spent all your money to get the deed to a mine, a small")
print("  backpack, a simple pickaxe and a magical portal stone.")
print()
print("How quickly can you get the 1000 GP you need to retire")
print("  and live happily ever after?")
print("-----------------------------------------------------------")

show_main_menu()
user_input = str(input("Your choice? "))
user_input = user_input.lower()
if user_input == 'n':
    player = input("Greetings, miner! What is your name? ")
    print("Pleased to meet you, {}. Welcome to Sundrop Town!".format(player))
    show_town_menu()
    tm_choice = input("Your choice? ")
    while True:
        if tm_choice.lower() == 'i':
            show_information(player)
        if tm_choice.lower() == 'm':

            
elif user_input == 'l':
    try:
        path = "Assignment 1\Assignment\saves"
        save_file = open(path+'gamesave.txt', 'r')
    except:
        print("No Save File Found!")
else:
    print("The only way to win is to not play.")
    