def solution(num_list):
    sum_result = 0
    gob_result = 1
    for i in range(len(num_list)):
        if len(num_list) >= 11:
            sum_result += num_list[i]
        else:
            gob_result *= num_list[i]
    
    if len(num_list) >= 11:
        return sum_result
    else:
        return gob_result
    