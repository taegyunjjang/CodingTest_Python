import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    s = []
    answer = []

    is_impossible = False
    top = 0
    for i in range(N):
        num = int(input())
        if i == 0:
            s = [i for i in range(1, num + 1)]
            answer = ['+']*num
            top = num
        else:
            if top < num:
                answer += ['-']
                s.pop()
                answer += ['+']*(num - top)
                s += [i for i in range(top + 1, num + 1)]
                top = num
            else:
                s.pop()
                answer += ['-']
                
                if s[-1] != num:
                    is_impossible = True
    answer += ['-']
    
    if is_impossible:
        print("NO")
        exit()
            
    for i in range(len(answer)):
        print(answer[i])
    
solution()