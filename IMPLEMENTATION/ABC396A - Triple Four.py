'''
ABC396A - Triple Four (https://atcoder.jp/contests/abc396/tasks/abc396_a)

There is an integer sequence of length N.
Determine if there is a case where the same element appears three or more times in a row.
'''

# TIME COMPLEXITY: O(N)

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

ans = "No"

now_element = 0
now_count = 0

for idx in range(length):
    
    if arr[idx] != now_element:
        now_element = arr[idx]
        now_count = 1
    else:
        now_count += 1
    
    if now_count == 3:
        ans = "Yes"
        break

print(ans)