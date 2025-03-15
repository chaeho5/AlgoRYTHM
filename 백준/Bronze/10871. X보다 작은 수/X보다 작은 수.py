import sys
N, X = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = [str(num) for num in numbers if num < X]
print(" ".join(result))