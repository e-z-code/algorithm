'''
BOJ28635 - Indicator (https://www.acmicpc.net/problem/28635)

You have a stopwatch that has an indicator.
Each time you press a button, the number increases by one.
After an indicator reaches M, the indicator returns to 1. 
Determine the minimum number to reach B from A.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT

max_num = int(sys.stdin.readline())
first_num = int(sys.stdin.readline())
goal_num = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM

if first_num <= goal_num:
    print(goal_num - first_num)
else:
    print(goal_num + max_num - first_num)