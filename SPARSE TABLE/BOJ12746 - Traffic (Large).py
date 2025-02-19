'''
BOJ12746 - Traffic (Large) (https://www.acmicpc.net/problem/12746)

There is a tree of N nodes.
You process Q queries: Add 1 to every edge on the path from node X to node Y.
Determine the segment with the highest value. 
'''

# TIME COMPLEXITY : O((N + Q) log N)

import sys
inf = float('inf')
sys.setrecursionlimit(300000)


# 2. FUNCTIONS TO CONSTRUCT TREE AND FIND LCA

def tree(now_node, parent_node, now_depth):
    
    depth[now_node] = now_depth
    
    for next_node in graph[now_node]:
        if parent_node != next_node:
            parent[next_node][0] = now_node
            children[now_node].append(next_node)
            tree(next_node, now_node, now_depth + 1)

def set_parent():
    
    for exp in range(1, 20):
        for node in range(node_count):
            if parent[node][exp-1] != -1:
                parent[node][exp] = parent[parent[node][exp-1]][exp-1]

def lca(nodeA, nodeB):
    
    if depth[nodeA] > depth[nodeB]:
        nodeA, nodeB = nodeB, nodeA
    
    # To level the depth of two nodes
    for exp in range(19, -1, -1):
        if depth[nodeB] - depth[nodeA] >= pow(2, exp):
            nodeB = parent[nodeB][exp]
    
    # To find LCA
    if nodeA == nodeB:
        return nodeA
    else:
        for exp in range(19, -1, -1):
            if parent[nodeA][exp] != parent[nodeB][exp]:
                nodeA = parent[nodeA][exp]
                nodeB = parent[nodeB][exp]
    
    return parent[nodeA][0]


# 5. TREE DP FUNCTIONS TO SOLVE THE PROBLEM

def total_count(now_node):
    
    for child_node in children[now_node]:
        total_count(child_node)
        count[now_node] += count[child_node]

def solve(now_node):
    
    ans_nodeA, ans_nodeB, ans_count = now_node, parent[now_node][0], count[now_node]
    if ans_nodeB == -1:
        ans_nodeB = inf
    if ans_nodeA > ans_nodeB:
        ans_nodeA, ans_nodeB = ans_nodeB, ans_nodeA
    
    for child_node in children[now_node]:
        
        now_nodeA, now_nodeB, now_count = solve(child_node)
        if now_nodeA > now_nodeB:
            now_nodeA, now_nodeB = now_nodeB, now_nodeA
        
        if ans_count < now_count:
            ans_nodeA, ans_nodeB, ans_count = now_nodeA, now_nodeB, now_count
        elif ans_count == now_count:
            candidates = [now_nodeA, now_nodeB, ans_nodeA, ans_nodeB]
            candidates.sort()
            ans_nodeA, ans_nodeB = candidates[0], candidates[1]
    
    return ans_nodeA, ans_nodeB, ans_count


# 1. TO GET THE INPUT

node_count, query_count = map(int, sys.stdin.readline().split())

graph = {}
for node in range(node_count):
    graph[node] = []
for edge in range(node_count - 1):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)


# 3. TO CONSTRUCT TREE AND FILL SPARSE TABLE

parent = [[-1 for exp in range(20)] for node in range(node_count)]
children = [[] for node in range(node_count)]

depth = [-1 for node in range(node_count)]

tree(0, -1, 0)
set_parent()


# 4. TO MARK THE BOTH END OF ROUTES
# If count[X] = Y, Y people use the edge between X and its parent.

count = [0 for node in range(node_count)]

for query in range(query_count):
    
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    
    least_common_ancestor = lca(nodeA, nodeB)
    count[nodeA] += 1
    count[least_common_ancestor] -= 1
    count[nodeB] += 1
    count[least_common_ancestor] -= 1


# 6. TO SOLVE THE PROBLEM

total_count(0)

ans_nodeA, ans_nodeB, ans_count = solve(0)
print(ans_nodeA + 1, ans_nodeB + 1, ans_count)