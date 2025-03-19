'''
BOJ18071 - Equidistant (https://www.acmicpc.net/problem/18071)

There is a tree graph of N nodes.
Given C teams, find the node of equal distance from all C teams. 
'''

# TIME COMPLEXITY : O(N)

import sys
from collections import deque


# 1. TO GET THE INPUT

node_count, team_count = map(int, sys.stdin.readline().split())
edge_count = node_count - 1

graph = {}
for node in range(1, node_count + 1):
    graph[node] = []
for edge in range(edge_count):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)

teams = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM - BFS

queue = deque([])
dist = [-1 for node in range(node_count + 1)]
equal_count = [-1 for node in range(node_count + 1)]

for team in teams:
    queue.append(team)
    dist[team] = 0
    equal_count[team] = 1

while queue:
    
    now_node = queue.popleft()
    for next_node in graph[now_node]:
        if dist[next_node] == -1:
            queue.append(next_node)
            dist[next_node] = dist[now_node] + 1
            equal_count[next_node] = equal_count[now_node]
        else:
            if dist[now_node] + 1 == dist[next_node]:
                equal_count[next_node] += equal_count[now_node]


# 3. TO SOLVE THE PROBLEM

possible = "NO"
ans_node = -1

for node in range(1, node_count + 1):
    if equal_count[node] == team_count:
        possible = "YES"
        ans_node = node
        break

print(possible)
if possible == "YES":
    print(ans_node)