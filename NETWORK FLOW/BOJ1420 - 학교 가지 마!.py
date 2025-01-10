'''
BOJ1420 - No School! (https://www.acmicpc.net/problem/1420)

Given an N X M grid, you want to make it impossible to reach H from K.
Determine the minimum number of cells to block.
'''

# TIME COMPLEXITY : O((NM)^3)

import sys
from collections import deque
inf = float('inf')


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())
node_count = row_count * col_count * 2

grid = []
for row_input in range(row_count):
    row = list(sys.stdin.readline().strip())
    grid.append(row)


# 2. TO CONSTRUCT A GRAPH
# For node N, 2 * N is a node for in-degree and 2 * N + 1 is a node for out-degree.

source = None
sink = None

capacity = {}
flow = {}

# To connect two nodes from the same cell

for row in range(row_count):
    for col in range(col_count):
        
        now_cell = row * col_count + col
        now_in_node = now_cell << 1
        now_out_node = (now_cell << 1) | 1
        
        if grid[row][col] == "#":
            continue
        else:
            if grid[row][col] == "K":
                source = now_in_node
            if grid[row][col] == "H":
                sink = now_out_node
        
        capacity[now_in_node] = {}
        capacity[now_out_node] = {} 
        flow[now_in_node] = {}
        flow[now_out_node] = {}
        
        if now_in_node == source or now_out_node == sink:
            capacity[now_in_node][now_out_node] = inf
        else:
            capacity[now_in_node][now_out_node] = 1
        capacity[now_out_node][now_in_node] = 0
        flow[now_in_node][now_out_node] = 0
        flow[now_out_node][now_in_node] = 0

# Connect nodes from different cells

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for row in range(row_count):
    for col in range(col_count):
        
        now_cell = row * col_count + col
        now_in_node = now_cell << 1
        now_out_node = (now_cell << 1) | 1
        
        if grid[row][col] != "#" and grid[row][col] != "H":
            for idx in range(4):
                next_row = row + dy[idx]
                next_col = col + dx[idx]
                
                next_cell = next_row * col_count + next_col
                next_in_node = next_cell << 1
                next_out_node = (next_cell << 1) | 1
                
                if 0 <= next_row < row_count and 0 <= next_col < col_count and grid[next_row][next_col] != "#" and grid[next_row][next_col] != "K":
                    
                    capacity[now_out_node][next_in_node] = 1
                    capacity[next_in_node][now_out_node] = 0
                    flow[now_out_node][next_in_node] = 0
                    flow[next_in_node][now_out_node] = 0


# 3. EDMOND-KARP

ans = 0

while True:
    
    # BFS to find the path
    
    parent = [-1 for node in range(node_count)]
    
    queue = deque([source])
    while queue and parent[sink] == -1:
        now_node = queue.popleft()
        for next_node in capacity[now_node]:
            if capacity[now_node][next_node] - flow[now_node][next_node] > 0 and parent[next_node] == -1:
                queue.append(next_node)
                parent[next_node] = now_node
    
    if parent[sink] == -1:
        break
    
    # Find maximum flow and add it
    
    max_flow = float('inf')
    node = sink
    while node != source:
        max_flow = min(max_flow, capacity[parent[node]][node] - flow[parent[node]][node])
        node = parent[node]
    
    node = sink
    while node != source:
        flow[parent[node]][node] += max_flow
        flow[node][parent[node]] -= max_flow
        node = parent[node]
    ans += max_flow


# 4. TO SOLVE THE PROBLEM

if sink - 1 in capacity[source + 1]:
    print(-1)
else:
    print(ans)