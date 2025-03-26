'''
BOJ28793 - Spy Network (https://www.acmicpc.net/problem/28793)

Divide N points into two sets such that the difference of cardinality is maximum and the convex set of each set overlaps.
'''

# TIME COMPLEXITY : O(N log N)

import sys


# 2. CCW FUNCTION

def ccw(p1, p2, p3):
    
    x1, y1, i1 = p1
    x2, y2, i2 = p2
    x3, y3, i3 = p3
    
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())

points = []
for idx in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y,idx+1))
points.sort()


# 3. TO GET THE CONVEX HULL - MONOTONE CHAIN

upper_hull = []

for point in points:
    while len(upper_hull) > 1 and ccw(upper_hull[-2], upper_hull[-1], point) >= 0:
        upper_hull.pop()
    upper_hull.append(point)

lower_hull = []

for point in points:
    while len(lower_hull) > 1 and ccw(lower_hull[-2], lower_hull[-1], point) <= 0:
        lower_hull.pop()
    lower_hull.append(point)

convex_hull = []

for idx in range(len(upper_hull)):
    convex_hull.append(upper_hull[idx])
for idx in range(len(lower_hull) - 2, 0, -1):
    convex_hull.append(lower_hull[idx])


# 4. TO SOLVE THE PROBLEM

# If the convex hull consists of all points, the answer is a segment that connects unconnected two points.

if len(convex_hull) == point_count:
    
    print(2)
    print(convex_hull[0][2], convex_hull[2][2])

# Otherwise, smaller set is a point that does not belong to the convex hull.

else:
    
    ans = set()
    for idx in range(1, point_count + 1):
        ans.add(idx)

    for x, y, idx in upper_hull:
        if idx in ans:
            ans.remove(idx)

    for x, y, idx in lower_hull:
        if idx in ans:
            ans.remove(idx)

    print(1)
    print(ans.pop())