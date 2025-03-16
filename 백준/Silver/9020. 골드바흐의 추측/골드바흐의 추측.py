import sys, math
input = sys.stdin.readline

def sosu(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    goldbach = n//2
    while goldbach > 1:
        if sosu(goldbach) and sosu(n-goldbach):
            print(goldbach, n-goldbach)
            break
        goldbach -= 1