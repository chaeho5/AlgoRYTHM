import sys
import heapq

v, e = map(int, input().split())

graph = {}
for i in range(v):#정점 개수
    graph[i] = []

for _ in range(e):#간선 개수
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))


queue = []
mst_weight = 0
visited = [False] * v

heapq.heappush(queue,(0, 0))

while queue:
    weight, vtx = heapq.heappop(queue)
    if not visited[vtx]:
        visited[vtx] = True
        mst_weight += weight

        for v, w in graph[vtx]:
            if not visited[v]:
                heapq.heappush(queue, (w, v))
 
print(mst_weight)