# adventure.py 6/28/18

# Added functionality: easier user inputs,
# change number of enemies, enemy movement,
# map boundaries, implement dodge chance,
# implement game over when all monsters are dead

import random
import os
from time import sleep


# clear terminal screen and keep print statement at the top
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Connect Four!")


width = 5  # the width of the board
height = 5  # the height of the board

# keep track of enemy i and j position
enemy_location = {}

# initialize enemy_location dict
num_enemies = 3
for i in range(num_enemies):
    enemy_location['enemy' + str(i)] = []

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position in the center
player_i = height // 2
player_j = width // 2

# add multiple enemies in random locations
# update the enemy location dict accordingly
for i in range(num_enemies):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    enemy_location['enemy' + str(i)] = [enemy_i, enemy_j]

# loop until the user says 'done' or dies
while True:

    # get the command from the user
    print('What is your command?')
    # noinspection SpellCheckingInspection
    command = input("(u)p, (d)own, (l)eft, (r)ight, "
                    "('done' or enter to quit): ")

    if command.lower() in ['', 'done']:
        print("Goodbye!")
        break  # exit the game

    # boundary checking
    elif command.lower() in ['l', 'left']:
        if player_j - 1 >= 0:
            player_j -= 1  # move left
    elif command.lower() in ['r', 'right']:
        if player_j + 1 <= width - 1:
            player_j += 1  # move right
    elif command.lower() in ['u', 'up']:
        if player_i - 1 >= 0:
            player_i -= 1  # move up
    elif command.lower() in ['d', 'down']:
        if player_i + 1 <= height - 1:
            player_i += 1  # move down
    else:
        print("That was not a valid input.")
        continue

    # make the monsters move randomly
    for i in range(num_enemies):
        move = random.choice(['move_i', 'move_j'])  # move either up or down
        if enemy_location['enemy' + str(i)]:  # check if enemy is alive
            # move one space in one direction, or don't move at all
            new_enemy_i = enemy_location['enemy' + str(i)][0] + \
                random.choice([-1, 0, 1])
            new_enemy_j = enemy_location['enemy' + str(i)][1] + \
                random.choice([-1, 0, 1])

            # update location if within boundaries
            if 'move_i' in move:
                if 0 <= new_enemy_i <= height - 1:
                    enemy_location['enemy' + str(i)][0] = new_enemy_i
            elif 'move_j' in move:
                if 0 <= new_enemy_j <= width - 1:
                    enemy_location['enemy' + str(i)][1] = new_enemy_j

    # check if the player is on the same space as an enemy
    if [player_i, player_j] in enemy_location.values():
        print("You've encountered an enemy!")
        print("What will you do?")
        # noinspection SpellCheckingInspection,SpellCheckingInspection
        action = input("(a)ttack, (r)un, (d)odge: ")
        if action.lower() in ['a', 'attack']:
            print('You\'ve slain the enemy!')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        elif action.lower() in ['r', 'run']:
            print("Successfully ran from the monster.")
            continue

        # 1 in 3 dodge chance
        elif action.lower() in ['d', 'dodge']:
            if 0 == random.choice([0, 1, 2]):
                print("Successfully dodged the attack!")
            else:
                print("Failed to dodge. You lose.")
                break

        sleep(1)

    # remove monster from monster list
    for i in range(num_enemies):
        if [player_i, player_j] == enemy_location['enemy' + str(i)]:
            enemy_location['enemy' + str(i)] = []

    # print out the board
    clear()
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            if [i, j] in list(enemy_location.values()):
                print('§', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()

    # check if all monsters have been killed
    if all(value == [] for value in enemy_location.values()):
        print("Congrats! You've killed all the monsters!")
        print("Thanks for playing!")
        break
