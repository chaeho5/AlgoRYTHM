def solution(num_list):
    holsum = ''
    jjaksum = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            holsum += str(num_list[i])
        elif num_list[i] % 2 == 0:
            jjaksum += str(num_list[i])
    result = int(holsum) + int(jjaksum)
    
    return result
            
