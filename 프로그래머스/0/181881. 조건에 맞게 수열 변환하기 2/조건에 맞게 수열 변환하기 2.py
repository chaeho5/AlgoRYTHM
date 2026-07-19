def solution(arr):
    result = 0
    
    while True:
        before = arr[:]
        for i in range(len(arr)): 
            if (arr[i] >= 50) and (arr[i] % 2 == 0):
                arr[i] = arr[i] // 2
            elif (arr[i] < 50) and (arr[i] % 2 == 1):
                arr[i] = arr[i] * 2 + 1
        
        if arr == before:
            break
            
        result += 1
        
    return result
        