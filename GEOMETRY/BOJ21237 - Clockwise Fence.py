'''
BOJ21237 - Clockwise Fence (https://www.acmicpc.net/problem/21237)

Determine if the given move is clockwise or counterclockwise.
'''

# TIME COMPLEXITY : O(NP) [P : The number of points of shape]

import sys


# 3. CCW FUNCTION

def ccw(p1, p2, p3):
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    val = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3

    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    fence = sys.stdin.readline().strip()
    
    
    # 2. TO STORE COORDINATES
    
    coordinates = [(0, 0)]
    
    for direction in fence:
        last_x, last_y = coordinates[-1]
        if direction == "N":
            coordinates.append((last_x, last_y + 1))
        elif direction == "E":
            coordinates.append((last_x + 1, last_y))
        elif direction == "W":
            coordinates.append((last_x - 1, last_y))
        else:
            coordinates.append((last_x, last_y - 1))
    
    coordinates.append(coordinates[1])
    
    
    # 4. TO SOLVE THE PROBLEM
    
    left = 0
    right = 0
    
    for idx in range(2, len(coordinates)):
        p1, p2, p3 = coordinates[idx-2], coordinates[idx-1], coordinates[idx]
        check = ccw(p1, p2, p3)
        if check > 0:
            left += 1
        elif check < 0:
            right += 1
    
    if left > right:
        print("CCW")
    else:
        print("CW")