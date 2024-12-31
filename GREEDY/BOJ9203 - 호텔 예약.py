'''
BOJ9203 - Booking (https://www.acmicpc.net/problem/9203)

Given B bookings with the dates of departure and arrival, determine the minimum number of rooms to satisfy all bookings.
'''

# TIME COMPLEXITY : O(TB log B)

import sys, heapq


# 1. A FUNCTION TO CONVERT DATE TO NUMBER
# The number equals minutes passed from 2013-01-01 00:00.

def date_to_num(date, time):
    
    day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    result = 0
    
    year, month, day = map(int, date.split("-"))
    if year == 2016:
        day_in_month[2] += 1
    
    result += (year - 2013) * 365 * 24 * 60
    result += sum(day_in_month[:month]) * 24 * 60
    result += (day - 1) * 24 * 60
    
    hour, minute = map(int, time.split(":"))
    
    result += hour * 60
    result += minute
    
    return result


# 2. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    plan_count, clean_time = map(int, sys.stdin.readline().split())
    
    plans = []
    
    for plan in range(plan_count):
        
        id, start_date, start_time, end_date, end_time = sys.stdin.readline().strip().split()
        start_num = date_to_num(start_date, start_time)
        end_num = date_to_num(end_date, end_time) + clean_time
        
        plans.append((start_num, end_num))
    
    plans.sort()
    
    
    # 3. TO SOLVE THE PROBLEM
    # The problem is well-known as "Interval Partitioning" problem.

    heap = []
    
    for start, end in plans:
        
        if len(heap) == 0:
            heapq.heappush(heap, end)
        else:
            last_end = heapq.heappop(heap)
            if last_end <= start:
                heapq.heappush(heap, end)
            else:
                heapq.heappush(heap, last_end)
                heapq.heappush(heap, end)
    
    print(len(heap))