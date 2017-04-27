import os

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

    return board


def print_board(board):
    for row in board:
        print(" ".join(row))

def insert_player(board, x, y):
    board[x][y] = "@"


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char

def move():

    if char == "w":
        insert_player(complete_board,1,2)
    print_board(complete_board)
    if char == "a":
        insert_player(complete_board, 2, 1)
    print_board(complete_board)
    if char == "s":
        insert_player(complete_board,3,2)
    print_board(complete_board)
    if char == "d":
        insert_player(complete_board, 2, 3)
    print_board(complete_board)
    # else:
    #     print("Use 'W-S-A-D'")
def main():
    complete_board = create_board(10,10)
    insert_player(complete_board,2,2)
    char = getch()
    move = move()







main()
