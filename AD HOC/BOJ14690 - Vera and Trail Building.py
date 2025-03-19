'''
BOJ14690 - Vera and Trail Building (https://www.acmicpc.net/problem/14690)

If it is possible to reach from A to B, then B to A, without hiking on the same trail, (A, B) is called a beautiful pair.
Construct the graph that contains K beautiful pairs.
'''

# TIME COMPLEXITY : O(√K)

import sys


# 1. TO CALCULATE C(X, 2)

pair_count = [0, 0]

while True:
    
    now_length = len(pair_count)
    now_count = (now_length) * (now_length - 1) // 2
    
    if now_count <= 10000000:
        pair_count.append(now_count)
    else:
        break


# 2. TO GET THE INPUT AND CONSTRUCT THE GRAPH

goal = int(sys.stdin.readline())

now_length = len(pair_count) - 1

now_head = 1
heads = []
edges = []

while goal != 0:
    
    if goal < pair_count[now_length]:
        now_length -= 1
        continue
    
    # Add cycle
    
    next_head = now_head + now_length
    for node in range(now_head, next_head - 1):
        edges.append((node, node+1))
    edges.append((next_head-1, now_head))
    
    heads.append(now_head)
    now_head = next_head
    
    goal -= pair_count[now_length]

# Add connection

if 2 <= len(heads):
    for idx in range(1, len(heads)):
        edges.append((heads[idx-1], heads[idx]))


# 3. TO SOLVE THE PROBLEM

print(now_head - 1, len(edges))
for nodeA, nodeB in edges:
    print(nodeA, nodeB)