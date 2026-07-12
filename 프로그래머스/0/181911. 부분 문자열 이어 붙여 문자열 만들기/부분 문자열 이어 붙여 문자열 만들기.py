def solution(my_strings, parts):
    result = ""
    for i in range(len(my_strings)):
        s = parts[i][0]
        e = parts[i][1]
        
        sli = my_strings[i][s:e+1]
        
        result += sli
        
    return result
        
        
        