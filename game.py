import os
import csv
import sys


def create_board():
    board = []
    text = open("mapa.csv").read()
    #print (text)
    board.append([])
    row = 0
    for i in text:
        if i == "\n":
            board.append([])
            row += 1
        else:
            board[row].append(i)
    return board


def print_board(board):
    for row in board:
        print("".join(row))

def text_insert (board, y, x, text):
    variable=0
    for variable in range(len(text)):
        board[x][y+variable+1] = text[variable]
    return board

def tree(board, y, x , leaf="#"):
    board[x][y] = "&"
    board[x-1][y]= "&"
    board[x-2][y]= "&"
    board[x-3][y-1]= leaf
    board[x-3][y+1]= leaf
    board[x-4][y-2]= leaf
    board[x-4][y+2]= leaf
    board[x-5][y-2]= leaf
    board[x-5][y+2]= leaf
    board[x-6][y-1]= leaf
    board[x-6][y+1]= leaf
    board[x-7][y]= leaf
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

def main():
    x_player = 10 #starting position of player
    y_player = 5
    board = create_board()
    player(board, y_player, x_player)
    #tree(board,14,15,"*")
    print_board(board)
    x = getch()
    while x != "q":

       char = getch()
       if char == "d":
           if board[y_player][x_player + 1] != "X":
               x_player += 1
       elif char == "a":
           if board[y_player][x_player - 1] != "X":
               x_player -= 1
       elif char == "s":
           if board[y_player + 1][x_player]: #!= "X"
               y_player += 1
       elif char == "w":
           if board[y_player - 1][x_player] != "X":
               y_player -= 1
       elif char == "q":
           sys.exit()

       board = create_board()
       #mage(board,10,10)

       text_insert(board,83,32,'Mana:')
       text_insert(board,83,34,'Range:')
       text_insert(board,83,36,'Skil:')
       text_insert(board,100,32,'Wisdom:')
       text_insert(board,100,34,'Atack:')
       text_insert(board,100,36,'Deff:')
       tree(board,15,11)
       tree(board,31,20)
       tree(board,40,21, '?')
       tree(board,61,20,'?')
       player(board, y_player, x_player)
       print_board(board)
       print(x_player,y_player)

main()
