'''
ABC392B - Who is Missing? (https://atcoder.jp/contests/abc392/tasks/abc392_b)

There is an array A of M integers.
Each element of A is an integer between 1 and N.
All elements are distinct.
List all integers between 1 and N that do not appear in A in ascending order.
'''

# TIME COMPLEXITY: O(N log N)

import sys


# 1. TO GET THE INPUT

max_num, arr_length = map(int, sys.stdin.readline().split())
arr = set(list(map(int, sys.stdin.readline().split())))


# 2. TO SOLVE THE PROBLEM

ans = sorted(list(set(list(range(1, max_num + 1))) - arr))

print(len(ans))
print(" ".join(map(str, ans)))