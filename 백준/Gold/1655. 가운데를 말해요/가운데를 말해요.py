import sys
import heapq
input = sys.stdin.readline

n = int(input())
lhip = []
rhip = []

for _ in range(n):
    k = int(input())

    if not lhip or k <= -lhip[0]:
        heapq.heappush(lhip, -k)
    else:
        heapq.heappush(rhip, k)


    if len(lhip) > len(rhip) + 1:
        heapq.heappush(rhip, -heapq.heappop(lhip))
    elif len(lhip) < len(rhip):
        heapq.heappush(lhip, -heapq.heappop(rhip))

    print(-lhip[0])