import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
dp = [[0] * (n+1) for _ in range(n + 1)]

hangryeol = []
r,c = map(int, input().split())
hangryeol.append(r)
hangryeol.append(c)
for _ in range(1, n):
    r, c = map(int, input().split())
    hangryeol.append(c)
#i와 j값이 같은 경우 baeyeol[i][j] = 0
for i in range(1, n+1):
    dp[i][i] = 0

for j in range(1, n+1):
    for i in range(j-1, 0, -1):
        min_value = INF
        for k in range(i,j) :
            temp_value = dp[i][k]+dp[k+1][j]+hangryeol[i-1]*hangryeol[k]*hangryeol[j]
            if min_value > temp_value :
                min_value = temp_value
        dp[i][j]= min_value
print(dp[i][n])

