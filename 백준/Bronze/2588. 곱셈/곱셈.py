import sys
input = sys.stdin.readline


def solution():
    answer = []
    A, B = int(input()), input().rstrip()
    for n in B[::-1]:
        answer.append(int(n) * A)
        
    tmp = 0
    for i in range(3):
        tmp += answer[i] * 10**i
    answer.append(tmp)
    
    print(*answer, sep='\n')
    
    
solution()
