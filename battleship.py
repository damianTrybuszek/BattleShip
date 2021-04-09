import string
import copy
import random
import time
import sys
from termcolor import colored
import graphics
import os

def game_quit(text):
    if text.lower() == 'quit':
        sys.exit()

def user_input_board_size():
    while True:
        board_size = input("Please insert board size: ")
        game_quit(board_size)
        if board_size.isdigit(): 
            board_size = int(board_size)
            if board_size in range(5,11):
                return board_size
            else:
                print(f"Please provide the number within the correct range (minimum - 5, maximum - 10)!")
        else:
            print(f"Please provide valid numeric input (5-10)!")

def user_input_ver_or_hor():
    while True:
        user_input_orientation = input(f"Please select orientation (H)oritzontal or (V)ertical: ")
        game_quit(user_input_orientation)
        if user_input_orientation.lower() == "h" or user_input_orientation.lower() == "v":
            return user_input_orientation
        else:
            print("Please select a valid orientation ('H' or 'V')! ")

def is_in_the_board(row, col, ship_len, user_input_orientation, coordinates):
    temp_row = row
    temp_col = col
    for i in range(ship_len):
        if (temp_row, temp_col) not in coordinates.values():
            return False
        if user_input_orientation.lower() == "h" and (temp_row, temp_col) in coordinates.values():
            temp_col += 1 
        if user_input_orientation.lower() == "v" and (temp_row, temp_col) in coordinates.values():
            temp_row += 1
    return True

def mark_ship(board, discrete_board, ship_length, coordinates, user_input, user_input_orientation, list_ships, row, col, ship_len):
    sunken_ships = []
    discrete_row = copy.deepcopy(row)
    discrete_col = copy.deepcopy(col)
    for i in range(ship_len):
        if discrete_board[row][col] == "-":
            board[row][col] = "X"
            sunken_ships.append((row, col))
            if user_input_orientation.lower() == "h":
                col += 1
            elif user_input_orientation.lower() == "v":
                row += 1
        else: 
            print(f"This place is already used!")
            break

    for i in range(ship_len):
        discrete_board[discrete_row][discrete_col] = "X"
        if user_input_orientation.lower() == "h":
            if (discrete_row-1, discrete_col) in coordinates.values():
                discrete_board[discrete_row-1][discrete_col] = "X"
            if (discrete_row+1, discrete_col) in coordinates.values():
                discrete_board[discrete_row+1][discrete_col] = "X"
            if (discrete_row, discrete_col-1) in coordinates.values():
                discrete_board[discrete_row][discrete_col-1] = "X"
            if (discrete_row, discrete_col+1) in coordinates.values():
                discrete_board[discrete_row][discrete_col+1] = "X"
            discrete_col += 1
        elif user_input_orientation.lower() == "v":
            if (discrete_row-1, discrete_col) in coordinates.values():
                discrete_board[discrete_row-1][discrete_col] = "X"
            if (discrete_row+1, discrete_col) in coordinates.values():
                discrete_board[discrete_row+1][discrete_col] = "X"
            if (discrete_row, discrete_col-1) in coordinates.values():
                discrete_board[discrete_row][discrete_col-1] = "X"
            if (discrete_row, discrete_col+1) in coordinates.values():
                discrete_board[discrete_row][discrete_col+1] = "X"
            discrete_row += 1
    return sunken_ships

