'''
BOJ34056 - Concert (https://www.acmicpc.net/problem/34056)

There are N sound-absorbing walls with different capabilities.
If there is a concert of noise D between X-th wall and (X+1)-th wall, the followings happen.

Let A[X] be the value of capability of X-th sound-absorbing wall.
(1) X-th wall absorbs the noise of min(A[X], D). If noise remains, it goes to (X-1)-th wall.
(2) The capability of wall increases by the amount of noise it absorbed.
The same happens for the opposite direction. 

Answer Q queries: What is the capability of X-th wall?
'''

# TIME COMPLEXITY : O(N log D)

import sys


# 1. TO GET THE INPUT

wall_count = int(sys.stdin.readline())
walls = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE QUERIES
# Since capability doubles, naive approach works.

query_count = int(sys.stdin.readline())

for query_num in range(query_count):
    
    query = list(map(int, sys.stdin.readline().split()))
    
    if query[0] == 1:
        
        loc, val = query[1:]
        
        # To left
        
        now_loc = loc - 1
        now_val = val
        while 0 <= now_loc and 0 < now_val:
            val_absorbed = min(walls[now_loc], now_val)
            walls[now_loc] += val_absorbed
            now_val -= val_absorbed
            now_loc -= 1
        
        # To right
        
        now_loc = loc
        now_val = val
        while now_loc < wall_count and 0 < now_val:
            val_absorbed = min(walls[now_loc], now_val)
            walls[now_loc] += val_absorbed
            now_val -= val_absorbed
            now_loc += 1
    
    else:
        
        loc = query[1]
        print(walls[loc-1])