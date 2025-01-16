'''
BOJ27014 - Cube Stacking (https://www.acmicpc.net/problem/27014)

There are N stacks consisting of a single cube.
Process the following two queries.

(1) Move the stack containing cube X on top of the stack containing cube Y.
(2) Count the number of cubes on the stack with cube X under the cube X.
'''

# TIME COMPLEXITY : O*(P)

import sys


# 2. UNION-FIND

def find(x):
    
    if parent[x] != x:
        dist, parent[x] = find(parent[x])
        to_parent[x] += dist

    return to_parent[x], parent[x]

def union(x, y):
    
    parentX = find(x)[1]
    parentY = find(y)[1]
    
    parent[parentX] = parentY
    to_parent[parentX] += size[parentY]
    size[parentY] += size[parentX]


# 1. INITIAL STATE

parent = [cube for cube in range(30000)]
to_parent = [0 for cube in range(30000)]

size = [1 for cube in range(30000)]


# 3. TO SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())

for query in range(query_count):
    
    query_info = list(sys.stdin.readline().strip().split())
    
    if query_info[0] == "M":
        cubeA, cubeB = int(query_info[1]) - 1, int(query_info[2]) - 1
        union(cubeA, cubeB)
    else:
        cube = int(query_info[1]) - 1
        find(cube)
        print(to_parent[cube - 1])