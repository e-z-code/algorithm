'''
CF2134A - Painting With Two Colors (https://codeforces.com/contest/2134/problem/A)

There is a row of N cells, initially all white.
First, you will choose an index X and paint the A consecutive cells red.
Second, you will choose an index Y and paint the B consecutive cells blue.
Determine if there exists X and Y such that the final coloring is symmetric.
'''

# TIME COMPLEXITY : O(T)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    cell_count, red_count, blue_count = map(int, sys.stdin.readline().split())
    
    if cell_count % 2 == blue_count % 2:
        if cell_count % 2 == red_count % 2 or red_count < blue_count:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")