'''
ABC396E - Min of Restricted Sum (https://atcoder.jp/contests/abc396/tasks/abc396_e)

There are three integer sequences: X, Y, and Z.
Construct an array A such that A[X[i]] ^ A[Y[i]] = Z[i].
If it exists, find one that minimizes sum(A).
'''

# TIME COMPLEXITY: O((N + M) log max(Z)) 


import sys
from collections import deque


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

graph = {}
for node in range(node_count):
    graph[node] = []
for edge in range(edge_count):
    nodeA, nodeB, val = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append((nodeB, val))
    graph[nodeB].append((nodeA, val))


# 2. TO CONSTRUCT AN ARRAY

possible = True
ans = [-1 for node in range(node_count)]

for node in range(node_count):
    if ans[node] == -1:
        
        queue = deque([node])
        ans[node] = 0
        component = [node]
        
        while queue:
            now_node = queue.popleft()
            for next_node, val in graph[now_node]:
                if ans[next_node] == -1:
                    ans[next_node] = ans[now_node] ^ val
                    queue.append(next_node)
                    component.append(next_node)
                else:
                    if ans[now_node] ^ ans[next_node] != val:
                        possible = False


        # 3. FIND THE MINIMUM ONE
        
        key_num = 0
        bits = [0 for exp in range(30)]
        
        for node in component:
            for exp in range(30):
                if ans[node] & (1 << exp):
                    bits[exp] += 1
        
        for exp in range(30):
            if bits[exp] > len(component) // 2:
                key_num ^= (1 << exp)
        
        for node in component:
            ans[node] ^= key_num


# 4. TO SOLVE THE PROBLEM

if possible:
    print(" ".join(list(map(str, ans))))
else:
    print(-1)
