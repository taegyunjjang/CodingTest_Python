def solution(brown, yellow):
    for a in range(1, int(yellow ** 0.5) + 1):
        if yellow % a == 0:
            b = yellow // a
            if (a + 2) * (b + 2) == brown + yellow:
                return [b + 2, a + 2]