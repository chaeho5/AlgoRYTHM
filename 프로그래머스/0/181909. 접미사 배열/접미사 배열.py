def solution(my_string):
    result = []
    
    for i in range(len(my_string)):
        sli = my_string[i:]
        result.append(sli)
        result.sort()
        
    return result