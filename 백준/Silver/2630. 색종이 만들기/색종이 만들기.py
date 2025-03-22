import sys
input = sys.stdin.readline

#입력 예제 부분
n = int(input())
paper = []
white, blue = 0, 0

for _ in range(n):
    p = list(map(int, input().split()))
    paper.append(p)

def four(x,y,n): #x,y좌표, n은 변
    global white, blue
    color = paper[x][y] #첫 색
        #탐색 시작
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                four(x, y, n//2)
                four(x, y+n//2, n//2)
                four(x+n//2, y, n//2)
                four(x+n//2, y+n//2, n//2)
                return
        
    if color == 1:
        blue += 1
    else:
        white += 1

#출력
four(0, 0, n)

print(white)
print(blue)

