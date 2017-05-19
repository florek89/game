import os
import csv
import sys

# def found_char(boards, x, y):
#     if boards[x][y] == "?":
#         boards = get_boards_with_text (boards, y, x, " ")
#     else:
#         print('nothing')
#     return boards

# def qest (baord, x_quest, y_quest):

# def get_boards_from_file():
#     scren_list = []
#     text = open("mapa.csv").read()
#     # print (tex


def get_boards_from_file():
    """Wczytywanie tablicy z pliku."""
    boards = []
    text = open("mapa.csv").read()
    # print (text)

    boards.append([])
    row = 0
    for i in text:
        if i == "\n":
            boards.append([])
            row += 1
        else:
            boards[row].append(i)
    return boards


def print_board(boards, start_row, end_row):
    """Drukowanie tablicy. """
    for row in boards[start_row: end_row]:
        print("".join(row))


def get_boards_with_text(boards, y, x, text):
    """Wprowadzenie napisow o okreslonej dlugosci w podanym na tablicy miejscu. """
    variable = 0
    y = y-1
    for variable in range(len(text)):

        boards[x][y+variable+1] = text[variable]
    return (boards)


def get_boards_with_player(boards, x, y):
    """Wczytywanie postaci bohatera - parametry to tablica oraz koordynaty, na których postac rozpoczyna gre. """
    boards[x][y] = "@"
    return boards


def getch():
    """Obsluga danych wejsciowych. Funkcja zwraca wprowadzony znak. """
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

def welcome_screen():
    """Wczytanie ekranu powitalnego. """
    boards = get_boards_from_file()
    print_board(boards, 1, 41)
    char = getch()


def get_player_name():
    """Wprowadzenie nazwy gracza, wybor jednej z trzech proponowanych postaci.  """
    while True:
        player_name = input('Press your name and press enter: ')
        if len(player_name) <= 10:
            break
        else:
            print("Error! Only 10 characters allowed!")
    return player_name


def get_apple_amount(int_apple):
    """Liczenie wszystkiych zebranych apple, docelowa iloss to 0"""
    apple_amount = str(int_apple)
    return apple_amount


def get_coins_amount(int_coins):
    """Liczenie wszystkiych zebranych coins, docelowa iloss to 0"""
    coins_amount = str(int_coins)
    return coins_amount


def get_scroll_amount(int_scroll):
    """Liczenie wszystkiych zebranych scroll, docelowa iloss to 0"""
    scroll_amount = str(int_scroll)
    return scroll_amount


def get_player_character():
    """Wybor jednej z trzech proponowanych postaci. """
    while True:
        choice_list = ["s", "c", "m"]
        control_character = input('Chose your player character (s/c/m): ').lower()
        if control_character in choice_list:
            if control_character == "s":
                player_character = "Scroll Master"
                break
            elif control_character == "c":
                player_character = "Coin Master"
                break
            elif control_character == "m":
                player_character = "Magic Master"
                break
        else:
            print("Error, try type s/c/m!")
    return player_character


def start_screen():
    """Drukowanie ekranu startowego gry. """
    boards = get_boards_from_file()
    print_board(boards, 42, 82)


def comunicat(boards, x_com, y_com, text):
    """Drukuje w ustalonej pozycji komunikat, dot.  skolekcjonowania podanego elementu. Parametry to:
     tablice, miejsce wyswietlania, oraz tekst dla gracza."""
    get_boards_with_text(boards, x_com, y_com + 1, '0-----------------------------0')
    get_boards_with_text(boards, x_com, y_com + 2, text)
    get_boards_with_text(boards, x_com, y_com + 3, '|                             |')
    get_boards_with_text(boards, x_com, y_com + 4, '|   Press move to continue:   |')
    get_boards_with_text(boards, x_com, y_com + 5, '0-----------------------------0')
    print_board(boards, 83, 123)


def get_boards_with_inwentory(boards, player_name, player_character, apple_amount, coins_amount, scroll_amount):
    # player_name = start_screen()
    boards = get_boards_with_text(boards, 3, 115, player_name)
    boards = get_boards_with_text(boards, 3, 117, player_character)
    boards = get_boards_with_text(boards, 92, 115, apple_amount)
    boards = get_boards_with_text(boards, 109, 115, coins_amount)
    boards = get_boards_with_text(boards, 93, 117, scroll_amount)
    # boards = get_boards_with_text(boards, 100, 115, 'Wisdom:')
    # boards = get_boards_with_text(boards, 100, 117, 'Atack:')
    return boards


def level_1(boards, x_player, y_player, player_name, player_character, apple_amount, coins_amount, scroll_amount):
    """Wczytywanie pierwszej planszy"""
    boards = get_boards_from_file()
    boards = get_boards_with_player(boards, y_player, x_player)
    boards = get_boards_with_inwentory(boards, player_name, player_character, apple_amount, coins_amount, scroll_amount)
    if x_player == 54 and y_player == 106:
        comunicat(boards, 45, 99, "|  Don't forget collect apple |")
    return boards


