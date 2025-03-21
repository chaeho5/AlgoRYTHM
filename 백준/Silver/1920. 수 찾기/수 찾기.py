import sys

input = sys.stdin.readline

# N: 배열 A의 길이
N = int(input().strip())
A = list(map(int, input().split()))
A.sort()

# M: 확인할 수의 개수, B: 확인할 수들의 리스트
M = int(input().strip())
B = list(map(int, input().split()))

def search(a, b):
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr)//2
        if a[pc] == b:
            return pc
        elif a[pc] < b:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1

for b in B:
    if search(A, b) != -1:
        print(1)
    else:
        print(0)