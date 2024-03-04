import sys
input = sys.stdin.readline

def solution():
    # I:1, V:5, X:10, L:50, C:100, D:500, M:1000
    # V, L, D는 한 번만 사용 가능
    # I, X, C, M은 연속해서 세 번까지만 사용 가능
    # IV:4, IX:9, XL:40, XC:90, CD:400, CM: 900 한 번만 사용 가능
    # (IV, IX), (XL, XC), (CD, CM) 동시에 안 됨
    # XCXC, CMCD
    # 553 + 1940 = 2493

    S1, S2 = input().rstrip(), input().rstrip()
    L1, L2 = len(S1), len(S2)
    dic = {
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
        'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900
    }

    tot = 0
    answer = ''

    i = 0
    if L1 == 1:
        tot += dic[S1]
    else:
        while i < L1 - 1:
            s = S1[i] + S1[i + 1]
            if s in dic.keys():
                tot += dic[s]
                i += 2
            else:
                tot += dic[S1[i]]
                i += 1

            if i == L1 - 1:
                tot += dic[S1[-1]]
                i += 1

    j = 0
    if L2 == 1:
        tot += dic[S2]
    else:
        while j < L2 - 1:
            s = S2[j] + S2[j + 1]
            if s in dic.keys():
                tot += dic[s]
                j += 2
            else:
                tot += dic[S2[j]]
                j += 1

            if j == L2 - 1:
                tot += dic[S2[-1]]
                j += 1

    s = str(tot)
    s = (4 - len(s))*'0' + s

    a = int(s[0])
    answer += a * 'M'
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])

    # 300, 400, 500, 900
    if b == 9:
        answer += 'CM'
    elif b >= 5:
        answer += 'D' + (b - 5)*'C'
    elif b == 4:
        answer += 'CD'
    else:
        answer += b*'C'

    # 10, 40, 50, 90
    if c == 9:
        answer += 'XC'
    elif c >= 5:
        answer += 'L' + (c - 5)*'X'
    elif c == 4:
        answer += 'XL'
    else:
        answer += c*'X'

    # 1, 4, 5, 9
    if d == 9:
        answer += 'IX'
    elif d >= 5:
        answer += 'V' + (d - 5)*'I'
    elif d == 4:
        answer += 'IV'
    else:
        answer += d*'I' 

    print(tot)
    print(answer)

solution()