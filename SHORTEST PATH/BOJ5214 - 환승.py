'''
BOJ5214 - Transfer (https://www.acmicpc.net/problem/5214)

There are M hyper-tubes that connect K nodes.
Determine the minimum number of nodes to visit to reach node N from node 1.
'''

# TIME COMPLEXITY : O(N + MK)

import sys
from collections import deque


# 1. TO GET THE INPUT AND CONSTRUCT THE GRAPH

stop_count, tube_size, tube_count = map(int, sys.stdin.readline().split())
node_count = stop_count + tube_count

graph = {}
for node in range(node_count):
    graph[node] = []

for tube_idx in range(tube_count):

    tube = stop_count + tube_idx
    
    tube_stops = list(map(int, sys.stdin.readline().split()))
    for stop in tube_stops:
        graph[stop-1].append(tube)
        graph[tube].append(stop-1)


# 2. TO SOLVE THE PROBLEM

visited = [-1 for node in range(node_count)]

queue = deque([0])
visited[0] = 0

while queue:
    
    now_node = queue.popleft()
    for next_node in graph[now_node]:
        if visited[next_node] == -1:
            queue.append(next_node)
            visited[next_node] = visited[now_node] + 1

if visited[stop_count] == -1:
    print(-1)
else:
    print(visited[stop_count - 1] // 2 + 1)