def solution(intStrs, k, s, l):
    ret = []
    
    for idx in intStrs:
        sli_num = idx[s: s+l]
        if int(sli_num) > k:
            ret.append(int(sli_num))
            
    return ret