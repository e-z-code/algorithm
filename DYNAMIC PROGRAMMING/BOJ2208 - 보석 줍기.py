'''
BOJ2208 - Jewels (https://www.acmicpc.net/problem/2208)

There are N jewels.
You can pick up at least M consecutive jewels only once.
Determine the maximum value you can pick up.
'''

# TIME COMPLEXITY : O(N)

import sys
inf = float('inf')


# 1. TO GET THE INPUT

jewel_count, min_count = map(int, sys.stdin.readline().split())

jewels = []
for jewel in range(jewel_count):
    jewels.append(int(sys.stdin.readline()))


# 2. PREFIX SUM

prefix_sum = [jewels[0]]

for idx in range(1, jewel_count):
    prefix_sum.append(prefix_sum[-1] + jewels[idx])


# 3. PREFIX MIN

prefix_min = []

for idx in range(jewel_count):
    if idx < min_count:
        prefix_min.append(0)
    else:
        prefix_min.append(min(prefix_min[-1], prefix_sum[idx - min_count]))


# 4. TO SOLVE THE PROBLEM

ans = 0

for idx in range(min_count-1, jewel_count):
    ans = max(ans, prefix_sum[idx] - prefix_min[idx])

print(ans)