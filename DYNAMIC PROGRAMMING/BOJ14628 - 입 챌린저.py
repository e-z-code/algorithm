'''
BOJ14628 - Alleged Challenger (https://www.acmicpc.net/problem/14628)

There are N skills.
Each time you use a skill, the mana required for the skill increases by K.
You have to attack the monster of M HP.
The monster dies if its HP becomes 0.
Determine the minimum mana needed to kill the monster.
'''

# TIME COMPLEXITY : O(NM^2)

import sys
inf = float('inf')


# 1. TO GET THE INPUT

skill_count, enemy_hp, added_mana = map(int, sys.stdin.readline().split())

skills = [(0, 0)]
for skill in range(skill_count):
    mana, attack_hp = map(int, sys.stdin.readline().split())
    for possible in range(enemy_hp // attack_hp + 2):
        skills.append((mana, attack_hp))
        mana += added_mana


# 2. KNAPSACK DP
# DP[i][j] = Minimum mana required to attack hp of j with i skills
# If N-th skill X is used, the skill X must have been used (N-1) times.

dp = [[inf for hp in range(enemy_hp + 1)] for idx in range(len(skills))]
dp[0][0] = 0

for idx in range(1, len(skills)):
    
    mana, attack_hp = skills[idx]
    
    for hp in range(enemy_hp + 1):
        
        if hp == 0:
            dp[idx][hp] = 0
        elif hp < attack_hp:
            dp[idx][hp] = dp[idx-1][hp]
        else:
            dp[idx][hp] = min(dp[idx-1][hp], dp[idx-1][hp - attack_hp] + mana)

print(dp[-1][-1])