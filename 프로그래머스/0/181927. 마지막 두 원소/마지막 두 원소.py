def solution(num_list):
    for i in range(len(num_list)):
        if num_list[len(num_list) - 1] > num_list[len(num_list) - 2]:
            num_list.append(num_list[len(num_list) - 1] - num_list[len(num_list) - 2])
            return num_list
        else:
            num_list.append(num_list[len(num_list)-1] * 2)
            return num_list
            