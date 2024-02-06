import sys

input = sys.stdin.readline

N = int(input())

stack = []
answer_list = []

for _ in range(N):
    S = input().rstrip()
    S_len = len(S)

    if S_len > 5:
        op, x = S.split()
        stack.append(x)
    else:
        op = S

        if op == 'pop':
            if stack:
                answer_list.append(stack.pop())
            else:
                answer_list.append(-1)
        elif op == 'size':
            answer_list.append(len(stack))
        elif op == 'empty':
            if stack:
                answer_list.append(0)
            else:
                answer_list.append(1)
        else:
            if stack:
                answer_list.append(stack[-1])
            else:
                answer_list.append(-1)

for num in answer_list:
    print(num)

