'''
BOJ4989 - Traveling by Stagecoach (https://www.acmicpc.net/problem/4989)

You have N tickets to increase your speed for an edge.
Determine the shortest time from a starting point to destination.
'''

# TIME COMPLEXITY : O(pow(2, N) X MP) 

import sys
from itertools import permutations
inf = float('inf')


# 1. TO GET THE INPUT

while True:

    max_length, node_count, edge_count, start_node, end_node = map(int, sys.stdin.readline().split())
    if max_length == 0 and node_count == 0 and edge_count == 0 and start_node == 0 and end_node == 0:
        break
    start_node -= 1
    end_node -= 1

    cars = list(map(int, sys.stdin.readline().split()))

    graph = {}
    for node in range(node_count):
        graph[node] = []
    for edge in range(edge_count):
        nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
        nodeA -= 1
        nodeB -= 1
        graph[nodeA].append((nodeB, dist))
        graph[nodeB].append((nodeA, dist))


    # 2. TO SOLVE THE PROBLEM - BIT-MASKING DP

    ans = inf
    
    time = [[inf for used_cars in range(1 << len(cars))] for node in range(node_count)]
    time[start_node][0] = 0
    
    for used_cars in range(1 << len(cars)):
        for node in range(node_count):
            
            for new_car in range(len(cars)):
                last_used_cars = used_cars ^ (1 << new_car)
                for last_node, dist in graph[node]:
                    time[node][used_cars] = min(time[last_node][last_used_cars] + dist / cars[new_car], time[node][used_cars])
    
    ans = min(ans, min(time[end_node]))
    
    if ans == inf:
        print("Impossible")
    else:
        print(ans)