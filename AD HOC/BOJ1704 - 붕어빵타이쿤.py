'''
BOJ1704 - Bungeoppang Tycoon (https://www.acmicpc.net/problem/1704)

There is an N X M Bungeoppang machine.
If you push a cell, the cell and four adjacent cells will be flipped.
Determine the minimum number of pushes to make all cells face top.
'''

# TIME COMPLEXITY : O(NMK) 

import sys


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

grid = []
for row in range(row_count):
    grid.append(list(map(int, sys.stdin.readline().split())))


# 2. TO CONSIDER ALL CASES

min_count = row_count * col_count + 1
answer = None

for case_num in range(1 << col_count):
    
    push_count = 0
    
    now_push = [[0 for col in range(col_count)] for row in range(row_count)]
    now_grid = []
    for row in grid:
        now_grid.append(row[:])
    
    dy = [-1, 0, 1, 0, 0]
    dx = [0, 1, 0, -1, 0]
    
    for col in range(col_count):
        if case_num & (1 << (col_count - 1 - col)):
            now_push[0][col] = 1
            push_count += 1
            for idx in range(5):
                row_to_push = 0 + dy[idx]
                col_to_push = col + dx[idx]
                if 0 <= row_to_push < row_count and 0 <= col_to_push < col_count:
                    now_grid[row_to_push][col_to_push] ^= 1
    
    for row in range(1, row_count):
        for col in range(col_count):
            if now_grid[row-1][col] == 1:
                now_push[row][col] = 1
                push_count += 1
                for idx in range(5):
                    row_to_push = row + dy[idx]
                    col_to_push = col + dx[idx]
                    if 0 <= row_to_push < row_count and 0 <= col_to_push < col_count:
                        now_grid[row_to_push][col_to_push] ^= 1

    valid = True
    for row in now_grid:
        if sum(row) != 0:
            valid = False
            break
    
    if valid and push_count < min_count:
        answer = now_push
        min_count = push_count


# 3. TO SOLVE THE PROBLEM

if answer == None:
    print("IMPOSSIBLE")
else:
    for row in answer:
        print(" ".join(map(str, row)))