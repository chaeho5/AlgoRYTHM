import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, a = map(int, input().split())

distance = [INF] * (n + 1)

def dijk(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, nod = heapq.heappop(queue)

        if distance[nod] < dist:
            continue
        
        for i in graph[nod]:
            next_dis = dist + i[1]
            if next_dis < distance[i[0]]:
                distance[i[0]] = next_dis
                heapq.heappush(queue, (next_dis, i[0]))

dijk(s)
print(distance[a])