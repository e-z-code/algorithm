'''
BOJ31782 - Hypothermia (https://www.acmicpc.net/problem/31782)

There is an N X M grid.
During the daytime, hypothermia is cured if two of the adjacent people are normal.
At night, most K people can newly be hypothermia patients.
Determine the number of people who can always be cured of hypothermia.
'''

# TIME COMPLEXITY : O(NM(N+M))

import sys
from collections import deque


# 1. TO GET THE INPUT

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

row_count, col_count, frostbite_count = map(int, sys.stdin.readline().split())

grid = []
for row in range(row_count):
    grid.append(list(sys.stdin.readline().strip()))


# 2. TO COUNT THE NORMAL PERSON FROM THE INITIAL STATE

frostbite = []

for row in range(row_count):
    for col in range(col_count):
        if grid[row][col] == ".":
            frostbite.append((row, col))

while frostbite:
    
    now_row, now_col = frostbite.pop()
    count = 0
    
    for idx in range(4):
        next_row = now_row + dy[idx]
        next_col = now_col + dx[idx]
        if 0 <= next_row < row_count and 0 <= next_col < col_count and grid[next_row][next_col] == "O":
            count += 1
    
    if count >= 2:
        grid[now_row][now_col] = "O"
        for idx in range(4):
            next_row = now_row + dy[idx]
            next_col = now_col + dx[idx]
            if 0 <= next_row < row_count and 0 <= next_col < col_count and grid[next_row][next_col] == ".":
                frostbite.append((next_row, next_col))


# 3. TO SOLVE THE PROBLEM
# The shape of each group is always rectangle.

ans = 0

for row in range(row_count):
    for col in range(col_count):
        if grid[row][col] == "O":
            
            row_max = row
            col_max = col
            
            queue = deque([(row, col)])
            grid[row][col] = "."
            while queue:
                now_row, now_col = queue.popleft()
                for idx in range(4):
                    next_row = now_row + dy[idx]
                    next_col = now_col + dx[idx]
                    if 0 <= next_row < row_count and 0 <= next_col < col_count and grid[next_row][next_col] == "O":
                        grid[next_row][next_col] = "."
                        queue.append((next_row, next_col))
                        row_max = max(row_max, next_row)
                        col_max = max(col_max, next_col)
            
            height = row_max - row + 1
            width = col_max - col + 1
            
            if min(height, width) > frostbite_count:
                ans += height * width

print(ans)