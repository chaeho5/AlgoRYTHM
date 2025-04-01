import sys
from collections import deque

input = sys.stdin.readline

#
n, m = map(int, input().split())

# 
graph = []
for i in range(n + 1):
    graph.append([])

#
indegree = [0] * (n + 1)

#
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 
queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

# 
result = []

# 
while queue:
    current = queue.popleft()
    result.append(current)

    for neighbor in graph[current]:
        indegree[neighbor] -= 1
        # 

        if indegree[neighbor] == 0:
            queue.append(neighbor)
#
print(" ".join(map(str, result)))
