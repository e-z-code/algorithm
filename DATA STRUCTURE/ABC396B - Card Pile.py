'''
ABC396B - Card Pile (https://atcoder.jp/contests/abc396/tasks/abc396_b)

There is a stack of 100 cards labeled 0.
Process Q queries of the following two types.

(1) Place a card labeled X on top of the stack.
(2) Remove the top card and output the integer written on that card.
'''

# TIME COMPLEXITY: O(Q)

import sys


# 1. TO GET THE INPUT

query_count = int(sys.stdin.readline())
stack = [0 for card in range(100)]


# 2. TO SOLVE THE PROBLEM

for query in range(query_count):
    
    query_info = list(map(int, sys.stdin.readline().split()))

    if query_info[0] == 1:
        stack.append(query_info[1])
    else:
        print(stack.pop())