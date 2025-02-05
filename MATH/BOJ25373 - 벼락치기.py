'''
BOJ25373 - Cram (https://www.acmicpc.net/problem/25373)

You have 7 days to study for mid-term and have to watch N lectures.
If you watch X lectures one day, you can only watch less than X lectures the next day.
Determine the minimum number of lectures you need to watch on day 1 to watch all lectures.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT

lecture_count = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM

if lecture_count <= 1:
    print(1)
elif lecture_count <= 3:
    print(2)
elif lecture_count <= 6:
    print(3)
elif lecture_count <= 10:
    print(4)
elif lecture_count <= 15:
    print(5)
elif lecture_count <= 21:
    print(6)
else:
    ans = (lecture_count + 21) // 7
    if (lecture_count + 21) % 7 != 0:
        ans += 1
    print(ans)