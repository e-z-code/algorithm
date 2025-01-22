'''
BOJ18721 - Preokret (https://www.acmicpc.net/problem/18721)

You recorded which team scored in a football match.
Calculate the final score, how often ties happened, and the largest turnover.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

goal_count = int(sys.stdin.readline())


# 2. TO RECORD THE RESULT

my_goal, opp_goal = 0, 0
tie_count = 1
max_turnover = 0

win_team = 1
win_count = 0

for goal in range(goal_count):
    
    team = int(sys.stdin.readline())
    
    # Turnover check
    
    if team == win_team:
        win_count += 1
    else:
        if win_team == 1:
            if my_goal - win_count < opp_goal and my_goal > opp_goal:
                max_turnover = max(max_turnover, win_count)
            win_team = 2
            win_count = 1
        else:
            if opp_goal - win_count < my_goal and opp_goal > my_goal:
                max_turnover = max(max_turnover, win_count)
            win_team = 1
            win_count = 1
    
    # Score check
    
    if team == 1:
        my_goal += 1
    else:
        opp_goal += 1
    
    # Tie check
    
    if my_goal == opp_goal:
        tie_count += 1

# To consider the last game result if turnover happened

if win_team == 1:
    if my_goal - win_count < opp_goal and my_goal > opp_goal:
        max_turnover = max(max_turnover, win_count)
else:
    if opp_goal - win_count < my_goal and opp_goal > my_goal:
        max_turnover = max(max_turnover, win_count)


# 3. TO SOLVE THE PROBLEM

print(my_goal, opp_goal)
print(tie_count)
print(max_turnover)