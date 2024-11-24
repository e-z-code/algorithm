'''
BOJ8972 - Crazy Arduino (https://www.acmicpc.net/problem/8972)

You control an arduino on an R X C board.
You aim to avoid crazy robots.
Each move consists of the following:

(1) Arduino moves to an adjacent cell or stay.
(2) If the arduino shares the cell with a crazy robot, you lose.
(3) Crazy robots move to an adjacent cell that minimizes the distance with your arduino.
(4) If a robot shares with the arduino, you lose.
(5) If there are two more robots in the same cell, they all explode.

Determine the state of the board after X moves.
'''

# TIME COMPLEXITY : O(RCX)

import sys


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

board = []
for row_input in range(row_count):
    row = list(sys.stdin.readline().strip())
    board.append(row)

moves = list(sys.stdin.readline().strip())
moves = list(map(int, moves))


# 2. TO SIMULATE

dy = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dx = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

now_move = 1
lose = False

for move in moves:
    
    new_board = [["." for col in range(col_count)] for row in range(row_count)]
    
    # To find the arduino and move
    
    my_row, my_col = 0, 0
    for row in range(row_count):
        for col in range(col_count):
            if board[row][col] == "I":
                my_row = row + dy[move]
                my_col = col + dx[move]
                if board[my_row][my_col] == "R":
                    lose = True
                else:
                    new_board[my_row][my_col] = "I"
    
    # To find robots and move
    
    for row in range(row_count):
        for col in range(col_count):
            if board[row][col] == "R":
                
                enemy_row, enemy_col = None, None
                for idx in range(1, 10):
                    next_row = row + dy[idx]
                    next_col = col + dx[idx]
                    if 0 <= next_row < row_count and 0 <= next_col < col_count:
                        if enemy_row == None or abs(my_row - enemy_row) + abs(my_col - enemy_col) > abs(my_row - next_row) + abs(my_col - next_col):
                            enemy_row, enemy_col = next_row, next_col
                
                if new_board[enemy_row][enemy_col] == ".":
                    new_board[enemy_row][enemy_col] = "R"
                elif new_board[enemy_row][enemy_col] == "I":
                    lose = True
                else:
                    new_board[enemy_row][enemy_col] = "X"
    
    # To process explosions
    
    for row in range(row_count):
        for col in range(col_count):
            if new_board[row][col] == "X":
                new_board[row][col] = "."
    
    board = new_board
    
    if lose:
        break
    now_move += 1


# 3. TO PRINT THE ANSWER

if lose:
    print("kraj {}".format(now_move))
else:
    for row in board:
        print("".join(row))