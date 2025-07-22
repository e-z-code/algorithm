'''
BOJ23322 - Steal the Chocolate (https://www.acmicpc.net/problem/23322)

There are N chocolate boxes: A[1], A[2], ..., A[N]
It satisfies A[1] <= A[2] <= ... <= A[N].

You can steal some chocolates in a day by the following operation. 
(1) Pick A[I] and steal A[I] - A[I-K] chocolates from there.
(2) Sort all boxes.

Determine how many chocolates you can steal in how many days.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

box_count, interval = map(int, sys.stdin.readline().split())
boxes = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM
# By performing an operation K times, you can make A[I-K] ~ A[I] all equal.
# Thus, you can always make every box equal with initial A[0].

ans_chocolate = 0
ans_count = 0

for box in boxes:
    ans_chocolate += box - boxes[0]
    if box != boxes[0]:
        ans_count += 1

print(ans_chocolate, ans_count)