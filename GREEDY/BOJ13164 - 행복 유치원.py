'''
BOJ13164 - Happy Kindergarten (https://www.acmicpc.net/problem/13164)

There are N children in a row sorted by height.
You want to make K groups of consecutive children.
The cost of each group is the difference between the maximum and the minimum height.
Determine the minimum cost.
'''

# TIME COMPLEXITY : O(N log N) 

import sys


# 1. TO GET THE INPUT

child_count, group_count = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM
# Assume you choose two adjacent students and put them in the same group.
# Then, the number of groups decrease by 1 and the cost increases by the height difference.

diff = []
for idx in range(child_count - 1):
    diff.append(heights[idx+1] - heights[idx])
diff.sort()

merge_count = child_count - group_count
print(sum(diff[:merge_count])) 