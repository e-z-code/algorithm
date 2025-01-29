'''
BOJ30508 - I hate puddles (https://www.acmicpc.net/problem/30508)

There is an N X M grid with K drains.
If water does not drain, the cell becomes a puddle.
You put on shoes of size H X W.
Determine the number of ways you can step on a grid without stepping on a puddle.
'''

# TIME COMPLEXITY : O(HW)

import sys
from collections import deque


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())
shoe_height, shoe_width = map(int, sys.stdin.readline().split())

grid = []
for row in range(row_count):
    grid.append(list(map(int, sys.stdin.readline().split())))

drain_count = int(sys.stdin.readline())

drains = []
for drain in range(drain_count):
    row, col = map(int, sys.stdin.readline().split())
    drains.append((row-1, col-1))


# 2. TO FIND DRY LANDS

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

visited = [[1 for col in range(col_count)] for row in range(row_count)]

queue = deque(drains[:])
for drain_row, drain_col in queue:
    visited[drain_row][drain_col] = 0

while queue:
    now_row, now_col = queue.popleft()
    for idx in range(4):
        next_row = now_row + dy[idx]
        next_col = now_col + dx[idx]
        if 0 <= next_row < row_count and 0 <= next_col < col_count and visited[next_row][next_col] == 1 and grid[now_row][now_col] <= grid[next_row][next_col]:
            visited[next_row][next_col] = 0
            queue.append((next_row, next_col))


# 3. 2-DIMENSIONAL PREFIX SUM

for row in range(row_count):
    for col in range(col_count):
        
        if row == 0:
            if col == 0:
                continue
            else:
                visited[row][col] += visited[row][col-1]
        else:
            if col == 0:
                visited[row][col] += visited[row-1][col]
            else:
                visited[row][col] += visited[row-1][col] + visited[row][col-1] - visited[row-1][col-1]


# 4. TO SOLVE THE PROBLEM

ans = 0

for row in range(shoe_height-1, row_count):
    for col in range(shoe_width-1, col_count):
        
        if row == shoe_height - 1:
            if col == shoe_width - 1:
                dry_count = visited[row][col]
            else:
                dry_count = visited[row][col] - visited[row][col-shoe_width]
        else:
            if col == shoe_width - 1:
                dry_count = visited[row][col] - visited[row-shoe_height][col]
            else:
                dry_count = visited[row][col] - visited[row-shoe_height][col] - visited[row][col-shoe_width] + visited[row-shoe_height][col-shoe_width]
        
        if dry_count == 0:
            ans += 1

print(ans)