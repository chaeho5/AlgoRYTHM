t = int(input())
results = [sum(map(int, input().split())) for _ in range(t)]
print("\n".join(map(str, results)))