def ships_placement(board, board_size, coordinates, alphabet, active_player):
    sunken_ships_coordinates = []
    print(f"\nHello {active_player}! Please place Your ships on the board!")
    ships = available_ships(board_size)
    list_ships = list(ships)
    ship_length = {"1x5":5, "1x4":4, "1x3":3, "1x2":2, "1x1":1}
    discrete_board = copy.deepcopy(board)
    while len(ships) > 0:
        print_board(board, board_size, alphabet)
        user_input = input(f"{active_player} please place your ships on the map. Available ships for placement: {ships}. Current ship being placed: {list_ships[0]}. Please select a valid coordinate: ")
        game_quit(user_input)
        if user_input.upper() in coordinates.keys():
            user_input_orientation = user_input_ver_or_hor()
            row, col = coordinates[user_input.upper()]
            ship_len = ship_length[list_ships[0]]
            if discrete_board[row][col] == "-":
                if is_in_the_board(row, col, ship_len, user_input_orientation, coordinates):
                    sunken_ship = mark_ship(board, discrete_board, ship_length, coordinates, user_input, user_input_orientation, list_ships, row, col, ship_len)
                    ships[list_ships[0]] -= 1
                    if ships[list_ships[0]] == 0:
                        ships.pop(list_ships[0])
                    list_ships = list(ships)
                    sunken_ships_coordinates.append(sunken_ship)
                else:
                    print(f"Ooops, you can't place a ship like that! Try again!")
            else:
                print(f"{user_input.upper()} is already taken! Try another one. ")
        else:
            print("Please select a valid coordinate!")
    print(f"\nThis is the {active_player}'s Battleship Board")  
    print_board(board, board_size, alphabet)
    input("Press Enter to continue...")
    print(100 * "\n")
    return board, sunken_ships_coordinates

def ships_placement_AI(board, board_size, coordinates, alphabet, active_player):
    sunken_ships_coordinates = []
    ships = available_ships(board_size)
    list_ships = list(ships)
    ship_length = {"1x5":5, "1x4":4, "1x3":3, "1x2":2, "1x1":1}
    discrete_board = copy.deepcopy(board)
    while len(ships) > 0:
        user_input = random.choice(list(coordinates.keys()))
        user_input_orientation = random.choice(["h","v"])
        row, col = coordinates[user_input]
        ship_len = ship_length[list_ships[0]]
        if discrete_board[row][col] == "-":
            if is_in_the_board(row, col, ship_len, user_input_orientation, coordinates):
                sunken_ship = mark_ship(board, discrete_board, ship_length, coordinates, user_input, user_input_orientation, list_ships, row, col, ship_len)
                ships[list_ships[0]] -= 1
                if ships[list_ships[0]] == 0:
                    ships.pop(list_ships[0])
                list_ships = list(ships)
                sunken_ships_coordinates.append(sunken_ship)
            else:
                continue
        else:
            continue
    print(f"\nThis is the {active_player}'s Battleship Board")  
    print_board(board, board_size, alphabet)
    time.sleep(2)
    print(100 * "\n")
    return board, sunken_ships_coordinates

def init_board(board_size):
    return  [["-"] * board_size for i in range(board_size)] 
    
def print_board(board, board_size, alphabet):
    first_row = [str(x+1) + " "  for x in range(board_size)]
    print("\n")
    print(f"  | {'| '.join(first_row)}")
    for element in range(len(board)):
        print(f"{board_size* '--+-'}--")
        print(alphabet[element]+ " | "+ ' | '.join(board[element]))
    print("\n")

def coordinates_dict(board_size, alphabet):
    coordinates_dict = {}
    for i in range(board_size):
        for j in range(board_size):
            coordinates_dict[alphabet[i]+str(j+1)]=i,j
    return coordinates_dict

def available_ships(board_size):
    if board_size == 5:
        available_ships = {"1x3":1, "1x2":1, "1x1":2}
    elif board_size == 6:
        available_ships = {"1x3":1, "1x2":2, "1x1":2}
    elif board_size == 7:
        available_ships = {"1x4":1, "1x3":1, "1x2":2, "1x1":2}
    elif board_size == 8:
        available_ships = {"1x4":1, "1x3":2, "1x2":2, "1x1":2}
    elif board_size == 9:
        available_ships = {"1x4":1, "1x3":2, "1x2":3, "1x1":2}
    else:
        available_ships = {"1x5":1, "1x4":2, "1x3":3, "1x2":4}
    return available_ships

def player_name():
    print(10*chr(9995))
    player_1 = input(f"Hello! What is name of Player 1? \n")
    game_quit(player_1)
    player_2 = input(f"Hello! What is name of Player 2? \n")
    game_quit(player_2)
    return player_1, player_2

def player_name_AI():
    print(10*chr(9995))
    player_1 = input(f"Hello! What is name of Human Player? \n")
    game_quit(player_1)
    with open("random_names.txt") as name_file:
        player_2 = "AI_" + random.choice(name_file.read().splitlines())
    print(f"Your opponent this time will be: {player_2}.")
    return player_1, player_2

