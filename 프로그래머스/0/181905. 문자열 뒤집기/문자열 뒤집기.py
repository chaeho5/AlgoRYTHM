def solution(my_string, s, e):
    
    one = my_string[0:s]
    two = my_string[s:e + 1]
    three = my_string[e + 1:]
    
    reverse_two = two[::-1]
    
    result = one + reverse_two + three
    
    return result