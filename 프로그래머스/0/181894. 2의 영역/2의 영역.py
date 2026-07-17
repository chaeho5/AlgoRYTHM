def solution(arr):
    result = []
    index = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            index.append(i)
    
    if index:
        for a in arr[index[0]: index[-1] + 1]:
            result.append(a)
        return result
    
    if not index:
        result.append(-1)
        return result
        