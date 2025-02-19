'''
BOJ16173 - Jump King Jelly (Small) (https://www.acmicpc.net/problem/16173)

There is an N X N grid.
Jelly wants to jump from (0, 0) to (N, N).
However, it can only jump as much as the number on the cell.
Determine if jelly can jump as it wants.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())

grid = []
for row in range(size):
    grid.append(list(map(int, sys.stdin.readline().split())))


# 2. CASEWORK

possible = False

if size == 2:
    
    if grid[0][0] == 1:
        if (grid[0][1] == 1 or grid[1][0] == 1):
            possible = True

elif size == 3:
    
    if grid[0][0] == 2:
        if (grid[0][2] == 2 or grid[2][0] == 2):
            possible = True
    
    if grid[0][0] == 1:
        if (grid[0][1] == 2 and grid[2][1] == 1) or (grid[1][0] == 2 and grid[1][2] == 1):
            possible = True
        if grid[0][1] == 1:
            if grid[0][2] == 2:
                possible = True
            if (grid[1][1] == 1 and grid[1][2] == 1) or (grid[1][1] == 1 and grid[2][1] == 1) or (grid[0][2] == 1 and grid[1][2] == 1):
                possible = True
        if grid[1][0] == 1:
            if grid[2][0] == 2:
                possible = True
            if (grid[2][0] == 1 and grid[2][1] == 1) or (grid[1][1] == 1 and grid[2][1] == 1) or (grid[1][1] == 1 and grid[1][2] == 1):
                possible = True


# 3. TO SOLVE THE PROBLEM

if possible:
    print("HaruHaru")
else:
    print("Hing")