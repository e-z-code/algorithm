'''
BOJ17487 - Typing Practice (https://www.acmicpc.net/problem/17487)

You type alphabets left to 'U', 'H', 'N' with a left hand.
A right hand will press the others.
You can press a space bar and 'Shift' key with both hands.
Calculate how much each hand presses keys when the difference is minimum.
'''

# TIME COMPLEXITY : O(|S|)

import sys


# 1. TO GET THE INPUT

sentence = sys.stdin.readline().strip()


# 2. TO COUNT HOW MUCH TIME EACH HAND NEEDS TO PRESS

left_key = "qwertyasdfgzxcvb"

add_count = 0

left_count = 0
right_count = 0

for char in sentence:
    
    if char == " ":
        add_count += 1
    else:
        
        if 65 <= ord(char) <= 90:
            add_count += 1
        
        if char.lower() in left_key:
            left_count += 1
        else:
            right_count += 1


# 3. TO SOLVE THE PROBLEM

while add_count:
    
    if left_count <= right_count:
        left_count += 1
        add_count -= 1
    else:
        right_count += 1
        add_count -= 1

print(left_count, right_count)