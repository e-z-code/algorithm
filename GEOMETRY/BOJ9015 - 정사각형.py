'''
BOJ9015 - Square (https://www.acmicpc.net/problem/9015)

Given N points, determine the maximum area of the square.
'''

# TIME COMPLEXITY : O(TN^2)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    point_count = int(sys.stdin.readline())
    
    points = []
    for point in range(point_count):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
    points.sort()
    
    
    # 2. TO SOLVE THE PROBLEM
    # If you fix one segment, there are two possible squares of which points are already determined.
        
    points_set = set(points[:])
    ans = 0
    
    for i in range(point_count):
        for j in range(i + 1, point_count):
            
            x1, y1 = points[i]
            x2, y2 = points[j]
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            
            if y1 <= y2:
                
                if (x1 - dy, y1 + dx) in points_set and (x2 - dy, y2 + dx) in points_set:
                    ans = max(ans, dx * dx + dy * dy)
                if (x1 + dy, y1 - dx) in points_set and (x2 + dy, y2 - dx) in points_set:
                    ans = max(ans, dx * dx + dy * dy)
            
            else:
                
                if (x1 + dy, y1 + dx) in points_set and (x2 + dy, y2 + dx) in points_set:
                    ans = max(ans, dx * dx + dy * dy)
                if (x1 - dy, y1 - dx) in points_set and (x2 - dy, y2 - dx) in points_set:
                    ans = max(ans, dx * dx + dy * dy)
    
    print(ans)