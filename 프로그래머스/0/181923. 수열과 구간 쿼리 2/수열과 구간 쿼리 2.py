def solution(arr, queries):
    result = []
    for s, e, k in queries:
        who_minimum = []
        for i in range(s, e + 1):
                if arr[i] > k:
                    who_minimum.append(arr[i])
        if not who_minimum :
            result.append(-1)
        else:
            result.append(min(who_minimum))
    return result