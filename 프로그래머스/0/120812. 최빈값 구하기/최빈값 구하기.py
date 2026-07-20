def solution(array):
    count = {}
    result = []
    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    maxvalue = max(count.values())
    maxkey = max(count, key=count.get)
    
    for key, value in count.items():
        if value == maxvalue:
            result.append(key)
            
    if len(result) >= 2:
        return -1
    else:
        return maxkey
        