def player_name_AI_only():
    print(10*chr(9995))
    with open("random_names.txt") as name_file:
        player_1 = "AI_" + random.choice(name_file.read().splitlines())
    with open("random_names.txt") as name_file:
        player_2 = "AI_" + random.choice(name_file.read().splitlines())
    print(f"The AI player 1 name is {player_1} and the AI player 2 name is {player_2}.")
    return player_1, player_2

def gameplay(active_player, shooting_board, coordinates, board_player, board_size, alphabet, sunken_ships_coordinates):
    print(f"{active_player} it is your shooting board!")
    print_board(shooting_board, board_size, alphabet)
    while True:
        shot_coordinate = input(f"{active_player}, please choose coordinates to shoot: ")
        game_quit(shot_coordinate)
        if shot_coordinate.upper() in coordinates.keys():
            row, col = coordinates[shot_coordinate.upper()]
            if shooting_board[row][col] == "-":
                if board_player[row][col] == "X":
                    shooting_board[row][col] = colored("H", "blue")
                    print(f"Good job! You have hit!")
                    break
                else:
                    shooting_board[row][col] = colored("M", "red")
                    print(f"Oooooops! You have missed!") 
                    break
            else:
                print("This place has already been selected!")
        else:
            print(f"Please select the valid coordinate!")
    is_sunken(shooting_board, sunken_ships_coordinates)
    print(f"{active_player}, check your shooting board once again.")
    print_board(shooting_board, board_size, alphabet)
    if is_won(shooting_board, board_player):
        print(f"Congratulations! {active_player} You have won! ")
        graphics.winner_screen_graph()
    input("Press Enter to continue...")

def gameplay_AI(active_player, shooting_board, coordinates, board_player, board_size, alphabet, sunken_ships_coordinates):
    while True:
        shot_coordinate = random.choice(list(coordinates.keys()))
        row, col = coordinates[shot_coordinate.upper()]
        if shooting_board[row][col] == "-":
            if board_player[row][col] == "X":
                shooting_board[row][col] = colored("H", "blue")
                print(f"\nGood job! You have hit!")
                break
            else:
                shooting_board[row][col] = colored("M", "red")
                print(f"\nUuuuupsssssssss! You have missed!")                
                break
    is_sunken(shooting_board, sunken_ships_coordinates)
    print(f"{active_player}, result.")
    print_board(shooting_board, board_size, alphabet)
    if is_won(shooting_board, board_player):
        print(f"\nCongratulations! {active_player} has won! ")
        graphics.winner_screen_graph()
    time.sleep(0.5)

def is_won(active_shooting_board, active_player_board):
    x_count = 0
    h_count = 0
    for element in active_shooting_board:
        h_count += element.count(colored("S", "green"))
    for element in active_player_board:
        x_count += element.count("X")
    return x_count == h_count

def is_tie(turn, board_size):
    return turn // 2 >= (board_size**2)*0.75

def turn_limit(board_size, turn):
    limit_of_turn = (board_size**2)*0.75 - turn/2
    print(colored(f"The limit of your turns is {int(limit_of_turn) }.\n", "yellow"))
    
def is_sunken(shooting_board, sunken_ships_coordinates):
    for element in sunken_ships_coordinates:
        ship_len = len(element)
        counter = 0
        for i in element:
            if shooting_board[i[0]][i[1]] == colored("H", "blue"):
                counter += 1
        if counter == ship_len:
            for i in element:
                shooting_board[i[0]][i[1]] = colored("S", "green")

def change_active_item(item_1, item_2, active_item):
    active_item = item_1 if active_item == item_2 else item_2 
    return active_item

