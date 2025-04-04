n, k = map(int, input().split())

cash = []
for _ in range(n):
    dongjun = int(input())
    cash.append(dongjun)
cash.sort(reverse=True)

result = 0
for coin in cash:
    if coin <= k:
        result += k//coin
        k %= coin
        if k <= 0:
            break

print(result)

    