import user_inputs
import string
import copy

def user_input_board_size():
    while True:
        board_size = input("Please insert board size: ")
        if board_size.isdigit(): 
            board_size = int(board_size)
            if board_size in range(5,11):
                return board_size
            else:
                print(f"Please provide input in the correct range!")
        else:
            print(f"Please provide valid input!!")

def user_input_ver_or_hor():
    while True:
        user_input_orientation = input(f"Please select orientation (H)oritzontal or (V)ertical: ")
        if user_input_orientation.lower() == "h" or user_input_orientation.lower() == "v":
            return user_input_orientation
        else:
            print("Please select a valid orientation! ")

def mark_ship(board, discrete_board, ship_length, coordinates, user_input, user_input_orientation, list_ships, row, col):
    ship_len = ship_length[list_ships[0]]
    # row, col = coordinates[user_input.upper()]
    for i in range(ship_len):
        if discrete_board[row][col] == "0":
            board[row][col] = "X"
            discrete_board[row][col] = "X"
            if user_input_orientation.lower() == "h" and (i == 0):
                if (row-1, col) in coordinates.values(): 
                    discrete_board[row-1][col] = "X"
                if (row, col-1) in coordinates.values():
                    discrete_board[row][col-1] = "X"
                if (row+1, col) in coordinates.values():
                    discrete_board[row+1][col] = "X"
            if user_input_orientation.lower() == "h" and (i == ship_len -1):
                if (row, col+1) in coordinates.values():
                    discrete_board[row][col+1] = "X"
                if (row-1, col) in coordinates.values():
                    discrete_board[row-1][col] = "X"
                if (row+1, col) in coordinates.values():
                    discrete_board[row+1][col] = "X"
            if user_input_orientation.lower() == "h" and i in range(1, ship_len -1):
                if (row-1, col) in coordinates.values():
                    discrete_board[row-1][col] = "X"
                if (row+1, col) in coordinates.values():
                    discrete_board[row+1][col] = "X"
            if user_input_orientation.lower() == "h":
                col += 1
            if user_input_orientation.lower() == "v" and (i == 0):
                if (row, col-1) in coordinates.values(): 
                    discrete_board[row][col-1] = "X"
                if (row-1, col) in coordinates.values():
                    discrete_board[row-1][col] = "X"
                if (row, col+1) in coordinates.values():
                    discrete_board[row][col+1] = "X"
            if user_input_orientation.lower() == "v" and (i == ship_len - 1):
                if (row+1, col) in coordinates.values():
                    discrete_board[row+1][col] = "X"
                if (row, col-1) in coordinates.values():
                    discrete_board[row][col-1] = "X"
                if (row, col+1) in coordinates.values():
                    discrete_board[row][col+1] = "X"
            if user_input_orientation.lower() == "v" and i in range(1, ship_len - 1):
                if (row, col-1) in coordinates.values():
                    discrete_board[row][col-1] = "X"
                if (row, col+1) in coordinates.values():
                    discrete_board[row][col+1] = "X"
            if user_input_orientation.lower() == "v":
                row += 1
        else: 
            print(f"This place is already used!")
            break

def ships_placement(board, board_size, coordinates, ships, alphabet, active_player):
    print(f"Hello {active_player}! Please place Your ships on the board!")
    list_ships = list(ships)
    ship_length = {"1x5":5, "1x4":4, "1x3":3, "1x2":2, "1x1":1}
    discrete_board = copy.deepcopy(board)
    while len(ships) > 0:
        user_input = input(f"Please place your ships on the map. Available ships for placement: {ships}. Current ship being placed: {list_ships[0]}. Please select a valid coordinate: ")
        user_input_orientation = user_input_ver_or_hor()
        row, col = coordinates[user_input.upper()]
        if user_input.upper() in coordinates and discrete_board[row][col] == "0":
            try:
                mark_ship(board, discrete_board, ship_length, coordinates, user_input, user_input_orientation, list_ships, row, col)
                ships[list_ships[0]] -= 1

                if ships[list_ships[0]] == 0:
                    ships.pop(list_ships[0])

                list_ships = list(ships)

                print("Board")
                print_board(board, board_size, alphabet)
                print("Discrete_Board")
                print_board(discrete_board, board_size, alphabet)
            except:
                print(f"Coordinate not in board! Please insert valid input!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        else:
            print("Please select a valid coordinate!")   
    return board



def init_board(board_size):
    return  [["0"] * board_size for i in range(board_size)] 
    


def print_board(board, board_size, alphabet):
    first_row = [str(x+1) + " "  for x in range(board_size)]
    print(f"  | {'| '.join(first_row)}")
    for element in range(len(board)):
        print(f"{board_size* '--+-'}--")
        print(alphabet[element]+ " | "+ ' | '.join(board[element]))


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

    player_1 = input(f"Hello! What is name of Player 1? ")
    player_2 = input(f"Hello! What is name of Player 2? ")
    return player_1, player_2

def change_player(player_1, player_2, active_player):
    active_player = player_1 if active_player == player_2 else player_1 
    return active_player




def gameplay(active_player, shooting_board, coordinates, board_player):

    print_board(shooting_board)
    shot_coordinate = input(f"Please choose coordinates to shoot!")
    while True:
        if shot_coordinate.upper() in coordinates:
            row, col = coordinates[shot_coordinate.upper()]
            if shooting_board[row][col] == "0":
                if board_player[row][col] == "X":
                    shooting_board[row][col] = "H"
                    break
                else:
                    shooting_board[row][col] = "M"
                    break
            else:
                print("This place is already taken!")
        else:
            print(f"Please select the valid coordinate!")

def is_won(active_shooting_board, active_player_board):
    x_count = 0
    h_count = 0

    for element in active_shooting_board:
        h_count += element.count("H")
    for element in active_player_board:
        x_count += element.count("X")

    return x_count == h_count

def change_player_board(board_player_1, board_player_2, active_player_board):
    active_player_board = board_player_1 if active_player_board == board_player_2 else board_player_2
    return active_player_board

def change_shooting_board(shooting_board_player_1, shooting_board_player_2, active_shooting_board):
    active_shooting_board = shooting_board_player_1 if active_shooting_board == shooting_board_player_2 else shooting_board_player_2 
    return active_shooting_board


def main():
    alphabet = string.ascii_uppercase        
    board_size = user_input_board_size()
    board = init_board(board_size)
    print_board(board, board_size, alphabet)
    coordinates = coordinates_dict(board_size, alphabet)
    ships = available_ships(board_size)
    player_1, player_2 = player_name()
    active_player = player_1
    board_player_1 = ships_placement(board, board_size, coordinates, ships, alphabet, active_player)
    print_board(board_player_1, board_size, alphabet)
    board = init_board(board_size)
    active_player = change_player(player_1, player_2, active_player)
    board_player_2 = ships_placement(board, board_size, coordinates, ships, alphabet, active_player)
    print_board(board_player_2, board_size, alphabet)
    shooting_board_player_1 = init_board(board_size)
    shooting_board_player_2 = init_board(board_size)
    active_player = change_player(player_1, player_2, active_player)
    active_player_board = board_player_2
    active_shooting_board = shooting_board_player_1

    while is_won(active_shooting_board, active_player_board) == False:
        gameplay(active_player, active_shooting_board, coordinates, active_player_board)
        if is_won(active_shooting_board, active_player_board):
            print(f"Congratulations! {active_player} You have won! ")
            break
        active_player = change_player(player_1, player_2, active_player)
        active_player_board = board_player_2
        active_shooting_board = shooting_board_player_1
    

    




main()