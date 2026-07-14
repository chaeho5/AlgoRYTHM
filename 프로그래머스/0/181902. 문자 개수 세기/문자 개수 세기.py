def solution(my_string):
    result = [0] * 52
    
    for ch in my_string:
        if 'A' <= ch <= 'Z':
            bignum = ord(ch) - ord('A')
            result[bignum] += 1
        else:
            smallnum = ord(ch) - ord('a') + 26
            result[smallnum] += 1
    return result
        
    