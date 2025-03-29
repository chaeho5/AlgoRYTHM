import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n + 1):
    graph.append([])

for _ in range(n - 1):
    fn, sn = map(int, input().split())
    graph[fn].append(sn)
    graph[sn].append(fn)

visited = [0] * (n + 1)

def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

dfs(1)

for x in range(2, n + 1):
    print(visited[x])
