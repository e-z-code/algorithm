'''
BOJ4672 - Don't Get Rooked (https://www.acmicpc.net/problem/4672)

There is an N X N chessboard with some walls.
Determine the maximum number of rooks placed on the board without attacking each other.
'''

# TIME COMPLEXITY : O(pow(N, 3) * pow(2, pow(N, 2)))

import sys


# 2. A FUNCTION TO CHECK VALIDITY

def valid(board):
    
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == "O":
                
                # Left
                
                now_row = row
                now_col = col - 1
                while 0 <= now_col and board[now_row][now_col] != "X":
                    if board[now_row][now_col] == "O":
                        return False
                    now_col -= 1
                
                # Right
                
                now_row = row
                now_col = col + 1
                while now_col < board_size and board[now_row][now_col] != "X":
                    if board[now_row][now_col] == "O":
                        return False
                    now_col += 1
                
                # Up 
                
                now_row = row - 1
                now_col = col
                while 0 <= now_row and board[now_row][now_col] != "X":
                    if board[now_row][now_col] == "O":
                        return False
                    now_row -= 1
                
                # Down
                
                now_row = row + 1
                now_col = col
                while now_row < board_size and board[now_row][now_col] != "X":
                    if board[now_row][now_col] == "O":
                        return False
                    now_row += 1
    
    return True


# 3. A FUNCTION TO CHECK THE NUMBER OF ROOKS PLACED IN THE CASE

def rook_count(case):
    
    count = 0
    
    while case != 0:
        if case % 2 == 1:
            count += 1
        case //= 2
    
    return count


# 1. TO GET THE INPUT

while True:
    
    board_size = int(sys.stdin.readline())
    if board_size == 0:
        break
    
    board = []
    for row_num in range(board_size):
        row = list(sys.stdin.readline().strip())
        board.append(row)
    
    
    # 4. BRUTE-FORCE
    # Number each cell. Then, number each case based on which cell is on.
    
    ans = 0
    
    for case in range(1 << (board_size * board_size)):
        
        possible = True
        
        board_copy = []
        for row in board:
            board_copy.append(row[:])
        
        for cell in range(board_size * board_size):
            
            row_num, col_num = cell // board_size, cell % board_size
            if case & (1 << cell): # If a cell is on
                if board_copy[row_num][col_num] == "X": # The cell cannot be on if it is a wall
                    possible = False
                    break
                else: # Change accordingly
                    board_copy[row_num][col_num] = "O" 
        
        if possible and valid(board_copy):
            ans = max(ans, rook_count(case))
    
    print(ans)