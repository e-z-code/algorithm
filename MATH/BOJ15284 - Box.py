'''
BOJ15284 - Box (https://www.acmicpc.net/problem/15284)

You have a rectangular piece of cardboard of size W X H.
The cardboard can be bent with sides parallel to the sides of the rectangle.
Determine if it is possible to make a box of size out of A X B X C out of the cardboard.
'''

# TIME COMPLEXITY : O(1)

import sys
from itertools import permutations


# 2. A FUNCTION TO DETERMINE FEASIBILITY

def possible(width_needed, height_needed):

    if width_needed <= board_width and height_needed <= board_height:
        return True
    if height_needed <= board_width and width_needed <= board_height:
        return True
    
    return False


# 1. TO GET THE INPUT

box_info = list(map(int, sys.stdin.readline().split()))
board_width, board_height = map(int, sys.stdin.readline().split())


# 3. TO SOLVE THE PROBLEM
# Considering all possible planar figure, there are 5 possible cases.

ans = "No"

for box in permutations(box_info, 3):
    
    x, y, z = box
    
    if possible(x + 2 * y, 2 * y + 2 * z):
        ans = "Yes"
        break
    if possible(x + y + z, 2 * y + 2 * z):
        ans = "Yes"
        break
    if possible(x + 2 * z, x + 2 * y + z):
        ans = "Yes"
        break
    if possible(x + y + z, x + 2 * y + z):
        ans = "Yes"
        break
    if possible(x + z, x + 3 * y + z):
        ans = "Yes"
        break

print(ans)