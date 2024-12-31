'''
BOJ6892 - Fix (https://www.acmicpc.net/problem/6892)

A collection of words is fix-free if no word is a prefix or a suffix of any other word.
Determine if a collection of three words is fix-free or not.
'''

# TIME COMPLEXITY : O(T|B|) [B : Second largest word]

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    words = []
    for word in range(3):
        words.append(sys.stdin.readline().strip())
    words.sort(key = lambda x : len(x))
    
    
    # 2. TO SOLVE THE PROBLEM
    
    fix_free = True
    
    first_len = len(words[0])
    second_len = len(words[1])
    
    # Prefix check
    if words[0] == words[1][:first_len + 1] or words[0] == words[2][:first_len + 1] or words[1] == words[2][:second_len + 1]:
        fix_free = False
    # Suffix check
    if words[0] == words[1][-first_len:] or words[0] == words[2][-first_len:] or words[1] == words[2][-second_len:]:
        fix_free = False
    
    if fix_free:
        print("Yes")
    else:
        print("No")