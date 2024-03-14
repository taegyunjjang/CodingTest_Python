import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    num_list = list(map(int, input().split()))
    
    if N == 1:
        print('A')
    elif N == 2:
        if num_list[0] == num_list[1]:
            print(num_list[0])
        else:
            print('A')
    else:
        # 그래프 : 상수
        if num_list[0] == num_list[1]:
            m = 0
        else:
            # 그래프 : 기울기 m인 직선
            m = (num_list[2] - num_list[1]) // (num_list[1] - num_list[0])
            
        k = num_list[1] - m*num_list[0]
        
        for i in range(1, N - 1):
            predict = m*num_list[i] + k
            if predict != num_list[i + 1]:
                print('B')
                return
        print(m*num_list[-1] + k)
                    
solution()