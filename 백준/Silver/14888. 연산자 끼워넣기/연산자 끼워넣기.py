import sys
input = sys.stdin.readline
#입력
n = int(input())
num = list(map(int, input().split()))
plus, minus, multi, divi = map(int, input().split())
#최댓값 최솟값 초기화
max_value = float('-inf')
min_value = float('inf')
#백트래킹 알고리즘
def backtrack(idx, result, plus, minus, multi, divi):
    global max_value, min_value
    #모든 숫자를 사용한 경우 최댓값과 최솟값 갱신
    if idx == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    
    #덧셈 연산자 사용
    if plus > 0:
        backtrack(idx + 1, result + num[idx], plus - 1, minus, multi, divi)
    #뺄셈 연산자 사용
    if minus > 0:
        backtrack(idx + 1, result - num[idx], plus, minus - 1, multi, divi)
    #곱셈 연산자 사용
    if multi > 0:
        backtrack(idx + 1, result * num[idx], plus, minus, multi - 1, divi)
    #나눗셈 연산자 사용
    if divi > 0:
        #나눗셈 연산은 음수를 양수로 나눌 때와 같은 효과를 가지지 않으므로 주의
        if result < 0:
            backtrack(idx + 1, -(-result // num[idx]), plus, minus, multi, divi - 1)
        else:
            backtrack(idx + 1, result // num[idx], plus, minus, multi, divi - 1)
#백트래킹 알고리즘 호출
backtrack(1, num[0], plus, minus, multi, divi)

#결과 출력
print(max_value)
print(min_value)