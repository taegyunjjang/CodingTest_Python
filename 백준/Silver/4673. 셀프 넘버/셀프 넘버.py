import sys
input = sys.stdin.readline

def solution():
    no_self_number = []; answer = []
    for num in range(1, 10000):
        if num not in no_self_number:
            answer.append(num)
        tmp = sum(list(int(n) for n in (str(num))))
        no_self_number.append(num + tmp)
    
    for num in answer:
        print(num)
    
solution()