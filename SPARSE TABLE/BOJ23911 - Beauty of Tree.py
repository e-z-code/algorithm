'''
BOJ23911 - Beauty of Tree (https://www.acmicpc.net/problem/23911)

There is a tree with N nodes.
You pick a node at random and paints it.
Then, you travel up the tree painting every A-th node until you reach the root.
Your friend also picks a node at random and paints it.
Then, your friend travels up the tree painting every B-th node until you reach the root.
Determine the expected number of painted nodes.
'''

# TIME COMPLEXITY : O(TN log N) 

import sys
from collections import deque
from math import lcm


# 3. A FUNCTION TO GET ANCESTOR OF GIVEN DISTANCE

def find_ancestor(node, dist):
    
    now_node = node
    now_dist = dist
    
    for exp in range(19, -1, -1):
        if (1 << exp) <= now_dist:
            now_node = sparse_table[now_node][exp]
            if now_node == -1:
                break
            now_dist -= (1 << exp)
    
    return now_node


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test_num in range(1, test_count + 1):
    
    node_count, intervalA, intervalB = map(int, sys.stdin.readline().split())
    parents = [0] + list(map(int, sys.stdin.readline().split()))
    
    
    # 2. SPARSE TABLE
    
    sparse_table = [[-1 for exp in range(20)] for node in range(node_count)]
    for node in range(node_count):
        sparse_table[node][0] = parents[node] - 1
    for exp in range(1, 20):
        for node in range(node_count):
            if sparse_table[node][exp-1] != -1:
                sparse_table[node][exp] = sparse_table[sparse_table[node][exp-1]][exp-1]
    
    
    # 3. COUNT THE NUMBER OF NODES FOR EACH NODE THAT ARE PAINTED TOGETHER WHEN INTERVAL = A
    
    # Connect node pairs of distance A
    
    countA = [1 for node in range(node_count)]
    in_degreeA = [0 for node in range(node_count)]
    
    graphA = [-1 for node in range(node_count)]
    for node in range(node_count):
        graphA[node] = find_ancestor(node, intervalA)
        if graphA[node] != -1:
            in_degreeA[graphA[node]] += 1
            
    # Count how many time each node is chosen when interval = A
    
    queue = deque()
    for node in range(node_count):
        if in_degreeA[node] == 0:
            queue.append(node)
    
    while queue:
        now_node = queue.popleft()
        if graphA[now_node] != -1:
            countA[graphA[now_node]] += countA[now_node]
            in_degreeA[graphA[now_node]] -= 1
            if in_degreeA[graphA[now_node]] == 0:
                queue.append(graphA[now_node])
    
    
    # 4. COUNT THE NUMBER OF NODES FOR EACH NODE THAT ARE PAINTED TOGETHER WHEN INTERVAL = B
    
    # Connect node pairs of distance B 

    countB = [1 for node in range(node_count)]
    in_degreeB = [0 for node in range(node_count)]
    
    graphB = [-1 for node in range(node_count)]
    for node in range(node_count):
        graphB[node] = find_ancestor(node, intervalB)
        if graphB[node] != -1:
            in_degreeB[graphB[node]] += 1
    
    # Count how many time each node is chosen when interval = B
    
    queue = deque()
    for node in range(node_count):
        if in_degreeB[node] == 0:
            queue.append(node)
    
    while queue:
        now_node = queue.popleft()
        if graphB[now_node] != -1:
            countB[graphB[now_node]] += countB[now_node]
            in_degreeB[graphB[now_node]] -= 1
            if in_degreeB[graphB[now_node]] == 0:
                queue.append(graphB[now_node])

    
    # 5. TO SOLVE THE PROBLEM
    
    total_count = [countA[node] * node_count + countB[node] * node_count - countA[node] * countB[node] for node in range(node_count)]
    ans = sum(total_count) / (node_count * node_count)
    
    print("Case #{}: {}".format(test_num, ans))