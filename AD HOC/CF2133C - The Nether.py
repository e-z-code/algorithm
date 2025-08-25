'''
CF2133C - Villagers (https://codeforces.com/contest/2133/problem/C)

There is a DAG of length N.
You can ask Steve a query with set of nodes and starting point.
Then, Steve will answer the distance of the longest path starting from the starting point only passes through the nodes in given set.
Find the longest path using at most 2N queries.
'''

# TIME COMPLEXITY : O(TN)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    node_count = int(sys.stdin.readline())
    
    
    # 2. TO FIND THE MAXIMUM LENGTH FROM EACH NODE
    
    count = [[] for max_length in range(node_count + 1)]
    
    nodes = [str(node) for node in range(1, node_count + 1)]
    for node in range(1, node_count + 1):
        print("?", node, node_count, " ".join(nodes))
        sys.stdout.flush()
        max_length = int(sys.stdin.readline())
        count[max_length].append(str(node))
    
    
    # 3. TO SOLVE THE PROBLEM
    
    ans = []
    
    now_idx = node_count
    while now_idx != 0:
        if len(count[now_idx]) == 0:
            now_idx -= 1
        else:
            if len(ans) == 0:
                ans.append(count[now_idx][0])
            else:
                for node in count[now_idx]:
                    print("?", ans[-1], 2, ans[-1], node)
                    sys.stdout.flush()
                    max_length = int(sys.stdin.readline())
                    if max_length == 2:
                        ans.append(node)
                        break
            now_idx -= 1
    
    print("!", len(ans), " ".join(ans))
    sys.stdout.flush()