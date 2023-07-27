def solution(n_str):
    str = '0'
    idx = 0
    for i in range(len(n_str)):
        if str != n_str[i]:
            return n_str[idx:]
        else:
            idx += 1