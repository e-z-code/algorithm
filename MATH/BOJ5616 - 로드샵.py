'''
BOJ5616 - Road Shop (https://www.acmicpc.net/problem/5616)

You want to make a necklace of R beads using at least M beads of color N.
Determine the number of distinct necklaces you can make.
'''

# TIME COMPLEXITY : O(max(N, R))

import sys


# 2. A FUNCTION FOR FACTORIAL

def factorial(x):
    
    result = 1
    for num in range(1, x + 1):
        result *= num
    return result


# 1. TO GET THE INPUT

color_count, color_min, total_count = map(int, sys.stdin.readline().split())


# 3. TO SOLVE THE PROBLEM

if color_min * color_count > total_count:
    print(0)
else:
    free_count = total_count - color_min * color_count
    print(factorial(free_count + color_count - 1) // (factorial(color_count - 1) * factorial(free_count)))