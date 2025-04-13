import sys
input = sys.stdin.readline

#학생들의 수 입력
n = int(input())
#임시로 나와있을 stack
stack = []
#승환이 앞에 서 있는 n명의 학생 번호표
stud = list(map(int, input().split()))
#1번 부터 오름차순으로 받아야 함
target = 1

while stack or stud:#순서대로 처리 되면 'Nice'출력
    #학생이 타겟과 같으면 간식을 받은 것으로 간주하고 pop하면서 target +1
    if stud and stud[0] == target:
        stud.pop(0)
        target += 1
    elif stack and stack[-1] == target:
        stack.pop()
        target += 1
    elif stud and stud[0] != target:
        stack.append(stud.pop(0))
    else:
        #이 중에 포함 되는 조건이 없으면 'SAD' 출력력
        print('Sad')
        sys.exit()

print('Nice')