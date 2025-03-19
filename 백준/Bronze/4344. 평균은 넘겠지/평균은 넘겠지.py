import sys
C = int(sys.stdin.readline())

for _ in range(C):
    jumsoo = list(map(int, sys.stdin.readline().split()))
    N = jumsoo[0]
    student_jumsoo = jumsoo[1:]
    average = sum(student_jumsoo) / N 

    count = sum(1 for jumsoo in student_jumsoo if jumsoo > average)
    percentage = (count / N) * 100 

    print(f"{percentage:.3f}%")