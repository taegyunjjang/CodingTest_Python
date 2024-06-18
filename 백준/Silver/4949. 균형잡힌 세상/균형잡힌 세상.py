# import sys
# input = sys.stdin.readline

def is_balance(P):
    stack = []
    for p in P:
        if p == ')':
            if not stack or stack.pop() != '(':
                return False
        elif p == ']':
            if not stack or stack.pop() != '[':
                return False
        else:
            stack.append(p)

    return not stack

def solution():
    while True:
        S = input()
        if S == '.':
            break
        
        tmp = ''
        for s in S:
            if s in '()[]':
                tmp += s
        
        if is_balance(tmp):
            print('yes')
        else:
            print('no')
                  
                        
solution()