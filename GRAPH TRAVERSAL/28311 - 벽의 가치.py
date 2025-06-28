'''
BOJ28311 - Value of Walls (https://www.acmicpc.net/problem/28311)

There is an R X C grid.
Let (r, c) be the destination cell and (X[i], Y[i]) be the i-th pawn's location.
The score of the grid equals the sum of the minimum distance from each pawn to the destination.

Assume you remove a wall.
The new path may become available, and thus, the score would change.
Let the difference in score be the value of the wall.

Calculate the score of the grid and the sum of the value of the walls.
'''

# TIME COMPLEXITY : O(W(N+M))

import sys
from collections import deque
inf = float('inf')

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    row_count, col_count, goal_count, start_row, start_col = map(int, sys.stdin.readline().split())
    start_row -= 1
    start_col -= 1
    
    goals = []
    for goal in range(goal_count):
        goal_row, goal_col = map(int, sys.stdin.readline().split())
        goal_row -= 1
        goal_col -= 1
        goals.append((goal_row, goal_col))
    
    grid = []
    for row_num in range(row_count):
        row = list(sys.stdin.readline().strip())
        grid.append(row)
    
    
    # 2. TO CALCULATE GAME POINT
    
    queue = deque([(start_row, start_col)])
    
    normal = [[inf for col in range(col_count)] for row in range(row_count)]
    normal[start_row][start_col] = 0
    
    while queue:
        now_row, now_col = queue.popleft()
        for idx in range(4):
            next_row = now_row + dy[idx]
            next_col = now_col + dx[idx]
            if 0 <= next_row < row_count and 0 <= next_col < col_count:
                if normal[next_row][next_col] == inf and grid[next_row][next_col] == ".":
                    normal[next_row][next_col] = normal[now_row][now_col] + 1
                    queue.append((next_row, next_col))
    
    score = 0
    for goal_row, goal_col in goals:
        score += normal[goal_row][goal_col]
    
    
    # 3. TO CALCULATE VALUE OF WALLS
    # modified[R][C][(r, c)] = Minimum distance to (R, C) when destroyed the wall (r, c)
    
    queue = deque([(start_row, start_col, -1, -1)])
    
    modified = [[{} for col in range(col_count)] for row in range(row_count)]
    modified[start_row][start_col][(-1, -1)] = 0
    
    while queue:
        now_row, now_col, now_break_row, now_break_col = queue.popleft()
        now_dist = modified[now_row][now_col][(now_break_row, now_break_col)]
        for idx in range(4):
            next_row = now_row + dy[idx]
            next_col = now_col + dx[idx]
            if 0 <= next_row < row_count and 0 <= next_col < col_count:
                if grid[next_row][next_col] == "W":
                    if now_break_row == -1 and now_break_col == -1:
                        if (next_row, next_col) not in modified[next_row][next_col]:
                            modified[next_row][next_col][(next_row, next_col)] = now_dist + 1
                            queue.append((next_row, next_col, next_row, next_col))
                else:
                    if now_break_row == -1 and now_break_col == -1:
                        if (-1, -1) not in modified[next_row][next_col]:
                            modified[next_row][next_col][(-1, -1)] = now_dist + 1
                            queue.append((next_row, next_col, -1, -1))
                    else:
                        if (now_break_row, now_break_col) not in modified[next_row][next_col] and normal[next_row][next_col] > now_dist + 1:
                            modified[next_row][next_col][(now_break_row, now_break_col)] = now_dist + 1
                            queue.append((next_row, next_col, now_break_row, now_break_col))
    
    
    # 4. TO SOLVE THE PROBLEM
    
    total_score = 0
    wall_value = 0
    
    for goal_row, goal_col in goals:
        score = modified[goal_row][goal_col][(-1, -1)]
        for break_row, break_col in modified[goal_row][goal_col]:
            if break_row != -1 and break_col != -1:
                wall_value += max(0, score - modified[goal_row][goal_col][(break_row, break_col)])
        total_score += score
    
    print(total_score, wall_value)