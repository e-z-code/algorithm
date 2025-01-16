'''
BOJ11900 - Difference Graph (https://www.acmicpc.net/problem/11900)

There is an array A and a graph of N nodes without edges.
If u > v and A[u - v] > 0, you add an edge <u, v> of length A[u - v].
If u < v and A[u - v + N], you add an edge <u, v> of length A[u - v + N].
Answer Q queries that ask the minimum distance between two nodes.
'''

# TIME COMPLEXITY : O(N^2 log N + Q)

import sys, heapq
inf = float('inf')


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())
cost = list(map(int, sys.stdin.readline().split()))


# 2. DIJKSTRA
# What only matters is the difference between two nodes.

dist = [inf for diff in range(node_count)]
dist[0] = 0

heap = [[0, 0]]
while heap:
    now_dist, now_diff = heapq.heappop(heap)
    if now_dist <= dist[now_diff]:
        for next_diff in range(node_count):
            if now_diff < next_diff and cost[now_diff - next_diff] > 0:
                new_dist = now_dist + cost[now_diff - next_diff] 
                if new_dist < dist[next_diff]:
                    dist[next_diff] = new_dist
                    heapq.heappush(heap, [new_dist, next_diff])
            if now_diff > next_diff and cost[now_diff - next_diff - 1] > 0:
                new_dist = now_dist + cost[now_diff - next_diff - 1]
                if new_dist < dist[next_diff]:
                    dist[next_diff] = new_dist
                    heapq.heappush(heap, [new_dist, next_diff])


# 3. TO ANSWER THE QUERIES

query_count = int(sys.stdin.readline())

for query in range(query_count):
    
    start, end = map(int, sys.stdin.readline().split())
    if dist[end - start] != inf:
        print(dist[end - start])
    else:
        print(-1)