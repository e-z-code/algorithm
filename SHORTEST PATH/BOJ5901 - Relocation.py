'''
BOJ5901 - Relocation (https://www.acmicpc.net/problem/5901)

You are given a graph with the locations of K markets.
Each day, you leave the farm, visit K markets, and return to your farm.
Determine the location of the farm that minimizes your daily travel schedule.
'''

# TIME COMPLEXITY : O(max(KM log N, K!N))

import sys, heapq
from itertools import permutations
INF = float('inf')


# 2. DIJKSTRA

def dijkstra(start):
    
    dist = [INF for idx in range(node_count + 1)]
    dist[start] = 0
    
    heap = [(0, start)]
    
    while heap:
        now_dist, now_loc = heapq.heappop(heap)
        if now_dist <= dist[now_loc]:
            for next_loc, next_dist in graph[now_loc]:
                total_dist = now_dist + next_dist
                if total_dist < dist[next_loc]:
                    dist[next_loc] = total_dist
                    heapq.heappush(heap, (total_dist, next_loc))

    return dist


# 1. TO GET THE INPUT

node_count, edge_count, market_count = map(int, sys.stdin.readline().split())

markets = []
for market in range(market_count):
    loc = int(sys.stdin.readline())
    markets.append(loc)

graph = {}
for node in range(1, node_count+1):
    graph[node] = []
for edge in range(edge_count):
    nodeA, nodeB, length = map(int, sys.stdin.readline().split())
    graph[nodeA].append((nodeB, length))
    graph[nodeB].append((nodeA, length))


# 3. TO SOLVE THE PROBLEM

min_dist = {} # Stores minimum distance from market to each vertices
for market in markets:
    min_dist[market] = dijkstra(market)

ans = INF

for permutation in permutations(markets, len(markets)): # Try all possible order of markets
    
    result = 0
    
    for idx in range(len(permutation) - 1):
        result += min_dist[permutation[idx]][permutation[idx+1]]
    
    best = INF
    for farm in range(1, node_count + 1):
        if farm not in min_dist:
            best = min(best, min_dist[permutation[0]][farm] + min_dist[permutation[-1]][farm])
    
    result += best
    ans = min(ans, result)

print(ans)