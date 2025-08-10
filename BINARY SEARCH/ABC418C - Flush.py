'''
ABC418C - Flush (https://atcoder.jp/contests/abc418/tasks/abc418_c)

There are tea bags of N different flavors.
You will play a game of difficulty B using the tea bags.
The game proceeds as follows.

(1) You choose an integer X such that B <= X <= (The number of tea bags)
(2) The dealer chooses X tea bags.
(3) You choose B tea bags from X tea bags.
(4) If all B tea bags are of the same flavor, you win. Otherwise, you lose.

Answer Q queries: Given B, determine the minimum X to guarantee a win.
'''

# TIME COMPLEXITY: O(max(N, Q) log N)

import sys
from bisect import bisect_left


# 1. TO GET THE INPUT

flavor_count, query_count = map(int, sys.stdin.readline().split())
tea_count = list(map(int, sys.stdin.readline().split()))

tea_count.sort()


# 2. PREFIX SUM

prefix_sum = [0]
for idx in range(flavor_count):
    prefix_sum.append(prefix_sum[-1] + tea_count[idx])


# 3. TO SOLVE THE PROBLEM

for query in range(query_count):
    
    minimum = int(sys.stdin.readline())
    
    if minimum > tea_count[-1]:
        print(-1)
    else:
        key_idx = bisect_left(tea_count, minimum - 1)
        ans = prefix_sum[key_idx] + (len(tea_count) - key_idx) * (minimum - 1) + 1
        print(ans)