'''
BOJ20950 - Artist Mimi (https://www.acmicpc.net/problem/20950)

There are N colors.
You want to make the color closest to color X by mixing at most 7 colors.
Determine the minimum difference between your new color and X. 
'''

# TIME COMPLEXITY : O(N ^ 7)

import sys
from itertools import combinations
inf = float('inf')


# 2. A FUNCTION TO GET NEW COLOR

def new_color(arr):
    
    red = 0
    blue = 0
    green = 0
    
    for color in arr:
        red += color[0]
        blue += color[1]
        green += color[2]
    
    return red // len(arr), blue // len(arr), green // len(arr)


# 1. TO GET THE INPUT

color_count = int(sys.stdin.readline())

colors = []
for color in range(color_count):
    red, green, blue = map(int, sys.stdin.readline().split())
    colors.append((red, green, blue))

goal_red, goal_green, goal_blue = map(int, sys.stdin.readline().split())


# 3. TO SOLVE THE PROBLEM

ans = inf

for choice_count in range(2, min(8, color_count + 1)):
    for choices in combinations(colors, choice_count):
        
        choices = list(choices)
        new_red, new_green, new_blue = new_color(choices)
        
        ans = min(ans, abs(new_red - goal_red) + abs(new_green - goal_green) + abs(new_blue - goal_blue))

print(ans)