def solution(number):
    result = 0
    
    for num in number:
        result += int(num)
    
    return result % 9