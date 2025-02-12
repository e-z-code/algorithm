'''
BOJ27208 - Melons (https://www.acmicpc.net/problem/27208)

There are N melons.
You put the melons from the X-th melon into the box.
If the total weight of the melons in the box exceeds L after putting the next melon in the box, you will put it into a new box.
Determine the number of boxes needed and the total weight of the melons in the last box for all X.
'''

# TIME COMPLEXITY : O(N log N)

import sys


# 1. TO GET THE INPUT

melon_count, limit = map(int, sys.stdin.readline().split())

melons = []
for melon in range(melon_count):
    melons.append(int(sys.stdin.readline()))


# 2. SUFFIX SUM

suffix_sum = [0 for melon in range(melon_count)]
suffix_sum[-1] = melons[-1]

for idx in range(melon_count-2, -1, -1):
    suffix_sum[idx] = suffix_sum[idx+1] + melons[idx]

suffix_sum.append(0)


# 3. DP + BINARY SEARCH
# DP[i] = The number of box required when starting from the i-th melon.

dp = [[-1, -1] for melon in range(melon_count)]

for melon in range(melon_count-1, -1, -1):
    
    if suffix_sum[melon] <= limit:
        
        dp[melon] = [1, suffix_sum[melon]]
        
    else:
        
        # See until what melon can be put in the same box 
        
        left = melon
        right = melon_count - 1
        
        while left + 1 < right:
            
            mid = (left + right) // 2
            
            if suffix_sum[melon] - suffix_sum[mid+1] <= limit:
                left = mid
            else:
                right = mid
        
        dp[melon] = [dp[right][0] + 1, dp[right][1]]


# 4. TO SOLVE THE PROBLEM

for melon in range(melon_count):
    print(dp[melon][0], dp[melon][1])