import os

width = 60
height = 40


def create_board(width, height):
    height_list = []
    width_list = []
    width_end = []
    for poz in range(width):
       width_list.append('X')
    for poz in range(height - 2):
       height_first = []
       height_list.append(height_first)
       for poz in range(width):
           if poz == 0 or poz == width - 1 :
               height_first.append('X')
           else:
               height_first.append(' ')

    for poz in range(width):
       width_end.append('X')
    board = [width_list, *height_list, width_end]
    return board


def print_board(board):
    for poz in board:
        print(*poz)

def tree(board, x, y):
    board[x][y] = "&"
    board[x-1][y]= "&"
    board[x-2][y]= "&"
    board[x-3][y-1]= "#"
    board[x-3][y+1]= "#"
    board[x-4][y-2]= "#"
    board[x-4][y+2]= "#"
    board[x-5][y-2]= "#"
    board[x-5][y+2]= "#"
    board[x-6][y-1]= "#"
    board[x-6][y+1]= "#"
    board[x-7][y]= "#"
    return board

def player(board, x, y):
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
    print(char)
    return char


def move():
    char = getch()
    getch()
    if char == "w":
        os.system("cls")
        board = create_board(width, height)
        player(board, 2, 1)
        print_board(board)
        move ()
    if char == "a":
        os.system("cls")
        player(board, 2, 1)
        print_board(board)
    if char == "s":
        os.system("cls")
        player(board,3,2)
        print_board(board)
    if char == "d":
        os.system("cls")
        player(board, 2, 3)
        print_board(board)
    #     print("Use 'W-S-A-D'")


def main():
     board = create_board(width, height)
     player(board, 1, 1)
     tree(board, 13,13)
     tree(board, 13,4)
     tree(board, 15,20)
     print_board(board)
     move ()

main()
