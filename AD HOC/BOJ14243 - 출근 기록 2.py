'''
BOJ14243 - Record 2 (https://www.acmicpc.net/problem/14243)

There is a string S consists of three characters: A, B, and C.
Print a permutation of S that satisfies the following conditions:

(1) Once B appears, the next B cannot appear for a character.
(2) Once C appears, the next C cannot appear for two characters.
'''

# TIME COMPLEXITY : O(|S|)

import sys


# 1. TO GET THE INPUT

a_count = 0
b_count = 0
c_count = 0

record = sys.stdin.readline().strip()
for char in record:
    if char == "A":
        a_count += 1
    elif char == "B":
        b_count += 1
    else:
        c_count += 1


# 2. TO CONSTRUCT THE ANSWER

ans = []
possible = True

# "BAC" and "AAC" are the smallest unit that can consume as many C as possible.

if c_count:
    ans.append("C")
    c_count -= 1

while c_count:
    if a_count and b_count:
        ans.append("BAC")
        a_count -= 1
        b_count -= 1
        c_count -= 1
    elif a_count >= 2:
        ans.append("AAC")
        a_count -= 2
        c_count -= 1
    else:
        possible = False
        break

# To consume as many B as possible

for idx in range(len(ans)):
    if b_count:
        if ans[idx] == "C":
            ans[idx] = "BC"
            b_count -= 1
        elif ans[idx] == "BAC":
            ans[idx] = "BABC"
            b_count -= 1
    else:
        break

# AB is the smallest unit to consume as many B as possible.

if b_count:
    ans.append("B")
    b_count -= 1

while b_count:
    if a_count:
        ans.append("AB")
        a_count -= 1
        b_count -= 1
    else:
        possible = False
        break

# To consume A

while a_count:
    ans.append("A")
    a_count -= 1


# 3. TO SOLVE THE PROBLEM

if possible:
    print("".join(ans))
else:
    print(-1)