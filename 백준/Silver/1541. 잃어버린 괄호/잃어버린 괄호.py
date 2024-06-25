import sys
input = sys.stdin.readline


def solution():
    S = input().rstrip()
    flag = False
    s1 = []
    s2 = []
    
    tmp = ''
    for s in S:
        if flag:
            if s.isdigit():
                tmp += s
            else:
                s2.append(int(tmp))
                tmp = ''
        else:
            if s.isdigit():
                tmp += s
            elif s == '+':
                s1.append(int(tmp))
                tmp = ''
            else:
                flag = True
                s1.append(int(tmp))
                tmp = ''
                
    if flag:
        s2.append(int(tmp))
    else:
        s1.append(int(tmp))
        
    print(sum(s1) - sum(s2))
    
            
solution()