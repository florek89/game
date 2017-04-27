width = 50
height = 10


def create_board(width, height):
   height_list = []
   width_list = []
   width2 = []
   for row in range(width):
       width_list.append('X')
   for row in range(height - 2):
       height_first = []
       height_list.append(height_first)
       for row in range(width):
           if row == 0 or row == width - 1 :
               height_first.append('X')
           else:
               height_first.append(' ')

   for el in range(width):
       width2.append('X')
   board = [width_list, *height_list, width2]
   return board



def print_board(board):
    for row in board:
        print(" ".join(row))

def insert_player(board, x, y):
    board[x][y] = "@"

def insert_player2(board, x, y):
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



def main():
    complete_board = create_board(width,height)
    insert_player(complete_board,2,2)
    #insert_player2(complete_board,2,2)
    char = getch()
    if char=="w":
        insert_player(complete_board,1,2)
    print_board(complete_board)

main()
