import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

queue = deque() 

basic_parts = [[0] * (n + 1) for _ in range(n + 1)] 


degree = [0] * (n + 1) 


graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    degree[x] += 1


for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)


while queue:

    now = queue.popleft()
    for next, next_part in graph[now]: 
        if basic_parts[now].count(0) == n + 1: 
            basic_parts[next][now] += next_part
        
        else:
            for i in range(1, n + 1):
                basic_parts[next][i] += basic_parts[now][i] * next_part
        
      
        degree[next] -= 1
        if degree[next] == 0:
            queue.append(next)
for i in range(len(basic_parts[n])):
    if basic_parts[n][i]:
        print(i, basic_parts[n][i])
