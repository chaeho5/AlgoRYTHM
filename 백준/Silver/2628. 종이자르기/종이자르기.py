import sys
input = sys.stdin.readline

# 첫 줄 입력 - 가로 길이, 세로 길이
GaroCm, SeroCm = map(int,input().split())
# 두번째 줄 입력 - 잘라야 할 점선의 갯수
n = int(input())
# 입력 받은 가로 길이
G = [0, GaroCm]
# 입력 받은 세로 길이
S = [0, SeroCm]

# 0이면 가로 1이면 세로 입력 각각 리스트 저장
for _ in range(n):
    GaroSero, JB = map(int,input().split())
    if GaroSero == 0:
        S.append(JB)
    elif GaroSero == 1:
        G.append(JB)
# 계산하기 좋게 오름차순 정렬
G.sort()
S.sort()

# 맨 뒤에 -1은 범위를 넘어가지 않게하기 위함, 오름 차순으로 정렬 된 리스트에서 숫자가 더 큰 뒷 부분에서 앞 부분을 뺌
# len을 이용하여 리스트의 길이만큼 반복
max_G = max(G[i + 1] - G[i] for i in range(len(G)-1))
max_S = max(S[i + 1] - S[i] for i in range(len(S)-1))
max_G*max_S
print(max_G*max_S)



