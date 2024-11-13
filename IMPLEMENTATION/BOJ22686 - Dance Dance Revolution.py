'''
BOJ22686 - Dance Dance Revolution (https://www.acmicpc.net/problem/22686)

Given a DDR score, determine whether the score is natural.

The score is natural if
(1) left-foot steps and right-foot steps appear in turn
(2) the same panel is not stepped on any two consecutive arrows
(3) a player can keep the upper body facing forward during a play, and
(4) the player's legs never cross each other.
'''

# TIME COMPLEXITY : O(T|S|)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    arrows = list(sys.stdin.readline().strip())
    
    
    # 2. TO SOLVE THE PROBLEM
    # To check condition (2) is enough. 
    
    ans = "Yes"
    
    for idx in range(1, len(arrows)):
        if arrows[idx] == arrows[idx-1]:
            ans = "No"
            break
    
    print(ans)