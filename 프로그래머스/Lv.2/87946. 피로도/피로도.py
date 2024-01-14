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



"""
# 백트래킹
answer = 0

def dfs(k, cnt, dungeons, visited):
    global answer 
    if cnt > answer:
        answer = cnt
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False
        
def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer
"""
