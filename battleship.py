import user_inputs
import string

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

def ships_placement(board, board_size, coordinates, ships, alphabet):
    list_ships = list(ships)
    ship_length = {"1x5":5, "1x4":4, "1x3":3, "1x2":2, "1x1":1}
    while len(ships) > 0:
        user_input = input(f"Please place your ships on the map. Available ships for placement: {ships}. Current ship being placed: {list_ships[0]}. Please select a valid coordinate: ")
        user_input_orientation = user_input_ver_or_hor()
        if user_input.upper() in coordinates:
            if user_input_orientation.lower() == "h":
                ship_len = ship_length[list_ships[0]]
                row, col = coordinates[user_input.upper()]
                for i in range(ship_len):
                    board[row][col] = "X"
                    col += 1
            elif user_input_orientation.lower() == "v":
                ship_len = ship_length[list_ships[0]]
                row, col = coordinates[user_input.upper()]
                for i in range(ship_len):
                    board[row][col] = "X"
                    row += 1
            
            print_board(board, board_size, alphabet)

            ships[list_ships[0]] -= 1

            if ships[list_ships[0]] == 0:
                ships.pop(list_ships[0])
            
            list_ships = list(ships)
        else:
            print("Please select a valid coordinate!")

    return board

def init_board(board_size):
    # board = []
    # for i in range(board_size):
    #     board.append([" 0 "] * board_size)
    return  [["0"] * board_size for i in range(board_size)] #return board
    
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
        available_ships = {"1x3":2, "1x2":2, "1x1":1}
    elif board_size == 6:
        available_ships = {"1x3":3, "1x2":3}
    elif board_size == 7:
        available_ships = {"1x4":1, "1x3":2, "1x2":4}
    elif board_size == 8:
        available_ships = {"1x4":1, "1x3":3, "1x2":4}
    elif board_size == 9:
        available_ships = {"1x4":2, "1x3":3, "1x2":4}
    else:
        available_ships = {"1x5":1, "1x4":2, "1x3":3, "1x2":4}

    return available_ships


def main():
    alphabet = string.ascii_uppercase        
    board_size = user_input_board_size()
    board = init_board(board_size)
    print_board(board, board_size, alphabet)
    coordinates = coordinates_dict(board_size, alphabet)
    ships = available_ships(board_size)
    print(coordinates)
    board_a = ships_placement(board, board_size, coordinates, ships, alphabet)
    print_board(board_a, board_size, alphabet)

main()