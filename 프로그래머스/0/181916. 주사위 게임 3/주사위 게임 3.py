def solution(a, b, c, d):
    count = {}
    
    for num in [a, b, c, d]:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    if len(count) == 1:
        return a * 1111
    
    if len(count) == 2:
        nums = list(count.keys())
        p = nums[0]
        q = nums[1]
        
        if count[p] == 3:
            return (10 * p + q) ** 2
        elif count[q] == 3:
            return (10 * q + p) ** 2
        elif count[p] == 2 and count[q] == 2:
            return (p + q) * abs(p - q)
    
    if len(count) == 3:
        result = 1
        
        for num in count:
            if count[num] == 1:
                result *= num
        return result
    
    if len(count) == 4:
        return min(a, b, c, d)
        
    