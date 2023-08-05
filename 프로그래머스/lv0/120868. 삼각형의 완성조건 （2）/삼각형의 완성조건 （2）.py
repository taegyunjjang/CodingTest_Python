def solution(sides):
    cnt = 0
    
    # 1) max(sides)가 빗변
    for d in range(1, max(sides) + 1):
        if d + min(sides) > max(sides):
            cnt += 1
    
    # 2) d가 빗변
    for _ in range(max(sides) + 1, max(sides) + min(sides)):
        cnt += 1
    
    return cnt