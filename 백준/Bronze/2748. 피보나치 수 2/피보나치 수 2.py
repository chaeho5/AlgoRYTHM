#저장할 배열 만들고
n = int(input())

memoi = [0] * (n + 1)

def fibo(n):
    if n == 1 or n == 2:
        return 1
    if memoi[n] != 0: #memoi배열이 0이 아니라면, 이미 계산했던 과정이라는 뜻이므로 저장된 값 반환
        return memoi[n]
    memoi[n] = fibo(n - 1) + fibo(n - 2)
    return memoi[n]

print(fibo(n))