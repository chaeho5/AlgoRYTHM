def solution(my_string, index_list):
    result=""
    
    for i in range(len(index_list)):
        result += my_string[index_list[i]]
        
    return result