'''
BOJ23087 - Shortest Shortest Path (https://www.acmicpc.net/problem/23087)

The shortest shortest path is the shortest path that uses the minimum number of edges.
Find the shortest shortest path and calculate how many distinct shortest shortest paths there are.
'''

# TIME COMPLEXITY : O(N + MK)

import sys, heapq
inf = float('inf')
mod = 10 ** 9 + 9


# 1. TO GET THE INPUT

node_count, edge_count, start, end = map(int, sys.stdin.readline().split())

graph = {}
for node in range(1, node_count + 1):
    graph[node] = []
for edge in range(edge_count):
    nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
    graph[nodeA].append((nodeB, dist))


# 2. TO SOLVE THE PROBLEM - DIJKSTRA

dist = [inf for idx in range(node_count + 1)]
edge_count = [inf for idx in range(node_count + 1)]
case_count = [0 for idx in range(node_count + 1)]

heap = [(0, 0, start)]
dist[start] = 0
edge_count[start] = 0
case_count[start] = 1

while heap:
    
    now_dist, now_edge_count, now_node = heapq.heappop(heap)
    
    if (now_dist < dist[now_node]) or (now_dist == dist[now_node] and now_edge_count <= edge_count[now_node]):
        for next_node, next_dist in graph[now_node]:
            
            new_dist = now_dist + next_dist
            new_edge_count = now_edge_count + 1
            
            if new_dist < dist[next_node]:
                
                dist[next_node] = new_dist
                edge_count[next_node] = new_edge_count
                case_count[next_node] = case_count[now_node] % mod
                heapq.heappush(heap, (new_dist, new_edge_count, next_node))
                
            elif new_dist == dist[next_node]:
                
                if new_edge_count < edge_count[next_node]:
                    
                    dist[next_node] = new_dist
                    edge_count[next_node] = new_edge_count
                    case_count[next_node] = case_count[now_node] % mod
                    heapq.heappush(heap, (new_dist, new_edge_count, next_node))
                    
                elif new_edge_count == edge_count[next_node]:
                    
                    dist[next_node] = new_dist
                    edge_count[next_node] = new_edge_count
                    case_count[next_node] += case_count[now_node]
                    case_count[next_node] %= mod


# 3. TO SOLVE THE PROBLEM

if dist[end] == inf:
    print(-1)
else:
    print(dist[end])
    print(edge_count[end])
    print(case_count[end])