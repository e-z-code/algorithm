'''
CF2132A - Homework (https://codeforces.com/contest/2132/problem/A)

There are two strings A and B.
You and I are asked to append all characters of B to A in any order.
You can only add characters to the beginning of the word, while I can only add them to the end.
Given the order, determine the string that you and I will end up with.
'''

# TIME COMPLEXITY : O(T(N + M))

import sys
from collections import deque


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    lengthA = int(sys.stdin.readline())
    stringA = list(sys.stdin.readline().strip())
    
    lengthB = int(sys.stdin.readline())
    stringB = list(sys.stdin.readline().strip())
    
    order = sys.stdin.readline().strip()
    
    
    # 2. TO SOLVE THE PROBLEM
    
    answer = deque(stringA)
    
    for idx in range(lengthB):
        if order[idx] == "D":
            answer.append(stringB[idx])
        else:
            answer.appendleft(stringB[idx])
    
    print("".join(list(answer)))