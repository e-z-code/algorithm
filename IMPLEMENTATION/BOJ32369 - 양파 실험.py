'''
BOJ32369 - Onion Experiment (https://www.acmicpc.net/problem/32369)

There are two onions.
You say good words to one onion - "good onion" - and bad words to the other - "bad onion."
Then, you compare the growth of the two.
Each day, you change the role of two onions if the good onion is shorter than the bad onion.
If the two lengths are the same, you cut the length of the bad onion by 1.
Determine the result of the experiment after N days.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

day_count, good_word_growth, bad_word_growth = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

good_onion = 1
bad_onion = 1

for day in range(day_count):
    
    good_onion += good_word_growth
    bad_onion += bad_word_growth
    
    if good_onion < bad_onion:
        good_onion, bad_onion = bad_onion, good_onion
    elif good_onion == bad_onion:
        bad_onion -= 1

print(good_onion, bad_onion)