'''
CF2057B - Gorilla and the Exam (https://codeforces.com/contest/2057/problem/B)

For an array A, f(A) is the number of distinct elements.
You can choose any element and change it to any integer at most K times.
Determine the smallest f(A) achievable after such replacements.  
'''

# TIME COMPLEXITY : O(TN log N)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length, change_count = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO COUNT EACH ELEMENTS
    
    count = {}
    for num in arr:
        if str(num) not in count:
            count[str(num)] = 1
        else:
            count[str(num)] += 1
    
    counts = list(count.values())
    counts.sort(reverse=True)
    
    
    # 3. TO SOLVE THE PROBLEM
    
    while len(counts) > 0 and change_count >= counts[-1]:
        change_used = counts.pop()
        change_count -= change_used
    
    print(max(1, len(counts)))