n = int(input())

memoi =[0] * (n + 1)

if n == 0:
    print(0)  # F(0) = 0인 경우를 별도로 처리
    exit()
elif n == 1:
    print(1)  # F(1) = 1인 경우를 별도로 처리
    exit()


memoi[1] = 1
memoi[2] = 1

for i in range(3, n + 1):
    memoi[i] = memoi[i - 1] + memoi[i - 2]

print(memoi[n])