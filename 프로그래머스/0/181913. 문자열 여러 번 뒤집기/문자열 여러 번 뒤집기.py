def solution(my_string, queries):
    result = ""
    arr = list(my_string)
    for s, e in queries:
        arr[s:e+1] = arr[s:e+1][::-1]
    
    result = ''.join(arr)
        
        
    return result