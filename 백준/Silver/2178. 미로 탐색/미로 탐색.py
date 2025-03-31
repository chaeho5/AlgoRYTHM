import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, list(input().rstrip()))))
queue = deque([(0, 0)])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if miro[nx][ny] == 1:
                queue.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1

print(miro[n - 1][m - 1])