'''
BOJ5608 - Problem 2 (https://www.acmicpc.net/problem/5608)

Given an encryption table, encrypt the given text.
'''

# TIME COMPLEXITY : O(M)

import sys


# 1. TO GET THE INPUT

convert_table = {}

convert_count = int(sys.stdin.readline())
for convert_rule in range(convert_count):
    text, code = sys.stdin.readline().strip().split()
    convert_table[text] = code


# 2. TO SOLVE THE PROBLEM

ans = []

text_count = int(sys.stdin.readline())
for text_num in range(text_count):
    text = sys.stdin.readline().strip()
    if text in convert_table:
        ans.append(convert_table[text])
    else:
        ans.append(text)

print("".join(ans))