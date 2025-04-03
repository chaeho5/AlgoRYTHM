import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    wall = list(input().strip())
    graph.append(wall)
visited = [[False] * m for _ in range(n)]
count = 0 

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            count += 1
            if graph[i][j] == '-':
                k = j          
                while k < m and graph[i][k] == '-':
                    visited[i][k] = True
                    k += 1
                    
            else:
                k = i
                while k < n and graph[k][j] == '|':
                    visited[k][j] = True
                    k += 1
print(count)