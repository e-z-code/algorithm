'''
BOJ11495 - Make the Grid 0 (https://www.acmicpc.net/problem/11495)

There is an N x M grid of positive integers.
In one time unit, you can choose two adjacent cells and decrease the numbers in the cell by 1.
If the number is 0, it remains 0.
Determine the minimum time units required to make all cells 0.
'''

# TIME COMPLEXITY : O(T X pow(NM, 3)) [T : Test count]

import sys
from collections import deque
inf = float('inf')


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    row_count, col_count = map(int, sys.stdin.readline().split())
    total_sum = 0
    
    grid = []
    for row_input in range(row_count):
        row = list(map(int, sys.stdin.readline().split()))
        grid.append(row)
        total_sum += sum(row)

    
    # 2. TO CONSTRUCT THE GRAPH
    # Paint the grid like a chessboard and only connect adjacent white cell and black cell pair.
        
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    node_count = row_count * col_count + 2
    
    source = row_count * col_count
    sink = row_count * col_count + 1
    
    graph = {}
    capacity = [[0 for j in range(node_count)] for i in range(node_count)]
    flow = [[0 for j in range(node_count)] for i in range(node_count)]
    
    for node in range(node_count):
        graph[node] = []
    
    for row in range(row_count):
        for col in range(col_count):
            
            node = row * col_count + col
            
            if (row + col) % 2 == 0:
                capacity[source][node] = grid[row][col]
                graph[source].append(node)
                graph[node].append(source)
            else:
                capacity[node][sink] = grid[row][col]
                graph[node].append(sink)
                graph[sink].append(node)
            
            for idx in range(4):
                
                new_row = row + dy[idx]
                new_col = col + dx[idx]
                new_node = new_row * col_count + new_col
                
                if 0 <= new_row < row_count and 0 <= new_col < col_count:
                    if (row + col) % 2 == 0:
                        capacity[node][new_node] = inf
                        graph[node].append(new_node)
                        graph[new_node].append(node)
                    else:
                        capacity[new_node][node] = inf
                        graph[new_node].append(node)
                        graph[node].append(new_node)
    
    
    # 3. EDMOND-KARP
    # Maximum flow equals the maximum count that decreases both numbers. 
    
    double_delete = 0
    
    while True:
        
        # BFS to find the path
        
        parent = [-1 for node in range(node_count)]
        
        queue = deque([source])
        while queue and parent[sink] == -1:
            now_node = queue.popleft()
            for next_node in graph[now_node]:
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
        
        double_delete += max_flow
    
    
    # 4. TO SOLVE THE PROBLEM
    
    print(total_sum - double_delete)