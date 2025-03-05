'''
BOJ11179 - Reversed Binary Numbers (https://www.acmicpc.net/problem/11179)

Given a number, calculate the value of its reversed binary form.
'''

# TIME COMPLEXITY : O(log N)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

num = int(sys.stdin.readline())
new_num = int(bin(num)[2:][::-1], 2)

print(new_num)