def solution(myString, pat):
    string = myString.upper()
    pat = pat.upper()
    
    if pat in string:
        return 1
    else:
        return 0
        