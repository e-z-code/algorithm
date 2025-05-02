'''
BOJ25288 - English Test (https://www.acmicpc.net/problem/25288)

There is a string X of length N consisting of given alphabets.
Print any string Y such that LCS(X, Y) = X for any X.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

length = int(sys.stdin.readline())
alphabets = sys.stdin.readline().strip()

print(length * alphabets)