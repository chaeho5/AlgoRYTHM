import sys
input = sys.stdin.readline

gusreum = int(input())

count = 0
while gusreum > 0:

    if gusreum % 5 == 0 :
        count += gusreum//5
        gusreum = 0
    else:
        gusreum -= 2
        count += 1
        
if gusreum == 0:
    print(count)
else:
    print(-1)
