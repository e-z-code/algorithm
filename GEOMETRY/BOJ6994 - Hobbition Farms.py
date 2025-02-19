'''
BOJ6994 - Hobbition Farms (https://www.acmicpc.net/problem/6994)

Given a rectangle and a circle, determine if they overlap or not.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    radius, x_center, y_center, x_left, y_left, x_right, y_right = map(float, sys.stdin.readline().split())
    
    
    # 2. TO FIND OVERLAPPING
    
    overlap = False
    
    # The point on or in rectangle that is the closest to the center of the circle
    x_closest = max(x_left, min(x_center, x_right))
    y_closest = max(y_left, min(y_center, y_right))
    
    if (x_center - x_closest) ** 2 + (y_center - y_closest) ** 2 <= radius ** 2:
        overlap = True


    # 3. TO SOLVE THE PROBLEM

    if overlap:
        print("The given circle and rectangle overlap.")
    else:
        print("The given circle and rectangle do not overlap.")