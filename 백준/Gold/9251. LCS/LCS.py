import sys
input = sys.stdin.readline

n = list(input().strip())
m = list(input().strip())

lcs = [[0] * (len(m)+1) for _ in range(len(n) + 1)]

for i in range(1, len(n)+1):
    for j in range(1, len(m)+1):     
        if n[i - 1] == m[j - 1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[i][j])