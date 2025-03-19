'''
BOJ17500 - Boundary (https://www.acmicpc.net/problem/17500)

Construct a fence so that no animals of different species belong together.
'''

# TIME COMPLEXITY : O(pow(4, N^2))

import sys
from collections import deque


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())

grid = []
for row in range(size):
    grid.append(list(sys.stdin.readline().strip()))


# 2. TO STORE POSSIBLE FENCES

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cases = []
stack = [(0, 1, [(0, 0)])]

# DFS to decrease the maximum size of the stack

while stack:
    
    now_loc, now_visited, now_order = stack.pop()
    now_row, now_col = now_loc // (size + 1), now_loc % (size + 1)
    
    for idx in range(4):
        
        next_row = now_row + dy[idx]
        next_col = now_col + dx[idx]
        next_loc = next_row * (size + 1) + next_col
        next_order = now_order[:] + [(next_row, next_col)]
        
        if 0 <= next_row <= size and 0 <= next_col <= size and not (now_visited & (1 << next_loc)):
            
            next_visited = now_visited | (1 << next_loc)
            next_order = now_order[:] + [(next_row, next_col)]
            
            if next_row == size and next_col == size:
                cases.append(next_order)
            else:
                stack.append((next_loc, next_visited, next_order))


# 3. TO CHECK EACH CASE

row_size = 2 * size + 3
col_size = 4 * size + 3

possible = "no"

for case in cases:
    
    now_case = [[" " for col in range(col_size)] for row in range(row_size)]
    
    # Boundary
    
    for row in range(row_size):
        now_case[row][0] = "#"
        now_case[row][-1] = "#"
    for col in range(col_size):
        now_case[0][col] = "#"
        now_case[-1][col] = "#"
    
    # Corner
    
    for row in range(size + 1):
        for col in range(size + 1):
            now_case[2*row+1][4*col+1] = "+"
    
    # Animal
    
    for row in range(size):
        for col in range(size):
            now_case[2*row+2][4*col+3] = grid[row][col]
    
    # Fence
    
    for idx in range(len(case) - 1):
        
        now_row, now_col = case[idx]
        now_row, now_col = 2*now_row+1, 4*now_col+1
        next_row, next_col = case[idx+1]
        next_row, next_col = 2*next_row+1, 4*next_col+1
        
        if now_row == next_row:
            if now_col > next_col:
                now_col, next_col = next_col, now_col
            for col in range(now_col+1, next_col):
                now_case[now_row][col] = "-"
        else:
            if now_row > next_row:
                now_row, next_row = next_row, now_row
            for row in range(now_row+1, next_row):
                now_case[row][now_col] = "|"
    
    # Check
    
    dy = [-2, 0, 2, 0]
    dx = [0, 4, 0, -4]
    
    valid = True
    visited = [[0 for col in range(size)] for row in range(size)]
    
    for row in range(size):
        for col in range(size):
            if visited[row][col] == 0:
                
                now_animal = grid[row][col]
                
                visited[row][col] = 1
                queue = deque([(row, col)])
                
                while queue:
                    
                    now_row, now_col = queue.popleft()
                    now_row, now_col = 2*now_row+2, 4*now_col+3
                    for idx in range(4):
                        next_row = now_row + dy[idx]
                        next_col = now_col + dx[idx]
                        if 0 <= next_row < row_size and 0 <= next_col < col_size and now_case[next_row][next_col] != "#" and now_case[(now_row + next_row) // 2][(now_col + next_col) // 2] == " ":
                            next_row, next_col = (next_row-2) // 2, (next_col-3) // 4
                            if visited[next_row][next_col] == 0:
                                next_animal = grid[next_row][next_col]
                                if now_animal == ".":
                                    visited[next_row][next_col] = 1
                                    queue.append((next_row, next_col))
                                    now_animal = next_animal
                                elif next_animal == ".":
                                    visited[next_row][next_col] = 1
                                    queue.append((next_row, next_col))
                                elif now_animal == next_animal:
                                    visited[next_row][next_col] = 1
                                    queue.append((next_row, next_col))
                                else:
                                    valid = False
    
    
    # 4. TO SOLVE THE PROBLEM
    
    if valid:
        possible = "yes"
        print(possible)
        for row in now_case:
            print("".join(row))
        break
    
if possible == "no":
    print(possible)