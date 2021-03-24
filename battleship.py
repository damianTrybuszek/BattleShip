import user_inputs
import string


def init_board(board_size):
    board = []
    for i in range(board_size):
        board.append([" 0 "] * board_size)
    return  board
    
def print_board(board, board_size, alphabet):
    first_row = [str(x+1) + " "  for x in range(board_size)]
    print(f"  | {'| '.join(first_row)}")
    for element in range(len(board)):
        print(f"{board_size* '--+-'}--")
        print(alphabet[element]+ " |"+ '|'.join(board[element]))

def coordinates_dict(board_size, alphabet):
    coordinates_dict = {}
    for i in range(board_size):
        for j in range(board_size):
            coordinates_dict[alphabet[i]+str(j+1)]=i,j
    return coordinates_dict

alphabet = string.ascii_uppercase        
board_size = user_inputs.user_input_board_size()
board = init_board(board_size)
print_board(board, board_size, alphabet)

print(coordinates_dict(board_size, alphabet))




