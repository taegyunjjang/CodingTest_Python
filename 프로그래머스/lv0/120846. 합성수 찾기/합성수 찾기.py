def solution(n):
    c = 0
    
    for i in range(2, n + 1):
        isComposite = False
        for j in range(2, i):
            if i % j == 0:
                isComposite = True
        if isComposite:
            c += 1
    return c