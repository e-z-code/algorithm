'''
ABC380E - 1D Bucket Tool (https://atcoder.jp/contests/abc380/tasks/abc380_e)

There are N cells in a row.
Initially, cell i is painted color i.
Two cells are reachable if they are adjacent and have the same color.

Answer the following two types of Q queries:

(1) 1 X C: Repaint all reachable cells from X to C.
(2) 2 C: Print the number of cells painted with color C.
'''

# TIME COMPLEXITY : O(max(N, Q))
# The basic idea is to push all information to the parent.

import sys


# 2. FUNCTIONS FOR UNION-FIND

def find(x):
    
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    
    parentA = find(x)
    parentB = find(y)
    
    if parentA < parentB:
        parent[parentA] = parentB
        size[parentB] += size[parentA]
        left[parentB] = min(left[parentA], left[parentB])
        right[parentB] = max(right[parentA], right[parentB])
    else:
        parent[parentB] = parentA
        size[parentA] += size[parentB]
        left[parentA] = min(left[parentA], left[parentB])
        right[parentA] = max(right[parentA], right[parentB])


# 1. TO GET THE INPUT

length, query_count = map(int, sys.stdin.readline().split())


# 3. PROCESS QUERIES

parent = [idx for idx in range(length + 1)]

color_count = [1 for idx in range(length + 1)]
size = [1 for idx in range(length + 1)]

color = [idx for idx in range(length + 1)]
left = [idx for idx in range(length + 1)]
right = [idx for idx in range(length + 1)]

for query_input in range(query_count):
    
    query = list(map(int, sys.stdin.readline().split()))
    
    if query[0] == 1:
        
        idx, new_color = query[1], query[2]
        
        # Re-paint
        
        ancestor = find(idx)
        color_count[color[ancestor]] -= size[ancestor]
        color_count[new_color] += size[ancestor]
        
        # Update reachable cells
        
        color[ancestor] = new_color
        if left[ancestor] != 1 and color[find(left[ancestor] - 1)] == new_color:
            union(ancestor, left[ancestor] - 1)
        if right[ancestor] != length and color[find(right[ancestor] + 1)] == new_color:
            union(ancestor, right[ancestor] + 1)
    
    else:
        
        new_color = query[1]
        print(color_count[new_color])