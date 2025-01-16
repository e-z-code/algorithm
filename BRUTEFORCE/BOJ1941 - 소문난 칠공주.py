'''
BOJ1941 - 7 Princesses (https://www.acmicpc.net/problem/1941)

There is a 5 X 5 grid. Each cell is either 'S' or 'Y'.
You want to choose seven connected cells such that at least four are 'S'.
Calculate the number of such cases.
'''

# TIME COMPLEXITY : O(1)

import sys
from itertools import combinations
from collections import deque


# 1. TO GET THE INPUT

grid = []

for row_input in range(5):
    row = list(sys.stdin.readline().strip())
    grid.append(row)


# 2. TO CONSTRUCT ADJACENCY GRAPH

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

adjacent = {}
for row in range(5):
    for col in range(5):
        adjacent[(row, col)] = []
        for idx in range(4):
            new_row = row + dy[idx]
            new_col = col + dx[idx]
            if 0 <= new_row < 5 and 0 <= new_col < 5:
                adjacent[(row, col)].append((new_row, new_col))


# 3. TO SOLVE THE PROBLEM
# There are 25C7 = 480700 cases.

ans = 0

for choice in combinations(adjacent.keys(), 7):

    team_count = 0
    for row, col in choice:
        if grid[row][col] == "S":
            team_count += 1
    
    # There is no need to traverse the graph for every case.
    
    if team_count >= 4:
        
        start_row, start_col = choice[0]
        
        queue = deque([(start_row, start_col)])
        visited = [[0 for col in range(5)] for row in range(5)]
        visited[start_row][start_col] = 1
        
        while queue:
            now_row, now_col = queue.popleft()
            for next_row, next_col in choice:
                if visited[next_row][next_col] == 0 and (next_row, next_col) in adjacent[(now_row, now_col)]:
                    visited[next_row][next_col] = 1
                    queue.append((next_row, next_col))
        
        valid = True
        for row, col in choice:
            if visited[row][col] == 0:
                valid = False
                break
        
        if valid:
            ans += 1

print(ans)