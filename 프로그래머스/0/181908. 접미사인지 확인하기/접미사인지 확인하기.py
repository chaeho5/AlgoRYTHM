def solution(my_string, is_suffix):
    suffix = []
    test = []
    for i in range(len(my_string)):
        suffix.append(my_string[i:])
        
    for ch in suffix:
        if ch == is_suffix:
            test.append(ch)
    
    if test:
        return 1
    else:
        return 0
