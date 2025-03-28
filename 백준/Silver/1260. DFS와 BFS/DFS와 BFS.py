import sys
from collections import deque

input = sys.stdin.readline
#n = 정점 개수, m = 간선 개수, v = 정점 번호
n, m, v = map(int, input().split())

#그래프 초기화
graph = []
for i in range(n+1):
    graph.append([])

#간선 정보 저장(양방향)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#그래프 오름차순 정렬
for i in range(1, n + 1):
    graph[i].sort()

#dfs
dfs_visited = [False] * (n + 1)
dfs_result = [] #방문한 결과값을 저장

def dfs(vtx):
    dfs_visited[vtx] = True
    dfs_result.append(vtx)

    for next_vtx in graph[vtx]:
        if not dfs_visited[next_vtx]:
            dfs(next_vtx)

#bfs
bfs_visited = [False] * (n + 1)
bfs_result = []

def bfs(start):
    queue = deque()
    queue.append(start) #시작 좌표
    bfs_visited[start] = True

    while queue:
        current = queue.popleft()
        bfs_result.append(current)
        
        for next_vtx in graph[current]:
            if not bfs_visited[next_vtx]:
                queue.append(next_vtx)
                bfs_visited[next_vtx] = True

dfs(v)
bfs(v)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))