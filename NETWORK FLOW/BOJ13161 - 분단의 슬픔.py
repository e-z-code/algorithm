import sys
from collections import deque
inf = float('inf')


# 2. DFS FOR DINITZ

def dinitz_dfs(now_node, now_flow):
    
    if now_node == partyB:
        return now_flow
    
    idx = check[now_node]
    while idx < len(graph[now_node]):
        next_node = graph[now_node][idx]
        if level[next_node] == level[now_node] + 1 and capacity[now_node][next_node] - flow[now_node][next_node] > 0:
            max_flow = dinitz_dfs(next_node, min(now_flow, capacity[now_node][next_node] - flow[now_node][next_node]))
            if max_flow > 0:
                flow[now_node][next_node] += max_flow
                flow[next_node][now_node] -= max_flow
                check[now_node] = idx
                return max_flow
        idx += 1

    check[now_node] = idx
    return 0


# 1. TO GET THE INPUT AND CONSTRUCT THE GRAPH

member_count = int(sys.stdin.readline())
partyA = member_count
partyB = member_count + 1

graph = {}
for node in range(member_count + 2):
    graph[node] = []

capacity = [[0 for j in range(member_count + 2)] for i in range(member_count + 2)]
flow = [[0 for j in range(member_count + 2)] for i in range(member_count + 2)]

is_party = list(map(int, sys.stdin.readline().split()))
for member in range(member_count):
    if is_party[member] == 1:
        graph[partyA].append(member)
        graph[member].append(partyA)
        capacity[partyA][member] = inf
    elif is_party[member] == 2:
        graph[partyB].append(member)
        graph[member].append(partyB)
        capacity[member][partyB] = inf

for i in range(member_count):
    cost = list(map(int, sys.stdin.readline().split()))
    for j in range(member_count):
        if cost[j] != 0:
            graph[i].append(j)
            graph[j].append(i)
            capacity[i][j] = cost[j]
            capacity[j][i] = cost[j]


# 3. DINITZ ALGORITHM
# The maximum flow is equal to the minimum cut cost. (Min-cut Max-flow theorem)

ans = 0

while True:
    
    # BFS to find paths and construct a level graph
    
    level = [-1 for node in range(member_count + 2)]
    level[partyA] = 0
    
    queue = deque([partyA])
    while queue:
        now_node = queue.popleft()
        for next_node in graph[now_node]:
            if level[next_node] == -1 and capacity[now_node][next_node] - flow[now_node][next_node] > 0:
                level[next_node] = level[now_node] + 1
                queue.append(next_node)
    
    if level[partyB] == -1:
        break
    
    # DFS to add flow
    
    check = [0 for node in range(member_count + 2)]
    
    while True:
        
        added_flow = dinitz_dfs(partyA, inf)
        if added_flow == 0:
            break
        ans += added_flow


# 4. TO SOLVE THE PROBLEM

visited = [0 for idx in range(member_count + 2)]

queue = deque([partyA])
visited[partyA] = 0

while queue:
    now_node = queue.popleft()
    for next_node in graph[now_node]:
        if visited[next_node] == 0 and capacity[now_node][next_node] - flow[now_node][next_node] > 0:
            visited[next_node] = 1
            queue.append(next_node)

print(ans)
for node in range(member_count):
    if visited[node] == 1:
        print(node + 1, end = ' ')
print()
for node in range(member_count):
    if visited[node] == 0:
        print(node + 1, end = ' ')
print()