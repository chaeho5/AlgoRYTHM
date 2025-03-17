import sys
input = sys.stdin.readline

n = int(input())

numbers = []

for _ in range(n):
    numbers.append(int(input()))

s_numbers = sorted(numbers)

for number in s_numbers:
    print(number)