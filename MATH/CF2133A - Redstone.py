'''
CF2133A - Redstone? (https://codeforces.com/contest/2133/problem/A)

There are N gears, where gear I has A[I] teeth.
After arranging them, you will spin the leftmost gear at a speed of 1.
Let X be the number of teeth of gear, Y be the number of teeth of the gear to its left, and Z be the speed of the gear to its left.
Then, for each of the other gears, its speed will be YZ / X revolutions.
Determine if the rightmost gear can spin at a speed of 1.
'''

# TIME COMPLEXITY : O(TN)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    gear_count = int(sys.stdin.readline())
    gears = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    # If A[1] == A[N], the rightmost gear spins at a speed of 1.
    
    if len(gears) == len(set(gears)):
        print("NO")
    else:
        print("YES")