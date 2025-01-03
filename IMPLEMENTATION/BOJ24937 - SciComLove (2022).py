'''
BOJ24937 - SciComLove (2022) (https://www.acmicpc.net/problem/24937)

Given a word, in each turn, you cut the first letter and paste it at the last.
The initial word is "SciComLove".
Determine the word you get after N turns.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

word = "SciComLove"

count = int(sys.stdin.readline())
start_idx = count % 10

print(word[start_idx:] + word[:start_idx])