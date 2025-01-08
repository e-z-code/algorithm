'''
BOJ2316 - Round Trip 2 (https://www.acmicpc.net/problem/2316)

There is a graph of N nodes and P edges.
You can visit a node at most once (except for nodes 1 and 2).
Determine the maximum number of paths from nodes 1 to 2.
'''

# TIME COMPLEXITY : O(N X P^2)

import sys
from collections import deque
inf = float('inf')


# 1. TO GET THE INPUT AND CONSTRUCT THE GRAPH
# For node N, 2 * N is a node for in-degree and 2 * N + 1 is a node for out-degree.

node_count, edge_count = map(int, sys.stdin.readline().split())

capacity = [[0 for j in range(node_count << 1)] for i in range(node_count << 1)]
flow = [[0 for j in range(node_count << 1)] for i in range(node_count << 1)]

for node in range(node_count):
    
    if node == 0 or node == 1:
        capacity[node << 1][(node << 1) | 1] = inf
    else:
        # Visit each vertex at most once.
        capacity[node << 1][(node << 1) | 1] = 1 
    
for edge in range(edge_count):
    
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    
    capacity[(nodeA << 1) | 1][(nodeB << 1)] = 1
    capacity[(nodeB << 1) | 1][(nodeA << 1)] = 1


# 2. EDMOND-KARP

ans = 0
source = 0
sink = 3

while True:
    
    # BFS to find the path
    
    parent = [-1 for node in range(node_count << 1)]
    
    queue = deque([source])
    while queue and parent[sink] == -1:
        now_node = queue.popleft()
        for next_node in range(node_count << 1):
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

print(ans)