import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

#dfs
dfs_visit = [False] * (n + 1)
dfs_result = []

def dfs(v):
    dfs_visit[v] = True
    dfs_result.append(v)

    for next_v in graph[v]:
        if not dfs_visit[next_v]:
            dfs(next_v)

#bfs
bfs_visit = [False] * (n + 1)
bfs_result = []

def bfs(start):
    queue = deque()
    queue.append(start)
    bfs_visit[start] = True

    while queue:
        current = queue.popleft()
        bfs_result.append(current)
        for next_start in graph[current]:
            if not bfs_visit[next_start]:
                queue.append(next_start)
                bfs_visit[next_start] = True

dfs(v)
bfs(v)

sys.stdout.write(" ".join(map(str, dfs_result)))
print()
sys.stdout.write(" ".join(map(str, bfs_result)))
