'''
BOJ4284 - A Walk Through the Forest (https://www.acmicpc.net/problem/4284)

You want to move from node 1 to node 2.
You can only take a path from X to Y if there is a route from Y to 2 that is shorter than any possible route from X.
Calculate how many different routes you may take.
'''

# TIME COMPLEXITY : O(M log N)

import sys, heapq
from collections import deque
inf = float('inf')


# 1. TO GET THE INPUT

while True:
    
    graph_info = list(map(int, sys.stdin.readline().split()))
    if len(graph_info) == 1:
        break
    
    node_count, edge_count = graph_info
    
    graph = {}
    for node in range(1, node_count + 1):
        graph[node] = []
    
    for edge in range(edge_count):
        nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
        graph[nodeA].append((dist, nodeB))
        graph[nodeB].append((dist, nodeA))
    
    
    # 2. DIJKSTRA
    
    min_dist = [inf for node in range(node_count + 1)]
    min_dist[2] = 0
    
    heap = [(0, 2)]
    
    while heap:
        now_dist, now_node = heapq.heappop(heap)
        if now_dist <= min_dist[now_node]:
            for next_dist, next_node in graph[now_node]:
                total_dist = now_dist + next_dist
                if total_dist < min_dist[next_node]:
                    min_dist[next_node] = total_dist
                    heapq.heappush(heap, (total_dist, next_node))
    
    
    # 3. TO CONSTRUCT NEW GRAPH WITH VALID EDGES
    
    new_graph = {}
    for node in range(1, node_count + 1):
        new_graph[node] = []
    in_degree = [0 for node in range(node_count + 1)]
    
    for node in range(1, node_count + 1):
        for dist, next_node in graph[node]:
            if min_dist[node] > min_dist[next_node]:
                new_graph[node].append(next_node)
                in_degree[next_node] += 1
    
    
    # 4. TOPOLOGICAL SORT + DP
    
    dp = [0 for node in range(node_count + 1)]
    dp[1] = 1
    
    t_sort = deque([])
    for node in range(1, node_count + 1):
        if in_degree[node] == 0:
            t_sort.append(node)
    
    while t_sort:
        now_node = t_sort.popleft()
        for next_node in new_graph[now_node]:
            dp[next_node] += dp[now_node]
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                t_sort.append(next_node)
    
    print(dp[2])