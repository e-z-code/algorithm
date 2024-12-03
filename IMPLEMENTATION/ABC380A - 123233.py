'''
ABC380A - 123233 (https://atcoder.jp/contests/abc380/tasks/abc380_a)

There is a 6-digit positive integer N.
Determine whether N satisfies all of the following conditions.

(1) The digit 1 appears once.
(2) The digit 2 appears twice.
(3) The digit 3 appears three times.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT

num = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM

if num.count("1") == 1 and num.count("2") == 2 and num.count("3") == 3:
    print("Yes")
else:
    print("No")