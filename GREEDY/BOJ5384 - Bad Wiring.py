'''
BOJ5384 - Bad Wiring (https://www.acmicpc.net/problem/5384)

There are N lights in a row.
If you flip the X-th switch, every light from the (X-D)th switch to the (X+D)th switch will be flipped.
sDetermine the minimum number of times flipping a switch to turn off all the lights.
'''

# TIME COMPLEXITY : O(pow(2, D) X ND)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    light_count, connection_length = map(int, sys.stdin.readline().split())
    lights = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    # Whether to click first D switches or not decides everything.
    
    ans = 10000
    
    for case in range(1 << connection_length):
        
        count = 0
        now_lights = lights[:]
        
        for switch in range(connection_length):
            if case & (1 << switch):
                count += 1
                for light in range(max(0, switch - connection_length), min(light_count, switch + connection_length + 1)):
                    now_lights[light] ^= 1
        
        for switch in range(connection_length, light_count):
            if now_lights[switch - connection_length] == 1:
                count += 1
                for light in range(max(0, switch - connection_length), min(light_count, switch + connection_length + 1)):
                    now_lights[light] ^= 1
        
        if sum(now_lights) == 0:
            ans = min(ans, count)
    
    if ans == 10000:
        print("impossible")
    else:
        print(ans)