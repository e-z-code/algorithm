'''
BOJ31491 - Olympic Goodies (https://www.acmicpc.net/problem/31491)

Given a tree with N nodes, you will place P items on the edges.
Then, the winner can choose a start node and an end node and will collect all items on the path.
Your job is to minimize the maximum number of items collected.
Determine the maximum number of items the winner can collect.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

node_count, item_count = map(int, sys.stdin.readline().split())

degree = [0 for node in range(node_count)]
for edge in range(node_count - 1):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    degree[nodeA] += 1
    degree[nodeB] += 1


# 2. TO SOLVE THE PROBLEM
# All items must be placed on the edge that connects a leaf node.

leaf_count = 0
for node in range(node_count):
    if degree[node] == 1:
        leaf_count += 1

print(item_count // leaf_count * 2 + min(2, item_count % leaf_count))