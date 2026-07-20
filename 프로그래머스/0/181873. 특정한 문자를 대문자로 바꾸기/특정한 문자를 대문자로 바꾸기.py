def solution(my_string, alp):
    result = ""
    for ch in my_string:
        if ch == alp:
            ch = ch.upper()
        result += ch
    return result