def solution(a, b):
    sum = int(str(a) + str(b))
    gob = 2*a*b
    
    return max(sum, gob)