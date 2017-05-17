import os
import csv
import sys


def found_char(board, x, y):
    if board[x][y] == "?":
        print('action')
    else:
        print('nothing')


def create_scren_from_file():
    scren_list = []
    text = open("mapa.csv").read()
    # print (text)
    scren_list.append([])
    row = 0
    for i in text:
        if i == "\n":
            scren_list.append([])
            row += 1
        else:
            scren_list[row].append(i)
    return scren_list


def print_scren(scren_list, start_row , end_row):
    for row in scren_list[start_row : end_row]:
        print("".join(row))


def text_insert (board, y, x, text):
    variable=0
    for variable in range(len(text)):
        board[x][y+variable+1] = text[variable]


def tree(board, y, x , leaf="#"):
    board[x][y] = "&"
    board[x-1][y] = "&"
    board[x-2][y] = "&"
    board[x-3][y-1] = leaf
    board[x-3][y+1] = leaf
    board[x-4][y-2] = leaf
    board[x-4][y+2] = leaf
    board[x-5][y-2] = leaf
    board[x-5][y+2] = leaf
    board[x-6][y-1] = leaf
    board[x-6][y+1] = leaf
    board[x-7][y] = leaf
    return board

def player(board, x, y):
    board[x][y] = "@"
    return board

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

def welcome_screen ():
    board = create_scren_from_file()
    print_scren(board, 42,82)

    while True:
        player_name = input('Press your name and press enter: ')
        if len(player_name) <= 10:
            break
        else:
            print("Error! Only 15 characters allowed!")
    control_character = input('Chose your player character (s/c/m): ').lower()
    #  Choose only S or B or M, or Q to quit
    player_character = []
    if control_character == "s":
        player_character = "Scroll Master"
    elif control_character == "c":
        player_character = "Coin Master"
    elif control_character == "m":
        player_character = "Magic Master"
    elif control_character == "q":
        sys.exit()

    return (player_name, player_character, control_character)

def main():
    player_name, player_character, control_character = welcome_screen()
    x_player = 10 #starting position of player
    y_player = 85
    board = create_scren_from_file()
    player(board, y_player, x_player)
    print_scren(board, 83, 123)
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
        board = create_scren_from_file()

        text_insert(board,3,115, player_name)
        text_insert(board,3, 117, player_character)
        text_insert(board,83,74,'Mana:')
        text_insert(board,83,76,'Range:')
        text_insert(board,83,78,'Skil:')
        text_insert(board,100,74,'Wisdom:')
        text_insert(board,100,76,'Atack:')
        text_insert(board,50,102,'?')
        text_insert(board,100,78,'Deff:')
        tree(board,14,52)
        tree(board,31,20)
        tree(board,40,21, '?')
        tree(board,61,20,'?')
        found_char(board,y_player,x_player)
        player(board, y_player, x_player)
        print_scren(board,82,123)
        print(x_player,y_player)

main()
