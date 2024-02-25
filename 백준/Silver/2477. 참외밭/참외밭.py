import sys
input = sys.stdin.readline

def solution():
    K = int(input())
    side = [list(map(int, input().split())) for _ in range(6)] 
    dic = {1:0, 2:0, 3:0, 4:0}
    for s in side:
        dic[s[0]] += 1
    
    answer = 0
    # ㄱ
    if dic[1] == dic[3] == 2:
        for i in range(len(side)):
            if side[i][0] == 4:
                answer += side[i][1] * side[(i+1)%6][1]
            elif side[i][0] == 1 and side[(i+1)%6][0] == 3:
                answer -= side[i][1] * side[(i+1)%6][1]
    # ┏
    elif dic[1] == dic[4] == 2:
        for i in range(len(side)):
            if side[i][0] == 2:
                answer += side[i][1] * side[(i+1)%6][1]
            elif side[i][0] == 4 and side[(i+1)%6][0] == 1:
                answer -= side[i][1] * side[(i+1)%6][1]
    # ┛
    elif dic[2] == dic[3] == 2:
        for i in range(len(side)):
            if side[i][0] == 1:
                answer += side[i][1] * side[(i+1)%6][1]
            elif side[i][0] == 3 and side[(i+1)%6][0] == 2:
                answer -= side[i][1] * side[(i+1)%6][1]
    # ㄴ
    elif dic[2] == dic[4] == 2:
        for i in range(len(side)):
            if side[i][0] == 3:
                answer += side[i][1] * side[(i+1)%6][1]
            elif side[i][0] == 2 and side[(i+1)%6][0] == 4:
                answer -= side[i][1] * side[(i+1)%6][1]

    print(answer * K)
    
solution()