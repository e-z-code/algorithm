'''
BOJ17611 - Orthogonal Polygon (https://www.acmicpc.net/problem/17611)

Given an orthogonal polygon, determine the maximum intersection of the polygon and a horizontal (or vertical) line.
However, the line cannot overlap with any segment of the polygon.
'''

# TIME COMPLEXITY : O(max(X, Y, N)) [X : Size of x-range, Y : Size of y-range]

import sys


# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

points.append(points[0]) # To consider all lines


# 2. IMOS
# Since the line cannot overlap with any segment of the polygon, such imos method works.

OFFSET = 500000 # To make coordinate non-negative

x_imos = [0 for x in range(10 ** 6 + 1)]
y_imos = [0 for y in range(10 ** 6 + 1)]

for idx in range(1, len(points)):
    
    x1, y1 = points[idx-1]
    x2, y2 = points[idx]

    if x1 == x2: # Vertical Line
        y_imos[min(y1, y2) + OFFSET] += 1
        y_imos[max(y1, y2) + OFFSET] -= 1
    else: # Horizontal Line
        x_imos[min(x1, x2) + OFFSET] += 1
        x_imos[max(x1, x2) + OFFSET] -= 1

for idx in range(1, 10 ** 6 + 2):
    x_imos[idx] += x_imos[idx-1]
    y_imos[idx] += y_imos[idx-1]


# 3. TO SOLVE THE PROBLEM

ans = 0

for x in range(10 ** 6 + 1):
    if ans < x_imos[x]:
        ans = x_imos[x]
for y in range(10 ** 6 + 1):
    if ans < y_imos[y]:
        ans = y_imos[y]

print(ans)