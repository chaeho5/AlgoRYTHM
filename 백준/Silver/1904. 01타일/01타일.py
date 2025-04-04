import sys
input = sys.stdin.readline

n = int(input())

memoi = [0] * 1000001
memoi[1] = 1
memoi[2] = 2

for i in range(3, n+1):
    memoi[i] = (memoi[i - 1] + memoi[i - 2]) % 15746
print(memoi[n])