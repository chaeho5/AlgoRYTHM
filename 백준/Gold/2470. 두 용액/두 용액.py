import sys
input = sys.stdin.readline


n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
l, r = 0, n - 1

ysum = float('inf')
yong1, yong2 = 0, 0

while l<r:
    mid = liquids[l] + liquids[r]

    if abs(mid) < ysum:
        ysum = abs(mid)
        yong1, yong2 = liquids[l], liquids[r]

    if mid < 0:
        l += 1
    elif mid > 0:
        r -= 1
    else:
        yong1, yong2 = liquids[l], liquids[r]
        break
print(yong1, yong2)