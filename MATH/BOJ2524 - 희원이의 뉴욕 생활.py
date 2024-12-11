'''
BOJ2524 - Hee-won's New York Life (https://www.acmicpc.net/problem/2524)

In Manhattan, every road is either horizontal or vertical.
The only exception is the Broadway, given as the line Ax + By = C.
Determine the minimum distance from (x1, y1) to (x2, y2).
'''

# TIME COMPLEXITY : O(1)

import sys
from decimal import Decimal


# 2. FUNCTION FOR DISTANCE

def euclidean_dist(p1, p2):
    
    x1, y1 = p1
    x2, y2 = p2
    
    return (pow(x1 - x2, Decimal('2')) + pow(y1 - y2, Decimal('2'))) ** Decimal('0.5')

def manhattan_dist(p1, p2):
    
    x1, y1 = p1
    x2, y2 = p2
    
    return abs(x1 - x2) + abs(y1 - y2)


# 1. TO GET THE INPUT

x1, y1, x2, y2, A, B, C = map(Decimal, sys.stdin.readline().split())


# 3. TO SOLVE THE PROBLEM

if x1 == x2:
    print(abs(y1 - y2))
elif y1 == y2:
    print(abs(x1 - x2))
else:
    
    # Think of the rectangle where (x1, y1) and (x2, y2) are two points.
    # The list 'intersection' stores two intersection points between the rectangle and the Broadway.
    
    intersection = set()
    if min(y1, y2) <= (C - A * x1) / B <= max(y1, y2):
        intersection.add((x1, (C - A * x1) / B))
    if min(y1, y2) <= (C - A * x2) / B <= max(y1, y2):
        intersection.add((x2, (C - A * x2) / B))
    if min(x1, x2) <= (C - B * y1) / A <= max(x1, x2):
        intersection.add(((C - B * y1) / A, y1))
    if min(x1, x2) <= (C - B * y2) / A <= max(x1, x2):
        intersection.add(((C - B * y2) / A, y2))
    intersection = list(intersection)
    
    # To get the minimum distance
    
    min_dist = manhattan_dist((x1, y1), (x2, y2))
    
    if len(intersection) == 2:
        min_dist = min(min_dist, manhattan_dist((x1, y1), intersection[0]) + euclidean_dist(intersection[0], intersection[1]) + manhattan_dist(intersection[1], (x2, y2)))
        min_dist = min(min_dist, manhattan_dist((x1, y1), intersection[1]) + euclidean_dist(intersection[1], intersection[0]) + manhattan_dist(intersection[0], (x2, y2)))

    print(min_dist)