'''
BOJ16057 - Water Testing (https://www.acmicpc.net/problem/16057)

There is a polygon in which vertices are lattice points, and sides do not intersect.
Determine the number of inner lattice points.
'''

# TIME COMPLEXITY : O(N log N)

import sys
from math import gcd


# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))
points.append(points[0])


# 2. TO SOLVE THE PROBLEM - PICK'S THEOREM

point_on_line = point_count
area = 0

for idx in range(point_count):
    
    x1, y1 = points[idx]
    x2, y2 = points[idx+1]
    
    point_on_line += gcd(abs(x1 - x2), abs(y1 - y2)) - 1
    
    area += x1 * y2
    area -= y1 * x2

area = abs(area) // 2

print(area + 1 - point_on_line // 2)