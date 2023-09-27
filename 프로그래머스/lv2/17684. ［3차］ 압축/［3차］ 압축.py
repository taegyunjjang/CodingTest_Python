def solution(msg):
    idxList = []
    w = {chr(idx + 64):idx for idx in range(1, 27)}
    i = 0

    while i < len(msg):
        tmp = msg[i]
        if i == len(msg) - 1:
            idxList.append(w[tmp])
            break

        if msg[i] + msg[i + 1] in w.keys():
            tmp += msg[i + 1]
            i += 1

            if i == len(msg) - 1:
                idxList.append(w[tmp])
                break

            while isInW(w, tmp, i, msg):
                tmp += msg[i + 1]
                i += 1
                if i == len(msg) - 1:
                    idxList.append(w[tmp])
                    return idxList

            w[tmp + msg[i + 1]] = len(w) + 1
            idxList.append(w[tmp])
        else:
            idxList.append(w[tmp])
            tmp += msg[i + 1]
            w[tmp] = len(w) + 1
        
        i += 1

    return idxList

def isInW(w, subStr, i, msg):
    if subStr + msg[i + 1] in w.keys():
        return True
    return False