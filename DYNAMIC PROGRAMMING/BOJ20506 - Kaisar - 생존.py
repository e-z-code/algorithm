'''
BOJ20506 - Kaisar - Alive (https://www.acmicpc.net/problem/20506)

There is a tree of N nodes.
For every pair (x, y), you record the LCA on an array.
Then, you sorted the array.
Determine the sum of all elements of odd indices and even indices.
'''

# TIME COMPLEXITY : O(N)

import sys
sys.setrecursionlimit(200001)


# 2. TREE DP FUNCTION
# DP[X] = pow(SIZE[X], 2) - sum(pow(SIZE[C], 2))

def fill_table(now_node):

    size[now_node] = 1
    
    offset = 0
    for child_node in children[now_node]:
        fill_table(child_node)
        size[now_node] += size[child_node]
        offset += size[child_node] ** 2
    
    dp[now_node] = size[now_node] ** 2 - offset


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())

root_node = 0

parent = [0] + list(map(int, sys.stdin.readline().split()))
children = [[] for node in range(node_count + 1)]

for node in range(1, node_count + 1):
    if parent[node] == 0:
        root_node = node
    else:
        children[parent[node]].append(node)


# 3. TREE DP
# DP[X] = The number of pairs of which LCA is X
# SIZE[X] = The size of sub-tree of which ancestor is X

dp = [0 for node in range(node_count + 1)]
size = [0 for node in range(node_count + 1)]

fill_table(root_node)


# 4. TO SOLVE THE PROBLEM

count = []
for node in range(1, node_count + 1):
    count.append((node, dp[node]))

now = 1

even_sum = 0
odd_sum = 0

for node, lca_count in count:
    
    if lca_count % 2 == 0:
        even_sum += node * (lca_count // 2)
        odd_sum += node * (lca_count // 2)
    else:
        if now % 2 == 0:
            even_sum += node * (lca_count // 2 + 1)
            odd_sum += node * (lca_count // 2)
        else:
            even_sum += node * (lca_count // 2)
            odd_sum += node * (lca_count // 2 + 1)
    now += lca_count
    
print(even_sum, odd_sum)