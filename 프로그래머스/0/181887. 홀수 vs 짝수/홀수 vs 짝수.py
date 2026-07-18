def solution(num_list):
    hol = num_list[::2]
    jjak = num_list[1::2]
    hol_sum = 0
    jjak_sum = 0
    for num in hol:
        hol_sum += num
    
    for num2 in jjak:
        jjak_sum += num2
    
    return max(hol_sum, jjak_sum)
        