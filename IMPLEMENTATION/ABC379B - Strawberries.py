'''
ABC379B - Strawberries (https://atcoder.jp/contests/abc379/tasks/abc379_b)

There is a string S of length N that represents the condition of your teeth.
If S[i] = O, the i-th tooth from the left is healthy. If S[i] = X, the tooth has a cavity.
When you have K consecutive healthy teeth, you can eat one strawberry using those K teeth.
After eating a strawberry, those K teeth develop cavities.
Determine the maximum number of strawberries you can eat.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

tooth_count, count_to_eat = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

now_count = 0
strawberry = 0

teeth = list(sys.stdin.readline().strip())
for tooth in teeth:
    if tooth == 'O':
        now_count += 1
        if now_count == count_to_eat:
            now_count = 0
            strawberry += 1
    else:
        now_count = 0

print(strawberry)