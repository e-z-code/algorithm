'''
BOJ25343 - Longest-Longest Increasing Subsequence (https://www.acmicpc.net/problem/25343)

There is an N X N grid.
Determine the length of LIS along the shortest path from the top left cell to the bottom right cell.
'''

# TIME COMPLEXITY : O(N^4)

import sys


# 1. TO GET THE INPUT
# To convert 2-dimensional array to 1-dimension array.

size = int(sys.stdin.readline())

arr = []
for row_input in range(size):
    row = list(map(int, sys.stdin.readline().split()))
    for num in row:
        arr.append(num)


# 2. TO CONSTRUCT THE GRAPH

graph = {}
for i in range(size * size):
    graph[i] = []

for i in range(size * size):
    i_row = i // size
    i_col = i % size
    for j in range(i + 1, size * size):
        j_row = j // size
        j_col = j % size
        if i_row <= j_row and i_col <= j_col and arr[i] < arr[j]:
            graph[j].append(i)


# 3. LIS

dp = [1 for idx in range(size * size)]

for j in range(size * size):
    for i in graph[j]:
        dp[j] = max(dp[i] + 1, dp[j])

print(max(dp))