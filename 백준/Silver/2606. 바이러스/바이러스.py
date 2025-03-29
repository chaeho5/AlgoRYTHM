from collections import deque
import sys
input = sys.stdin.readline

nod = int(input())
gan = int(input())

graph = []
for i in range(nod + 1):
    graph.append([])

visited = [False] * (nod + 1)

for _ in range(gan):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
bfs(graph, 1, visited)

result = sum(visited) - 1
print(result)
