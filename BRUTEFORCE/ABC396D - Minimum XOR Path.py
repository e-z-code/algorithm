'''
ABC396D - Minimum XOR Path (https://atcoder.jp/contests/abc396/tasks/abc396_d)

There is a graph of N nodes and M edges.
Among all simple paths from node 1 to node N, find the minimum XOR value of the labels of the edges on the path.
'''

# TIME COMPLEXITY: O(N!) 

import sys
from collections import deque


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

graph = {}
for node in range(node_count):
    graph[node] = []
for edge in range(edge_count):
    nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append((nodeB, dist))
    graph[nodeB].append((nodeA, dist))


# 2. BRUTE-FORCING

ans = float('inf')

queue = deque([(0, 1, 0)])

while queue:
    
    now_node, now_visited, now_val = queue.popleft()
    
    for next_node, dist in graph[now_node]:
        if now_visited & (1 << next_node) == 0:
            next_visited = now_visited | (1 << next_node)
            next_val = now_val ^ dist
            if next_node == node_count - 1:
                ans = min(ans, next_val)
            else:
                queue.append((next_node, next_visited, next_val))

print(ans)