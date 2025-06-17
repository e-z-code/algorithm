'''
BOJ26218 - Production System Management (https://www.acmicpc.net/problem/26218)

There are N machines.
Machine X can process a work at P(X)% probability.
If you upgrade the machine with the cost of C(X), the probability increases by A(X)%.
Given the budget, determine the optimal way such that all machines process their work.
'''

# TIME COMPLEXITY : O(NB)

import sys


# 1. TO GET THE INPUT

machine_count, total_cost = map(int, sys.stdin.readline().split())

init_probs = []

machines = [(-1, -1, -1)]
for machine in range(machine_count):
    init_prob, add_prob, add_cost = map(int, sys.stdin.readline().split())
    init_probs.append(init_prob)
    machines.append((init_prob, add_prob, add_cost))


# 2. DP
# DP[i][j] = (Best probability when considering first i machines with the budget of j)

dp = [[1 for cost in range(total_cost + 1)] for idx in range(machine_count + 1)]
prev = [[0 for cost in range(total_cost + 1)] for idx in range(machine_count + 1)]

for idx in range(1, machine_count + 1):
    init_prob, add_prob, add_cost = machines[idx]
    for cost in range(total_cost + 1):
        now_cost = 0
        now_prob = init_prob
        while now_cost <= cost:
            if dp[idx][cost] < dp[idx-1][cost-now_cost] * now_prob:
                dp[idx][cost] = dp[idx-1][cost-now_cost] * now_prob
                prev[idx][cost] = now_cost // add_cost
            if now_prob == 100:
                break
            now_cost += add_cost
            now_prob = min(100, now_prob + add_prob)


# 3. TO SOLVE THE PROBLEM

print(dp[-1][-1])

ans = []
now_idx = machine_count
now_cost = total_cost
while now_idx != 0:
    ans.append(prev[now_idx][now_cost])
    now_cost -= machines[now_idx][2] * prev[now_idx][now_cost]
    now_idx -= 1
for idx in range(len(ans)-1, -1, -1):
    print(ans[idx], end = ' ')