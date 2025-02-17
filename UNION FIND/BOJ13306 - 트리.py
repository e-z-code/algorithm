'''
BOJ13306 - Tree (https://www.acmicpc.net/problem/13306)

There is a tree.
Process the following two queries.

(1) Delete an edge that connects X and its parent.
(2) Determine if X and Y are connected.
'''

# TIME COMPLEXITY : O*(N + M)

import sys
sys.setrecursionlimit(10 ** 6)


# 2. UNION-FIND

def find(x):
    
    if x != now_parent[x]:
        now_parent[x] = find(now_parent[x])
    return now_parent[x]

def union(x, y):
    
    parent_x = find(x)
    parent_y = find(y)
    
    if parent_x < parent_y:
        now_parent[parent_y] = parent_x
    else:
        now_parent[parent_x] = parent_y


# 1. TO GET THE INPUT

node_count, query_count = map(int, sys.stdin.readline().split())

final_parent = [-1, -1]
for node in range(node_count - 1):
    final_parent.append(int(sys.stdin.readline()))


# 3. OFFLINE QUERY
# Reverse the order of the query.
# Then, the problem is equal to connect disjoint sets and determine the connectivity.

queries = []

for query in range(query_count + node_count - 1):
    
    query_info = list(map(int, sys.stdin.readline().split()))
    queries.append(query_info)

queries = queries[::-1]


# 4. TO SOLVE THE PROBLEM

ans = []

now_parent = [node for node in range(node_count + 1)]

for query in queries:
    
    if len(query) == 2:
        node = query[1]
        union(node, final_parent[node])
    else:
        nodeA, nodeB = query[1], query[2]
        if find(nodeA) == find(nodeB):
            ans.append("YES")
        else:
            ans.append("NO")

while ans:
    print(ans.pop())