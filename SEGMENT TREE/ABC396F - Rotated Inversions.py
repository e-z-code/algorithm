'''
ABC396F - Rotated Inversions (https://atcoder.jp/contests/abc396/tasks/abc396_f)

There is an array A of length N.
Let B an array such that B[i] = (A[i] + K) % M.
Find the inversion number of B for 0 <= K < M.
'''

# TIME COMPLEXITY: O(N log N + M) 

import sys


# 2. FUNCTIONS TO COUNT INVERSION USING SEGMENT TREE

def add(val):
    
    val += OFFSET
    
    while val != 0:
        seg_tree[val] += 1
        val >>= 1

def suffix_sum(start):
    
    start += OFFSET
    end = (1 << 22) - 1
    
    result = 0
    
    while start <= end:
        if start % 2 == 1:
            result += seg_tree[start]
            start += 1
        if end % 2 == 0:
            result += seg_tree[end]
            end -= 1
        start >>= 1
        end >>= 1
    
    return result


# 1. TO GET THE INPUT

length, mod = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
locations = [[] for val in range(mod)]

for idx in range(length):
    arr[idx] %= mod
    locations[arr[idx]].append(idx)


# 3. TO COUNT INVERSION WHEN K = 0 USING SEGMENT TREE

OFFSET = 1 << 21
node_count = 1 << 22

seg_tree = [0 for idx in range(node_count)]

inversion_count = 0

for idx in range(length):
    add(arr[idx])
    inversion_count += suffix_sum(arr[idx] + 1)


# 4. COUNT INVERSION FOR ALL K
# Let's assume A[X] is the largest value that becomes 0 when 1 is added.
# Then, N-X-1 inversions are removed while X inversions are added.

now_zero = mod - 1

answer = [0 for remainder in range(mod)]
answer[0] = inversion_count

while now_zero != 0:
    for idx in range(len(locations[now_zero])):
        loc = locations[now_zero][idx]
        inversion_count -= (length - 1 - loc) 
        inversion_count += loc
    answer[now_zero] = inversion_count
    now_zero -= 1


# 5. TO SOLVE THE PROBLEM

now_zero = 0
count = mod

while count > 0:
    print(answer[now_zero])
    now_zero = (now_zero - 1) % mod
    count -= 1