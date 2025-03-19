import sys

# 입력받기
n = int(sys.stdin.readline())
count = [0] * 10001  # 숫자는 1부터 10,000까지 존재

# 입력받은 숫자 세기
for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

# 결과 출력
for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)