def battleships_Human_Human():
    turn = 0
    alphabet = string.ascii_uppercase        
    board_size = user_input_board_size()
    board = init_board(board_size)
    print_board(board, board_size, alphabet)
    coordinates = coordinates_dict(board_size, alphabet)
    player_1, player_2 = player_name()
    active_player = player_1
    board_player_1, sunken_ships_coordinates_1 = ships_placement(board, board_size, coordinates, alphabet, active_player)
    board = init_board(board_size)
    active_player = change_active_item(player_1, player_2, active_player)
    board_player_2, sunken_ships_coordinates_2 = ships_placement(board, board_size, coordinates, alphabet, active_player)
    shooting_board_player_1 = init_board(board_size)
    shooting_board_player_2 = init_board(board_size)
    active_player = change_active_item(player_1, player_2, active_player)
    active_player_board = board_player_2
    active_shooting_board = shooting_board_player_1
    active_sunken_ships_coordinates = sunken_ships_coordinates_2

    while is_won(active_shooting_board, active_player_board) == False:
        turn_limit(board_size, turn)
        gameplay(active_player, active_shooting_board, coordinates, active_player_board, board_size, alphabet, active_sunken_ships_coordinates)
        if is_won(active_shooting_board, active_player_board):
            break
        turn +=1
        if is_tie(turn, board_size):
            print(f"Game over! It's a tie!")
            graphics.tie_screen_graph()
            break
        active_player = change_active_item(player_1, player_2, active_player)
        active_player_board = change_active_item(board_player_1, board_player_2, active_player_board)
        active_shooting_board = change_active_item(shooting_board_player_1, shooting_board_player_2, active_shooting_board)
        active_sunken_ships_coordinates = change_active_item(sunken_ships_coordinates_1, sunken_ships_coordinates_2, active_sunken_ships_coordinates)
    
def battleships_Human_AI():
    turn = 0
    alphabet = string.ascii_uppercase        
    board_size = user_input_board_size()
    board = init_board(board_size)
    print_board(board, board_size, alphabet)
    coordinates = coordinates_dict(board_size, alphabet)
    player_1, player_2 = player_name_AI()
    active_player = player_1
    board_player_1, sunken_ships_coordinates_1 = ships_placement(board, board_size, coordinates, alphabet, active_player)
    board = init_board(board_size)
    active_player = change_active_item(player_1, player_2, active_player)
    board_player_2, sunken_ships_coordinates_2 = ships_placement_AI(board, board_size, coordinates, alphabet, active_player)
    shooting_board_player_1 = init_board(board_size)
    shooting_board_player_2 = init_board(board_size)
    active_player = change_active_item(player_1, player_2, active_player)
    active_player_board = board_player_2
    active_shooting_board = shooting_board_player_1
    active_sunken_ships_coordinates = sunken_ships_coordinates_2
   
    while is_won(active_shooting_board, active_player_board) == False:
        turn_limit(board_size, turn)
        if active_player == player_1:
            gameplay(active_player, active_shooting_board, coordinates, active_player_board, board_size, alphabet, active_sunken_ships_coordinates)
        elif active_player == player_2:
            gameplay_AI(active_player, active_shooting_board, coordinates, active_player_board, board_size, alphabet, active_sunken_ships_coordinates)
        if is_won(active_shooting_board, active_player_board):
            break
        turn +=1
        if is_tie(turn, board_size):
            print(f"Game over! It's a tie!")
            graphics.tie_screen_graph()
            break
        active_player = change_active_item(player_1, player_2, active_player)
        active_player_board = change_active_item(board_player_1, board_player_2, active_player_board)
        active_shooting_board = change_active_item(shooting_board_player_1, shooting_board_player_2, active_shooting_board)
        active_sunken_ships_coordinates = change_active_item(sunken_ships_coordinates_1, sunken_ships_coordinates_2, active_sunken_ships_coordinates)