def change_level(x_player, y_player, start_row, end_row):
    """Drukowanie nastepnej tablicy"""
    if y_player > 83 and y_player < 90:
        start_row = 83
        end_row = 123
        y_player = 141
        print(start_row)
    # if y_player > 90:
    #     start_row = 124
    #     end_row = 164
    #     print(start_row)
    return x_player, y_player, start_row, end_row

# def  get_boards_apple ():
#     if x_player == 16 and y_player == 89:
#         int_apple = int_apple+1
#         comunicat (boards, 13, 90, "|    You collect 1 apple      |")
#         boards = get_boards_with_text(boards, 16, 89, 'X')
#         is_contact_apple_1 = True
#         apple_amount = get_apple_amount(int_apple)
#     if is_contact_apple_1 == False:
#         boards = get_boards_with_text(boards, 16, 89, 'o')


def main():
    """Głowna petla programu"""
    int_apple = 0
    int_coins = 0
    int_scroll = 0
    apple_amount = get_apple_amount(int_apple)
    coins_amount = get_coins_amount(int_coins)
    scroll_amount = get_scroll_amount(int_scroll)
    welcome_screen()  # insert scree welcome
    start_screen()
    player_name = get_player_name()
    player_character = get_player_character()
    # player_character = "demoni"
    start_screen()  # insert start_screen
    x_player = 20  # starting position of player
    y_player = 100
    print(x_player, y_player)
    boards = get_boards_from_file()
    get_boards_with_player(boards, y_player, x_player)

####################

    is_contact_scroll_1 = False   # add 1 scroll

    is_contact_apple_1 = False  # add 1 apple
    is_contact_apple_2 = False  # add 2 apple
    is_contact_apple_3 = False  # add 3 apple
    is_contact_apple_4 = False  # add 4 apple

####################
    start_row = 83
    end_row = 123
    # print_board(boards, 83, 123)

    # x = getch()
    char = ""

    while char != "q":
        boards = level_1(boards, x_player, y_player, player_name, player_character, apple_amount, coins_amount, scroll_amount)
####################

        # add 1 scroll ---->
        if x_player == 43 and y_player == 99:
            int_scroll = int_scroll+1
            comunicat(boards, 35, 94, "|    You collect 1 scroll     |")
            is_contact_scroll_1 = True
            scroll_amount = get_scroll_amount(int_scroll)
        if is_contact_scroll_1 == False:
            boards = get_boards_with_text(boards, 43, 99, '/')
        # end add 1 scroll <-----

        # add 1 apple ------>
        if x_player == 16 and y_player == 89:
            int_apple = int_apple+1
            comunicat(boards, 13, 90, "|    You collect 1 apple      |")
            is_contact_apple_1 = True
            apple_amount = get_apple_amount(int_apple)
        if is_contact_apple_1 == False:
            boards = get_boards_with_text(boards, 16, 89, 'o')
        # end add 1 apple <-------

        # add 2 apple ------>
        if x_player == 15 and y_player == 105:
            int_apple = int_apple+1
            comunicat(boards, 9, 99, "|    You collect 1 apple      |")
            is_contact_apple_2 = True
            apple_amount = get_apple_amount(int_apple)
        if is_contact_apple_2 == False:
            boards = get_boards_with_text(boards, 15, 105, 'o')
        # end add 2 apple <-------

        # add 3 apple ------>
        if x_player == 3 and y_player == 105:
            int_apple = int_apple+1
            comunicat(boards, 3, 99, "|    You collect 1 apple      |")
            is_contact_apple_3 = True
            apple_amount = get_apple_amount(int_apple)
        if is_contact_apple_3 == False:
            boards = get_boards_with_text(boards, 3, 105, 'o')
        # end add 3 apple <-------

        # add 4 apple ------>
        if x_player == 6 and y_player == 89:
            int_apple = int_apple+2
            comunicat(boards, 3, 92, "|    You collect 2 apple      |")
            is_contact_apple_4 = True
            apple_amount = get_apple_amount(int_apple)
        if is_contact_apple_4 == False:
            boards = get_boards_with_text(boards, 6, 89, 'o')
        # end add 4 apple <-------

####################

        change_level(x_player, y_player, start_row, end_row)
        print_board(boards, start_row, end_row)
        element = ["X", "x"]
        char = getch()
        if char == "d":
            if boards[y_player][x_player + 1] not in element:
                x_player += 1
        elif char == "a":
            if boards[y_player][x_player - 1] not in element:
                x_player -= 1
        elif char == "s":
            if boards[y_player + 1][x_player] not in element:
                y_player += 1
        elif char == "w":
            if boards[y_player - 1][x_player] not in element:
                y_player -= 1
        print(x_player, y_player)


main()
