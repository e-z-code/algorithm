'''
BOJ16519 - Other Side (https://www.acmicpc.net/problem/16519)

There are W wolves, S sheep, and C cabbages.
You want to transport them using a boat with the capacity of K.
When left unsupervised, wolves will eat sheep, and sheep will eat cabbages.
Determine if you can complete transportation without any loss.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT

wolf_count, sheep_count, cabbage_count, capacity = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

if min(wolf_count + cabbage_count, sheep_count) < capacity:
    print("YES")
elif min(wolf_count + cabbage_count, sheep_count) == capacity:
    if max(wolf_count + cabbage_count, sheep_count) <= capacity * 2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")