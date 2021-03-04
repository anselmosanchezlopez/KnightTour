import pprint
import numpy as np


def kt(n):
    board = [[-1 for i in range(n)] for j in range(n)]
    kt_recur(n=n, board=board, x=2, y=2, counter=0)
    print(np.array(board))

# define the movement of the knight


x_moves = [1, 1, 2, 2, -1, -1, -2, -2]


y_moves = [2, -2, -1, 1, 2, -2, 1, -1]


def kt_recur(n, board, x, y, counter):
    if counter == n*n:
        return True
    if x<0 or x >= n or y < 0 or y >= n or board[x][y] != -1:
        return False
    board[x][y] = counter
    for x_move, y_move in zip(x_moves, y_moves):
        if kt_recur(n, board, x+x_move, y+y_move, counter+1):
            return True
    board[x][y] = -1
    return False
kt(5)


'''board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]'''


'''pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(board)'''
