'''
BOJ25970 - Hyundai Mobis Air Suspension (https://www.acmicpc.net/problem/25970)

There are B highness substrings and B lowness substrings.
Given N data, calculate the difference in the occurrence of highness substrings and lowness substrings for each data.
'''

# TIME COMPLEXITY : O(NX^3) [X = The length of the longest data]

import sys


# 1. TO GET THE INPUT

key_count = int(sys.stdin.readline())

low_keys = set()
high_keys = set()

for low_key in range(key_count):
    low_keys.add(sys.stdin.readline().strip())
for high_key in range(key_count):
    high_keys.add(sys.stdin.readline().strip())


# 2. TO COUNT THE OCCURRENCE

data_count = int(sys.stdin.readline())

for data in range(data_count):

    now_data = sys.stdin.readline().strip()
    
    low_count = 0
    high_count = 0
    
    for i in range(len(now_data)):
        for j in range(i, len(now_data)):
            now_substring = now_data[i:j+1]
            if now_substring in low_keys:
                low_count += 1
            if now_substring in high_keys:
                high_count += 1


    # 3. TO SOLVE THE PROBLEM

    result = high_count - low_count

    if result > 0:
        print("LOW", result)
    elif result == 0:
        print("GOOD")
    else:
        print("HIGH", abs(result))