def solution(my_string, m, c):
    arr = []
    for i in range(0, len(my_string), m):
        piece = my_string[i: i+m]
        arr.append(piece)
    
    result = ""
    
    for i in range(len(arr)):
        result += arr[i][c - 1]
        
            
    return(result)
    