'''
CF2132E - Arithmetics Competition (https://codeforces.com/contest/2132/problem/E)

You have N cards and I have M cards.
In each of the Q rounds, three integers are given: X, Y, and Z.
That is, you and I will choose Z cards while you can choose no more than X cards and I can choose no more than Y cards.
Determine the highest possible sum for each of the Q rounds.
'''

# TIME COMPLEXITY : O(max(N, M) log max(N, M) + Q log X)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    lengthA, lengthB, round_count = map(int, sys.stdin.readline().split())
    
    cardsA = list(map(int, sys.stdin.readline().split()))
    cardsB = list(map(int, sys.stdin.readline().split()))
    cardsA.sort(reverse=True)
    cardsB.sort(reverse=True)
    
    
    # 2. PREFIX SUM
    
    prefixA = [0]
    for idx in range(lengthA):
        prefixA.append(prefixA[-1] + cardsA[idx])
    
    prefixB = [0]
    for idx in range(lengthB):
        prefixB.append(prefixB[-1] + cardsB[idx])
    
    
    # 3. TO SOLVE THE PROBLEM - BINARY SEARCH ON HOW MANY CARDS YOU WILL CHOOSE
    
    for round in range(round_count):
        
        countA, countB, count_total = map(int, sys.stdin.readline().split())
        
        left = max(0, count_total - countB)
        right = min(countA, count_total)
        
        while left + 1 < right:
            
            choiceA = (left + right) // 2
            choiceB = count_total - choiceA
            
            if choiceA < lengthA and 0 < choiceB and cardsA[choiceA] > cardsB[choiceB - 1]:
                left = choiceA
            elif 0 < choiceA and choiceB < lengthB and cardsA[choiceA - 1] < cardsB[choiceB]:
                right = choiceA
            else:
                left = choiceA
                break
        
        print(max(prefixA[left] + prefixB[count_total - left], prefixA[right] + prefixB[count_total - right]))