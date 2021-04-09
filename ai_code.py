import battleship as bt
import os
import copy
import random
import time

def ships_placement_AI(board, board_size, coordinates, alphabet, active_player):
    sunken_ships_coordinates = []
    ships = bt.available_ships(board_size)
    list_ships = list(ships)
    ship_length = {"1x5":5, "1x4":4, "1x3":3, "1x2":2, "1x1":1}
    discrete_board = copy.deepcopy(board)
    while len(ships) > 0:
        user_input = random.choice(list(coordinates.keys()))
        user_input_orientation = random.choice(["h","v"])
        row, col = coordinates[user_input]
        ship_len = ship_length[list_ships[0]]
        if user_input.upper() in coordinates and discrete_board[row][col] == "-":
            if bt.is_in_the_board(row, col, ship_len, user_input_orientation, coordinates):
                sunken_ship = bt.mark_ship(board, discrete_board, ship_length, coordinates, user_input, user_input_orientation, list_ships, row, col, ship_len)
                ships[list_ships[0]] -= 1
                if ships[list_ships[0]] == 0:
                    ships.pop(list_ships[0])
                list_ships = list(ships)
            else:
                continue
        else:
            continue
        sunken_ships_coordinates.append(sunken_ship)
    print(f"\nThis is the {active_player}'s Battleship Board")  
    bt.print_board(board, board_size, alphabet)
    time.sleep(2)
    print("\n" * 100)
    return board, sunken_ships_coordinates