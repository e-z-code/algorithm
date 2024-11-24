'''
BOJ11626 - Physical Music (https://www.acmicpc.net/problem/11626)

You are given two charts: one based on both CD singles and downloads and another based purely on the downloads.
Determine singles that are available as CD singles.
'''

# TIME COMPLEXITY : O(TN)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    song_count = int(sys.stdin.readline())
    
    
    # 2. TO SOLVE THE PROBLEM
    # Let S be a song, T(S) be its rank in the Single Top 100, and D(S) be its rank in the download top 100.
    # If X exists such that T(S) < T(X) and D(S) > D(X), S is available as CD single.
    
    ans = [0 for download_rank in range(song_count + 1)]
    stack = []
    
    for total_rank in range(1, song_count + 1):
        download_rank = int(sys.stdin.readline())
        while len(stack) != 0 and stack[-1] > download_rank:
            ans[stack.pop()] = 1
        stack.append(download_rank)
    
    print(sum(ans))
    for song in range(1, song_count + 1):
        if ans[song] == 1:
            print(song)