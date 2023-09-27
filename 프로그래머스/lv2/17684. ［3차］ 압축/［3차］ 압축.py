def solution(msg):
    idxList = []
    w = {chr(idx + 64):idx for idx in range(1, 27)}
    i = 0

    while i < len(msg):
        tmp = msg[i]
        
        # 마지막 idx라면 idxList에 넣고 종료
        if i == len(msg) - 1:
            idxList.append(w[tmp])
            break
        
        # 현재 문자 + 다음 문자가 딕셔너리에 있는 경우
        if msg[i] + msg[i + 1] in w.keys():
            tmp += msg[i + 1]
            i += 1
            
            # 다음 idx가 마지막 idx라면 idxList에 넣고 종료
            if i == len(msg) - 1:
                idxList.append(w[tmp])
                break
            
            # 딕셔너리에 존재하는 가장 긴 문자열 찾기
            while isInW(w, tmp, i, msg):
                tmp += msg[i + 1]
                i += 1
                
                # 가장 긴 문자열에 해당하는 idx가 마지막 idx라면 idxList에 넣고 종료
                if i == len(msg) - 1:
                    idxList.append(w[tmp])
                    return idxList
                
            w[tmp + msg[i + 1]] = len(w) + 1
            idxList.append(w[tmp])
        
        # 현재 문자 + 다음 문자가 딕셔너리에 없는 경우
        else:
            idxList.append(w[tmp])
            tmp += msg[i + 1]
            w[tmp] = len(w) + 1
        
        i += 1
    return idxList

# 현재 문자 + 다음 문자가 딕셔너리에 존재하는지에 대한 함수
def isInW(w, tmp, i, msg):
    if tmp + msg[i + 1] in w.keys():
        return True
    return False