'''
CF2133B - Villagers (https://codeforces.com/contest/2133/problem/B)

There are N villagers, each of which with a grumpiness of G[I].
You can perform the following operation any number of times:

Select two villagers X and Y and give them max(X, Y) emeralds to share.
Both of their grumpiness decrease by min(G[X], G[Y]) and they become friends.

Determine the minimum number of emeralds to make all villagers connected.
'''

# TIME COMPLEXITY : O(TN log N)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    
    ans = 0
    for idx in range(length-1, -1, -2):
        ans += arr[idx]
    print(ans)