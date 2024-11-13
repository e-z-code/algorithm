'''
BOJ1214 - Cool Purchase (https://www.acmicpc.net/problem/1214)

You have an infinite amount of P cents and Q cents coins.
You want to buy an apple of D cents.
Determine the minimum price you need to pay.
'''

# TIME COMPLEXITY : O(min(max(P, Q) / D, min(P, Q)))

import sys
inf = float('inf')


# 1. TO GET THE INPUT

cost, coinA, coinB = map(int, sys.stdin.readline().split())

# Make coinA >= coinB
if coinA < coinB: 
    coinA, coinB = coinB, coinA


# 2. TO SOLVE THE PROBLEM

ans = inf
checked = set()

totalA = 0
while totalA <= cost:
    
    # If the remainder is checked, every calculation from that point is already checked.
    # Note that the remainder R satisfies 0 <= R < coinB.
    if (cost - totalA) % coinB in checked:
        break
    else:
        checked.add((cost - totalA) % coinB)
    
    # Otherwise, calculate the price you need to pay.
    # This will repeated at most cost / totalA + 1 times. 
    totalB = ((cost - totalA) // coinB) * coinB
    if (cost - totalA) % coinB != 0:
        totalB += coinB
    
    if ans > totalA + totalB:
        ans = totalA + totalB

    totalA += coinA

if cost < totalA < ans:
    ans = totalA

print(ans)