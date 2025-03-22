import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

queue = deque()
result = []

for _ in range(n):
    c = input().split()
    
    if c[0] == "push":
        queue.append(c[1])
        
    elif c[0] == "pop":
        if queue:
            result.append(queue.popleft())
        else:
            result.append("-1")

    elif c[0] == "size":
        result.append(str(len(queue)))

    elif c[0] == "empty":
        result.append("0" if queue else "1")

    elif c[0] == "front":
        result.append(queue[0] if queue else "-1")

    elif c[0] == "back":
        result.append(queue[-1] if queue else "-1")

sys.stdout.write("\n".join(result))
