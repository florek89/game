def create_board(width, height):
    '''This function creates board with parametrs: width and height'''
    board = []
    upper_board = []
    lower_board = []
    frame_board = []

    for row in range(width):
        upper_board.append("X")
    board.append(upper_board)
    lower_board = upper_board

    for row in range(width):
        if row == 0 or row == height-1:
            frame_board.append("X")
        else:
            frame_board.append("-")

    for i in range(height-2):
        board.append(frame_board[:])

    board.append(lower_board)
    print(board)
    return board


def print_board(board):
    for row in board:
        print(" ".join(row))

def insert_player(board, x, y):
    board[x][y] = "@"

def insert_player2(board, x, y):
    board[x][y] = "@"


def main():
    complete_board = create_board(10,10)
    insert_player(complete_board,2,2)
    insert_player2(complete_board,3,4)
    print_board(complete_board)

main()
