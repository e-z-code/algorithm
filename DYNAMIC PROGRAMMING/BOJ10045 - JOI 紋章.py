'''
BOJ10045 - JOI Emblem (https://www.acmicpc.net/problem/10045)

There is an N X M JOI emblem and a 2 X 2 JOI flag.
Both consist of 'J', 'O', and 'I'.
You can change a cell of the emblem to any character you want.
Determine the maximum number of matches between the emblem and the flag.
'''

# TIME COMPLEXITY : O(NM)

import sys


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

grid = []
for row in range(row_count):
    grid.append(list(sys.stdin.readline().strip()))

key = []
for row in range(2):
    key.append(list(sys.stdin.readline().strip()))


# 2. TO SOLVE THE PROBLEM
# change[i][j][k] = The number of increased match when changing (i, j) to the character k.

char_to_num = {"J":0, "O":1, "I":2}

count = 0
change = [[[0, 0, 0] for col in range(col_count)] for row in range(row_count)]

for row in range(row_count - 1):
    for col in range(col_count - 1):
        
        unmatched_cell = []
        
        if grid[row][col] != key[0][0]:
            unmatched_cell.append((row, col, key[0][0]))
        if grid[row][col+1] != key[0][1]:
            unmatched_cell.append((row, col+1, key[0][1]))
        if grid[row+1][col] != key[1][0]:
            unmatched_cell.append((row+1, col, key[1][0]))
        if grid[row+1][col+1] != key[1][1]:
            unmatched_cell.append((row+1, col+1, key[1][1]))
        
        # If all cells match, to change any of cells would decrease the number of match by 1.
        if len(unmatched_cell) == 0:
            count += 1
            for num in range(3):
                change[row][col][num] -= 1
                change[row+1][col][num] -= 1
                change[row][col+1][num] -= 1
                change[row+1][col+1][num] -= 1

        # If only a cell is different, to properly change the cell can increase the number of match by 1.
        elif len(unmatched_cell) == 1:
            row_to_change, col_to_change, char_to_change = unmatched_cell[0]
            change[row_to_change][col_to_change][char_to_num[char_to_change]] += 1

best_change = 0
for row in range(row_count):
    for col in range(col_count):
        best_change = max(best_change, max(change[row][col]))

print(count + best_change)