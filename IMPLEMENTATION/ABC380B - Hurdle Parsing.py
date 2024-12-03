'''
ABC380B - Hurdle Parsing (https://atcoder.jp/contests/abc380/tasks/abc380_b)

Your friend had a sequence of positive integers A of length N.
She generated a string S using A as follows:

- Start with |.
- For 1 <= i <= N, append A[i] copies of - and append one | to the end of S.

Given S, reconstruct the sequence A.
'''

# TIME COMPLEXITY : O(|S|)

import sys


# 1. TO GET THE INPUT

string = sys.stdin.readline().strip().strip("|")


# 2. TO SOLVE THE PROBLEM

arr = list(string.split("|"))
for element in arr:
    print(len(element), end = ' ')