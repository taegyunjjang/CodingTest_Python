from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for dungeon in permutations(dungeons):
        cnt = 0
        tmp = k
        
        for minNeedFatigue, consumption in dungeon:
            if tmp >= minNeedFatigue:
                tmp -= consumption
                cnt += 1
                
        if answer < cnt:
            answer = cnt
    
    return answer