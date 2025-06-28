'''
BOJ25340 - On Time (https://www.acmicpc.net/problem/25340)

There are N traffic lights.
The i-th traffic light starts operating at C[i] and needs D[i] seconds to cross.
It has an interval of A[i] seconds and is on for the first B[i] seconds.

You can only decide when to start.
Given information regarding traffic lights, print if it is possible to arrive at exactly T.
'''

# TIME COMPLEXITY : O(N log T)

import sys


# 2. A FUNCTION TO CALCULATE ARRIVAL TIME

def arrival_time(start_time):
    
    now_time = start_time + move_time[0]
    
    for light in range(1, light_count + 1):
        
        interval, green_time, start_time, cross_time = lights[light]
        
        if now_time < start_time:
            now_time = start_time
            
        now_light = (now_time - start_time) % interval
        if now_light < green_time and now_light + cross_time <= green_time:
            now_time += cross_time
        else:
            now_time += (interval - now_light) + cross_time
        now_time += move_time[light]
    
    return now_time


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    light_count, goal_time = map(int, sys.stdin.readline().split())
    
    lights = [(-1, -1, -1, -1)]
    for light in range(light_count):
        interval, green_time, start_time, cross_time = map(int, sys.stdin.readline().split())
        lights.append((interval, green_time, start_time, cross_time))
    
    move_time = list(map(int, sys.stdin.readline().split()))
    
    
    # 3. PARAMETRIC SEARCH
    
    left = 0
    right = goal_time + 1
    
    while left + 1 < right:
        mid = (left + right) // 2
        if arrival_time(mid) <= goal_time:
            left = mid
        else:
            right = mid
    
    
    # 4. TO SOLVE THE PROBLEM
    
    if arrival_time(left) == goal_time:
        print("YES")
    else:
        print("NO")