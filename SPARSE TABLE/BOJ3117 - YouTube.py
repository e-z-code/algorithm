'''
BOJ3117 - YouTube (https://www.acmicpc.net/problem/3117)

N students are watching one of K popular videos.
Every minute, every student picks the next video from the top of the recommendation list.
Determine for each student which video the student will watch after M minutes.
'''

# TIME COMPLEXITY : O(max(K, N) log M)

import sys


# 1. TO GET THE INPUT

student_count, video_count, time_left = map(int, sys.stdin.readline().split())
init_video = list(map(int, sys.stdin.readline().split()))
next_video = list(map(int, sys.stdin.readline().split()))


# 2. SPARSE TABLE

parent = [[-1 for exp in range(31)] for video in range(video_count)]

for video in range(video_count):
    parent[video][0] = next_video[video] - 1

for exp in range(1, 31):
    for video in range(video_count):
        if parent[video][exp-1] != -1:
            parent[video][exp] = parent[parent[video][exp-1]][exp-1]


# 3. TO SOLVE THE PROBLEM

for student in range(student_count):
    
    now_video = init_video[student] - 1
    now_time_left = time_left - 1
    
    for exp in range(31, -1, -1):
        if now_time_left >= (1 << exp):
            now_video = parent[now_video][exp]
            now_time_left -= (1 << exp)
    
    print(now_video + 1, end = ' ')