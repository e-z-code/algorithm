'''
BOJ2613 - Number Beads (https://www.acmicpc.net/problem/2613)

You need to divide N number beads into M groups.
Your goal is to minimize the maximum sum of groups.
Determine the minimal value of the maximum sum and the number of beads of each group for such a case. 
'''

# TIME COMPLEXITY : O(MN)


import sys
inf = float('inf')


# 1. TO GET THE INPUT

bead_count, group_count = map(int, sys.stdin.readline().split())
beads = [0] + list(map(int, sys.stdin.readline().split()))


# 2. PREFIX SUM

prefix_sum = [0]

for idx in range(1, bead_count + 1):
    prefix_sum.append(prefix_sum[-1] + beads[idx])


# 3. DYNAMIC PROGRAMMING
# dp[g][i] = Minimum value to divide first i beads into g groups.

dp = [[inf for i in range(bead_count + 1)] for group in range(group_count + 1)]
prev = [[(inf, inf) for i in range(bead_count + 1)] for group in range(group_count + 1)]

for group in range(1, group_count + 1):
    for i in range(1, bead_count + 1):
        
        if group == i:
            if group == 1:
                dp[group][i] = beads[i]
                prev[group][i] = (0, 0)
            else:
                dp[group][i] = min(dp[group][i], max(dp[group-1][i-1], beads[i]))
                prev[group][i] = (group-1, i-1)
        elif group < i:
            if group == 1:
                dp[group][i] = prefix_sum[i]
                prev[group][i] = (0, 0)
            else:
                for j in range(group-1, i):
                    if max(dp[group-1][j], prefix_sum[i] - prefix_sum[j]) < dp[group][i]:
                        dp[group][i] = max(dp[group-1][j], prefix_sum[i] - prefix_sum[j])
                        prev[group][i] = (group-1, j)


# 4. TO SOLVE THE PROBLEM (TRACING)

print(dp[group_count][bead_count])

ans = []

now_group = group_count
now_bead = bead_count

while now_group != 0 or now_bead != 0:
    
    next_group, next_bead = prev[now_group][now_bead]
    ans.append(now_bead - next_bead)
    now_group, now_bead = next_group, next_bead

print(" ".join(map(str, ans[::-1])))