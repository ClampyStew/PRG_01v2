#This is the testing file for individual functions
#DO NOT REMOVE ANY LINES, JUST COMMENT IT
user_input = str(input("Your choice? "))
user_input = user_input.lower()
'''while True:
    if user_input == 'n':
        username = input("Greetings, miner! What is your name? ")
        print('Pleased to meet you, {}. Welcome to Sundrop Town!'.format(username))
        break
    if user_input == 'l':
        print('Loading Save... This may take a while.')
    if user_input == 'q':
        print('Thanks for playing! pedro ૮ • ﻌ - ა')
        break'''

import os
file_path = '[PATH]'
while True:
    if user_input == 'n':
        username = input("Greetings, miner! What is your name? ")
        print('Pleased to meet you, {}. Welcome to Sundrop Town!'.format(username))
        break
    if user_input == 'l':
        print('Loading Save... This may take a while.')
        if os.path.exists(file_path):
            print('Save file found! Loading...')
            break
        else:
            print('An unknown exception occured. Did Dokkaebi hack your files?')
            break
    if user_input == 'q':
        print('The only winning move is to not play. pedro ૮ • ﻌ - ა')
        break

