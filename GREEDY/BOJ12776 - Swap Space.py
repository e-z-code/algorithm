'''
BOJ12776 - Swap Space (https://www.acmicpc.net/problem/12776)

There are N drives currently in use and filled with important data.
You want to reformat all drives without losing any of the data.
Reformatting a drive may significantly change the capacity.
Determine the minimum size of extra storage needed.
'''

# TIME COMPLEXITY : O(N log N)

import sys


# 1. TO GET THE INPUT

drive_count = int(sys.stdin.readline())

better_drives = []
worse_drives = []

for drive in range(drive_count):
    
    old_size, new_size = map(int, sys.stdin.readline().split())
    
    if old_size <= new_size:
        better_drives.append((old_size, new_size))
    else:
        worse_drives.append((old_size, new_size))


# 2. TO SOLVE THE PROBLEM
# The greedy can be proved using exchange argument.

ans = 0
free_size = 0

# To increase the size

better_drives.sort(key = lambda x : x[0])

for old_size, new_size in better_drives:
    
    if free_size < old_size:
        ans += old_size - free_size
        free_size += old_size - free_size
    free_size += new_size - old_size

# To decrease the size

worse_drives.sort(key = lambda x : -x[1])

for old_size, new_size in worse_drives:
    
    if free_size < old_size:
        ans += old_size - free_size
        free_size += old_size - free_size
    free_size += new_size - old_size

print(ans)
