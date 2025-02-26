'''
BOJ4159 - Alaska (https://www.acmicpc.net/problem/4159)

Your car can travel up to 200 miles once charged at a station.
You are now at Dawson Creek and want to drive to Delta Junction and return.
Delta Junction is 1422 miles far from Dawson Creek.
Determine if your trip is possible.
'''

# TIME COMPLEXITY : O(TN log N)

import sys


# 1. TO GET THE INPUT

while True:
    
    station_count = int(sys.stdin.readline())
    if station_count == 0:
        break
    
    stations = []
    for station in range(station_count):
        loc = int(sys.stdin.readline())
        stations.append(loc)
        stations.append(2844 - loc)
    
    stations.sort()
    
    
    # 2. TO SOLVE THE PROBLEM
    
    possible = True
    
    for idx in range(1, len(stations)):
        
        if stations[idx] - stations[idx-1] > 200:
            possible = False
    
    if possible:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")