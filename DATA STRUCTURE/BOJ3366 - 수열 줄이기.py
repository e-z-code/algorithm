'''
BOJ3366 - Reduce an Array (https://www.acmicpc.net/problem/3366)

There is a sequence A.
You can manipulate the sequence using the operation R(i), which replaces A[i] and A[i+1] with the single element max(A[i], A[i+1]).
The cost of the operation is max(A[i], A[i+1]).
Compute the cost of the optimal reducing scheme.
'''

# TIME COMPLEXITY : O(N log N)

import sys
inf = float('inf')


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())

arr = []
for idx in range(length):
    arr.append(int(sys.stdin.readline()))


# 2. TO FIND NUMBER EACH INDEX CAN REDUCE TO
# Each element can disappear with the cost of an element equal to or larger than itself.
# It is always optimal to choose the minimum between the left-nearest or the right-nearest one.

right_num_to_reduce = [inf for idx in range(length)]

stack = []
for now_idx in range(length):
    now_num = arr[now_idx]
    while len(stack) > 0 and now_num >= stack[-1][0]:
        last_num, last_idx = stack.pop()
        right_num_to_reduce[last_idx] = now_num
    stack.append((now_num, now_idx))

left_num_to_reduce = [inf for idx in range(length)]

stack = []
for now_idx in range(length-1, -1, -1):
    now_num = arr[now_idx]
    while len(stack) > 0 and now_num > stack[-1][0]:
        last_num, last_idx = stack.pop()
        left_num_to_reduce[last_idx] = now_num
    stack.append((now_num, now_idx))


# 3. TO SOLVE THE PROBLEM

num_to_reduce = []

for idx in range(length):
    num_to_reduce.append(min(left_num_to_reduce[idx], right_num_to_reduce[idx]))
num_to_reduce.sort()

print(sum(num_to_reduce[:-1]))