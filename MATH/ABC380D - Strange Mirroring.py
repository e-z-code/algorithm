'''
ABC380D - Strange Mirroring (https://atcoder.jp/contests/abc380/tasks/abc380_d)

There is a string S consisting of alphabets.
You perform the following operation on S 10 ^ 100 times:

(1) Create a string T by changing uppercase letters in S to lowercase and lowercase letters to uppercase.
(2) S += T

Answer Q queries which ask the K-th character from the beginning of S after all operations are completed.
'''

# TIME COMPLEXITY : O(Q log K)

import sys


# 1. TO GET THE INPUT

string = sys.stdin.readline().strip()

query_count = int(sys.stdin.readline())
queries = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

length = len(string)

for target in queries:
    
    # To count how many times the capitalization of the character has been changed
    
    arr = [length]
    while arr[-1] <= target:
        arr.append(arr[-1] * 2)
    
    swap_count = 0
    
    string_idx = target - 1
    arr_idx = len(arr) - 1
    while string_idx >= length:
        if string_idx >= arr[arr_idx]:
            string_idx -= arr[arr_idx]
            swap_count += 1
        else:
            arr_idx -= 1

    # To print the result
    
    char = string[string_idx]
    
    if char == char.lower():
        if swap_count % 2 == 0:
            print(char, end = ' ')
        else:
            print(char.upper(), end = ' ')
    else:
        if swap_count % 2 == 0:
            print(char, end = ' ')
        else:
            print(char.lower(), end = ' ')