def battleships_AI_Human():
    turn = 0
    alphabet = string.ascii_uppercase        
    board_size = user_input_board_size()
    board = init_board(board_size)
    print_board(board, board_size, alphabet)
    coordinates = coordinates_dict(board_size, alphabet)
    player_2, player_1 = player_name_AI()
    active_player = player_1
    board_player_1, sunken_ships_coordinates_1 = ships_placement_AI(board, board_size, coordinates, alphabet, active_player)
    board = init_board(board_size)
    active_player = change_active_item(player_1, player_2, active_player)
    board_player_2, sunken_ships_coordinates_2 = ships_placement(board, board_size, coordinates, alphabet, active_player)
    shooting_board_player_1 = init_board(board_size)
    shooting_board_player_2 = init_board(board_size)
    active_player = change_active_item(player_1, player_2, active_player)
    active_player_board = board_player_1
    active_shooting_board = shooting_board_player_2
    active_sunken_ships_coordinates = sunken_ships_coordinates_2

    while is_won(active_shooting_board, active_player_board) == False:
        turn_limit(board_size, turn)
        if active_player == player_2:
            gameplay(active_player, active_shooting_board, coordinates, active_player_board, board_size, alphabet, active_sunken_ships_coordinates)
        elif active_player == player_1:
            gameplay_AI(active_player, active_shooting_board, coordinates, active_player_board, board_size, alphabet, active_sunken_ships_coordinates)
        if is_won(active_shooting_board, active_player_board):
            break
        turn +=1
        if is_tie(turn, board_size):
            print(f"Game over! It's a tie!")
            graphics.tie_screen_graph()
            break
        active_player = change_active_item(player_1, player_2, active_player)
        active_player_board = change_active_item(board_player_1, board_player_2, active_player_board)
        active_shooting_board = change_active_item(shooting_board_player_1, shooting_board_player_2, active_shooting_board)
        active_sunken_ships_coordinates = change_active_item(sunken_ships_coordinates_1, sunken_ships_coordinates_2, active_sunken_ships_coordinates)

def battleships_AI_AI():
    turn = 0
    alphabet = string.ascii_uppercase
    board_size = user_input_board_size()
    board = init_board(board_size)
    print_board(board, board_size, alphabet)
    coordinates = coordinates_dict(board_size, alphabet)
    player_1, player_2 = player_name_AI_only()
    active_player = player_1
    board_player_1, sunken_ships_coordinates_1 = ships_placement_AI(board, board_size, coordinates, alphabet, active_player)
    board = init_board(board_size)
    active_player = change_active_item(player_1, player_2, active_player)
    board_player_2, sunken_ships_coordinates_2 = ships_placement_AI(board, board_size, coordinates, alphabet, active_player)
    shooting_board_player_1 = init_board(board_size)
    shooting_board_player_2 = init_board(board_size)
    active_player = change_active_item(player_1, player_2, active_player)
    active_player_board = board_player_2
    active_shooting_board = shooting_board_player_1
    active_sunken_ships_coordinates = sunken_ships_coordinates_2

    while is_won(active_shooting_board, active_player_board) == False:
        turn_limit(board_size, turn)
        gameplay_AI(active_player, active_shooting_board, coordinates, active_player_board, board_size, alphabet, active_sunken_ships_coordinates)
        if is_won(active_shooting_board, active_player_board):
            break
        turn +=1
        if is_tie(turn, board_size):
            print(f"Game over! It's a tie!")
            graphics.tie_screen_graph()
            break
        active_player = change_active_item(player_1, player_2, active_player)
        active_player_board = change_active_item(board_player_1, board_player_2, active_player_board)
        active_shooting_board = change_active_item(shooting_board_player_1, shooting_board_player_2, active_shooting_board)
        active_sunken_ships_coordinates = change_active_item(sunken_ships_coordinates_1, sunken_ships_coordinates_2, active_sunken_ships_coordinates)

def play_again():
    while True:
        user_input = input(f"Would you like to play again? (Y)es / (N)o: ")
        if user_input.lower() == "y":
            main_menu()
            break
        elif user_input.lower() == "n":
            sys.exit()
        else:
            print("Please select 'Y' or 'N'...")

def main_menu():
    graphics.main_menu_graph()
    print(f"""
    1. Human vs Human 
    2. Human vs AI
    3. AI vs AI
    """)
    while True:   
        gamemode = input(f"Please choose the game mode: ")
        if gamemode in ["1", "2", "3"]:
            if gamemode == "1":
                battleships_Human_Human()
                break
            elif gamemode == "2":
                graphics.who_starts_graph()
                who_starts= input(f"Please choose who goes first: ")
                if who_starts == "1":
                    battleships_Human_AI()
                    break
                elif who_starts == "2":
                    battleships_AI_Human()
                    break
                else:
                    print(f"Please provide valid input!")
            else:
                battleships_AI_AI()
                break
        else:
            print(f"Please provide valid input!")
    play_again()

def main():
    main_menu()

main()