'''
BOJ34060 - Robot Cleaner (https://www.acmicpc.net/problem/34060)

Robot cleaner found N cells with waste.
It sorts all N cells and only sends y-coordinates in order.
Determine the maximum and minimum possible number of connected components of cells with waste.
'''

# TIME COMPLEXITY : O(N)

import sys
sys.setrecursionlimit(200005)


# 2. UNION-FIND

def find(x):
    
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    
    parentX = find(x)
    parentY = find(y)
    
    if parentX < parentY:
        parent[parentX] = parentY
    else:
        parent[parentY] = parentX


# 1. TO GET THE INPUT

cell_count = int(sys.stdin.readline())

y_coordinates = []
for y_coordinate in range(cell_count):
    y_coordinates.append(int(sys.stdin.readline()))


# 3. TO SOLVE THE PROBLEM
# Maximum number equals the number of cells.
# Minimum number equals when you compress cells as much as you can.

parent = {}

now_x = 0
now_y = 0
for y_coordinate in y_coordinates:
    
    if now_y >= y_coordinate:
        now_x += 1
    now_y = y_coordinate
    
    parent[(now_x, now_y)] = (now_x, now_y)
    if (now_x-1, now_y) in parent:
        union((now_x-1, now_y), (now_x, now_y))
    if (now_x, now_y-1) in parent:
        union((now_x, now_y-1), (now_x, now_y))

captains = set()
for cell in parent:
    captains.add(find(cell))
print(len(captains))
print(cell_count)