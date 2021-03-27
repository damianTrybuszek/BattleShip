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

def ships_placement(board, coordinates, ships):
    list_ships = list(ships)
    ship_length = {"1x5":5, "1x4":4, "1x3":3, "1x2":2, "1x1":1}
    while len(ships) > 0:
        user_input = input(f"Please place your ships on the map. Available ships for placement: {ships}. Current ship being placed: {list_ships[0]}. Please select a valid coordinate: ")
        user_input_orientation = input(f"Please select orientation (H)oritzontal or (V)ertical: ")
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
            
            ships[list_ships[0]] -= 1

            if ships[list_ships[0]] == 0:
                ships.pop(list_ships[0])
            
            list_ships = list(ships)
        else:
            print("Please select a valid coordinate!")

    return board