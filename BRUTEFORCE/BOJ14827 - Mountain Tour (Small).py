'''
BOJ14827 - Mountain Tour (Small) (https://www.acmicpc.net/problem/14827)

There is a graph with C nodes and 2 X C edges.
Each node has an in-degree of 2 and an out-degree of 2.
Determine the minimum-cost Eulerian cycle.
'''

# TIME COMPLEXITY : O(4^N)

import sys
from collections import deque
inf = float('inf')


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(1, test_count + 1):
    
    camp_count = int(sys.stdin.readline())

    # There are two outward edges for each node.
    
    edges = []
    for edge in range(camp_count * 2):
        end, start_time, duration = map(int, sys.stdin.readline().split())
        end -= 1
        edges.append((end, start_time, duration))
    
    
    # 2. TO SOLVE THE PROBLEM
    
    ans = inf
    
    queue = deque([(0, 0, 0)])
    while queue:
        
        # "Path" is a bit representation of edges used.
        
        now_loc, now_cost, now_path = queue.popleft()
        
        # Used all edges
        
        if now_path == (1 << (camp_count * 2)) - 1 and now_loc == 0:
            ans = min(ans, now_cost)
            continue
        
        # Used edge 1 if not used
        
        if now_path & (1 << (now_loc * 2)) == 0:
            
            endA, startA, durationA = edges[now_loc * 2]
            
            next_loc = endA
            next_cost = now_cost + (startA - now_cost % 24) + durationA
            if startA < now_cost % 24:
                next_cost += 24
            next_path = now_path | (1 << (now_loc * 2))
            
            queue.append((next_loc, next_cost, next_path))
        
        # Use edge 2 if not used
        
        if now_path & (1 << (now_loc * 2 + 1)) == 0:
            
            endB, startB, durationB = edges[now_loc * 2 + 1]
            
            next_loc = endB
            next_cost = now_cost + (startB - now_cost % 24) + durationB
            if startB < now_cost % 24:
                next_cost += 24
            next_path = now_path | (1 << (now_loc * 2 + 1))
            
            queue.append((next_loc, next_cost, next_path))

    print("Case #{}: {}".format(test, ans))