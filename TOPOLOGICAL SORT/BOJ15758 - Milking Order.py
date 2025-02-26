'''
BOJ15758 - Milking Order (https://www.acmicpc.net/problem/15758)

There are N cows and M orders.
You want to maximize the value of X so that your order meets the conditions outlined in the first X orders.
If multiple orders satisfy conditions, you want to use the lexicographically smallest one.
Determine the best order.
'''

# TIME COMPLEXITY : O((N+M) log M)

import sys, heapq


# 1. TO GET THE INPUT

cow_count, order_count = map(int, sys.stdin.readline().split())

orders = []
for order_num in range(order_count):
    order = list(map(int, sys.stdin.readline().split()))[1:]
    orders.append(order)


# 2. BINARY SEARCH

left = 0
right = order_count + 1

while left + 1 < right:
    
    mid = (left + right) // 2
    
    # To check if given number of orders do not contradict
    # To check if cycle exists in directed graph
    
    in_degree = {}
    graph = {}
    for node in range(1, cow_count + 1):
        graph[node] = set()
        in_degree[node] = 0
    
    for order_idx in range(mid):
        order = orders[order_idx]
        for idx in range(len(order) - 1):
            graph[order[idx]].add(order[idx+1])
            in_degree[order[idx+1]] += 1

    t_sort = []
    visited = [0 for node in range(cow_count + 1)]
    
    for node in range(1, cow_count + 1):
        if in_degree[node] == 0:
            t_sort.append(node)
            visited[node] = 1
    
    while t_sort:
        now_node = heapq.heappop(t_sort)
        for next_node in graph[now_node]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                heapq.heappush(t_sort, next_node)
                visited[next_node] = 1
    
    valid = True
    for node in range(1, cow_count + 1):
        if visited[node] == 0:
            valid = False
            break
    
    if valid:
        left = mid
    else:
        right = mid


# 3. TO SOLVE THE PROBLEM - TOPOLOGICAL SORT

ans = []

in_degree = {}
graph = {}
for node in range(1, cow_count + 1):
    graph[node] = set()
    in_degree[node] = 0
    
for order_idx in range(left):
    order = orders[order_idx]
    for idx in range(len(order) - 1):
        graph[order[idx]].add(order[idx+1])
        in_degree[order[idx+1]] += 1

t_sort = []
    
for node in range(1, cow_count + 1):
    if in_degree[node] == 0:
        t_sort.append(node)
    
while t_sort:
    now_node = heapq.heappop(t_sort)
    ans.append(now_node)
    for next_node in graph[now_node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            heapq.heappush(t_sort, next_node)

print(" ".join(map(str, ans)))