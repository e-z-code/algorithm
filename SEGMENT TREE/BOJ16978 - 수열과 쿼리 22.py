'''
BOJ16978 - Sequence and Queries 22 (https://www.acmicpc.net/problem/16978)

Given a sequence A, process the two following types of queries.

(1) Change A[i] to v.
(2) Print sum(A[i:j+1]) when the first k (1) queries are processed.
'''

# TIME COMPLEXITY : O(max(N, M) log max(N, M))

import sys


# 4. FUNCTIONS FOR SEGMENT TREE

def update(idx, val):
    
    node = OFFSET + idx
    seg_tree[node] = val
    node >>= 1
    
    while node != 0:
        seg_tree[node] = seg_tree[node << 1] + seg_tree[(node << 1) | 1]
        node >>= 1

def seg_sum(left, right):
    
    left += OFFSET
    right += OFFSET
    
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

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO CONSTRUCT THE SEGMENT TREE
# The segment tree stores the sum of every child node.

OFFSET = 1 << 17

seg_tree = [0 for node in range(1 << 18)]

for idx in range(length):
    seg_tree[OFFSET + idx] = arr[idx]

for node in range(OFFSET-1, 0, -1):
    seg_tree[node] = seg_tree[node << 1] + seg_tree[(node << 1) | 1]


# 3. TO STORE QUERIES

query_count = int(sys.stdin.readline())

queryA_record = []
queryB_record = []

for query_input in range(query_count):
    
    query = list(map(int, sys.stdin.readline().split()))
    
    if query[0] == 1:
        idx, val = query[1], query[2]
        idx -= 1
        queryA_record.append((idx, val))
    else:
        last_queryA, left, right = query[1], query[2], query[3]
        left -= 1
        right -= 1
        queryB_record.append((last_queryA, left, right, len(queryB_record)))

queryB_record.sort()


# 5. TO SOLVE THE PROBLEM (OFFLINE QUERY)
# Rather than processing queries in the given order, process queries in a temporal order.

ans = [0 for id in range(len(queryB_record))]

queryA_id = 0
for queryB in queryB_record:
    
    last_queryA, left, right, queryB_id = queryB
    
    # To synchronize the update status
    while queryA_id < last_queryA:
        idx, val = queryA_record[queryA_id]
        update(idx, val)
        queryA_id += 1
    
    # To put the query result in the right order
    ans[queryB_id] = seg_sum(left, right)

for query_result in ans:
    print(query_result)