import sys
input = sys.stdin.readline

n = int(input())

hansoo = 0

for i in range(1, n+1):
    if 0 < i < 100:
        hansoo += 1
    else:
        o = i % 10
        t = (i//10) % 10
        h = i // 100
        if (h-t) == (t-o):
            hansoo += 1

print(hansoo)