'''
BOJ5899 - Overplanting (https://www.acmicpc.net/problem/5899)

There are N rectangles that may overlap.
Calculate the area covered by the rectangles.
'''

# TIME COMPLEXITY : O(N^2 log N)

import sys


# 2. A FUNCTION TO CALCULATE THE LENGTH

def length(arr):
    
    result = 0
    
    low = None
    high = None
    
    for now_low, now_high in arr:
        
        if low == None and high == None:
            low, high = now_low, now_high
        else:
            if now_low > high:
                result += high - low
                low, high = now_low, now_high
            else:
                high = max(high, now_high)

    result += high - low
    return result


# 1. TO GET THE INPUT

rectangle_count = int(sys.stdin.readline())

segments = []
for rectangle in range(rectangle_count):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    segments.append((x1, y2, y1, 1))
    segments.append((x2, y2, y1, -1))

segments.sort()


# 3. TO SOLVE THE PROBLEM

ans = 0
valid_y = []

for idx in range(rectangle_count * 2):
    
    x, y_low, y_high, key = segments[idx]
    
    if idx != 0:
        ans += (x - segments[idx-1][0]) * length(valid_y)

    if key == 1:
        valid_y.append((y_low, y_high))
        valid_y.sort()
    else:
        valid_y.remove((y_low, y_high))
    
print(ans)