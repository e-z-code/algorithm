'''
BOJ29598 - Two Endian (https://www.acmicpc.net/problem/29598)

Given a number in Big Endian, determine its value in Small Endian.
'''

# TIME COMPLEXITY : O(log N)

import sys


# 1. TO GET THE INPUT

num = int(sys.stdin.readline())


# 2. STORE BYTE VALUES

bytes = []
now = pow(2, 16)
while now != 0:
    bytes.append(num // now)
    num %= now
    now //= 256

while len(bytes) != 0 and bytes[0] == 0:
    bytes.pop(0)


# 3. TO SOLVE THE PROBLEM

ans = 0
for idx in range(len(bytes)):
    ans += bytes[idx] * pow(256, idx)
print(ans)