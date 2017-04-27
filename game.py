def create_board(width,height):


   main_board = []
   inner_board = ["#"*width]

   for column in range(height):
       main_board.append(inner_board[:])

   for row in range(1, height - 1):
       main_board[row] = ["x" + int(width-2) * " " + "#"]

   return main_board

def print_board(board):
   for line in board:
       print(*line)


def main():
   print_board(create_board(143,42))

main()
