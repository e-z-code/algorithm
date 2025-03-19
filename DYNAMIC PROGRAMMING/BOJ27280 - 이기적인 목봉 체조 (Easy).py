'''
BOJ27280 - Selfish Training (Easy) (https://www.acmicpc.net/problem/27280)

You want to group N soldiers into M groups.
Each group consists of one or more consecutive soldiers.
Since all soldiers are selfish, only the tallest ones in the group will lift the weight.
Find the grouping such that soldiers lift the maximum weight.
'''

# TIME COMPLEXITY : O(N^2 X M)

import sys


# 1. TO GET THE INPUT

soldier_count, group_count = map(int, sys.stdin.readline().split())

soldiers = []
for solider in range(soldier_count):
    height, power = map(int, sys.stdin.readline().split())
    soldiers.append((height, power))


# 2. MAXIMUM WEIGHT EACH GROUP CAN LIFT

group_power = [[0 for end in range(soldier_count)] for start in range(soldier_count)]

for start in range(soldier_count):
    
    now_height = 0
    now_power = 0
    
    for end in range(start, soldier_count):
        
        soldier_height, soldier_power = soldiers[end]
        
        if now_height < soldier_height:
            now_height = soldier_height
            now_power = soldier_power
        elif now_height == soldier_height:
            now_power += soldier_power
        
        group_power[start][end] = now_power


# 3. TO SOLVE THE PROBLEM - DP
# DP[g][s] = The maximum weight first s soldiers can lift when there are g groups.

dp = [[0 for soldier in range(soldier_count)] for group in range(group_count + 1)]

for group in range(1, group_count + 1):
    for soldier in range(soldier_count):
        
        if group == 1:
            dp[group][soldier] = group_power[0][soldier]
        else:
            for last_group_soldier in range(soldier):
                dp[group][soldier] = max(dp[group][soldier], dp[group-1][last_group_soldier] + group_power[last_group_soldier+1][soldier])

print(dp[-1][-1])