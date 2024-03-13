import sys
input = sys.stdin.readline

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    n = int(num**0.5) + 1
    for i in range(3, n, 2):
        if num % i == 0:
            return False
    return True

def solution():
    N = int(input())
    num_list = list(map(int, input().split()))
    
    cnt = 0
    for num in num_list:
        if is_prime(num):
            cnt += 1
    print(cnt)        
    
        
solution()