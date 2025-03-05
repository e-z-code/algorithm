'''
BOJ28346 - XOR Necklace (https://www.acmicpc.net/problem/28346)

There is a necklace of N beads.
The value of the necklace is the sum of the XOR value of each pair of consecutive beads.
You can remove zero or more beads to maximize the value.
Determine the maximum value of the necklace.
'''

# TIME COMPLEXITY : O(TN)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    bead_count = int(sys.stdin.readline())
    beads = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    # The value never increases when removing a bead.
    
    ans = 0
    for idx in range(bead_count):
        ans += beads[idx-1] ^ beads[idx]
    print(ans)