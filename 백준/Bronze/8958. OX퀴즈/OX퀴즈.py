import sys
N = int(sys.stdin.readline())


for _ in range(N):
    result = sys.stdin.readline()
    score = 0
    consecutive = 0 

    for char in result:
        if char == 'O':
            consecutive += 1
            score += consecutive  
        else:
            consecutive = 0

    print(score)