'''
BOJ26073 - Lonely Gomgomi Has a Friend (https://www.acmicpc.net/problem/16563)

There are N friends.
Each friend has multiple options of distance.
At each move, the friend chooses a distance and moves by the distance.
Friends can only move parallel to the x-axis or y-axis.
Determine if each friend can arrive (0, 0).
'''

# TIME COMPLEXITY : O(NK log A)


import sys
from math import gcd


# 1. TO GET THE INPUT

friend_count = int(sys.stdin.readline())

for friend in range(friend_count):
    
    x, y = map(int, sys.stdin.readline().split())
    
    info = list(map(int, sys.stdin.readline().split()))
    distance = info[1:]
    
    
    # 2. TO SOLVE THE PROBLEM - BEZOUT'S IDENTITY
    
    unit_dist = distance[0]
    for dist in distance:
        unit_dist = gcd(unit_dist, dist)
    
    if x % unit_dist == 0 and y % unit_dist == 0:
        print("Ta-da")
    else:
        print("Gave up")