'''
BOJ6474 - Palindromes (https://www.acmicpc.net/problem/6474)

Determine if a given string is palindrome, mirrored string, or neither.
'''

# TIME COMPLEXITY : O(TS) [T : Number of strings / S : Maximum length of string]

import sys


# 1. TO STORE MIRROR PAIRS

key = "AEHIJLMOSTUVWXYZ12358"
value = "A3HILJMO2TUVWXY51SEZ8"

mirror_pair = {}
for idx in range(len(key)):
    mirror_pair[key[idx]] = value[idx]


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

while True:
    try:
        
        palindrome = True
        mirror = True
        
        word = input()
        for idx in range(len(word)):
            if word[idx] != word[-idx-1]:
                palindrome = False
            if (word[idx] not in mirror_pair) or (mirror_pair[word[idx]] != word[-idx-1]):
                mirror = False
        
        if palindrome:
            if mirror:
                print("{} -- is a mirrored palindrome.".format(word))
            else:
                print("{} -- is a palindrome.".format(word))
        else:
            if mirror:
                print("{} -- is a mirrored string.".format(word))
            else:
                print("{} -- is not a palindrome.".format(word))
        print()

    except:
        break