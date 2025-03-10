'''
ABC396C - Buy Balls (https://atcoder.jp/contests/abc396/tasks/abc396_c)

There are N black balls and M white balls with the values.
Choose zero or more balls so that the number of black balls is equal to or more than white balls.
Among all such choices, find the maximum possible sum of the values of the chosen balls.
'''

# TIME COMPLEXITY: O(X log X) [X = max(N, M)]

import sys


# 1. TO GET THE INPUT

black_count, white_count = map(int, sys.stdin.readline().split())
black_balls = list(map(int, sys.stdin.readline().split()))
white_balls = list(map(int, sys.stdin.readline().split()))

black_balls.sort()
white_balls.sort()


# 2. TO SOLVE THE PROBLEM

ans = 0
choice = 0

while len(black_balls) > 0 and black_balls[-1] >= 0:
    ans += black_balls.pop()
    choice += 1
while len(white_balls) > 0 and white_balls[-1] > 0 and choice > 0:
    ans += white_balls.pop()
    choice -= 1
while len(black_balls) > 0 and len(white_balls) > 0 and black_balls[-1] + white_balls[-1] > 0:
    ans += black_balls.pop() + white_balls.pop()

print(ans)