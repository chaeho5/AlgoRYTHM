import sys
input = sys.stdin.readline

n, c = map(int, input().split())
homes = []
for _ in range(n):
    homes.append(int(input()))
homes.sort()

din, dax = 1, homes[-1] - homes[0]
result = 0

while din <= dax:
    mid = (din + dax) //2
    count = 1
    lasthome = homes[0]

    for i in range(1, len(homes)):
        if homes[i] - lasthome >= mid:
            count += 1
            lasthome = homes[i]

    if count >= c:
        result = mid
        din = mid + 1
    else:
        dax = mid -1
print(result)