'''
BOJ12995 - Tree Land (https://www.acmicpc.net/problem/12995)

There is a tree of N nodes.
You want to choose K consecutive nodes on a tree.
Determine the number of possible cases.
'''

# TIME COMPLEXITY : O(pow(NK, 2))

import sys
MOD = 10 ** 9 + 7


# 2. A FUNCTION TO CONSTRUCT A TREE

def tree(now_node, parent_node):
    
    for next_node in graph[now_node]:
        if next_node != parent_node:
            tree(next_node, now_node)
            parent[next_node] = now_node
            children[now_node].append(next_node)


# 3. TREE DP

def solve(now_node):
    
    dp[now_node][0] = 1
    dp[now_node][1] = 1
    
    for child_node in children[now_node]:
        
        solve(child_node)
        
        result = [0 for length in range(paint_count + 1)]
        result[0] = 1
        
        for now_paint in range(1, paint_count + 1):
            for branch_paint in range(paint_count + 1):
                if now_paint + branch_paint <= paint_count:
                    result[now_paint + branch_paint] += dp[now_node][now_paint] * dp[child_node][branch_paint]
                    result[now_paint + branch_paint] %= MOD

        for paint in range(paint_count + 1):
            dp[now_node][paint] = result[paint]


# 1. TO GET THE INPUT

node_count, paint_count = map(int, sys.stdin.readline().split())

graph = {}
for node in range(node_count):
    graph[node] = []
for edge in range(node_count - 1):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)


# 4. TO SOLVE THE PROBLEM

parent = [-1 for node in range(node_count)]
children = [[] for node in range(node_count)]

tree(0, -1)

dp = [[0 for length in range(paint_count + 1)] for node in range(node_count)]

solve(0)

ans = 0
for node in range(node_count):
    ans += dp[node][-1]
print(ans)