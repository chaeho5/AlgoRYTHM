import sys
input = sys.stdin.readline

n = int(input())

heighter = []

for _ in range(n):
    heighter.append(int(input()))

heightest = 0
cansee = 0

for height in heighter[::-1]:
    if height > heightest:
        cansee += 1
        heightest = height

print(cansee)
