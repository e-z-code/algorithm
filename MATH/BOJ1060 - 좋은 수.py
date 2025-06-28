'''
BOJ1060 - Good Number (https://www.acmicpc.net/problem/1060)

Given a set of positive integers S, a good range [A, B] satisfies the following conditions.

(1) A and B are positive integers such that A < B.
(2) X does not belong to S when A <= X <= B.

Let N(X) be the number of good range that includes X.
If N(X) < N(Y), X is a better number than Y.
Also, if N(X) = N(Y) and X < Y, X is a better number than Y.
Given S, determine the best N numbers.
'''

# TIME COMPLEXITY : O(N|S|)

import sys


# 1. TO GET THE INPUT

bomb_count = int(sys.stdin.readline())
bombs = list(map(int, sys.stdin.readline().split()))
ans_count = int(sys.stdin.readline())

bombs.sort()


# 2. TO COUNT THE NUMBER OF GOOD RANGE FOR EACH NUMBER

ans = []

for idx in range(bomb_count):
    
    now_bomb = bombs[idx]
    last_bomb = 0
    if idx != 0:
        last_bomb = bombs[idx-1]
    
    ans.append((0, now_bomb))
    
    # Count the number of good range for numbers between bombs[idx-1] and bombs[idx]
    # There is no need to check more than N numbers.
    
    count = 1
    left = last_bomb + 1
    right = now_bomb - 1
    
    while left < right and count <= 100:
        
        range_count = (left - last_bomb) * (now_bomb - left) - 1
        ans.append((range_count, left))
        ans.append((range_count, right))
        left += 1
        right -= 1
        count += 2
        
    if left == right:
        range_count = (left - last_bomb) * (now_bomb - left) - 1
        ans.append((range_count, left))
    
    # The number of good range for numbers larger than bombs[-1] equals infinity.
    
    if idx == bomb_count - 1:
        
        count = 1
        num = now_bomb + 1
        while count <= 100:
            ans.append((float('inf'), num))
            num += 1
            count += 1

ans.sort()


# 3. TO SOLVE THE PROBLEM

for idx in range(ans_count):
    print(ans[idx][1], end = ' ')