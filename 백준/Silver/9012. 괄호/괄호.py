t = int(input())

for _ in range(t):
    g = input()
    stack = []

    for i in g:
        if i =='(':
           stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")