'''
BOJ8443 - Super-numbers in permutation (https://www.acmicpc.net/problem/9001)

There is a permutation of length N.
A number is a super-number if it is a part of any LIS.
Find all the super-numbers.
'''

# TIME COMPLEXITY : O(N log N)

import sys


# 3. FUNCTIONS FOR SEGMENT TREE

def put(num, val):
    
    loc = num + OFFSET
    seg_tree[loc] = val
    loc >>= 1
    
    while loc:
        seg_tree[loc] = max(seg_tree[loc << 1], seg_tree[(loc << 1) | 1])
        loc >>= 1
    
    
def get_max(num):
    
    result = 0
    
    left = OFFSET
    right = num + OFFSET - 1
    
    while left <= right:
        if left % 2 == 1:
            result = max(result, seg_tree[left])
            left += 1
        if right % 2 == 0:
            result = max(result, seg_tree[right])
            right -= 1
        left >>= 1
        right >>= 1
    
    return result


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO CONSTRUCT SEGMENT TREE

OFFSET = 1 << 17
node_count = 1 << 18

seg_tree = [0 for node in range(node_count)]


# 4. O(N log N) LIS

dp = [0 for num in range(size + 1)]
loc = [0 for num in range(size + 1)]

for idx in range(size):
    
    num = arr[idx]
    loc[num] = idx
    dp[num] = get_max(num) + 1
    
    put(num, dp[num])


# 5. TO SOLVE THE PROBLEM

lis_length = max(dp)
ans_num = []

max_loc = [-1 for dp_val in range(lis_length + 1)]

# A number X is a super-number if there is a number Y such that X < Y, dp[X] + 1 = dp[Y], and Y is a super-number.

for num in range(size, 0, -1):
    if dp[num] == lis_length:
        ans_num.append(num)
        max_loc[dp[num]] = max(max_loc[dp[num]], loc[num])
    else:
        if loc[num] < max_loc[dp[num] + 1]:
            ans_num.append(num)
            max_loc[dp[num]] = max(max_loc[dp[num]], loc[num])

ans_num.sort()

print(len(ans_num))
print(" ".join(map(str, ans_num)))