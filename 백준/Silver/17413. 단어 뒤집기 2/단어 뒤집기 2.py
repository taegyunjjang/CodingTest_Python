import sys


input = sys.stdin.readline
S = input()

is_continue = False
is_stack = True

stack = []

answer = ""
for ch in S:
    if ch == '<':
        while stack:
            answer += stack.pop()
        answer += ch
        is_continue = True
        is_stack = False
        continue
    elif ch == '>':
        answer += ch
        is_continue = False
        is_stack = True
        continue
    
    if is_continue:
        answer += ch
    if is_stack:
        if ch == ' ' or ch == '\n':
            while stack:
                answer += stack.pop()
            answer += ch
        else:
            stack.append(ch)

print(answer)