'''
ABC418E - Trapezium (https://atcoder.jp/contests/abc418/tasks/abc418_e)

There are N points on a 2D plane.
How many combinations of four points can form a trapezoid?
No three points are collinear.
'''

# TIME COMPLEXITY: O(N^2)

import sys


# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))
    

# 2. TO COUNT THE OCCURRENCE OF EACH SLOPE AND MIDPOINT
# If midpoints of two opposite point pairs are equal, then it is parallelogram.

slope_count = {}
midpoint_count = {}

for i in range(point_count):
    for j in range(i+1, point_count):
        
        x1, y1 = points[i]
        x2, y2 = points[j]
        
        mid_x, mid_y = x1 + x2, y1 + y2
        midpoint_count[(mid_x, mid_y)] = midpoint_count.get((mid_x, mid_y), 0) + 1
        
        if x1 == x2:
            slope = float('inf')
        else:
            slope = (y1 - y2) / (x1 - x2)
        slope_count[slope] = slope_count.get(slope, 0) + 1


# 3. TO SOLVE THE PROBLEM

ans = 0

for count in slope_count.values():
    ans += count * (count - 1) // 2
for count in midpoint_count.values():
    ans -= count * (count - 1) // 2

print(ans)