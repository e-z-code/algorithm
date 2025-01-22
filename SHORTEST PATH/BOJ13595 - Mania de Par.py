'''
BOJ13595 - Mania de Par (https://www.acmicpc.net/problem/13595)

Determine the minimum distance from node 1 to node N that uses an even number of edges.
'''

# TIME COMPLEXITY : O(E log V)

import sys, heapq
inf = float('inf')


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

graph = {}
for node in range(1, node_count + 1):
    graph[node] = []

for edge in range(edge_count):
    nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
    graph[nodeA].append((nodeB, dist))
    graph[nodeB].append((nodeA, dist))


# 2. DIJKSTRA

dist = [[inf, inf] for node in range(node_count + 1)]

heap = [(0, 1, 0)]
dist[1][0] = 0

while heap:
    
    now_dist, now_node, now_parity = heapq.heappop(heap)
    next_parity = (now_parity + 1) % 2
    
    if dist[now_node][now_parity] >= now_dist:
        for next_node, next_dist in graph[now_node]:
            total_dist = now_dist + next_dist
            if dist[next_node][next_parity] > total_dist:
                dist[next_node][next_parity] = total_dist
                heapq.heappush(heap, (total_dist, next_node, next_parity))


# 3. TO SOLVE THE PROBLEM

if dist[node_count][0] == inf:
    print(-1)
else:
    print(dist[node_count][0])