'''
BOJ5973 - Bovine Bridge Battle (https://www.acmicpc.net/problem/5973)

There are N points.
A set of four points is called a bridge if and only if there is a point X such that rotating any cows in the group 180 degrees about the point gives the position of some other cow in the group.
Determine the number of bridges.
'''

# TIME COMPLEXITY : O(N^2)

import sys


# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))


# 2. TO CALCULATE THE MID POINTS
# For a set to be a bridge, the middle points of two pairs must be equal. 

count = {}

for i in range(point_count):
    for j in range(i+1, point_count):
        
        x1, y1 = points[i]
        x2, y2 = points[j]
        
        if (x1 + x2, y1 + y2) in count:
            count[(x1 + x2, y1 + y2)] += 1
        else:
            count[(x1 + x2, y1 + y2)] = 1


# 3. TO SOLVE THE PROBLEM

ans = 0
for middle_point in count:
    ans += count[middle_point] * (count[middle_point] - 1) // 2
print(ans)