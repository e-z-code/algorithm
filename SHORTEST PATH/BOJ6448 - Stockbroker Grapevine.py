'''
BOJ6448 - Stockbroker Grapevine (https://www.acmicpc.net/problem/6448)

Given a network of N stockbrokers, determine the starting point of your rumor so that you can spread it as fast as you can.
'''

# TIME COMPLEXITY : O(T X N^3)

import sys
inf = float('inf')


# 1. TO GET THE INPUT

while True:
    
    broker_count = int(sys.stdin.readline())
    if broker_count == 0:
        break

    graph = [[inf for end in range(broker_count)] for start in range(broker_count)]
    for node in range(broker_count):
        graph[node][node] = 0
    
    for start in range(broker_count):
        contact_info = list(map(int, sys.stdin.readline().split()))
        for idx in range(1, len(contact_info), 2):
            end = contact_info[idx] - 1
            graph[start][end] = contact_info[idx+1]
        
    
    # 2. FLOYD-WARSHALL
    
    for mid in range(broker_count):
        for start in range(broker_count):
            for end in range(broker_count):
                if graph[start][end] > graph[start][mid] + graph[mid][end]:
                    graph[start][end] = graph[start][mid] + graph[mid][end]
    
    
    # 3. TO SOLVE THE PROBLEM
    
    ans_start = -1
    ans_dist = inf
    
    for start in range(broker_count):
        if max(graph[start]) < ans_dist:
            ans_start = start + 1
            ans_dist = max(graph[start])
    
    if ans_dist == inf:
        print("disjoint")
    else:
        print(ans_start, ans_dist)