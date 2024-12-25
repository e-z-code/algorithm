'''
BOJ27513 - Snake (https://www.acmicpc.net/problem/27513)

There is an N X M grid.
Print the snake of maximum length in the Snake game such that the head and the tail are adjacent.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT

width, height = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

if width % 2 == 0:
    
    print(width * height)
    for y in range(1, height + 1):
        print(1, y)
    for x in range(2, width + 1):
        print(x, height)
    for x in range(width, 1, -1):
        if (x - 1) % 2 == 0:
            for y in range(1, height):
                print(x, y)
        else:
            for y in range(height - 1, 0, -1):
                print(x, y)

else:
    
    if height % 2 == 0:
        
        print(width * height)
        for x in range(1, width + 1):
            print(x, 1)
        for y in range(2, height + 1):
            print(width, y)
        for y in range(height, 1, -1):
            if (y - 1) % 2 == 0:
                for x in range(1, width):
                    print(x, y)
            else:
                for x in range(width - 1, 0, -1):
                    print(x, y)
        
    else:
        
        print(width * height - 1)
        print(2, 1)
        print(2, 2)
        for y in range(2, height + 1):
            print(1, y)
        for y in range(height, 2, -1):
            if (height - y) % 2 == 0:
                for x in range(2, width + 1):
                    print(x, y)
            else:
                for x in range(width, 1, -1):
                    print(x, y)
        for x in range(width, 2, -1):
            if (width - x) % 2 == 0:
                print(x, 2)
                print(x, 1)
            else:
                print(x, 1)
                print(x, 2)