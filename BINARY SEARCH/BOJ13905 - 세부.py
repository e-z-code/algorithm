'''
BOJ13905 - Cebu (https://www.acmicpc.net/problem/13905)

There is a weighted graph with N nodes and M edges.
You cannot carry gold heavier than the weight of an edge.
Determine the maximum weight of gold from start to end.
'''

# TIME COMPLEXITY : O((N + M)sqrt(K))

import sys
from collections import deque


# 2. BFS FUNCTION

def bfs(weight):
    
    queue = deque([start])
    
    visited = [0 for idx in range(node_count + 1)]
    visited[start] = 1
    
    while queue:
        now = queue.popleft()
        for next, max_weight in graph[now]:
            if visited[next] == 0 and weight <= max_weight:
                queue.append(next)
                visited[next] = 1
    
    if visited[end] == 1:
        return True
    else:
        return False


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

start, end = map(int, sys.stdin.readline().split())

graph = {}
for node in range(1, node_count + 1):
    graph[node] = []

for edge in range(edge_count):
    nodeA, nodeB, weight = map(int, sys.stdin.readline().split())
    graph[nodeA].append((nodeB, weight))
    graph[nodeB].append((nodeA, weight))


# 3. BINARY SEARCH
# Binary search on weight you carry

left = 0
right = 1000000

while left + 1 < right:
    
    mid = (left + right) // 2
    possible = bfs(mid)
    
    if possible:
        left = mid
    else:
        right = mid

print(left)