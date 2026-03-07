def solution(numLog):
    result = ""
    for i in range(len(numLog) - 1):
        if (numLog[i+1]) - numLog[i] == 1 :
            result += "w"
        elif (numLog[i+1]) - numLog[i] == -1:
            result += "s"
        elif (numLog[i+1]) - numLog[i] == 10:
            result += "d"
        elif (numLog[i+1]) - numLog[i] == -10:
            result += "a"
    return result
            