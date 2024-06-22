import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    num_list = list(map(int, input().split()))
    sorted_list = sorted(set(num_list))
    dic = {}
    for i in range(len(sorted_list)):
        dic[sorted_list[i]] = i
        
    for num in num_list:
        print(dic[num], end=' ')
    
            
solution()