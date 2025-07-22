'''
BOJ15461 - Milk Measurement (https://www.acmicpc.net/problem/15461)

Initially, every cow produces G gallons of milk per day.
Every day, you display on the wall the picture of cow(s) with the highest milk output.
Given records of change, determine how many times you would change the display.
'''

# TIME COMPLEXITY : O(N log N)

import sys


# 3. A FUNCTION TO UPDATE SEGMENT TREE

def update(idx, val):
    
    node = idx + OFFSET
    seg_tree[node] = (seg_tree[node][0] + val, 1)
    node >>= 1
    
    while node != 0:
        left_val, left_count = seg_tree[node << 1]
        right_val, right_count = seg_tree[(node << 1) | 1]
        if left_val > right_val:
            seg_tree[node] = seg_tree[node << 1]
        elif left_val < right_val:
            seg_tree[node] = seg_tree[(node << 1) | 1]
        else:
            seg_tree[node] = (left_val, left_count + right_count)
        node >>= 1


# 1. TO GET THE INPUT

record_count, init_val = map(int, sys.stdin.readline().split())

cow_num = 0
cow_label = {}

records = []
for record in range(record_count):
    day, cow, diff = map(int, sys.stdin.readline().split())
    if cow not in cow_label:
        cow_label[cow] = cow_num
        cow_num += 1
    records.append((day, cow_label[cow], diff))
records.sort()


# 2. TO CONSTRUCT A SEGMENT TREE

OFFSET = 1 << 17
node_count = 1 << 18 

seg_tree = [(init_val, 1) for node in range(node_count)]
for node in range(OFFSET-1, 0, -1):
    left_val, left_count = seg_tree[node << 1]
    right_val, right_count = seg_tree[(node << 1) | 1]
    if left_val > right_val:
        seg_tree[node] = seg_tree[node << 1]
    elif left_val < right_val:
        seg_tree[node] = seg_tree[(node << 1) | 1]
    else:
        seg_tree[node] = (left_val, left_count + right_count)


# 4. TO SOLVE THE PROBLEM

ans = 0

for day, cow, diff in records:
    
    now_val, now_count = seg_tree[OFFSET + cow]
    now_best_val, now_best_count = seg_tree[1]
    update(cow, diff)
    new_val, new_count = seg_tree[OFFSET + cow]
    new_best_val, new_best_count = seg_tree[1]
    
    if now_best_val != new_best_val or now_best_count != new_best_count:
        if now_val == now_best_val and now_count == now_best_count and new_val == new_best_val and new_count == new_best_count:
            continue
        else:
            ans += 1

print(ans)