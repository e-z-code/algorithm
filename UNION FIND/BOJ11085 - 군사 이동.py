'''
BOJ11085 - Military Mobilization (https://www.acmicpc.net/problem/11085)

Given source and sink, determine the maximum capacity of the bottleneck edge.
'''

# TIME COMPLEXITY : O(W log W)

import sys


# 2. UNION-FIND

def find(x):
    
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    
    parent_x = find(x)
    parent_y = find(y)
    
    if parent_x < parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

source, dest = map(int, sys.stdin.readline().split())

edges = []
for edge in range(edge_count):
    start, end, width = map(int, sys.stdin.readline().split())
    edges.append((start, end, width))

edges.sort(key = lambda x : -x[2])


# 3. TO SOLVE THE PROBLEM

parent = [node for node in range(node_count)]

for start, end, width in edges:
    
    union(start, end)
    
    if find(source) == find(dest):
        print(width)
        break