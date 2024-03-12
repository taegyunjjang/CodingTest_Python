import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    num_list = list(map(int, input().split()))
    M = max(num_list)
    answer = sum(num/M*100 for num in num_list)/N
    print(answer)
    
solution()