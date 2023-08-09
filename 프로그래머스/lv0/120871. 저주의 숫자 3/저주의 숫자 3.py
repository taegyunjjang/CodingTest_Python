def solution(n):
    l = []
    i = 1
    while len(l) != n:
        if i % 3 != 0 and '3' not in str(i):
            l.append(i)
        i += 1
    return l[n - 1]