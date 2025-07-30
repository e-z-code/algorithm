'''
BOJ11319 - Count Me In (https://www.acmicpc.net/problem/11319)

Given a sentence, count the number of consonants and vowels.
'''

# TIME COMPLEXITY : O(T|S|) [T : The number of testcases / S : The longest input string]

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    sentence = list(sys.stdin.readline().strip().lower().split())
    
    
    # 2. TO SOLVE THE PROBLEM
    
    char_count = 0
    vowel_count = 0
    
    for word in sentence:
        for char in word:
            char_count += 1
            if char in vowels:
                vowel_count += 1
    
    print(char_count - vowel_count, vowel_count)