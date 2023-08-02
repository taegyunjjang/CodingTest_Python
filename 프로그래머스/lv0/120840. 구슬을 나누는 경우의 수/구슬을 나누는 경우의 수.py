def solution(balls, share):
    n, a, b = 1, 1, 1
    for i in range(balls, 0, -1):
        n *= i
    for j in range(share, 0, -1):
        a *= j
    for k in range(balls - share, 0, -1):
        b *= k
    
    return n // (a * b)
    