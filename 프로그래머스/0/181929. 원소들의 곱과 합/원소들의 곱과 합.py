def solution(num_list):
    sum=0
    double=0
    gob=1
    for i in range(len(num_list)):
        sum += num_list[i]
        double = sum ** 2
        gob *= num_list[i]
        if gob < double:
            result = 1
        elif gob > double:
            result = 0
            
    return result
            