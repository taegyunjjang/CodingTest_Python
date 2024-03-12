import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    
    is_stop = False
    for _ in range(T):
        S = input().rstrip()
        
        stack = [] 
        is_stop = False
        for s in S:
            if s == '(':
                stack.append(s)
            elif s == ')':
                if stack:
                    stack.pop()
                else:
                    print("NO")
                    is_stop = True 
                    break
        if is_stop:
            continue
                   
        if stack:
            print("NO")
        else:
            print("YES")
        
solution()