import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n = int(input())

miro = []
for _ in range(n):
    miro.append(list(map(int, list(input().strip()))))

queue = deque([(0, 0)])

dx =[0, 0, -1 , 1]
dy =[-1, 1, 0, 0]

wall = [[INF] * n for _ in range(n)]
wall[0][0] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0 <= ny < n:
            if miro[nx][ny] == 1 and wall[nx][ny] > wall[x][y]:
                wall[nx][ny] = wall[x][y]
                queue.appendleft((nx, ny))
            elif miro[nx][ny]== 0 and wall[nx][ny] > wall[x][y] + 1:
                wall[nx][ny] = wall[x][y] + 1
                queue.append((nx, ny))

print(wall[n-1][n-1])