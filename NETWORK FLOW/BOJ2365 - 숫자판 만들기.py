'''
BOJ2365 - Number Grid (https://www.acmicpc.net/problem/2365)

There is an N X N grid.
You are only given the sum of each row and column.
Fill the grid so that the maximum number is the minimum.
'''

# TIME COMPLEXITY : O(N^5)

import sys
from collections import deque
inf = float('inf')


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())
row_sum = list(map(int, sys.stdin.readline().split()))
col_sum = list(map(int, sys.stdin.readline().split()))

cell_count = size * size


# 2. BINARY SEARCH

left = 0
right = 10000

ans = [[0 for col in range(size)] for row in range(size)]

while left + 1 < right:
    
    mid = (left + right) // 2
    
    
    # 3. TO CONSTRUCT A GRAPH
    # Cell : 0 ~ cell_count - 1 / Row : cell_count ~ cell_count + size - 1 / Col : cell_count + size ~ cell_count + 2 * size - 1
    
    source = cell_count + 2 * size
    sink = cell_count + 2 * size + 1
    node_count = cell_count + 2 * size + 2
    
    capacity = {}
    flow = {}
    
    for node in range(node_count):
        
        capacity[node] = {}
        flow[node] = {}
        
    for cell in range(cell_count):
        
        row = cell // size
        col = cell % size
        
        capacity[cell_count + row][cell] = mid
        capacity[cell][cell_count + row] = 0
        flow[cell_count + row][cell] = 0
        flow[cell][cell_count + row] = 0
        
        capacity[cell][cell_count + size + col] = mid
        capacity[cell_count + size + col][cell] = 0
        flow[cell][cell_count + size + col] = 0
        flow[cell_count + size + col][cell] = 0
    
    for row in range(size):
        
        capacity[source][cell_count + row] = row_sum[row]
        capacity[cell_count + row][source] = 0
        flow[source][cell_count + row] = 0
        flow[cell_count + row][source] = 0
    
    for col in range(size):
        
        capacity[cell_count + size + col][sink] = col_sum[col]
        capacity[sink][cell_count + size + col] = 0
        flow[cell_count + size + col][sink] = 0
        flow[sink][cell_count + size + col] = 0
    
    
    # 4. EDMOND-KARP
    
    total_flow = 0
    
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
        
        max_flow = inf
        node = sink
        while node != source:
            max_flow = min(max_flow, capacity[parent[node]][node] - flow[parent[node]][node])
            node = parent[node]
        
        node = sink
        while node != source:
            flow[parent[node]][node] += max_flow
            flow[node][parent[node]] -= max_flow
            node = parent[node]
        total_flow += max_flow
    
    
    # 5. TO SOLVE THE PROBLEM
    
    if total_flow == sum(row_sum):
        right = mid
        for cell in range(cell_count):
            row = cell // size
            col = cell % size
            ans[row][col] = flow[cell_count + row][cell]
    else:
        left = mid

print(right)
for row in ans:
    print(" ".join(map(str, row)))