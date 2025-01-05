'''
CF2057A - MEX Table (https://codeforces.com/contest/2057/problem/A)

There is an N X M table.
You want to arrange 0, 1, ..., N X M - 1 in the table.
Determine the maximum sum of MEX across all rows and columns.
'''

# TIME COMPLEXITY : O(T)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM
# If a row or a column does not contain 0, the MEX value is 0.
# To achieve the maximum value, you need to put 1, 2, ... on the same line. 

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    row_count, col_count = map(int, sys.stdin.readline().split())
    print(max(row_count, col_count) + 1)