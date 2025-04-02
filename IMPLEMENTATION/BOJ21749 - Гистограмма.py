'''
BOJ21749 - Histogram (https://www.acmicpc.net/problem/21749)

Given a paragraph, show the occurrences of each character as a histogram.
'''

# TIME COMPLEXITY : O(X) [X : Length of the paragraph]

# 1. TO GET THE INPUT

count_dict = {}

while True:
    try:
        line = list(input().split())
        for word in line:
            for char in word:
                count_dict[char] = count_dict.get(char, 0) + 1
    except:
        break


# 2. TO SORT THE OCCURRENCE

count = []
max_count = 0

for char in count_dict.keys():
    count.append((char, count_dict[char]))
    max_count = max(max_count, count_dict[char])

count.sort()


# 3. TO SOLVE THE PROBLEM

ans = [[" " for col in range(len(count))] for row in range(max_count + 1)]

for col in range(len(count)):
    
    char, char_count = count[col]
    
    ans[max_count][col] = char
    for row in range(max_count-1, max_count-1-char_count, -1):
        ans[row][col] = "#"

for row in ans:
    print("".join(row))