import sys
input = sys.stdin.readline

def binary_search(num, N_list, i, j):
    mid = (i + j)//2
    
    if i == j and N_list[i] != num:
        return False    
    
    if N_list[mid] == num:
        return True
    elif N_list[mid] < num:
        return binary_search(num, N_list, mid + 1, j)
    else:
        if mid == 0:
            return False
        return binary_search(num, N_list, 0, mid - 1)


def solution():
    N = int(input())
    N_list = list(map(int, input().split()))
    N_list.sort()
    
    M = int(input())
    M_list = list(map(int, input().split()))
    
    answer = []
    for m in M_list:
        if binary_search(m, N_list, 0, N - 1):
            answer.append(1)
        else:
            answer.append(0)

    for num in answer:
        print(num)
        
solution()