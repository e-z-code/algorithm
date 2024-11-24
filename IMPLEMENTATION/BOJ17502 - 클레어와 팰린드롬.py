'''
BOJ17502 - Claire and Palindrome (https://www.acmicpc.net/problem/17502)

Given some characters of a palindrome, construct a palindrome.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
string = list(sys.stdin.readline().strip())


# 2. TO SOLVE THE PROBLEM

for idx in range(length):
    
    if string[idx] == "?":
        if string[-idx-1] == "?":
            string[idx] = "a"
        else:
            string[idx] = string[-idx-1]

print("".join(string))