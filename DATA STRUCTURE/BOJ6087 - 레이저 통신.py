'''
BOJ6087 - Laser Phones (https://www.acmicpc.net/problem/6087)

There is a W X H grid.
You can install mirrors that bend the light by 90 degrees anywhere.
Given two points, determine the minimum number of mirrors such that a light can reach from one point to the other point.
'''

# TIME COMPLEXITY : O(WH log WH)

import sys, heapq

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


# 1. TO GET THE INPUT

col_count, row_count = map(int, sys.stdin.readline().split())

start_row, start_col = None, None
end_row, end_col = None, None

grid = []
for row_num in range(row_count):
    row = list(sys.stdin.readline().strip())
    for col_num in range(col_count):
        if row[col_num] == "C":
            if start_row == None:
                start_row, start_col = row_num, col_num
            else:
                end_row, end_col = row_num, col_num
    grid.append(row)


# 2. TO SOLVE THE PROBLEM

visited = [[-1 for col in range(col_count)] for row in range(row_count)]
visited[start_row][start_col] = 0

heap = [(0, start_row, start_col)]

while heap:
    now_val, now_row, now_col = heapq.heappop(heap)
    for idx in range(4):
        new_row = now_row + dy[idx]
        new_col = now_col + dx[idx]
        while 0 <= new_row < row_count and 0 <= new_col < col_count:
            if grid[new_row][new_col] == "*":
                break
            else:
                if visited[new_row][new_col] == -1:
                    visited[new_row][new_col] = now_val
                    heapq.heappush(heap, (now_val + 1, new_row, new_col))
                new_row += dy[idx]
                new_col += dx[idx]

print(visited[end_row][end_col])