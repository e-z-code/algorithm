'''
BOJ31222 - Sequence and Not Difficult Queries (https://www.acmicpc.net/problem/31222)

If elements of a substring are all equal, the substring is called CUS (continuous uniform substring).
If a CUS is not a part of any other CUSs, the CUS is called ICUS (important continuous uniform substring).

Given a sequence S, process the two following types of queries.
(1) Change S[i] to X.
(2) Print the number of ICUSs in S[i:j+1].
'''

# TIME COMPLEXITY: O((N + Q) log N)

import sys


# 2. FUNCTIONS FOR SEGMENT TREE

def update(node, val):
    
    seg_tree[node] = val
    node >>= 1
    
    while node != 0:
        seg_tree[node] = seg_tree[node << 1] + seg_tree[(node << 1) | 1]
        node >>= 1

def seg_sum(left, right):
    
    result = 0
    while left <= right:
        if left % 2 == 1:
            result += seg_tree[left]
            left += 1
        if right % 2 == 0:
            result += seg_tree[right]
            right -= 1
        left >>= 1
        right >>= 1
    
    return result


# 1. TO GET THE INPUT

length, query_count = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


# 3. TO CONSTRUCT A SEGMENT TREE
# For every index, the segment tree marks the index 1 if arr[index-1] != arr[index] and 0 otherwise.

OFFSET = 1 << 18
seg_tree = [0 for node in range(1 << 19)]
for idx in range(length):
    if idx != 0 and arr[idx-1] != arr[idx]:
        update(idx + OFFSET, 1)


# 4. TO SOLVE THE PROBLEM

for query_input in range(query_count):
    
    query = list(map(int, sys.stdin.readline().split()))
    
    # Query 1 : To modify arr[idx] and mark idx and idx+1 accordingly. 

    if query[0] == 1:
        
        idx, val = query[1], query[2]
        idx -= 1
        arr[idx] = val
        
        if idx != 0:
            if arr[idx-1] == arr[idx]:
                update(idx + OFFSET, 0)
            else:
                update(idx + OFFSET, 1)
        if idx != length - 1:
            if arr[idx] == arr[idx+1]:
                update(idx + 1 + OFFSET, 0)
            else:
                update(idx + 1 + OFFSET, 1)
    
    # Query 2 : To get the sum from left + 1 to right in the segment tree and plus 1.
    # The number of ICUSs = The number of indices where the number changes + 1
    
    else:
        
        left, right = query[1], query[2]
        left += OFFSET - 1
        right += OFFSET - 1
        
        print(seg_sum(left + 1, right) + 1)