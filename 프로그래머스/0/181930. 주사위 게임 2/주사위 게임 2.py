def solution(a, b, c):
    result = 0
    if a == b == c :
        result += (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b != c or a == c != b or b == c != a:
        result += (a + b+ c) * (a**2 + b**2 + c**2)
    else :
        result += a + b+ c
    

    return result
        