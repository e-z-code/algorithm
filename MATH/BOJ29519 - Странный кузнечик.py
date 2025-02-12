'''
BOJ29519 - Strange Grasshopper (https://www.acmicpc.net/problem/29519)

There are N stones. Some of them are destroyed.
A grasshopper is now at the first stone. 
If the grasshopper is on the K-th stone, it only jumps exactly K stones forward.
Determine if the grasshopper can reach the last stone.
'''

# TIME COMPLEXITY : O(log N)

import sys


# 1. TO GET THE INPUT

stone_count = int(sys.stdin.readline())
valid = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM
# Grasshopper steps on K-th stone if K is a power of two.

power_of_two = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]

if stone_count not in power_of_two:
    
    print("No")

else:
    
    possible = True
    for num in power_of_two:
        if num > len(valid):
            break
        else:
            if valid[num-1] == 0:
                possible = False
                break
    
    if possible:
        print("Yes")
    else:
        print("No")