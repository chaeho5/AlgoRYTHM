def solution(l, r):
    result = []
    for num in range(l, r+1):
        valid = True

        for ch in str(num):
            if ch != "5" and ch != "0":
                valid = False
                break
        
        if valid :
            result.append(num)
            
    if len(result) == 0:
        return [-1]
        
    return result