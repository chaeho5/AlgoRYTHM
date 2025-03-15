def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
numbers = list(map(int, input().split()))

prime_count = 0
for number in numbers:
    if is_prime(number):
        prime_count += 1

print(prime_count)
