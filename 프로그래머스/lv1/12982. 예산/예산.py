def solution(d, budget):
    tot = 0
    cnt = 0
    
    for num in sorted(d):
        tot += num
        if tot > budget:
            return cnt
        else:
            cnt += 1
    return cnt