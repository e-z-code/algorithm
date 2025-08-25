'''
BOJ34052 - PE is Math 2 (https://www.acmicpc.net/problem/34052)

Determine if A + B + C + D + 300 <= 1800.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

first_lap = int(sys.stdin.readline())
second_lap = int(sys.stdin.readline())
third_lap = int(sys.stdin.readline())
fourth_lap = int(sys.stdin.readline())

if first_lap + second_lap + third_lap + fourth_lap <= 1500:
    print("Yes")
else:
    print("No")